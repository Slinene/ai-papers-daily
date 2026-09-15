---
title: 'DataFlex-RL: An Evaluation Platform for RLVR Data Policies'
title_zh: DataFlex-RL：RLVR 数据策略评估平台
authors:
- Hao Liang
- Mingrui Chen
- Hengyi Feng
- Meiyi Qiang
- Wentao Zhang
affiliations:
- Peking University
- UCAS
- Institute for Advanced Algorithms Research, Shanghai
- Zhongguancun Academy
arxiv_id: '2609.06107'
url: https://arxiv.org/abs/2609.06107
pdf_url: https://arxiv.org/pdf/2609.06107
published: '2026-09-04'
collected: '2026-09-15'
category: Training
direction: RLVR 训练数据策略评测
tags:
- RLVR
- GRPO
- data policy
- evaluation
- LLM
- training data
one_liner: 构建统一 GRPO 配方下评估 RLVR 数据策略的平台，发现选择/加权/自适应策略相比均匀采样无可复现提升
practical_value: '- 在电商/推荐/Agent 场景中用 RLVR 训练生成式推荐、Query 推荐或文案生成时，均匀采样是强 baseline；引入任何
  rollout 选择或加权策略前，先按统一超参多 seed 配对检验，避免无效复杂化。

  - 评估指标集合对策略排名影响极大：仅用部分业务指标（如只看点击不看转化或多样性）可能导致排名负相关；需要领域平衡的综合指标，并在上线前检查指标选择是否稳健。

  - 可复用 DataFlex-RL 开源平台作为内部 RLVR 数据策略 A/B 测试模板，快速验证新数据策略是否真的带来可复现提升。

  - 自适应多域混合不优于固定等权混合，在多任务/多场景推荐中不要盲目上自适应采样权重的复杂设计，先确保数据质量和训练稳定性。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：RLVR 数据策略（rollout 选择、加权方式、多域混合）直接决定训练批次构成，但缺乏统一评估，不清楚哪些策略真正带来可复现提升。

**方法关键点**：推出 DataFlex-RL，固定 GRPO 配方，比较 13 种数据策略配置；主实验用 Qwen2.5-7B-Base，12 个匹配种子，覆盖 12 个数学、逻辑、科学基准；另在 Llama-3.1-8B-Base 做 12 seed 扩展，并分析评价指标敏感性。

**关键结果**：均匀 GRPO 相比未训练 checkpoint 提升领域平衡平均准确率 7.76 个百分点；8 种 rollout 选择/加权方法相对均匀采样的配对 95% 置信区间均不排除零；3 种自适应混合未能在同等精度下超越固定等权混合；扩展实验无一致赢家；将评价从 12 基准换成 6 基准（5 数学 + GPQA-Diamond，无逻辑）导致排名负相关（ρ = -0.33），而保留全部 12 基准则排名基本一致。

结论：在受控设置内，改变数据策略确实改变训练过程，但未产生相对均匀训练的可复现提升。
