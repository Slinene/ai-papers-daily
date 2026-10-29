---
title: "UNIQUE: A Unified Retrieval and Ranking System for Large-Scale Feed Recommendation"
authors: "Zhuang Liu, Yongkang Fu, Zuodong Yang, Guangxing Chen, Zonggang Wu et al. (9 人)"
affiliation: "Beihang University × Baidu × City University of Hong Kong"
date: "2026-09"
venue: "RecSys 2026"
topic: gen-rec
topic_name: 生成式推荐
topic_icon: 🎯
idea: "把召回和排序塞进同一个 early-fusion Transformer：用户前缀后面同时拼候选 code token 和候选 item token，一次前向既出 code 分布（生成式召回）又出多目标分数（判别式排序），排序监督直接塑造召回表示。SID 侧放弃 RQ-VAE 分层量化，改用由 DSSM 多任务双塔（吸收了用户反馈）的 item 塔驱动的单层 16384 平铺码本，并用按使用频率加权的分配距离 d_j=||z-e_j||^2·r_j^tau 压制头部 code。"
paperUrl: https://arxiv.org/abs/2609.23718
codeUrl: null
tags:
- "Unified Retrieval-Ranking"
- "Flat Single-Layer Codebook"
- "Feedback-Aware Quantization"
- "Early Fusion Target Attention"
- "Baidu Feed Deployment"
unverified: false
---
## 核心思路

UNIQUE 针对工业 feed 推荐的两个痛点：一是 RQ-VAE 类分层语义 ID 在长尾流量下的量化不稳（粗层错分传播、头部 item 挤占 code 容量），二是召回与排序分阶段训练造成的信息损失。它的做法是两件事：

1. **单层平铺量化（EQN）**：每个 item 只有一个 code（线上 16384 个），item 表示来自一个用多目标用户反馈训练的 DSSM item 塔，码本用 EMA 更新，并在最近邻分配时用 `r_j^tau`（code 使用频率相对均值的幂次）放大头部 code 的距离，压制马太效应。
2. **Early-fusion 统一模型（UIGN + TDN）**：用户画像与多粒度行为序列作为前缀，后面同时拼候选 code token 和候选 item token，目标 token 只 attend 前缀、彼此不互看。code token 位置的输出过 MLP 得到 code logit（生成式召回），item token 位置的输出过多任务头得到相关性/CTR/时长/完播等分数（判别式排序）。召回和排序在一次前向、同一份表示中完成，排序监督直接塑造召回表示。

与常见生成式召回最大的区别：code logit 不是“用户向量 · code embedding”，而是 code 作为目标 token 与用户前缀交叉后的表示打分，本质上是一个以 code 为候选的 target-attention 排序模型。

## 整体实现思路

- **训练**：EQN 的多任务双塔先给出归一化 item 向量 z̄_i 并量化得到 c_i；主模型同时优化 code 分类交叉熵 `L_gen`、多目标判别损失 `L_disc`、双塔损失 `L_code` 和量化正则 `L_quant`：`L = L_disc + α·L_gen + η·L_code + β·L_quant`。
- **推理**（线上）：编码用户前缀 → 对所有 code 打分取 top N=100 → code-to-item 索引取回（共数十万 item）→ 用户/item embedding 内积粗排 → top 10k 按 code 分组送精排 → 每个 code 产出 M=30 个 item 给下游。
- **部署范围**：手机百度首页 feed、发现页、短视频三个场景的召回阶段，三场景共用一套架构，只换输入特征与训练数据。

## 子模块实现（可复现细节）

### EQN：反馈感知的单层平铺量化

- item 塔：`z_i = f_item(x_i)`，x_i 包括 item ID、类目、子类目、发布者、标题词等先验特征和行为后验信号；归一化 `z̄_i = z_i / ||z_i||_2`。
- DSSM 多任务双塔：每个反馈目标 k（相关性、CTR、时长、短视频完播等）一个用户塔 `u_u^k`，共享 item 塔，`s^k_{u,i} = <u_u^k, z_i>`；正样本与 batch 内随机重配 item 组成对比监督，二值目标用二值反馈、时长用回归式反馈。这样码本是被“已经吸收了用户反馈”的 item 表示更新的，而不是只靠元数据。
- 量化：`c_i = argmin_j ||z̄_i − e_j||²`，`q_i = e_{c_i}`；直通估计 `q̃_i = z̄_i + sg(q_i − z̄_i)`。
- EMA 更新：`e_j ← γ·e_j + (1−γ)·mean_{z̄∈B_j}(z̄)`，本 batch 未被分配的 code 保持不变。
- 使用监控：`PPL = exp(−Σ_j p_j·log(p_j+ε))`，p_j 为 batch 内 code j 的使用概率。
- 平衡分配：`r_j = p_j / (1/M)`，`d_j(z) = ||z̄ − e_j||² · r_j^tau`，tau≥0，tau=0 即标准最近邻。r_j>1 的头部 code 距离被放大，尾部 code 被拉近。论文没有给出 tau 与 γ 的取值。

