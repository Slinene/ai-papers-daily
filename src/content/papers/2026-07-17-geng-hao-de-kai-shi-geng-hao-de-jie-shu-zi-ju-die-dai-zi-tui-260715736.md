---
title: 'Better Starts, Better Ends: Bootstrapped Iterative Self-Reasoning Distillation
  for Compressed Reasoning'
title_zh: 更好的开始，更好的结束：自举迭代自推理蒸馏实现压缩推理
authors:
- Leichao Dong
- Dongxu Zhang
- Yiding Sun
- Qirui Wang
- Yuhan Wang
- Lin Chen
- Jihua Zhu
affiliations:
- 西安交通大学
- 北京大学
arxiv_id: '2607.15736'
url: https://arxiv.org/abs/2607.15736
pdf_url: https://arxiv.org/pdf/2607.15736
published: '2026-07-17'
collected: '2026-07-20'
category: Training
direction: 压缩推理 · 自蒸馏
tags:
- reasoning distillation
- on-policy
- self-distillation
- chain-of-thought
- bootstrapping
- efficient inference
one_liner: 提出 BIRD 两阶段自蒸馏，先引导模型生成简洁推理再在线蒸馏，显著减少推理长度同时提升精度
practical_value: '- **多轮对话或 Agent 推理压缩**：两阶段思路可直接迁移——先用简短指令采样高质量响应做 prompt-switch
  SFT，再上线时用在线蒸馏微调，减少冗长推理 token 消耗

  - **搜索/推荐推理链精简**：在需要模型生成多步推理（如用户意图分析、长 query 改写）时，用类似方法抑制冗余验证和自我修正，降低延迟

  - **蒸馏起始状态优化**：避免在噪声前缀上做 KL 蒸馏，先从干净分布启动，再在线策略改进，这对其他在线蒸馏场景（如广告文案生成、商品描述推理）有通用价值

  - **长度控制与准确率权衡**：简洁预热模型可在不牺牲甚至提升精度下大幅缩短输出，可用于实时性要求高的推荐系统推理节点'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：大型推理模型产生冗长的思维链，包含大量冗余推导和自我验证。现有在线策略自蒸馏方法直接匹配学生模型采样前缀与简洁教师，但因模型初期生成的前缀嘈杂、偏离正轨，导致蒸馏效率低。

**方法**：提出 BIRD 两阶段自蒸馏。第一阶段：用简洁指令从基础模型采样正确答案的轨迹，再通过 prompt-switch SFT（用原始任务提示学习这些轨迹），将指令诱导的简洁性内化为模型默认行为，得到预热模型。第二阶段：在此预热模型上执行标准的在线反向 KL 蒸馏，使用一个简洁的自教师模型，此时前缀质量更高，从而更有效地压缩推理。

**结果**：在 Qwen3-8B 上，MATH-500 准确率从 86.2% 提升至 92.0%，平均响应长度从 3099 tokens 降至 1115 tokens，大幅超越提示工程和冷启动在线蒸馏基线。关键发现：改善前缀支持分布是高效推理蒸馏的核心。
