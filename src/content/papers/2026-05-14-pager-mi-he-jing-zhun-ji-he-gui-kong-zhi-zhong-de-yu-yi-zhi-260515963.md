---
title: 'PAGER: Bridging the Semantic-Execution Gap in Point-Precise Geometric GUI
  Control'
title_zh: PAGER：弥合精准几何 GUI 控制中的语义-执行鸿沟
authors:
- Jingxuan Wei
- Xi Bai
- Shan Liu
- Caijun Jia
- Zheng Sun
- Xinglong Xu
- Siyuan Li
- Linzhuang Sun
- Bihui Yu
- Conghui He
affiliations:
- University of Chinese Academy of Sciences
- Shanghai Artificial Intelligence Laboratory
- China University of Petroleum-Beijing
arxiv_id: '2605.15963'
url: https://arxiv.org/abs/2605.15963
pdf_url: https://arxiv.org/pdf/2605.15963
published: '2026-05-14'
collected: '2026-05-18'
category: Agent
direction: 精准 GUI 代理 · 像素级控制
tags:
- GUI Agent
- Point-Precise Control
- Reinforcement Learning
- Semantic-Execution Gap
- Geometric Construction
- Process Supervision
one_liner: 提出拓扑感知代理 PAGER，通过像素级监督微调与精度对齐强化学习，解决点级精确 GUI 构造问题
practical_value: '- **像素级过程监督数据集**：PAGE Bench 包含 224K 过程监督像素动作，可为电商设计自动化、交互式推荐布局等场景提供细粒度操作标注范例，直接用于训练可执行动作语法。

  - **精度对齐强化学习**：通过状态条件几何反馈缓解 rollout 曝光偏差，该思想可迁移到任何序列决策任务，适合在电商推荐的多步交互中纠正累积误差。

  - **拓扑感知依赖规划**：将复杂构造任务分解为依赖结构子任务再执行，类似思路可用于电商页面生成时先规划组件关系再渲染，提高结构化输出的准确性。

  - **语义-执行鸿沟的警示**：提醒在 Agent 开发中，即使语义理解准确率很高，几何级精度缺失仍会导致任务失败，需在设计奖励和度量时引入执行精度指标。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：当前 GUI 代理依赖区域容错范式，但几何构造任务要求像素级精确点击，局部坐标错误会引发连锁拓扑失败。强调该类任务需点级精度、几何验证和依赖错误传播鲁棒性，然而通用模型存在显著的语义-执行鸿沟（动作类型准确率高但任务成功率极低）。

**方法**：首先构建基准 PAGE Bench（4906 个问题，>224K 过程监督像素动作）。提出 PAGER 代理，将构造任务分解为依赖结构规划和像素级执行。像素监督微调建立可执行动作语法；精度对齐强化学习利用状态条件几何反馈，纠正 rollout 累积的曝光偏差，实现端到端的点精确控制。

**结果**：通用多模态模型动作类型准确率超 88%，但任务成功率不足 6%；PAGER 将任务成功率提高 4.1 倍，步骤成功率从 GUI 专用代理的不足 9% 提升至 62% 以上，成为点精确 GUI 控制的新 SOTA。
