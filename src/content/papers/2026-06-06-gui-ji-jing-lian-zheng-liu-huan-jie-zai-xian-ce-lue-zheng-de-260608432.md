---
title: Trajectory-Refined Distillation
title_zh: 轨迹精炼蒸馏：缓解在线策略蒸馏的前缀失效
authors:
- Li Jiang
- Haoran Xu
- Yichuan Ding
- Amy Zhang
affiliations:
- McGill University
- Mila Quebec AI Institute
- University of Texas at Austin
arxiv_id: '2606.08432'
url: https://arxiv.org/abs/2606.08432
pdf_url: https://arxiv.org/pdf/2606.08432
published: '2026-06-06'
collected: '2026-06-09'
category: Training
direction: LLM 在线策略蒸馏 · 轨迹级纠正
tags:
- On-policy distillation
- Prefix failure
- Trajectory refinement
- LLM reasoning
- Knowledge distillation
one_liner: 提出轨迹精炼蒸馏(TRD)，由教师修正学生生成的错误前缀后再进行蒸馏，突破token级干预局限
practical_value: '- 在线蒸馏中，直接对错误轨迹做逐token KL会导致监督退化；可借鉴TRD思路：先用强模型（教师）修正学生生成的整个推理轨迹，再蒸馏，以根治前缀错误。

  - 正向KL配合全词表匹配在蒸馏中更稳定，避免模式崩塌；在电商Agent的生成式推理训练中可优先采用此损失形式。

  - 自蒸馏时，利用参考答案等特权信息生成精炼轨迹，能在不增加外部模型的情况下有效提升学生推理能力和探索宽度。

  - 精炼轨迹通常更简短，可缩短训练序列、降低算力开销，适合大规模工业蒸馏任务。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：在线策略蒸馏(OPD)在LLM后训练中广泛使用，但存在前缀失效问题：当学生模型生成错误推理前缀时，逐token KL监督使教师分布变成双峰混合，梯度碎片化，无法沿正确修正路径传播监督。现有token级损失重加权或截断无法修复失败前缀本身，导致监督信号退化甚至消失。

**方法关键点**：
- 提出轨迹精炼蒸馏(TRD)：先让学生生成原始轨迹yo，再让教师以yo和参考答案为上下文生成精炼轨迹yr，最后在yr上计算逐token KL进行蒸馏。
- 通过教师重写失败前缀，将监督上下文从冻结的错误路径转移到连续的正确修正路径上，恢复理想梯度结构。
- 同时适用于OPD和自蒸馏(OPSD)；OPSD中教师与学生共享参数，仅通过特权信息（参考答案）进行精炼。
- 蒸馏损失采用正向KL和全词表匹配，提供模式覆盖监督，稳定训练。

**关键结果**：
- 在AIME24/25、HMMT25、BeyondAIME、AMOBench等五个竞赛数学基准及代码任务上，Qwen3-1.7B/4B/8B模型上TRD均取得最佳Avg@16，尤其在AMOBench上Qwen3-8B OPSD的Pass@16相对提升约50%。
- 训练数据分析显示，TRD将轨迹验证准确率从65.8%提升至81.4%，且大幅压缩推理长度，训练效率提升约60%。
