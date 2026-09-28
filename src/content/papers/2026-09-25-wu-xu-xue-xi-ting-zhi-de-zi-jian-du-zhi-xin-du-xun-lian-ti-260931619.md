---
title: 'Learning to Stop without Learning to Stop: Self-Supervised Confidence Training
  Improves Reasoning Efficiency'
title_zh: 无需学习停止的自监督置信度训练提升推理效率
authors:
- Parsa Hosseini
- Akasha Tigalappanavara
- Sumit Nawathe
- Chenrui Fan
- Sourya Basu
- Genta Indra Winata
- Anirban Das
- Soheil Feizi
- Nima Chitsazan
affiliations:
- University of Maryland
- Capital One
arxiv_id: '2609.31619'
url: https://arxiv.org/abs/2609.31619
pdf_url: https://arxiv.org/pdf/2609.31619
published: '2026-09-25'
collected: '2026-09-28'
category: Training
direction: 自监督置信度训练提升推理效率
tags:
- LLM
- reasoning efficiency
- self-supervised learning
- confidence training
- inference cost
one_liner: 自监督置信度训练仅用600题微调，不改变标准生成，最高减少25%推理tokens且精度匹配
practical_value: '- 对推荐理由、Agent规划/反思、query改写等长推理LLM链路，可在不引入长度惩罚或早停的前提下，增加置信度预测头做自监督辅助训练；线上仍用标准解码，避免额外控制逻辑。

  - 中间置信度标签可通过模型自身采样轨迹构造：以最终答案对错/一致性作为软标签，几百条样本即可启动试验，适合业务低成本验证。

  - 若线上有大模型生成链路，可优先在数学/逻辑类子任务（如价格计算、规则校验）复用；推荐主链路需设计点击/转化等业务置信度信号再验证。

  - 论文显示效率提升来自元认知信号，而非抑制某些推理行为；这提示我们保留推理组成，可能比强制缩短更稳。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：推理模型常生成超长推理链，推理成本高。现有方法多靠推理时早停或训练时长度惩罚。本文探索另一条路：用置信度监督。

方法：自监督微调，让推理模型预测自身推理轨迹中间位置对最终答案的置信度；仅使用600道训练题。损失只包含置信度预测目标，不包含推理长度、效率或停止目标。推理阶段保持标准生成流程，不做置信度提取或早停。

结果：在Gemma、Qwen、Nemotron、GPT-OSS等模型上，覆盖数学、科学、代码推理基准，生成tokens最高减少25%，且准确率匹配；效率增益与显式优化短推理的方法相当。分析显示，置信度监督大体保留基座模型的高层推理结构，而非选择性抑制某些行为。

结论：高效推理可能是学习元认知信号的下游结果，无需直接优化效率。
