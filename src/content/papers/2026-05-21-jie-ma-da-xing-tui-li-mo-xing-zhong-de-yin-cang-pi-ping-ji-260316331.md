---
title: Decoding the Critique Mechanism in Large Reasoning Models
title_zh: 解码大型推理模型中的隐藏批评机制
authors:
- Hoang Phan
- Quang H. Nguyen
- Hung T. Q. Le
- Xiusi Chen
- Heng Ji
- Khoa D. Doan
affiliations:
- VinUni-Illinois Smart Health Center, VinUniversity
- University of Illinois Urbana-Champaign
arxiv_id: '2603.16331'
url: https://arxiv.org/abs/2603.16331
pdf_url: https://arxiv.org/pdf/2603.16331
published: '2026-05-21'
collected: '2026-05-27'
category: Reasoning
direction: 大型推理模型 · 隐藏批评机制与向量操控
tags:
- Large Reasoning Models
- critique vector
- self-correction
- interpretability
- test-time scaling
- representation steering
one_liner: 发现并操控大型推理模型内部的批评向量，无需训练即可提升自纠和测试时扩展性能
practical_value: '- 在构建多步推理的电商推荐或 Agent 时，可借鉴“插入错误”探测法评估模型自身的错误检测能力，识别推理短板，针对性提升鲁棒性。

  - 提取类似批评向量，在推理阶段通过无训练的表示操控，自动纠正生成式推荐解释或 Agent 规划中的中间步骤错误，提升最终输出质量。

  - 测试时扩展（如多数投票、Best-of-N）中引入批评向量操控，可进一步增强复杂决策链的性能，直接应用于 Agent 多智能体协作或长程推理。

  - 批评向量的存在暗示模型隐式感知错误，可为强化学习微调设计奖励信号：增加对批评向量激活的奖励，增强自我纠错能力。'
score: 8
source: huggingface-daily
depth: abstract
---

**动机**：大型推理模型（LRM）虽展现回溯和自我纠正，但许多行为冗余，真正关键的是其内部错误检测（批评）能力。探究该隐藏机制，以理解并增强自我纠正。

**方法**：向中间步骤注入算术错误，发现模型即使不产生口头修正也能最终输出正确答案，说明存在隐藏批评机制。通过隐藏状态分析，定位到一个可解释的“批评向量”：该向量在错误步骤出现时显著激活，正确步骤则不然。进一步通过操控该向量（在残差流上沿其方向缩放）调节自我纠正行为——增强方向提升检错，削弱方向抑制纠正。

**结果**：在多个推理模型（DeepSeek-R1-Distill-Qwen 系列、Qwen3）和数学推理基准（GSM8K、MATH）上，批评向量操控将错误检测准确率平均提升 10–15%，并在多数投票等测试时扩展方法上带来 2–5% 的增益，全程无需额外训练。该发现揭示了 LRM 内部一致的批评机制，为无训练的性能优化提供了新途径。
