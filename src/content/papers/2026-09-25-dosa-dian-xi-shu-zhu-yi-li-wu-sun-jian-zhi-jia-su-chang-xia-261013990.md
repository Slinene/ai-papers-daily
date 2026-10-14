---
title: 'DoSA: Dots Sparse Attention'
title_zh: DoSA：点稀疏注意力无损剪枝加速长上下文索引器
authors:
- Fanxu Meng
- Taosong Fang
affiliations:
- Dots Studio, Xiaohongshu Inc.
arxiv_id: '2610.13990'
url: https://arxiv.org/abs/2610.13990
pdf_url: https://arxiv.org/pdf/2610.13990
published: '2026-09-25'
collected: '2026-10-14'
category: LLM
direction: LLM 稀疏注意力推理加速
tags:
- Sparse Attention
- Indexer
- Top-K
- LLM Inference
- GPU Kernel
- Lossless Pruning
one_liner: 为有符号多哈希索引器构建可证上界，利用种子阈值无损筛除多数 key，避免全头打分，长上下文预填充最高快 2.74 倍
practical_value: '- 在长用户行为序列/商品库的 LLM 检索或生成式推荐中，可借鉴“种子阈值+分数上界”的无损剪枝：先用少量头部或代理模型计算上界，只对可能进入
  Top-K 的候选项算完整分，避免全量打分。特别适合有符号多目标融合打分，负头不能简单丢弃时，用激活频率支撑聚合保住下界紧度。

  - 工程实现可复用：将剪枝与 GPU kernel 融合，规则 screening 用 Tensor Core，SIMT 做 bound 评估和候选 compact；refinement
  阶段同组查询共享 key 加载，稀疏写回只写达到阈值的记录，明显降低 HBM 带宽。若自建长上下文检索/推荐打分服务，这套数据流可直接参考。

  - 成本分析给了一个重要信号：上下文越长，选择 token 的索引器占比迅速上升（~1M 时 73%-90.8%），加速索引器比加速注意力本身收益更大。用 Amdahl
  定律可提前估算优化收益，避免把力气花在低占比模块。

  - 解码阶段利用时间相干性，用近期选中 key 的分数做阈值下界，压缩选择输入，这种“候选记忆 + 阈值预测”思路可迁移到实时推荐/搜索的候选生成与重排中，减少重复打分。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长上下文 LLM 推理中，稀疏注意力旨在减少 attention 计算，但选择哪些 key 的索引器本身仍需对每个 key 计算所有 head 分数，形成 dense scoring 瓶颈。在 ~1M token 时，索引器占 prefill GPU 时间 73.0%（GLM-5.2）到 90.8%（DeepSeek-V3.2），其占逻辑 FLOPs 比例也接近一半以上。现有 Top-K 加速方法（如 LiteTopK）仍要全头打分，MISA 用少头筛会漏掉候选。因此需要一种无损方法避免全头打分。

### 方法关键点
- 对 signed ReLU 索引器，构建分数上界 U_i：评估保留头 R，为正头用非负投影+残差联合边界，为负头用聚合下界。
- 种子阈值 τ：从可见 key 中取 K 个种子，其第 K 大分数是真实 Top-K 阈值的下界。若 U_i < τ，安全拒绝 i。
- 正头投影：q_h 分解为 β_h q_j + d_h，利用 ReLU 次可加性和 Cauchy-Schwarz 得到 bound；折叠权重 e_w_j 复用已算点积；残差使用联合 allowance。
- 负头聚合：选择激活频率 p_h ≥ 1/2 的负头聚合，避免 inactive head 因 ReLU 前抵消而减弱下界。
- 只对通过筛选的候选计算完整 H 头分数，只写回分数 ≥τ 的记录，确保 exact Top-K。
- GPU kernel：规则 screening 用 Tensor Core，SIMT 评估 bound、compact survivors；refinement 阶段同组查询共享 key 加载，减少 HBM 传输。

### 关键结果
- 微基准（GLM-5.2，128K-1M 上下文，60 配置）：完整 Indexer 相对 SGLang 最高 2.74×，相对 LiteTopK 最高 1.69×；1M 时分别 2.47-2.74× 和 1.47-1.69×。
- 端到端 TTFT（TP8）：GLM-5.2 和 DeepSeek-V3.2 在 1M token 分别相对 SGLang 1.86× 和 1.94×，相对 LiteTopK 1.26× 和 1.50×。
- 消融：screening 单独减少 37.4% 延迟，sparse writeback 单独 23.4%，两者结合 47.3%（1.90×）。移除负头聚合使候选存活率从 2.65% 升至 95.06%，延迟增 9.51×。

### 最值得记住的一句话
有符号多头索引器做 Top-K 选择时，不必为每个 key 计算完整分数，只要有种子阈值和紧的分数上界，就能无损地筛掉绝大多数 key，把计算集中在可能胜出的候选上。
