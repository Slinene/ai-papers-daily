---
title: 'Beyond Correctness: Benchmarking and Aligning Response Behaviors in Hybrid-Thinking
  MLLMs'
title_zh: 超越正确性：混合思考多模态大模型的响应行为基准与对齐
authors:
- Xinming Wang
- Weinong Wang
- Hongming Yang
- Yansong Lin
- Zheng Ruan
- Shangpin Peng
- Qiming Peng
- Nan Qiao
- Fengyuan Lu
- Guoqing Ma
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- Large Language Model Department, Tencent
- University of Electronic Science and Technology of China
- Hong Kong University of Science and Technology
- Zhongguancun Academy
arxiv_id: '2608.12781'
url: https://arxiv.org/abs/2608.12781
pdf_url: https://arxiv.org/pdf/2608.12781
published: '2026-08-16'
collected: '2026-08-24'
category: Multimodal
direction: MLLM 响应行为对齐与 RL 训练
tags:
- Hybrid-Thinking
- MLLM
- Response Alignment
- RLHF
- Benchmark
one_liner: 提出 PatternEval 诊断基准与 PatternRL 训练框架，缓解混合思考 MLLM 思考/非思考模式响应行为失配
practical_value: '- 混合思考部署模式（如电商客服/推荐 Agent 中快速模式与深度推理模式并存）需监控响应行为一致性，尤其防止 CoT 泄漏暴露内部推理链（可能泄露用户特征或策略细节），论文的
  PatternEval 四类失败可作为线上评测指标。

  - RL 训练阶段引入 pattern-specific penalties（PatternRL）可在不显著影响任务准确率的前提下对齐非思考与思考模式，这种分模式惩罚思路可迁移到生成式推荐中，用于约束不同解码策略（如
  greedy vs. beam）下输出风格一致。

  - 构建评估集时主动注入已知失败模式（failure-enriched）比均匀采样更能暴露模式差异，可用于生成式推荐/Agent 的离线和回归测试，提前发现长尾行为问题。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：混合思考 MLLM 允许单一模型在思考（慢思考）和非思考（快速）推理间切换，两者最终响应应满足相同用户标准；仅评估任务正确性无法刻画响应质量，需关注响应模式失败。
方法：提出 PatternEval，包含 2415 个多模态提示，覆盖视觉感知与定位、结构化图像理解、多模态知识推理，聚焦四类失败：CoT 泄漏、响应重复、逻辑矛盾、表演性推理。在多家模型上诊断发现非思考模式失败率显著更高，导致跨模式系统性失配。基于此提出 PatternRM（响应级奖励模型）和 PatternRL，在强化学习中引入模式特定惩罚，对齐最终响应行为。
结果：在 Qwen3-VL-4B 和 Qwen3-VL-8B 实验显示 PatternRL 能缓解跨模式失配，任务性能损失很小。
