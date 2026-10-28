---
title: "PLAIN: An Explainable Generative Search System Enhanced by Multi-granularity Semantic Alignment"
authors: "Guoliang Zhang, Weifan Wang, Junyao Zhao, Zhuo Li, Hongjing Zhang et al. (13 人)"
affiliation: "Kuaishou Technology"
date: "2026-09"
venue: "RecSys 2026"
topic: semantic-id
topic_name: Semantic ID
topic_icon: 🗂
idea: "把 SID 构建看作结构化语义推理：6 层码本按层分工，L1-L3 硬绑定人工类目树（54/586/4049），L4-L5 用 LLM CoT 生成的关键词和主播描述做软蒸馏，L6 不加约束，使 SID 前缀就是可读的类目路径。对称 query/item 多分面编码器、带拓扑 mask 的半监督 VQ 和 BART 式解码器五 loss 联合训练，在线用 Trie 加类目约束解码；快手直播搜索 HR@200 比 UniSearch 相对 +17.5%，线上 TPC +3.90%。"
paperUrl: https://doi.org/10.1145/3773078.3831884
codeUrl: null
tags:
- "Taxonomy-Anchored Codebook"
- "LLM CoT Label Distillation"
- "Hierarchical Constrained Decoding"
- "Live-Stream Search"
- "Explainable Semantic ID"
unverified: false
---
## 核心思路

PLAIN（快手直播搜索）认为现有生成式搜索的 SID 有两个问题：一是 SID 没有明确的语义对应，检索结果无法解释；二是无结构的码本让 SID 前缀树近似全连接，解码空间纠缠。它的做法是把 SID 构建当成"结构化语义推理"：用 LLM 的 CoT 给每个直播间打结构化标签，再把 6 层码本按层分工。L1–L3 硬绑定到人工整理的三级类目树（domain → category → subcategory，规模 54/586/4049），L4–L5 用 LLM 生成的关键词和主播描述做软监督（蒸馏），L6 不加约束，留给实例级区分。这样，SID 前三位本身就是可读的类目路径，解码时还能用类目树做父子 mask。

系统由两部分组成：MCC（Multi-stage Codebook Construction，分层任务分配 + 语义对齐）和 UGR（Unified Generative Retrieval：对称 query/item 编码器 SCE + 半监督分层 VQ 量化 + BART 式自回归解码器，五个 loss 联合训练）。

## 整体实现思路

1. **标签体系**：类目树由大规模直播标签自底向上聚类，再经多轮人工标注修订得到，是闭集；元数据标签（关键词、主播描述）是开集。
2. **LLM 标注**：领域 LLM 用 CoT 给每个直播间和 query 生成结构化标注，包括类目路径、关键词和主播描述。生成的类目标签通过 embedding 相似度映射回预定义类目树节点，保证落在合法节点上。
3. **Y → E → C 映射**：快手搜索通用多模态编码器把每个文本标签编码成连续参考向量（E 空间），作为双塔蒸馏目标；同时，类目标签以硬分配方式映射到码本 L1–L3，元数据标签以软分配方式映射到 L4–L5，L6 端到端学习。
4. **UGR 联合训练**：item 塔和 query 塔各输出 k=6 个"分面" embedding，与 6 层码本一一对应，同时服务三件事：蒸馏对齐、对比匹配、VQ 量化。BART 式解码器以 query 的 6 个 embedding 为 encoder 输出，通过 cross-attention 生成 6 位 SID。
5. **部署**：item 编码器订阅直播流，每 2 分钟用最新动态特征（片段级标签、视觉向量）重算 SID 并插入 Trie，已下播房间每 12 分钟清理一次；在线解码时用 Trie mask 做约束 beam search，并用 TensorRT 和 KV cache 加速。

## 子模块实现（可复现细节）

### 1. 分层任务分配（Layer-wise Task Assignment）
- 码本 6 层，大小 {54, 586, 4049, 500, 500, 500}，embedding 维度 d=768。
- L1–L3 = 类目树三级（例：Gaming → MOBA → Honor of Kings），前三位 SID 必须服从类目树结构。
- L4–L5 = 元数据标签（关键词，如 "jungle"、"ranked match"；主播描述，如 "a professional MOBA streamer focusing on high-rank gameplay"），用于同一子类目内部的细粒度语义区分。
- L6 = 无约束层，保留实例级表示。