### UIGN：多粒度用户兴趣前缀

- 每个行为 token 拼接 item ID、类目、行为类型、时间特征、反馈字段的 embedding，经 `h_t = f_seq(x_t)` 投影到 d 维。
- 前缀 `X_u = [h_user; H_st; H_mt; H_int]`。公开集上长度 501：1 个静态用户 token；100 个短期 token（最近 100 次曝光，含点击与曝光未点击，提供即时正负反馈）；200 个中期 token（最近 200 次满意观看）；200 个长期兴趣 token（按 item 类目分组，每类取最近 n 条后截断）。

### Early-fusion 编码器与 target-attention split

- 输入 `Z = [X_u; V_i; R_c]`：V_i 是候选 item 目标 token（由 item-target embedding 层编码 item ID、类目、内容元数据等线上可用特征），R_c 是候选 code 目标 token。
- 注意力掩码：前缀内部 self-attention；目标 token 只看前缀：`Attn(t, X_u) = softmax(W_q t (W_k X_u)^T / √d) W_v X_u`；目标之间不互看，因此所有候选可以并行打分，同时保持“从历史生成”的因果含义。
- 公开集配置：3 层、4 头、hidden 512、GELU、无 dropout；user/item embedding 256，code embedding 64。

### Code 预测（生成式召回头）

- `o^code_{u,j} = F_enc(X_u, r_j)`，`ℓ_j = f_code(o^code_{u,j})`（所有 code 共享的 MLP），`p(c=j|S_u) = softmax_j(ℓ_j)`，`L_gen = −log p(c_i|S_u)`。
- 单层码本意味着一次 softmax 就是完整解码，不需要多层 beam search。

### TDN：目标感知多目标判别

- `o_{u,i} = F_enc(X_u, v_i)`，`ŷ^k = σ(f_k(o_{u,i}))`，k 为相关性、CTR、归一化时长、完播等。
- 二值任务加权 BCE：`L_k = −w^k[y log ŷ + (1−y) log(1−ŷ)]`，不满意点击降权；时长用加权 MSE；`L_disc = Σ_k λ_k L_k`。

### 训练与线上工程

- 公开集：Adam lr 1e-3，指数衰减，batch 2048，码本 1024（因只有 7,583 个 item）。
- 线上：码本 16384，替换原 128×128 分层码本（容量相同）；约 400 张 NVIDIA L20，单卡单实例，TensorRT FP16；GPU 推理引擎集成索引与预测，实时产出多目标用户表示；item embedding 每小时预计算并经消息队列同步；新 item 首次曝光后 5 分钟内进入训练流、1 小时内完成量化；参数服务器保持 UIGN 与 TDN 版本一致。
- 检索参数：N=100 个 code、每 code M=30 个 item。N 提到 200 多样性收益很小、成本约 2 倍；M 降到 10 显著伤害召回。

## 实验设置与结果

### 数据与协议

| 数据集 | 用户 | Item | 交互 | 平均长度 |
|---|---|---|---|---|
| KuaiRand-Pure | 27,285 | 7,583 | 1,186,059 | 43.47 |

按时间排序、过滤交互少于 3 条的用户；leave-one-out（最后一条测试、倒数第二条验证）；召回在全库上排序算 HR@K/NDCG@K，排序报 CTR-AUC。

### 主结果（KuaiRand-Pure）

| 模型 | HR@10 | HR@50 | NDCG@10 | NDCG@50 | CTR-AUC |
|---|---|---|---|---|---|
| SASRec | 0.0304 | 0.0847 | 0.0189 | 0.0310 | – |
| TIGER | 0.0380 | 0.0902 | 0.0205 | 0.0378 | – |
| DIN | – | – | – | – | 0.6812 |
| DCN | – | – | – | – | 0.7037 |
| HSTU | 0.0453 | 0.1418 | 0.0273 | 0.0412 | 0.7150 |
| UniGRF-HSTU | 0.0511 | 0.1453 | 0.0298 | 0.0430 | 0.7168 |
| **UNIQUE** | **0.0575** | **0.1510** | **0.0310** | **0.0473** | **0.7252** |

相对 UniGRF-HSTU：HR@10 +12.52%，HR@50 +3.92%，NDCG@10 +4.03%，NDCG@50 +10.00%，CTR-AUC +0.0084（相对 HSTU +0.0102）。

### 消融

