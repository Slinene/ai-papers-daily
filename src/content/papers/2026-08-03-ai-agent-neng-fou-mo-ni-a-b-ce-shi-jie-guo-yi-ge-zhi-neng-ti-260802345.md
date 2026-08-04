---
title: Can AI Agents Simulate A/B Test Outcomes? A Validation Framework for Agentic
  Experimentation
title_zh: AI Agent 能否模拟 A/B 测试结果？一个智能体实验验证框架
authors:
- Stefan Hut
- Lorenzo Masoero
affiliations:
- Amazon
arxiv_id: '2608.02345'
url: https://arxiv.org/abs/2608.02345
pdf_url: https://arxiv.org/pdf/2608.02345
published: '2026-08-03'
collected: '2026-08-04'
category: Eval
direction: Agent 模拟 A/B 测试效果预测
tags:
- S-RCT
- Agent Simulation
- A-B Testing
- Calibration
- Within-Subject Design
- Error Decomposition
one_liner: 提出 S-RCT 框架并验证：预校准和 within-subject 设计可将 Agent 模拟 A/B 测试的平方误差降低约 77 倍
practical_value: '- **预校准消除幅度偏差**：利用实验前历史数据训练轻量校准函数（如 Platt scaling），纠正 Agent 对用户行为反应幅度的系统性放大，可将平方误差降低约
  77 倍，直接用于在线模拟预测。

  - **Within-subject 设计降方差**：每个 Agent 同时接受 treatment 和 control 条件，消除 Agent 间个体差异，标准误平均减小
  2.4 倍，在有限 Agent 预算下显著提升灵敏度。

  - **方向性信号用于廉价筛选**：即使幅度不准，Agent 模拟的方向性准确率（sign overlap 0.70）足以在真实实验前筛掉大概率有害的干预，节省流量与工程成本。

  - **智能采样降低计算成本**：对 KPI 进行分层，预先估算各层标准差，采用 Neyman 分配，对高方差连续指标（如收入）可用更少 Agent 达到相同模拟精度，适合大型电商多实验并行场景。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
A/B 测试是产品迭代的核心手段，但每次实验消耗真实流量、工程师时间并需数周等待。若能利用 AI Agent 在投入真实流量前低成本预测实验结果，将极大加速试错效率。然而，现有工作缺乏系统的误差诊断框架和实用性验证。

### 方法关键点
1. **S-RCT 形式化**：将 Agent 模拟视作“模拟随机对照试验”，输入为 persona（用户画像）、context（干预描述）和 task（决策任务），输出模拟结果。
2. **两层误差分解**：总误差 = 近似误差（Agent 行为与真实用户的偏差）+ 子采样误差（有限 Agent 数导致的估计方差）。两者可独立优化。
3. **Agent 实例化**：使用通用基础模型，每个 Agent 绑定一个真实用户（agentic twins），并让同一 Agent 暴露于 treatment 和 control 双臂，实现全反事实查询。
4. **预校准协议**：Phase 1 用实验前数据（A/A 模拟）拟合校准函数（如 Platt scaling），Phase 2 在正式模拟时修正输出，系统性地缩小幅度偏差。
5. **智能子采样**：基于历史数据预估各用户分层的方差，采用 Neyman 分配，用更少 Agent 达到指定精度，大幅降低计算消耗。

### 关键结果
- 在 67 个历史营销创意 A/B 测试（CTR 指标）上验证，基线（无校准、between-subject）sign overlap 0.70，方向可接受但幅度偏差大。
- 两阶段预校准将平方预测误差压缩约 **77 倍**；within-subject 设计将标准误平均降低 **约 2.4 倍**。
- 方向性信号已可用于筛选有害实验，甚至可以贝叶斯先验的形式加速真实实验决策。

### 一句话
AI Agent 模拟 A/B 测试的最大障碍不是方向判断，而是幅度系统性放大，廉价的预校准就能将误差压低近两个数量级。