### 2. 对称上下文编码器 SCE
- item 侧输入：直播元数据、多模态信息、辅助统计特征。用 multi-query attention 和 k 个可学习 query 向量聚合，得到 d = {d(1..k)}。
- query 侧输入：query 文本，拼接用户历史行为序列和后验特征（CTR、停留时长等），再接 k 个可学习的 [TAG] token，得到 q = {q(1..k)}，与 item 侧逐位对齐。
- 蒸馏（只作用于前 k-1=5 层）：每个 LLM 标签前加 [CLS]，送入通用编码器，得到 e_d(j)、e_q(j)。L_distill = Σ_i Σ_{j=1..k-1} [ (1 - cos(q_i(j), e_q_i(j))) + (1 - cos(d_i(j), e_d_i(j))) ]。第 k 层不参与蒸馏。
- 对比：sim(q,d) = (1/k) Σ_i cos(q(i), d(i))。L_contrast = InfoNCE，使用 batch 内负样本、温度 τ；正样本取历史 query 在多个互动等级（长播、点击）下对应的 item。

### 3. 半监督分层量化（VQ-VAE 瓶颈）
- 逐层打分：z_iv(j) = γ <d_i(j), c_v(j)>（L2 归一化后做内积，γ 为缩放系数），取 argmax 得到 SID 第 j 位。
- L_codebook = Σ_j α1 ||sg[d_i(j)] - c(j)||^2 + α2 ||d_i(j) - sg[c(j)]||^2。码本用 EMA 更新，衰减 0.99；分配用 Sinkhorn-Knopp 均衡，τ=0.05，防止码本坍缩。
- L1–L3 的类目 CE：复用 z 并加拓扑 mask M（不是上一层预测节点合法子节点的位置置为 -∞），P = softmax(z + M)；L_CE = -(1/N) Σ_i Σ_{j=1..3} w_j log P(ŷ_i(j))，w_j 逐层衰减。即：L1–L3 硬对齐类目（CE），L4–L5 软对齐元数据（蒸馏），L6 只受 L_codebook 约束。

### 4. 自回归 SID 生成
- BART 式结构：query 塔输出堆成 h_q ∈ R^{k×d} 作为 encoder 表示，Transformer decoder 通过 cross-attention 逐位生成 6 位 SID。L_NTP = -Σ_n log P(s(n) | h_q, s(<n))。

### 5. 联合训练
- L_total = λ1 L_CE + λ2 L_NTP + λ3 L_codebook + λ4 L_contrast + λ5 L_distill，λ = {1.0, 0.1, 1.0, 1.0, 0.5}。
- λ2 初始为 0，第 15,000 步开启（先让表示和码本稳定，再训生成）；共训练 80,000 步收敛，约 56 小时。
- 8 张 RTX 4090，每卡 batch 16；AdamW，lr 1e-4，weight decay 0.01。
- 推理：beam size 256，取 top-200 item 评测；所有对比模型都约 0.23B 参数，码本大小对齐。

### 6. 在线约束解码
- p̃(s_i | s_<i) = p 当 s_i ∈ C(s_<i)（Trie 中合法的下一个 token），否则为 0。前三层同时受类目树约束。论文案例：query "Honor of Kings"，L1 选 38（Gaming），L2 从 Gaming 的 23 个合法子节点中选 37（MOBA），L3 从 MOBA 的 4 个子类中选 1171（Honor of Kings），L4–L6 在完整 VQ 码本内（仍受 Trie 约束）beam search，得到如 <38, 37, 1171, 344, 421, 17> 的路径，每条路径对应一个或多个直播间。

## 实验设置与结果

**数据**（快手直播搜索日志）：

| 划分 | Session | Query | Item | 正样本 | 负样本 | 有标注 |
|---|---|---|---|---|---|---|
| Train（2026-01-14 至 01-22） | 26,108,537 | 2,399,013 | 8,072,895 | 144,135,860 | 718,953,694 | 8,072,895 |
| Test（2026-02-01 采样） | 40,000 | 24,429 | 26,079 | 149,057 | – | – |

训练正样本是至少有一次点击或长播的 item；测试正样本是"线上排序系统排在 top-4 的 item"。

**主结果（表 2）**：

