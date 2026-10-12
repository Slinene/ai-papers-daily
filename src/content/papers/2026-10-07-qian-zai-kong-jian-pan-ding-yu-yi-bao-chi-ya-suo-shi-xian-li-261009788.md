---
title: 'Judging in Latent Space: Efficient Generative Reward Modeling via Semantics-Preserving
  Compression'
title_zh: 潜在空间判定：语义保持压缩实现高效生成式奖励模型
authors:
- Mingqing Yuan
- Xiaobo Liang
- Junwei Yang
- Ziwei Chen
- Zeren Zhang
- Hejin Wang
- Yubin Wang
- Juntao Li
affiliations:
- Soochow University
- University of Cambridge
- Chalmers University of Technology
- Peking University
- Tsinghua University
arxiv_id: '2610.09788'
url: https://arxiv.org/abs/2610.09788
pdf_url: https://arxiv.org/pdf/2610.09788
published: '2026-10-07'
collected: '2026-10-12'
category: LLM
direction: 生成式奖励模型 · 潜在推理压缩
tags:
- Latent Reasoning
- Reward Model
- Semantic Compression
- LLM Judge
- Inference Efficiency
one_liner: LatentGRM 用语义分块与压缩替代逐 token 评估，在保持判断质量下将推理耗时降低 6-7 倍
practical_value: '- 在电商/广告场景中用 LLM-as-a-judge 做数据筛选、候选评分或 A/B 评测时，可借鉴 LatentGRM 的思路：对多准则评价过程做语义分块与压缩，不逐
  token 展开文本，而用连续潜在轨迹完成判断，能显著降低推理成本。

  - 其 rubric-guided 压缩方式可迁移到「相关性+广告质量+商品匹配」等多维度评估 prompt：按准则边界压缩关键语义段，保留任务相关的偏好信息，避免生成冗长解释。

  - vote@k 场景下节省明显：LatentGRM-8B 在 vote@5 时总推理时间降低 6.1-7.0 倍，适合批量生成候选排序信号时的成本控制。

  - 独立解释器从潜在轨迹重建评估文本，提供离线可审计性：生产环境若需追溯 LLM 判断依据，可在不增加在线成本的前提下抽样重建解释。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：LLM 奖励模型做多准则评估时，需要逐 token 生成评估文本，推理成本高。潜在推理研究表明，连续状态可能以更紧凑的方式支持这类计算。

方法关键点：LatentGRM 采用语义分块、压缩与重建三段结构。利用 rubric 引导评估的结构来指导压缩，学习紧凑的连续轨迹，直接支持成对偏好判断，而无需生成文本评估。独立解释器可从轨迹重建评估文本，离线查看压缩后保留的信息。

关键结果：在匹配训练数据和 backbone 的条件下，LatentGRM 在 4B 和 8B 规模上与显式 SFT judge 达到可比的 aggregate preference accuracy。LatentGRM-8B 将评估轨迹压缩 8.9-9.2 倍，在 vote@5 时总 judge 推理时间减少 6.1-7.0 倍，覆盖 RewardBench 与 RewardBench2 多个 domain。受控 rubric 干预实验表明，criterion 相关的偏好信息确实被潜在序列携带。
