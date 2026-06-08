---
title: 'From Correctness to Utility: Gain-Based Prefix Evaluation for LLM Reasoning'
title_zh: 从正确性到效用：基于增益的LLM推理前缀评估
authors:
- Yuhang Zhou
- Yixin Cao
- Guangnan Ye
affiliations:
- Fudan University
- Shanghai Innovation Institute
arxiv_id: '2606.07190'
url: https://arxiv.org/abs/2606.07190
pdf_url: https://arxiv.org/pdf/2606.07190
published: '2026-06-05'
collected: '2026-06-08'
category: Reasoning
direction: 过程监督 · 前缀效用评估 · 数学推理
tags:
- Prefix Evaluation
- Process Supervision
- Gain-based Utility
- Mathematical Reasoning
- Best-of-N
- Reinforcement Learning
one_liner: 用轻量级学生模型群估计前缀对求解率的边际增益，训练前缀效用模型，在Best-of-N、束搜索和RL中均有效提升推理性能。
practical_value: '- **用轻量模型群估计前缀效用**：无需人工标注步骤正确性，通过对比有/无前缀时多个小模型的解题率变化得到增益，再转为偏好对训练评估模型。电商场景中，对用户行为序列的部分轨迹（例如浏览前缀）评估能否提高最终转化率，类似地可采用轻量模型群采样转化率增益来构建排序信号。

  - **增益偏好对构建训练数据**：将前缀效用差转为 pairwise 偏好，使用 Bradley-Terry 损失训练标量评估头，过滤掉高噪声对比对。在生成式推荐中，评估生成物品序列的中间状态效用时，可用同样方法从偏好对中学习价值模型，避免直接回归噪声大的转化率。

  - **提供过程级监督缓解RL稀疏奖励**：将前缀效用差作为过程优势（dense advantage），与稀疏的最终答案奖励结合，稳定RL训练且防止reward
  hacking。Agent 行为决策中，可对子任务完成度建立类似的增益模型，提供中间奖励以加速策略学习。

  - **弱到强泛化**：方法训练出的前缀效用模型能迁移到更强的策略模型，且支持按下游模型能力调整学生模型权重。这意味着在业务中，可用低成本小模型群构建评估信号，再去指导更强大的生产模型的行为搜索或生成。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：推理前缀影响LLM的后续解题轨迹，现有过程评价方法（如PRM）基于局部步骤正确性，但正确性并非直接等价于前缀对最终成功的贡献。本文提出“增益”定义：前缀p带来的下游解题概率的边际提升（有p与无p的求解率差）。这一指标更直接地衡量前缀对解决问题的帮助，且与问题难度、模型先验能力解耦。

**方法关键点**：
- 使用6个轻量级学生模型（约2B大小）作为探针，分别采样有前缀p和无前缀时的解题轨迹，计算每个学生的增益 `gs(x,p) = qs(x,p) - qs(x,∅)`，得到跨能力等级的增益分布。
- 将增益分布标准化后取平均作为“内在效用”目标，构建280K个 pairwise 偏好对（垂直对比同轨迹不同截断点、水平对比不同轨迹等长前缀），并用自适应边界和冲突过滤确保标签可靠。
- 基于 Bradley-Terry 损失训练 Prefix Utility Model (PUM)，在 Qwen3-4B 骨干上加 MLP 值头，输入问题+前缀，输出标量效用分数。
- 训练数据仅需约20K条推理轨迹和6.72M学生模型续写，对比 Math-Shepherd 节省约18.5倍标注计算量，且无需人工步骤标注。

**关键实验结果**：
- Best-of-N 选择：在 MATH500、GAOKAO2023、AIME2025 上，PUM 在 N 较大时（N≥32）明显优于 PRM 和 PQM，并提升最差正确排名和最佳错误排名，表现出更鲁棒的轨迹排序。
- 束搜索：在 MATH500 和 GAOKAO2023 上，PUM 在全部搜索预算下均最优，随预算增大优势更显著（MATH500 上 Qwen 策略 N=100 时达78.00%）。
- 强化学习：PUM 提供的过程优势与 GRPO 结合，在多个数学基准上加权平均准确率从55.21%提升至58.09%；纯过程奖励时 PUM 仍稳定到57.21%，而 PRM/PQM 出现 reward hacking 导致性能坍塌。在起始无正确解的高难问题上（DAPO-Math 子集），PUM 的训练速度是 GRPO 的5.4倍。

**一句话**：以前缀对下游求解率的边际增益替代步骤正确性，训练出的前缀效用模型作为一种过程监督信号，更稳定、更具迁移性，在搜索和RL中显著提升了推理性能。
