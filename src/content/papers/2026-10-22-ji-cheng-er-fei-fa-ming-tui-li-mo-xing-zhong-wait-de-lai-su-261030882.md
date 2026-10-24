---
title: 'Inherited, Not Invented: Tracing the Provenance of Wait in Reasoning Models'
title_zh: 继承而非发明：推理模型中 Wait 的来源追溯
authors:
- Zhizhuo Kou
- Sizai Hou
- Long Chen
- Jian Yang
- Junyu Luo
- Jingshu Peng
- Wenkai Zhang
- Sirui Han
- Yike Guo
affiliations:
- The Hong Kong University of Science and Technology
- Peking University
- Huawei Noah’s Ark Lab
arxiv_id: '2610.30882'
url: https://arxiv.org/abs/2610.30882
pdf_url: https://arxiv.org/pdf/2610.30882
published: '2026-10-22'
collected: '2026-10-24'
category: Reasoning
direction: LLM 推理行为训练溯源 · RL 角色
tags:
- RL
- reasoning
- LLM
- training data
- evaluation
- revision marker
one_liner: 通过追踪开放模型训练历史，证明 wait 等修订标记主要继承自训练数据而非 RL 凭空创造
practical_value: '- 训练推理型 Agent 时，显式在 SFT 数据中加入“wait/reconsider”等自我修正 trace，不要寄希望于
  RL 后期涌现；RL 只能放大已有行为，不能无中生有。

  - 对线上 LLM 推理/推荐 Agent 做行为归因时，用无标签指标（标记频率、位置、形式、注入错误后是否触发）替代主观印象；marker 频率不应单独作为“推理增强”的
  KPI。

  - 评估 query 改写、解释生成或自检质量时，谨慎使用 LLM-as-judge：自动裁判可能反转人工标注趋势，建议人工抽检或多种 judge 交叉验证。

  - 复现或调 RL 配方（如 GRPO）时，先检查基础模型是否已含目标语言行为、是否带 KL 约束；这些因素决定 RL 是放大、不变还是擦除该行为，影响线上文案/推荐解释的风格一致性。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：RL 被广泛认为教会模型在重新考虑某一步前写下 wait，但大 RL 精度提升并不需要这个词。这混淆了 RL 发现与模型从训练数据中继承的行为，需要追溯该标记的真正来源。

**方法**：追踪多个开放模型的训练历史，使用无需人工标签的指标——频率、位置、形式、用法及注入错误测试，全部从采样输出中计算。

**关键结果**：zero-RL 几乎不创造 wait：在缺少该词的基础上，RL 显著提升 MATH-500 准确率，但 wait 仍接近缺失。该词随训练数据出现：在 OLMo-3 中期训练中出现，对缺少该词的模型用推理轨迹做 SFT 也能安装 wait。若基础模型已使用该词，两种已发布的 RL-Zero 配方（OLMo-3、MiMo）会使其成倍增加，而同一基础模型的 KL-free GRPO 不增加。OLMo-3 配方会磨损其形式，使其成为更敏感但更宽松的警报；SFT 后接 RL 几乎不改变它，而 GRPO 配方会擦除由 SFT 播种的 marker。此外，marker 频率不能单独指示 RL 诱导的推理，且要警惕 LLM-as-judge 修订指标，因为自动裁判可能反转人工标注趋势。
