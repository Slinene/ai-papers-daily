---
title: Test-Time Scaling for Diffusion Language Models with Frequency-Aware Remasking
title_zh: 扩散语言模型的测试时缩放：频率感知重掩码
authors:
- Bowen Zuo
- Yue Yu
- Dongruo Zhou
- Yinglun Zhu
affiliations:
- University of California, Riverside
- Indiana University
arxiv_id: '2611.10486'
url: https://arxiv.org/abs/2611.10486
pdf_url: https://arxiv.org/pdf/2611.10486
published: '2026-11-06'
collected: '2026-11-12'
category: Reasoning
direction: 扩散语言模型 · 测试时缩放与重掩码
tags:
- Diffusion Language Models
- Test-Time Scaling
- Remasking
- Inference Compute
- Reasoning
- Decoding Strategy
one_liner: 提出频率感知重掩码，把测试时算力自适应分配给难题，提升扩散语言模型推理准确率与覆盖率
practical_value: '- 把推理预算做成两阶段自适应分配：线上先用低成本解码策略解决简单 query/样本，仅对困难样本启用高成本 diffusion
  remasking/多采样；搜索、推荐和 Agent 场景可按 query 难度或模型置信度做分流，控制平均延迟与算力成本。

  - 用多步解码中的 token 预测翻转频率作为不确定性信号，比单步 entropy/confidence 更鲁棒；可迁移到 Semantic ID 生成、候选标题/文案生成或
  Agent 推理路径搜索中，作为 commit、retry 或触发多路采样的判据。

  - 该方法可视为推理时 wrapper，不改变模型权重；若已有 DLM 或并行解码模块，可低成本试跑 AB，重点观察长尾 hard case 的覆盖率提升。

  - 对生成式推荐中的 token/ID 序列解码，可保留局部未决位置的探索多样性，避免过早固定到模型偏好路径，尤其适合长尾商品/冷启动候选生成。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：扩散语言模型（DLM）推理中，token 的 commit/remask 决策决定输出质量；现有 certainty-aware 策略只看当前步置信度或熵，在困难推理问题上容易误导。

**方法**：将 DLM 测试时缩放建模为推理算力与解码策略的自适应分配。两阶段：先用快速基础采样器解决简单样本；对剩余困难样本启用 frequency-aware remasking。该策略跟踪每个 token 在去噪步骤中预测变化的频率，优先固定高频变化 token，使样本在未决位置产生分叉，避免过早坍缩到模型偏好路径。

**结果**：在 LLaDA-8B-Instruct 和 Dream-7B-Instruct 上，比强 adaptive allocation 基线一致提升：MATH-500 绝对准确率最多 +3.73 / +7.33 个百分点；HumanEval 覆盖率最多 +11.39 / +10.98 个百分点。对 100 次采样后仍未被基线解决的题目，能恢复 3.75%–18.75% 的解法。
