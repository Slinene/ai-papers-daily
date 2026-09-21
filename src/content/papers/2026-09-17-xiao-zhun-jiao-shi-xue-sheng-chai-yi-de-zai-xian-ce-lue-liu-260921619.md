---
title: Calibrating Teacher--Student Discrepancy for On-Policy Distillation
title_zh: 校准教师-学生差异的在线策略蒸馏
authors:
- Qiangqiang He
- Jin Li
- MingCai Chen
affiliations:
- Nanjing University
- Southeast University
- Nanjing University of Posts and Telecommunications
arxiv_id: '2609.21619'
url: https://arxiv.org/abs/2609.21619
pdf_url: https://arxiv.org/pdf/2609.21619
published: '2026-09-17'
collected: '2026-09-21'
category: Training
direction: LLM 在线策略蒸馏 · 教师偏差校准
tags:
- On-Policy Distillation
- Teacher-Student Discrepancy
- Privileged Information
- Reasoning
- LLM Training
one_liner: 提出 Cal-OPD，用正负特权干预估计教师自身偏差区域，只保留超出的差异作为训练信号
practical_value: '- 在业务中用大模型（teacher）蒸馏线上小模型做排序/召回/文案生成时，教师输出里混有自身偏差，尤其当输入包含特权信息（如用户真实意图、后验成交标签）时偏差更大；不要全盘学习教师输出，可借鉴
  Cal-OPD 思路，通过正向/负向干预构造参考区间，只保留超出该区间的差异作为学习目标。

  - 对推荐/广告场景里的生成式特征（如 query 改写、兴趣标签、商品卖点）进行蒸馏时，可以先用提示词注入正确与错误上下文，观察教师输出变化来定位不稳定区域，只对稳定差距做蒸馏，减少噪声传播。

  - 实验表明只保留约 52-65% 的原始差异信号就能稳定超越标准 OPD，说明蒸馏数据不是越多越好，过滤掉教师自身波动能提升小模型泛化和训练效率，可指导工程上对蒸馏样本的筛选策略。'
score: 7
source: huggingface-daily
depth: abstract
---

## 动机
On-policy distillation（OPD）通过学生自己生成的轨迹，利用教师-学生 token 级似然差异提供稠密监督，在数学推理等任务上优于依赖稀疏奖励的 RLVR。但这一差异不只包含师生能力差距，还包含教师自身的偏差：同一个教师在不同上下文或特权信息下会产生似然偏移，这些偏差被标准 OPD 无差别地学习，污染训练信号。尤其在 privileged OPD 中，特权信息会放大教师侧似然偏移，使学生学到更多教师自身偏差。

## 方法
提出 Calibrated On-Policy Distillation（Cal-OPD），核心是估计教师的“自我偏差区域”。方法通过正向和负向特权干预：对同一学生轨迹，分别给教师提供正确和错误的特权上下文，观察教师似然的变化范围，从而界定教师自身波动区域。原始教师-学生差异只保留超出该区域的分量作为优化信号，避免学生模仿教师自身的非能力性波动。

## 结果
在数学推理基准上，Cal-OPD 只保留约 52-65% 的原始教师-学生差异作为优化信号，仍一致优于标准 OPD 及其变体，并在不同模型规模下保持稳定优势。
