---
title: Error Certificates for KV-Cache Eviction via Randomized Design
title_zh: 基于随机设计的 KV 缓存驱逐误差证书
authors:
- Peng Xie
affiliations:
- Technical University of Munich
arxiv_id: '2607.21475'
url: https://arxiv.org/abs/2607.21475
pdf_url: https://arxiv.org/pdf/2607.21475
published: '2026-07-23'
collected: '2026-07-24'
category: LLM
direction: 随机化 KV cache 驱逐实现误差归因
tags:
- KV-cache eviction
- randomized design
- error certificate
- attribution
- survey sampling
- inference
one_liner: 随机化 KV 缓存驱逐使系统能给出每步注意力误差的置信区间，用于归因缓存导致的失败
practical_value: '- 在电商搜索/推荐/Agent 长上下文推理中，采用随机化逐出（如 Poisson 采样尾部 token）并计算误差证书，可在线检测
  KV cache 压缩是否导致注意力偏差，触发全量重算或回退逻辑。

  - 证书虽然预测失败的能力弱于输出 log-probability，但归因能力（AUC 0.73–0.75 vs. 0.47–0.54）可用于调度资源：仅对证书超阈值的高风险请求重新分配计算，避免浪费。

  - 确定性 top-k 驱逐无法自我诊断（Theorem 1），因此生产系统中不应依赖保留状态计算的自检指标；改用随机化设计是从根本上获得可观测性。

  - 工程实现上，可沿用论文的 Hájek 校正（单 logit 偏移）和调查抽样方差估计，无需大幅改动模型推理管线，即可获得每步无偏误差估计和 0.97 经验覆盖率。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：长上下文推理中 KV 缓存通过重要性评分选择 top-k 保留，但确定性驱逐无法知道丢弃信息对当前查询造成的真正误差。论文证明：在保留状态完全相同的情况下，被删除的值可任意改变使得真实注意力输出误差无限大，而所有保留的 key/value/score 均不变，因此任何服务时自诊断器都不一致。

**方法**：引入随机化驱逐，对低重要性 token 以已知概率 Poisson 采样保留，形成包含概率已知的尾部集合。在 softmax 内使用一个 logit 偏移量进行 Hájek 校正，实现无偏注意力估计。再基于调查抽样的方差估计器，利用保留集合计算每步误差的置信区间（certificate），覆盖率达到 0.97，且未增加精度损失。

**关键结果**：预注册的 7 个声明中 3 个被否定——① 问题感知驱逐在 25–50% 预算下几乎无精度代价；② 输出 log-probability 比证书更能预测失败；③ 证书门控的动态预算升级无额外收益。但证书的关键价值在于**归因**：能够分离缓存引起的失败与固有失败（AUC 0.73–0.75），远超输出置信度（AUC 0.47–0.54）；据此调度重计算优于随机或置信门控。结论：随机化不是为了预测，而是为了获得可解释的归因。
