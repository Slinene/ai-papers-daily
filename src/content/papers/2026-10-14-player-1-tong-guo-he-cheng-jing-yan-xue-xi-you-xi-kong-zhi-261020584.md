---
title: 'Player-1: Learning to Play from Synthetic Experience'
title_zh: Player-1：通过合成经验学习游戏控制的后训练框架
authors:
- Mingyu Ouyang
- Yiran Wang
- Siyuan Hu
- Xingyilang Yin
- Huiqiang Sun
- Guangzhi Wang
- Junfu Pu
- Cheng Cheng
- Honghao Chen
- Ying Shan
affiliations:
- National University of Singapore
- ARC Lab, Tencent IEG
- Nanyang Technological University
arxiv_id: '2610.20584'
url: https://arxiv.org/abs/2610.20584
pdf_url: https://arxiv.org/pdf/2610.20584
published: '2026-10-14'
collected: '2026-10-18'
category: Agent
direction: 游戏智能体 · 合成经验强化学习
tags:
- Game Agent
- Reinforcement Learning
- Synthetic Environments
- PPO
- Computer Use
- Post-training
one_liner: Player-1利用合成环境和PPO强化学习，将游戏智能体MineDojo-300成功率提升至38.33%，远超SFT基线
practical_value: '- **合成环境+程序化奖励训练Agent决策**：可借鉴到电商搜索/推荐Agent的离线策略优化，构建模拟用户交互（点击、浏览、反馈）的合成环境，避免线上试错成本，用PPO在多样化模拟器中提升Agent多步决策能力。

  - **复合动作空间扩展**：论文中同时组合键盘+鼠标的复合动作在RL中使用频率增加，类比到对话式推荐或搜索Agent，可建模同时生成query+点击筛选等复合操作，更贴近真实用户行为，值得在动作空间设计上尝试。

  - **SFT初始化+多环境PPO两阶段范式**：先用人类演示数据SFT，再在多个随机化合成环境中用PPO探索优化，这比单纯SFT能获得超越模仿的策略，适用于电商客服Agent、自动谈判Agent等需要长期回报优化的场景。

  - **环境随机化提升迁移泛化**：通过对观察和动力学进行随机化，覆盖更广状态空间，可应用于构建电商搜索模拟器时加入用户偏好扰动、延迟响应等噪声，提高策略鲁棒性。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：游戏环境视觉丰富、机制多样，现有游戏智能体学习依赖大规模演示，对动态游戏状态覆盖有限，且缺乏可扩展的交互训练环境。

**方法关键点**：
- 扩展计算机使用动作空间：加入相对指针移动、持续输入和复合动作（同时组合多个键盘/鼠标输入）。
- 监督初始化：在6044条精选游戏轨迹（配对动作、任务指令和视觉推理）上微调计算机使用模型。
- 构建Player-1-Gym：16个合成2D/3D环境，围绕游戏共有的控制需求设计，提供程序化可验证奖励、随机化观察与控制动力学。
- 多环境强化学习：使用PPO在多个合成环境上联合训练。

**关键结果**：
- Player-1-9B和Player-1-35B-A3B在MineDojo-300成功率相对SFT策略分别提升27.8和17.7个百分点。
- Player-1-9B达到38.33%成功率，最强评估基线仅为12.63%。
- 在ViZDoom-10和GameWorld上同样超越SFT，证明泛化能力。
- 分析显示更广的合成环境覆盖提升迁移，RL过程中复合动作使用频率增加。
