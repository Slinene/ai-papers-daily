---
title: 'RoboTALES: Learning Reasoning-Guided Robot Policies via Task-Aligned Simulated
  Futures'
title_zh: 'RoboTALES: 用任务对齐模拟未来学习推理引导的机器人策略'
authors:
- Hanan Gani
- Tejal Kulkarni
- Madhoolika Chodavarapu
- Nicklas Hansen
- Manmohan Chandraker
affiliations:
- University of California, San Diego
arxiv_id: '2607.06018'
url: https://arxiv.org/abs/2607.06018
pdf_url: https://arxiv.org/pdf/2607.06018
published: '2026-07-06'
collected: '2026-07-12'
category: Agent
direction: LLM/VLM 协同推理与视频想象策略
tags:
- LLM Planner
- VLM Critic
- Video Generation
- Hierarchical Reasoning
- Policy Learning
- World Model
one_liner: 提出层次LLM规划器与VLM批评家联合引导视频生成，使机器人策略在长视野操作任务上显著优于现有方法
practical_value: '- **层次化LLM任务分解可用于复杂推荐流程**：将多步推荐（如先吸引兴趣再推荐买点）拆解为子目标序列，指导生成式模型逐步生成商品描述、话术或创意，提升过程可控性。

  - **VLM critic 反馈对齐生成目标**：在文案/素材生成中引入视觉-语言模型做“想象结果”评估，通过 reward 微调内部表征，让生成内容更贴合最终转化意图，类似
  RLHF 但针对多模态生成。

  - **单阶段端到端训练框架**：无需预训练视频模型分离，直接把规划、想象与策略学习串联优化，适合将 Agent 的规划模块与执行模块联合训练，减少模块间误差累积。

  - **用生成式模型做“世界模拟器”**：在推荐系统中，可以预测用户兴趣演化轨迹（想象未来行为），据此提前布局推荐序列，类似用扩散模型生成用户状态 rollouts。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：预训练视频生成模型用于视觉运动控制时，其“想象”的观察演变常常偏离任务意图，且动作条件不可靠，导致难以提取策略或进行规划。人类则善于先分解任务、再想象未来并筛选行动，这促使作者设计一个能对齐任务目标的推理引导框架。

**方法关键点**：提出单阶段框架 RoboTALES，核心是：1）层次化 LLM 规划器，将复杂操控任务自动分解为一系列子目标（如“打开抽屉→拿起物体→放入抽屉”），用自然语言子目标序列指导视频生成模型的未来想象；2）VLM 批评家，对生成的想象视频评估任务完成度并产生奖励信号，该奖励直接反馈到生成模型的隐藏表征，使其内部状态持续聚焦于最终目标。视频生成采用扩散模型，在规划器和批评家共同约束下单阶段训练，输出既对齐任务又时间一致的想象轨迹，然后直接从中解码动作。

**关键结果**：在 RoboCasa 和 LIBERO10 的多类操作任务上评估，尤其在长视野任务中，RoboTALES 一致优于现有 baseline（包括 SuSIE、RT-1 等）。例如在 RoboCasa 长任务平均成功率提升 15-20 个百分点，消融实验验证了 LLM 规划器和 VLM 批评家均对性能有显著贡献。