| 模型 | HR@200 | HR@300 | NDCG@200 | NDCG@300 |
|---|---|---|---|---|
| MCA（级联召回 + 粗排） | 38.96 | 45.54 | 19.26 | 20.90 |
| UniSearch | 43.06 | 49.00 | 18.18 | 19.32 |
| HiGR | 45.01 | 50.10 | 16.16 | 17.12 |
| OneLive | 47.18 | 52.90 | 17.85 | 18.93 |
| **PLAIN** | **50.59** | **55.47** | **21.01** | **21.94** |

相对提升：HR@200 / NDCG@200 对 MCA 分别为 +29.85% / +9.08%，对 UniSearch 为 +17.49% / +10.07%，对 HiGR 为 +12.40% / +30.01%，对 OneLive 为 +7.23% / +17.70%。

**消融（表 3）**：

| 设置 | HR@200 | HR@300 | NDCG@200 | NDCG@300 |
|---|---|---|---|---|
| PLAIN | 50.59 | 55.46 | 21.01 | 21.94 |
| w/o distill_loss | 46.81 | 51.74 | 20.85 | 21.79 |
| w/o codebook_loss | 48.26 | 53.78 | 17.70 | 17.71 |
| w/o ce_loss | 39.51 | 45.24 | 11.56 | 11.58 |
| w/o contrast_loss | 16.20 | 18.80 | 6.15 | 6.64 |
| w/o path_constraint | 46.45 | 54.36 | 18.22 | 19.06 |

（论文正文中写的 "HR@200 下降 3.78%" 等数字都是绝对百分点。）

**码本健康度（表 4）**：

| 方法 | Collision Rate | Avg-IPC | Max-IPC |
|---|---|---|---|
| RQ-Kmeans | 22.66% | 3.85 | 432 |
| RQ-VAE | 12.82% | 3.67 | 694 |
| VQ-VAE | 21.60% | 4.75 | 700 |
| VQ-VAE w/ CoT | 13.24% | 3.07 | 220 |

**在线 A/B**：7 天，两组各占 5% 直播搜索流量，对照组为线上的 UniSearch-Live。结果 TPC +3.90%、PCTR +1.66%、PLVR +1.30%。按 query 频次分桶：长尾 TPC +3.10%，高频 TPC +0.80%。

## 思考与可参考价值

- **类目树当作 SID 前缀**：前三层直接等于业务类目，好处是可解释、可做类目级约束和干预，类目分布也天然决定了码本均衡性（Max-IPC 从 700 降到 220）。电商场景有现成的叶子类目树，可以直接照搬：L1–L3 = 一/二/三级类目，L4–L5 = 属性/卖点，L6 = 残差区分。
- **"硬 CE + 软蒸馏 + 自由残差"三档监督**：把"哪些层由人定义、哪些层由数据学习"写成显式分工，比全 RQ-KMeans 或全语义 ID 更折中，值得在我们的 SID 上做对照实验。
- **拓扑 mask 同时用于训练和解码**：训练时 CE 内加父子 mask，解码时用 Trie 加类目树约束；去掉 path constraint 后 HR@200 降 4.14pt。
- **需要警惕的点**（推断）：(1) 测试正样本是线上排序 top-4，评测偏向与现有系统一致，而不是用户真实反馈；(2) 只有 2 天的时间外推，没有冷启动或新类目实验；(3) 对比模型都缩到 0.23B，而 HiGR/OneLive 原本是推荐模型，适配方式比较简单；(4) 正文说 L1–L3"硬分配"，但量化仍是对 d(j) 做 argmax，推理时 SID 前三位来自模型预测还是直接取 LLM 标签，文中没有说清楚，类目预测错误会怎样传导也没有分析；(5) 线上整体 TPC +3.90%，同时高于长尾 +3.10% 和高频 +0.80%，加权平均不应如此，分桶口径存疑；(6) 表 2 与表 3 的 PLAIN HR@300 分别为 55.47 和 55.46，有小出入；(7) 没有开源代码。
- **落地前要检查**：类目树的覆盖率和 LLM 标签映射回类目树的准确率；类目调整后码本是否需要重建；每 2 分钟重算 SID 引起的 SID 漂移对生成器训练的影响（直播特有，电商商品 SID 相对稳定）。
