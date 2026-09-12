---
title: 'Beyond Solver Verdicts: Generative Reward Models for Autoformalization'
title_zh: 超越求解器裁决：用于自动形式化的生成式奖励模型
authors:
- Vikash Singh
- Debargha Ganguly
- Aman Goel
- Ali Torkamani
- Xiaoxue Han
- Joseph Lilien
- Ferhat Erata
- Vipin Chaudhary
affiliations:
- Case Western Reserve University
- Amazon Web Services
arxiv_id: '2609.11085'
url: https://arxiv.org/abs/2609.11085
pdf_url: https://arxiv.org/pdf/2609.11085
published: '2026-09-09'
collected: '2026-09-12'
category: Reasoning
direction: Autoformalization · 生成式验证
tags:
- Autoformalization
- Generative Reward Model
- VPU
- Z3
- Test-time Compute
- SAE
one_liner: 将离线 Z3 等价 oracle 蒸馏为生成式连续等价评分，检测 VPU，AUROC 0.961，并带来 11.3 点下游提升
practical_value: '- 把验证器从结构化硬判定升级为连续、参考无关的 reward model：在 query 改写、商品属性约束生成、Agent
  工具调用结果校验等场景，训练一个生成式等价性打分器，能捕捉“执行成功但语义偏移”的失败样本，弥补规则/校验器只查语法和返回码的盲区。

  - 用离线 oracle 蒸馏低成本验证器：电商/推荐里可用大模型、人工标注或仿真环境构造等价/非等价对，蒸馏到轻量 LM 作为 reward model，再用于线上样本过滤、beam
  search 重排或 RLHF-style 优化。

  - 将连续验证分数用于 agentic test-time compute allocation：对候选生成结果按参考等价性评分动态分配采样/回溯预算，比固定采样或仅按
  solver 成功分配更稳；可直接借鉴到多步商品推荐解释、购物 Agent 路径选择。

  - 机制分析 trick：通过 decision-projected logit lens / sparse autoencoders 定位 LM 生成中的错误坐标，可用于诊断商品属性约束生成中“哪个
  token 维度导致不可满足或不一致”，帮助后续提示或微调。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：神经符号系统用数学求解器保证推理正确性，但求解器只检查是否可满足，无法判断形式化翻译与指定形式化是否严格等价。定义 VPU 失败模式：错误编码也能执行成功并匹配预期裁决；理论上证明仅结构/裁决启发式在欺骗性有效轨迹上检测能力退化至随机水平（AUROC≈0.500）。方法：提出 GenV，将离线 Z3 等价 oracle 蒸馏为无参考、连续 reference-equivalence score，复用语言模型原生词汇空间做生成式读出。机制上利用 decision-projected logit lenses 和 sparse autoencoders 显示该读出能够自然提取精确的空间误差坐标，无需显式定位训练。结果：oracle-mined 验证器 GenV+HN 在 reference-equivalence 验证上 AUROC 达 0.961，可零样本泛化到未见翻译器和不同形式化风格，并在 agentic test-time compute allocation 中带来 11.3 点下游精度提升。
