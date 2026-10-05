---
title: Divergence controls entropy in distillation
title_zh: 散度选择控制蒸馏中的熵变化
authors:
- Nicolas Zucchet
- Scott W. Linderman
affiliations:
- Stanford University
arxiv_id: '2610.03529'
url: https://arxiv.org/abs/2610.03529
pdf_url: https://arxiv.org/pdf/2610.03529
published: '2026-10-02'
collected: '2026-10-05'
category: Training
direction: LLM 蒸馏目标的熵效应
tags:
- distillation
- entropy
- forward KL
- reverse KL
- LLM training
one_liner: 证明 forward KL 抬高学生熵、reverse KL 压低熵，散度成为隐式熵正则器
practical_value: '- 蒸馏生成式推荐或 query 生成模型时，按输出分布需求选散度：forward KL 会抬高学生熵，适合增加候选多样性/探索性；reverse
  KL 压低熵，适合需要集中、高置信输出的广告文案、push 文案等场景，但需注意 student-teacher 差距过大时 reverse KL 会欠拟合。

  - on-policy 蒸馏中低熵主要来自 token-level reverse KL，而非 on-policy 采样本身；如果 RL/on-policy 训练后模型行为过于
  deterministic，可以直接调整 token 级散度损失，而不必改动采样数据策略。

  - 使用 interpolated KL 时，训练早期熵变化平滑、收敛时突变；可在训练中监控熵曲线，在收敛前设置早停或动态温度，避免熵崩溃损伤生成多样性。

  - self-distillation 中 teacher 拥有特权特征会降低 student 熵，此时应调节散度超参或 softmax 温度做补偿；在电商 teacher-student
  迁移中，student 无法使用用户实时行为等特权信息时，可提高 forward KL 权重或降低温度以保持输出多样性。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM 蒸馏已广泛用于预训练、后训练，但蒸馏目标中的散度选择如何影响 student 输出分布（熵）尚不清晰。熵关系到生成多样性与探索行为，因此亟需从熵视角厘清散度作用的规律。

**方法关键点**：将蒸馏目标视为 categorical 分布上的散度最小化，重点对比 forward KL、reverse KL 及二者插值；将 cross-entropy 训练视为 forward KL 特例，通过理论证明和在预训练、SFT 中的定量验证，分析 student 熵随训练数据与散度超参的变化；进一步区分 on-policy 采样与 token-level 散度对熵的贡献。

**关键结果**：forward KL 使 student 熵高于 teacher；reverse KL 先降低熵，直到 student-teacher 差距过大而失效；插值 KL 在训练早期平滑改变熵，收敛时则发生突变。on-policy 蒸馏的低熵来自 token-level reverse KL，而非 on-policy 采样本身。self-distillation 中，teacher 使用特权信息会压低 student 熵，最佳散度超参恰好用于补偿这种熵损失，说明散度是隐式熵正则器。
