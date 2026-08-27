---
title: 'TransRetrieval: Scaling Up Transformer-Based Retrieval for Industrial Recommendation'
title_zh: TransRetrieval：工业推荐 Transformer 召回规模化
authors:
- Zhifei Zheng
- Yunfei Liu
- Bin Liu
- Qiren Zhu
- Hanbing Liu
- Ziru Xu
- Han Zhu
- Jian Xu
- Qi Qi
- Bo Zheng
affiliations:
- Renmin University of China
- Taobao & Tmall Group of Alibaba
- Beijing Key Laboratory of Research on Large Models and Intelligent Governance
- Engineering Research Center of Next-Generation Intelligent Search and Recommendation,
  MOE
arxiv_id: '2608.25528'
url: https://arxiv.org/abs/2608.25528
pdf_url: https://arxiv.org/pdf/2608.25528
published: '2026-08-26'
collected: '2026-08-27'
category: RecSys
direction: 模型化召回 · Transformer 规模化
tags:
- Transformer Retrieval
- Scaling Law
- Feature Aggregation
- Multi-Domain
- Model-based Retrieval
- Industrial Recommendation
one_liner: 通过加权平均聚合、目标 token 压缩与位置式域嵌入，让 Transformer 召回实现 log-linear scaling
practical_value: '- 多值/异构特征进 Transformer 前，用 weighted average 替代 weighted sum 或 concat，可低成本消除
  token norm 随 feature cardinality 增长的问题，避免 attention 被高范数 token 主导；这是一行无参改动，适合先做验证。

  - 模型化召回中，将目标侧特征压缩成单 token 可砍掉约 85% per-candidate FLOPs，再把算力重新投到更深/更宽的用户侧 Transformer，比保留多
  target token + 小 backbone 更划算；压缩后向量也天然适配 HNSW 索引。

  - 多域统一不必用 domain token 或 gate：位置式 domain embedding 逐元素加所有 token，共享全部 Transformer
  参数，稀疏域能吃到跨域梯度，推理时零额外序列成本。

  - 工程上可复用：同一请求所有候选共享用户侧 KV cache 并 broadcast；将单 query token 的多候选打包成 batch 并用 mask
  隔离，解决 GPU 利用率低问题；检索算子全 GPU 化避免 host-device 往返；target compressor 独立成子图，支持 near-line
  增量更新索引。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：工业推荐召回候选池可达 10^8 量级、时延预算只有几十毫秒。传统深度推荐模型简单堆叠 Transformer 会因异构特征导致 token 范数发散，扩展收益递减。已有规模化工作多聚焦排序阶段，模型化召回仍受 per-candidate 前向成本约束，难以放大模型容量。

**方法关键点**：
- **Weighted average aggregation**：对每个 feature field 的 (key, weight) 对按权重平均，而非加权求和，消除输出范数对 feature cardinality 和权重量纲的依赖，恢复 Transformer 依赖的同质 token 假设。
- **Target token compression**：用 3 层 MLP 将目标侧全部特征压缩成单个 D 维 token，per-candidate FLOPs 降低 85%，释放的算力重新投入更深更宽的 Transformer；单 token 也直接作为 HNSW 索引向量。
- **Position-style domain embedding**：学到的域向量逐元素加到所有 token，类似位置编码，不增加序列长度和 attention 复杂度；多域共享全部 Transformer 参数，稀疏域通过跨域梯度受益。
- **工程实现**：同一请求所有候选共享用户侧 KV cache 并 broadcast；将多候选打包 batch 提高 GPU 利用率；检索算子全 GPU 化；target compressor 独立部署支持 near-line 索引更新。

**关键结果**：在 40B 交互、52M items、4 个业务域的工业数据集和公开 KuaiRand 上，TransRetrieval-64D3L 用 0.45 MFLOPs 即超过 production baseline 的 0.576 R@2000，达到 0.603；128D5L 达到 0.657，比 RankMixer-768D-16T 高 12.6 pt，且算力低近两个数量级。从 32D1L 到 128D5L，Industrial 和 KuaiRand 分别提升 +19.3 pt、+22.2 pt，R² 为 0.82/0.88。月在线 A/B 测试平台收入 +2.53%，RPM +1.28%，P99 延迟与 baseline 相同。<br><br>**最值得记住的一句话**：输入条件化比改架构更重要——补齐 token norm 同质性后，压缩目标 token 不是牺牲，而是把算力重新分配到更关键的交叉交互上。
