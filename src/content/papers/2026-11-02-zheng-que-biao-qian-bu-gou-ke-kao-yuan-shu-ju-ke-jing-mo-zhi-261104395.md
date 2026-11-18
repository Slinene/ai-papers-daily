---
title: 'Correct Labels Are Not Enough: Reliable Metadata Can Silently Control Model
  Behavior'
title_zh: 正确标签不够：可靠元数据可静默控制模型行为
authors:
- Renee Jia
- Jinzhou Wu
affiliations:
- R2M AI
- Cornell University
arxiv_id: '2611.04395'
url: https://arxiv.org/abs/2611.04395
pdf_url: https://arxiv.org/pdf/2611.04395
published: '2026-11-02'
collected: '2026-11-18'
category: Training
direction: LLM 训练数据偏差与 cue-following
tags:
- metadata
- cue-following
- fine-tuning
- model behavior
- shortcut learning
- adversarial audit
one_liner: 可靠元数据即使标签全对，也会让模型学会跟随线索，测试时移动该元数据可致 97-100% 错误选择
practical_value: '- 在电商/广告/搜索推荐 LLM 微调中，常将 reward model 分数、质量标签、CTR 等作为输入特征，这些元数据若与
  label 强相关，极易诱发 shortcut。上线前应做 adversarial audit：固定候选集和真值，随机移动或删除可见元数据，观察生成结果是否跟随；即使移除元数据后指标不掉，也不能证明模型没有依赖。

  - 训练侧降低元数据可靠性，例如对 reward/quality 字段加噪声、随机遮挡、以一定概率替换为中性词，或限制其注意力，能显式抑制模型对单一强线索的依赖；但论文显示中性/无意义词仍可能被利用，所以需要结合测试期审计。

  - 评估体系要包含“错误元数据”测试集，不能只看标准 set；尤其做 DPO / RM 融合时，option-level score 也会受到 cue 影响，需检查打分是否被文本中的数字、标签等
  shortcut 控制。

  - 对搜索推荐 Agent 的 prompt 设计，不要在上下文里放直接预测答案的强特征（如“高质量”标记、排名字段），如果需要使用，建议作为模型不可见的外部控制而非文本元数据。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：微调数据常包含能预测正确答案的元数据（如 reward model 分数、质量标签），即使所有训练标签正确，模型也可能学会跟随元数据而非真正解决任务；移除元数据后准确率仍高，传统评估会漏掉这种依赖。

**方法关键点**：在多项选择任务中，训练时设置 `(Reward: 5)` 始终标记正确选项，并变化该注解在训练时的可靠性；测试时移动或移除注解、固定问题和正确选项，观察模型是否跟随。微调 7-9B 开源模型（三个家族），数据集为 CommonsenseQA；进一步在 Qwen3 上做 DPO 实验，检查选项字母分数的 cue 依赖。

**关键结果数字**：测试时将 `(Reward: 5)` 移到错误选项，模型在 97-100% 的 CommonsenseQA 样本上选择错误选项；移除注解后多数答案仍正确，说明仅看无注解准确率会漏掉依赖。cue-following 随训练可靠性急剧上升，即使中性或无意义词也产生依赖，测试措辞影响强度；DPO 后同样存在选项字母分数的 cue 依赖。结论：正确标签不足以保证模型不利用可见元数据，审计应主动移动或移除注解来测试。
