---
title: Scaling to Tens of Thousands of Test-Time Iterations with Loop-Native Attention
  Residuals
title_zh: 测试时迭代扩展至数万步的循环原生注意力残差
authors:
- Pengxiang Li
- Dilxat Muhtar
- Di He
- Guinan Su
- Lu Yin
- Shiwei Liu
affiliations:
- The Hong Kong Polytechnic University
- Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences
- Peng Cheng Laboratory
- University of Chinese Academy of Sciences
- ELLIS Institute Tübingen
arxiv_id: '2610.11570'
url: https://arxiv.org/abs/2610.11570
pdf_url: https://arxiv.org/pdf/2610.11570
published: '2026-10-07'
collected: '2026-10-09'
category: Reasoning
direction: 循环 Transformer 测试时迭代扩展
tags:
- Looped Transformers
- Test-Time Compute
- Residual Connections
- Streaming Memory
- Reasoning
- Architecture
one_liner: 提出 InfiLoop 循环原生残差连接，使 7M 模型在数万次测试时迭代中保持推理提升，Sudoku 97.9%，ARC-AGI-2 13.6%
  pass@2
practical_value: '- 对 Agent 多轮推理/工具调用场景：借鉴 InfiLoop 的循环原生残差，在 agent 状态更新中引入 content-based
  weighting + learned temporal decay，保留关键中间推理、抑制噪声 proposal，避免长链路中正确中间状态被覆盖。

  - 工程实现上：exact streaming recurrence 使聚合内存恒定，适合在线推理和流式数据处理；在电商推荐中可用于实时会话状态维护或长期用户行为序列建模，避免循环步数增加带来的记忆膨胀和误差累积。

  - 测试时扩展以小参数（7M）获得显著推理提升，对资源受限的线上推理服务有参考价值：可以设计轻量循环模块，通过增加循环步数而非模型参数来提升复杂 query 理解或多步策略决策能力。

  - 普通 residual connection 在 loop 中可能不够，需要为循环结构单独设计门控残差；具体 trick 是学习每个新更新接受多少、保留多少，而非简单加权平均。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 looped Transformers 随着循环迭代次数增加会出现推理性能下降：噪声状态更新会覆盖正确的中间推理结果，甚至撤销已完成解；错误一旦在早期循环中出现，后续循环难以从已退化的表示中恢复。

**方法关键点**：提出 InfiLoop，一种 loop-native 残差连接，学习保留哪些历史计算、以多大比例接受每个新更新。它结合 content-based weighting 和 learned temporal decay 维持循环状态的运行摘要；精确流式递归保证聚合内存不随循环次数增长。自适应更新机制抑制不可靠 proposal，保留有用中间状态。

**关键结果**：7M 参数 InfiLoop 在多个推理任务上超越现有递归架构：Sudoku-Extreme 精确率 97.9%，ARC-AGI-2 pass@2 13.6%；在 Sudoku-Extreme 上，测试时循环超过 20,000 有效步仍持续提升，证明增加循环深度可直接转化为更强的推理能力。
