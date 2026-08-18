---
title: Scaling Domain Data Repetition in LLM Pretraining
title_zh: LLM 预训练中领域数据重复的规模化规律
authors:
- Jingwei Li
- Xinran Gu
- Rui Dai
- Xintong Hao
- Chengyin Xu
- Yan Wu
- Shuran Zheng
- Jingzhao Zhang
affiliations:
- Tsinghua University
- ByteDance Seed
arxiv_id: '2608.14071'
url: https://arxiv.org/abs/2608.14071
pdf_url: https://arxiv.org/pdf/2608.14071
published: '2026-08-13'
collected: '2026-08-18'
category: Training
direction: LLM 预训练数据重复策略
tags:
- LLM Pretraining
- Data Repetition
- Data Mixture
- Scaling Laws
- TPP
one_liner: 固定 TPP 下最优领域重复次数随模型规模略增且与领域验证损失强负相关，可用小模型外推
practical_value: '- 高质量领域数据有限时，不必盲目避免重复：对模型拟合好、验证损失低的领域，可以安全增加重复次数；可先在小模型上观察不同重复率对验证损失的影响，找到临界点。

  - 在数据配比流程中，不要只依据唯一数据量判断领域重要性；用小代理模型（相同 TPP）快速扫描各领域最优重复次数，再将结果外推到大模型，可大幅降低大模型实验成本。

  - 推荐/搜索场景中，若某些高价值目标域（如特定类目、核心 query 意图）数据稀缺，可借鉴该重复策略，但需持续监控验证损失，防止从“低损失高可重复”偏移为过拟合。

  - 工程上可建立“数据重复率—验证损失”曲线作为数据配比决策的轻量工具，纳入预训练/持续预训练的数据准备 pipeline。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 规模增大时，训练 token 预算必须同步增长以维持合理的 tokens-per-parameter 比例（TPP）。但高质量领域数据远不如通用网页数据容易扩展，其混合占比会随总预算增长而下降。重复已有领域数据能缓解稀释，但过度重复会导致过拟合。

**方法关键点**：在训练 token 预算与模型大小成比例增长的 practical scaling 设定下，研究固定 TPP 时不同领域最优重复次数的变化。作者在多个领域、多个模型规模上扫描重复次数，并用较小代理模型（相同 TPP）进行调优外推。

**关键结果**：1）同一领域在固定 TPP 下，最优重复次数随模型规模轻微增加；2）跨领域比较显示，最优重复次数与领域最终验证损失强负相关——损失越低的领域可受益于更多重复；3）唯一领域数据量与最优重复次数仅弱相关；4）小模型上调优的重复次数可作为大模型的实用估计。
