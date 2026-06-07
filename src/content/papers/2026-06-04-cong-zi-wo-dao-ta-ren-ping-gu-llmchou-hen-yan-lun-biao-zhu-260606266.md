---
title: 'From Self to Other: Evaluating Demographic Perspective-Taking in LLM Hate
  Speech Annotation'
title_zh: 从自我到他人：评估LLM仇恨言论标注的视角采择
authors:
- Paloma Piot
- Javier Parapar
affiliations:
- Universidade da Coruña
arxiv_id: '2606.06266'
url: https://arxiv.org/abs/2606.06266
pdf_url: https://arxiv.org/pdf/2606.06266
published: '2026-06-04'
collected: '2026-06-07'
category: Eval
direction: LLM 视角采择与标注公平性评估
tags:
- Hate Speech
- Perspective-Taking
- LLM Evaluation
- Demographic Alignment
- Vicarious Prompting
- Annotation Disagreement
one_liner: 评估LLM模拟人口统计视角在仇恨言论标注中的人类一致性，发现替代提示表现最佳
practical_value: '- 在需要模拟不同用户群体对内容主观判断的场景（如评论审核、风险内容检测）中，考虑使用「替代提示」（vicarious prompting），让模型预测其他群体的判断，可能比直接扮演角色更准确。

  - 简单的最小化身份提示（如“你是一个黑人女性”）并不足以可靠地引发符合人类模式的群体间分歧；在实际系统里，如果需要模拟多样性视角，需要更精细的提示工程。

  - 模拟视角的效果高度依赖模型选择，不同LLM的表现差异大；实际部署前应在目标群体数据上严格评估，不能假设默认能力。

  - 借鉴这种多人口统计视角的评估范式，可以对推荐/生成内容的公平性和包容性进行自动化审查，但需谨慎对待模型对敏感群体的潜在偏见。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机：** 仇恨言论标注高度主观，不同人口统计群体对相同内容的感知差异显著，但收集多群体标注成本高、难以规模化。研究者尝试使用条件于特定人口统计身份的大语言模型（persona-conditioned LLMs）来模拟多样化视角，但尚不清楚这些模型是否真正反映了人类群体的分歧模式。
**方法：** 论文系统评估了LLM模拟人口统计视角的三个核心维度：（1）群体间分歧（inter-group disagreement），即不同身份提示下的模型判断是否产生类似人类的群体间意见分歧；（2）内群体敏感性（in-group sensitivity），即当内容针对自身身份时模型是否变得更敏感；（3）替代预测（vicarious prediction），即模型能否准确预测另一群体的判断。实验使用多种LLM，对比了简单身份提示（如“你是一个黑人女性”）和替代提示（要求模型预测另一群体的反应）两种策略。
**关键结果：** 没有任何模型同时在所有三个维度上表现良好；性能高度依赖具体模型和人口统计轴，简单身份提示无法可靠地复现人类分歧模式。但使用Llama 3.1的替代提示在多数人口统计轴上取得了最高的跨群体一致性，最接近真实人类的分歧模式，表明这一配置可能为与人类判断对齐的自动标注提供了更可靠的设置。
