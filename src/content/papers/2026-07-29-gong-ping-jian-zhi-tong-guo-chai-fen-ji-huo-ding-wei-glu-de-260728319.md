---
title: 'Fairness Pruning: Locating Demographic Bias in GLU-MLP Layers via Differential
  Activations'
title_zh: 公平剪枝：通过差分激活定位GLU-MLP层中的人口统计偏见
authors:
- Pere Martra
- Eugenio Martínez Cámara
- Alfonso Ureña López
affiliations:
- Universidad Internacional Menéndez Pelayo
- Universidad de Jaén
arxiv_id: '2607.28319'
url: https://arxiv.org/abs/2607.28319
pdf_url: https://arxiv.org/pdf/2607.28319
published: '2026-07-29'
collected: '2026-08-02'
category: LLM
direction: LLM 偏见定位与结构性干预
tags:
- fairness
- bias mitigation
- mechanistic interpretability
- differential activation
- GLU-MLP
- neural pruning
one_liner: 提出一种轻量级结构干预方法，利用差分激活定位LLM中与人口偏见相关的极少神经元，剪枝即可解耦偏见与能力
practical_value: '- 差分激活定位方法可迁移到推荐/对话模型中，用于定位特定行为（如价格敏感、品牌偏好）的神经元回路

  - 极少量神经元剪枝（<0.031% 参数量）即能改变模型输出，启发在保持主任务性能下进行精细行为干预，对模型压缩和可控生成有参考价值

  - 发现偏见神经元存在正负双向性，提示未来可分别调制“推高偏见”与“压低偏见”的神经元，实现定向公平性控制

  - 该工作完全基于推理时激活捕获，无需重新训练，适合快速在已有LLM推荐或文案生成管线中做偏见审计与干预'
score: 6
source: huggingface-daily
depth: abstract
---

**动机：** 大语言模型(LLM)会从训练语料中习得并放大人口统计偏见，现有缓解方法往往重训练成本高或定位不够精细。本文提出一种轻量级结构干预方法“公平剪枝”，旨在精准定位并操纵偏见神经元，同时保持模型能力。

**方法：** 设计最小对比提示对（仅人口属性词不同），在GLU架构的down_proj输入捕获激活值，计算差分激活并排序，识别对特定人口群体（如性别、种族）响应差异显著的神经元。通过置零这些神经元（结构化剪枝）来干预。使用CrowS-Pairs等基准评估偏见，并监控推理与常识能力变化。

**关键结果：** 在Llama-3.2-1B上仅剪枝40个神经元（<0.031% MLP宽度），模型推理和常识能力保留率高达99.49%，但偏见方向出现双向不稳定：无符号BiasScore混合了对刻板印象有相反推动作用的神经元，导致整体偏见指标变化取决于哪个方向的神经元主导。这实证了偏见处理与通用能力在回路层面是可分离的，并揭示了从简单置零转向定向行为调制的必要性。
