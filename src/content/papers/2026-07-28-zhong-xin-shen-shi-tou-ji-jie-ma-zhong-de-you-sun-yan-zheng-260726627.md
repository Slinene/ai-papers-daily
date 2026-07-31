---
title: 'Revisiting Lossy Verification in Speculative Decoding: Mechanisms, Trade-offs,
  and Failure Modes'
title_zh: 重新审视投机解码中的有损验证：机制、权衡与失效模式
authors:
- Tianyu Wang
- Yuxuan Zhou
- Wenbin Wang
- Heng Li
- Zikai Xiao
- Junyuan Shang
affiliations:
- Independent Researcher
- Baidu Inc.
- Zhejiang University
arxiv_id: '2607.26627'
url: https://arxiv.org/abs/2607.26627
pdf_url: https://arxiv.org/pdf/2607.26627
published: '2026-07-28'
collected: '2026-07-31'
category: LLM
direction: LLM 推理加速 · 有损验证分析
tags:
- Speculative Decoding
- Lossy Verification
- LLM Inference
- Distribution Distortion
- Collaborative Verification
- Truncation-based Verification
one_liner: 将有损验证方法分为截断式和协作式两类，揭示截断式分布失真的性能衰退风险与协作式需控制过度超出的关键准则
practical_value: '- 在电商对话推荐、Agent 推理等延迟敏感场景使用投机解码加速时，应优先选择协同验证等保持分布一致的方法，避免直接用截断式验证造成输出质量剧烈下滑。

  - 若必须用截断式验证（如严格时间限制），需通过校准目标概率与草案概率的差距，设置阈值避免过度截断，减少分布失真。

  - 评估加速效果时，务必以真实的目标模型采样（而非错误基线）作为对照，否则会严重误判方法优劣。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：投机解码通过小模型提案、大模型并行验证来加速 LLM 推理。近期出现的“有损验证”进一步放松分布匹配以换取更高效率，但这种放松会悄悄改写解码分布，导致生成质量不稳甚至严重退化。缺少对这类方法机理与风险的透彻分析。

**方法**：论文系统推导了有损验证产生的有效分布，将现有方法归为“截断式验证”（基于概率截断）和“协作式验证”（草案与目标概率混合）两类。设计了一套诊断评估框架，在数学推理与困难知识基准（GSM8K,MATH,AIME）上衡量加速效果与质量损失，并揭示常用基线选择的陷阱。

**关键结果**：截断式验证由于分布失真，其实际精度显著低于“真实截断采样”基线，且任务越难，差距越大（如 AIME 上 SOTA 方法与真实基线相差 6.67 个百分点）。如果误用目标模型原始分布作为基线，则会错误地给出质量提升的结论（偏差可达 6.67 点）。协作式验证的关键在于控制草案概率相对目标概率的“过度超出”，否则会大幅增加低质量 token 的风险。
