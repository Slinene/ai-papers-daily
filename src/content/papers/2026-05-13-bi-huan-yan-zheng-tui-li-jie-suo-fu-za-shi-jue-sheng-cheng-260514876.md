---
title: Unlocking Complex Visual Generation via Closed-Loop Verified Reasoning
title_zh: 闭环验证推理解锁复杂视觉生成
authors:
- Hanbo Cheng
- Limin Lin
- Ruo Zhang
- Yicheng Pan
- Jun Du
affiliations:
- University of Science and Technology of China (USTC)
- Independent Researcher
arxiv_id: '2605.14876'
url: https://arxiv.org/abs/2605.14876
pdf_url: https://arxiv.org/pdf/2605.14876
published: '2026-05-13'
collected: '2026-05-17'
category: Multimodal
direction: 多模态生成 · 闭环验证推理
tags:
- text-to-image
- reasoning
- reinforcement learning
- distillation
- verification
- test-time scaling
one_liner: 提出闭环验证推理框架，结合自动化数据引擎、PPRL强化学习与DSWM权重融合，解决多步规划幻觉、优化不稳定及延迟问题，性能逼近商业模型。
practical_value: '- **自动化闭环数据引擎**：用步级视觉验证自动筛选可靠推理轨迹，可迁移到电商 Agent 的多步规划数据合成，提升轨迹质量。

  - **PPRL 解决长上下文 RL 不稳定**：将交错多模态历史蒸馏为显式奖励信号，在电商对话代理中可类似处理长对话上下文，稳定策略优化。

  - **DSWM 权重融合加速推理**：将对齐权重与蒸馏先验融合，将每步 denoising 成本从 50 步降至 4 NFE，适合实时推荐/生成场景的低延迟需求。

  - **测试时扩展**：多步验证推理解锁复杂任务能力，电商搜索中的复杂查询理解与多级意图生成可借鉴该测试时扩展范式。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：当前文生图模型多采用单步生成，面对复杂语义时易出现属性混淆、实体丢失等问题；多步推理方法虽有潜力，但存在幻觉无验证、事后反思式优化不稳定、推理延迟过高三大瓶颈。

**方法**：提出 CLVR 框架，核心包含三部分：1）自动化数据引擎，以步级视觉验证闭环生成可靠推理轨迹；2）Proxy Prompt RL (PPRL)，将交错多模态历史提炼为显式奖励信号，解决长上下文优化中的因果归因困难；3）Δ-Space Weight Merge (DSWM)，理论推导的对齐权重与蒸馏先验融合方法，将每步推理的扩散步数从典型 50 步压缩至仅 4 NFE，无需昂贵重蒸馏。

**结果**：CLVR 在 PRISM 等基准上超越现有开源基线，性能接近商业闭源模型，并展现出测试时扩展能力，为复杂视觉生成提供了通用 solution。
