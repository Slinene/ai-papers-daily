---
title: Bayesian Sparse Low-Rank Adaptation for Large Language Model Uncertainty Estimation
title_zh: 贝叶斯稀疏低秩适应实现大语言模型不确定性估计
authors:
- Jijie Zhang
- Zhe Ren
- Quan Zhang
- Dandan Guo
affiliations:
- Jilin University
- Michigan State University
arxiv_id: '2607.02182'
url: https://arxiv.org/abs/2607.02182
pdf_url: https://arxiv.org/pdf/2607.02182
published: '2026-07-02'
collected: '2026-07-03'
category: Training
direction: LoRA 变分贝叶斯稀疏训练 · 不确定性校准
tags:
- LoRA
- Uncertainty Estimation
- Variational Bayesian
- Sparse Masking
- Calibration
one_liner: 在LoRA的秩维度上施加随机掩码实现变分贝叶斯稀疏化，高效校准LLM推理置信度
practical_value: '- 电商/推荐系统中用 LoRA 微调 LLM 做预测时，可直接引入秩维度的随机掩码（如训练时 Dropout 某个 rank
  component）来抑制过自信，无需修改模型主体。

  - 将 DALorRA 的变分贝叶斯训练视为一种轻量集成：推理时多次随机采样子 rank 结构取平均，低成本获得校准后的预测分布，适合线上需要可信度打分的场景。

  - 该工作验证了在仅操作 LoRA 参数的情况下即可实现有效校准，对线上部署友好，可避免昂贵地维护多个模型副本。

  - 方法简单、即插即用，可直接嵌入现有的 LoRA 微调流程（如广告预估、搜索相关性判断等分类/回归微调任务）获得置信度更可靠的输出。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：LLM 微调后常产生过度自信的预测，即使错误也输出高置信度，损害可信部署。传统贝叶斯推断需在全量参数上操作，计算量过大；基于 LoRA 的方法虽轻量，但现有工作在 LoRA 适配器上量化不确定性仍引入较大开销，抵消了 LoRA 的高效性。

方法：提出 **Data-Adaptive Lower-Rank Adaptation (DALorRA)**，核心思想是将不确定性量化从稠密参数空间转移到 LoRA 的“秩”这个轻量级维度。LoRA 本质是多个秩‑1 成分的叠加，可能提供冗余容量。DALorRA 在训练时对每个秩向量施加随机伯努利掩码，实现变分贝叶斯稀疏化：掩码起到模型容量正则作用，并诱导出一个变分后验。推理时通过多次随机采样掩码并对预测平均，得到类似集成的校准效果。该框架无需修改基座 LLM，仅在 LoRA 参数上引入极少量额外计算。

关键结果：在多个推理任务上，DALorRA 的预期校准误差（ECE）和负对数似然（NLL）显著优于确定性 LoRA 及其他基于 LoRA 的不确定性基线，且推理准确率不下降。例如在常识推理上，ECE 相对降低约 30%∼50%，同时保持甚至略微提升精确匹配准确率。消融实验表明稀疏掩码训练是关键，且秩的取舍具有数据自适应性。