| 变体 | HR@50 | CTR-AUC |
|---|---|---|
| UNIQUE | 0.1510 | 0.7252 |
| w/o early fusion（late fusion） | 0.1398 (−7.42%) | 0.7164 (−1.21%) |
| w/o flat quantization（换 RQ-VAE 式分层） | 0.1421 (−5.89%) | 0.7190 (−0.85%) |
| w/o target-attention split | 0.1456 (−3.58%) | 0.7207 (−0.62%) |
| w/o generative objective | 0.1374 (−9.01%) | 0.7115 (−1.89%) |

去掉生成目标对召回伤害最大；去掉 early fusion 召回和排序都掉，说明共享监督有效。

### 线上码本分析（128×128 分层 → 16384 单层）

| 指标 | 分层 128×128 | 单层平铺 |
|---|---|---|
| code 资源数方差 | 1510.85 | 389.57 |
| 平均 top-1 类目占比 | 65.43% | 78.08% |

Figure 2 显示单层码本下最拥挤的 top-N code 累计资源占比明显更低。

### 线上 A/B（手机百度，一周全量，p<0.05）

| 指标 | 相对提升 |
|---|---|
| 总观看时长 | +0.96% |
| 总分发量 | +1.08% |
| 用户留存率 | +0.70% |

| 人群 | 时长 | 分发量 |
|---|---|---|
| 高活（周活 >5 天） | +1.11% | +1.29% |
| 中活（2–5 天） | +0.63% | +0.65% |
| 低活（<2 天） | +0.29% | +0.15% |
| 新用户（注册 14 天内） | +1.44% | +1.24% |

- UNIQUE 占召回候选池 22.5%。
- 多样性（Figure 3）：二级类目覆盖 +23.3%，人均 Shannon 熵 +13.0%，top-1K 候选中尾部占比 +25.7%（尾部=历史点击后 20%，约 182 万 item）；长尾 item 曝光占比 1.04%。

### 线上效率

| 指标 | 数值 |
|---|---|
| P80 延迟 | 35 ms |
| P99 延迟 | 89 ms |
| 在线推理 MFU | 44.23% |
| 午高峰缓存命中（15s 窗口） | 37% |
| 晚高峰缓存命中（30s 窗口） | 60% |

峰值约 10,000 QPS、平均延迟 37 ms、每千次请求成本约 $0.0013。

## 思考与可参考价值

**值得借鉴的点**

- **单层大码本是 RQ 多层 beam 之外的务实选择**：一次 softmax 选 top-100 code，没有层间误差传播；配合 code 内粗排/精排，把“code 太粗”的问题交给下游排序解决。对电商来说，可以先作为一路新召回通道上线，用候选池占比（百度 22.5%）衡量真实贡献。
- **SID 由行为反馈塔驱动**：直接复用多目标 DSSM 的 item 塔作为量化输入，code 带上点击/时长等后验，比纯文本/图像 embedding 更贴近业务目标。电商可换成点击/加购/成交多塔。
- **`r_j^tau` 频率惩罚**：几乎零成本，可加在任何 EMA/K-Means 码本分配上；监控建议照搬论文的三项：code 资源数方差、top-N code 资源累计占比、code 内 top-1 类目占比（防止平衡过头打散语义）。
- **用户×code 交叉打分**：把 code 当作候选 token 走 target attention，比双塔点积的 code 打分表达力更强；target-attention split 让大量候选可以并行打分。

**需要警惕的点**

- 离线证据很薄：只有 KuaiRand-Pure（7,583 item、码本 1024），基线中缺少 LETTER/ETEGRec/OneRec 等近期 SID 方法，也没有和平衡化 RQ（如 RQ-KMeans、FSQ）比较；tau 没有单独消融，“单层”和“频率惩罚”各自贡献不清。
- 标题说统一召回与排序，但线上只部署在召回阶段、对比的是原召回链路；下游排序是否被替换没有说明（推断：TDN 主要承担召回内部的 code 内排序，最终排序仍是独立模型）。
- 单层码本在千万级商品池下每个 code 平均挂上千个商品，code 内截断（M=30）的损失、16384 个 code token 全量 early-fusion 前向的算力，都需要自己实测。
- α/η/β/λ/μ/tau/γ 等关键超参全部未公开，复现需要自行调参；文中上线时间前后不一致（2 月 vs 1 月），也没有代码。

**落地前检查清单**：(1) 在自家商品池上对比单层 16k 与 RQ 3×256 的召回率和 code 内商品数分布；(2) 扫 tau，同时看资源方差与类目纯度；(3) 评估新品量化时效（论文 1 小时）是否满足大促；(4) 先在召回侧作为新通道 A/B，再考虑把排序头并入。
