---
title: Detecting Pretraining Data in Large Language Models from a Free-Energy Perspective
title_zh: 从自由能视角检测大语言模型预训练数据
authors:
- Chenye Ke
- Zirui Liu
- Qi Liu
- Yan Zhuang
- Jintao Zhang
- Zhenya Huang
- Shijin Wang
affiliations:
- State Key Laboratory of Cognitive Intelligence, University of Science and Technology
  of China
- Institute of Artificial Intelligence, Hefei Comprehensive National Science Center
- College of Artificial Intelligence, Nanjing University of Aeronautics and Astronautics
- iFLYTEK AI Research (Central China), iFLYTEK Co., Ltd
arxiv_id: '2609.21888'
url: https://arxiv.org/abs/2609.21888
pdf_url: https://arxiv.org/pdf/2609.21888
published: '2026-09-18'
collected: '2026-09-21'
category: Eval
direction: LLM 预训练数据检测 · 自由能视角
tags:
- Membership Inference
- Pretraining Data Detection
- Entropy Correction
- Free Energy
- Data Contamination
one_liner: 用预测熵修正似然得分，提出自由能检测 ETD，提升预训练数据成员推理的 AUROC 与鲁棒性
practical_value: '- 在生成式推荐或 query 生成模型上线前，可用 ETD 做训练数据泄漏审计：同时取模型输出的 next-token loss
  和预测熵，构造 loss 与 entropy 的倾斜边界，替代单纯困惑度，可降低对高频通用文本的误报，更准确识别是否见过用户历史或私域语料。

  - 做推荐系统评测集污染检测时，把候选 item 描述或用户评论作为文本，计算模型预测该文本的 loss 和 entropy；若 loss 低且 entropy
  也低则可能是被记忆的成员，熵校正能缓解“未见但高可预测”样本被误判的问题。

  - 工程实现轻量：无需训练辅助模型或访问训练集，只需模型 logits 额外计算 token 级熵，容易嵌入现有线上推理链路做实时数据审计或隐私合规监控。

  - 自由能视角提供的“宏观能量转移”可以作为监控指标：当模型在线上新数据上的标准化自由能分数出现异常偏移时，可能预示数据泄露、分布漂移或评测集被污染，可用于告警。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM 预训练数据审计困难，因为高似然既可能来自训练接触，也可能来自强泛化。仅依赖似然 loss 的水平边界容易把可预测的非成员误判为成员。  
**方法**：在预测 loss 与预测熵的联合空间中，引入倾斜边界评估 loss 相对 entropy 的关系。分析表明熵校正能在保留期望成员信号的同时降低方差，改善标准化成员-非成员分离度；进一步推广到非零均值熵差的一般情形。该熵调整分数具备 Helmholtz 自由能解释，由此提出 Energy Transfer Detection (ETD)，从宏观残余自由能转移角度检测预训练数据。  
**结果**：在多样实验设置下，ETD 平均检测性能最优，平均 AUROC 最高提升 3.5%，TPR@5%FPR 最高提升 5.1%，并保持鲁棒性。
