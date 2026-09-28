---
title: 'Just Ask Jev: Reinforcement Learning for Calibrated Decisions as a Zero-Shot
  Detector of AI Alignment Failures'
title_zh: 直接问Jev：强化学习校准决策作为零样本AI对齐失败检测器
authors:
- Ruoqi Guo
- Yi Liu
- Gelei Deng
- Yuekang Li
- Lida Zhao
- Yutao Wu
- Simin Chen
- Ying Zhang
- Leo Yu Zhang
affiliations:
- Griffith University
- Nanyang Technological University
- UNSW
- Deakin University
- George Mason University
arxiv_id: '2609.29429'
url: https://arxiv.org/abs/2609.29429
pdf_url: https://arxiv.org/pdf/2609.29429
published: '2026-09-23'
collected: '2026-09-28'
category: Eval
direction: AI对齐失败检测与基准评估
tags:
- RLCD
- Alignment failures
- Zero-shot detection
- Calibrated decisions
- LLM judge
- AUROC
one_liner: 提出RLCDAlignBench，证明RLCD训练的Jev单次调用零样本检测十类对齐失败，中位AUROC 0.886，成本比LLM judge低63倍
practical_value: '- 借鉴Jev的单次多问题校准概率输出，在内容安全审核或商品合规检测中，用一个轻量判别模型替代LLM judge，一次前向同时输出多个风险标签及置信度，成本降低数十倍，适合在线实时过滤。

  - 将“问什么”与“看什么”分离：设计通用问题模板，通过变化输入字段（如商品标题、描述、用户评论、上下文）快速构建零样本评估器，无需为每个业务场景单独标注数据。

  - 利用校准概率作为触发人工复核的阈值信号，对低置信预测进行抽检，可提前发现标注噪声或数据缺陷，改善训练数据质量。

  - 在Agent安全评估中，采用类似RLCD对齐检测思路，对模型输出进行多维度失败检测（如幻觉、泄露隐私、越权），作为上线前的自动化闸门。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有对齐失败检测器要么是生成式judge需要多次解码，要么分类器每次只能输出一个固定标签，成本和灵活性不足。Jev用RLCD（强化学习校准决策）训练，单次调用能回答多个问题并输出校准概率，但尚未在检测对齐失败上系统评估。

**方法关键点**：提出RLCDAlignBench，覆盖十类对齐失败（谄媚、越狱、欺骗、提示注入、幻觉、隐私泄露、社会偏见、奖励黑客、隐瞒不确定性、权力寻求），包含44个基准、5个目标模型，标签来自各基准评分器及部分人工标注。核心设计是将“问什么”与“看什么”分离：变化问题措辞和答案类型，同时变化输入字段；使用单个通用问题零样本评估。

**关键结果**：单个通用问题中位AUROC 0.886，超过监督基线；问题措辞影响小，上下文更重要，主要通过编码标签的字段起作用；Jev匹配参考评分者与人类标签的一致性，发现现有基准中的标签缺陷，成本比LLM-judge评分器低63倍。
