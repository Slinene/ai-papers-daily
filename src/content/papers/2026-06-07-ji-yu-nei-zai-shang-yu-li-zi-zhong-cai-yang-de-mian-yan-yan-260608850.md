---
title: Intrinsic Selection and Particle Resampling for Inference-Time Scaling Beyond
  Domain Verifiability
title_zh: 基于内在熵与粒子重采样的免验验证推理时扩展
authors:
- Giorgio Giannone
- Mustafa Eyceoz
- Shabana Baig
- Shivchander Sudalairaj
- Anna C. Doris
- Faez Ahmed
- Akash Srivastava
- Kai Xu
affiliations:
- Red Hat
- MIT
- IBM
arxiv_id: '2606.08850'
url: https://arxiv.org/abs/2606.08850
pdf_url: https://arxiv.org/pdf/2606.08850
published: '2026-06-07'
collected: '2026-06-09'
category: Reasoning
direction: 推理时扩展 · 内在熵选择与粒子滤波
tags:
- Inference-Time Scaling
- Entropy
- Particle Filter
- Verification-Free
- Intrinsic Selection
one_liner: 利用样本集的内在尾部熵统计来选择和引导生成，无需外部奖励模型即可实现跨领域推理时扩展。
practical_value: '- **推荐/Agent输出的无奖励模型排序**：iS 利用生成样本的尾部熵中位数进行候选排序，不依赖任何外部解析器或奖励模型，可直接用于
  Agent 多轮规划或推荐结果的二次筛选。

  - **多步推理的步级重采样**：iPF 用 token 熵作为伪观察似然，在推理过程中动态重采样粒子，将计算集中在高置信度轨迹上，适用于困难问题的 Agent
  推理树搜索，可减少无效探索。

  - **特权信息蒸馏以引导约束遵循**：dPF 通过 logit 混合和 KL 引导的重采样，将规则、提示等特权信息注入生成过程，可在电商广告文案生成、合规性要求高的场景中替代昂贵的奖励模型微调。

  - **难度自适应路由**：利用初始样本集的熵统计自动判定问题难度，为简单任务立即用 iS 选优，难题则动态路由到 iPF 或 dPF，可落地为 Agent 工作流中的动态预算分配策略。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

**动机**  
推理时扩展（ITS）在数学、编程等可验证领域已取得显著收益，但在缺乏廉价外部验证器的开放或硬验证领域，如工程设计、临床推理，现有方法严重依赖奖励模型或启发式解析，成本高且脆弱。本文探索如何仅用生成样本集的内在统计量，实现免验证的候选选择和推理引导。

**方法关键点**  
- **内在选择 (iS)**：基于样本集长度分布与逐 token 尾部熵，自适应截取尾部区域，取每样本尾部熵的中位数作为评分，选择熵最小的候选作为最终输出，完全不需输出解析或外部奖励。
- **内在粒子滤波 (iPF)**：将 token 熵指数化作为伪观察似然，在生成过程中对粒子进行重采样，结合 Z-score 归一化，使低熵（高置信）轨迹获得更高权重，从而将计算偏向正确但稀少的推理方向。
- **粒子蒸馏 (dPF)**：在早期步骤用 logit 线性混合融合特权信息（如提示、评分标准），之后用 KL 散度引导的步级重采样，将引导效果蒸馏回自由生成过程，可纠正系统性的早期错误假设。
- **难度估计**：使用固定少量样本的尾部熵均值，以统计分布自动识别高熵难题，为后续计算路由提供依据。

**关键实验与数字**  
在七个数学、推理、编程数据集（AIME、HMMT、GPQA、LiveCodeBench 等）上，使用 Qwen3-4B 评估，**iS 获得最佳中位数 47.7%、加权平均 41.9% 的准确率**，与利用正确答案一致性投票的 Self-Consistency 相当但无需任何形式的验证。在更难 25% 的 AIME 子集上，**iPF 使 pass@1 平均提升 6.1 点（AIME-2026 提升 9.2 点）**。在 CAD 生成任务（Fusion360）上，iS 将 pass@1 的 IoU 从 0.41 提升至 0.45，且随着采样预算增加稳定缩放。在临床推理 HealthBench-Hard 上，**dPF 仅用 8 个粒子就使得分提升 26.5%**（复杂回应主题），iPF 则在健康数据任务上提升 32.2%。实验覆盖文本和多模态架构，证明内在熵是跨模型的鲁棒质量信号。

**核心洞见**  
> 并行样本集的长度调整尾部熵，是无外部验证时区分解质量的可靠信号，并能动态路由计算资源。
