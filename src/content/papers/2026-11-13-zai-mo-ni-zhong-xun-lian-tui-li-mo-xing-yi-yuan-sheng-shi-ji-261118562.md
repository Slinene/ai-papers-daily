---
title: Training Reasoning Models in Simulation to Natively Use Real Robots
title_zh: 在模拟中训练推理模型以原生使用真实机器人
authors:
- Jiaming Tang
- Zhuoyang Zhang
- Junxian Guo
- Fangzhou Zhao
- Yilong Zhao
- Zekai Li
- Xingyang Li
- Yuyang Zhao
- Song Bian
- Zhijian Liu
affiliations:
- MIT
- UC Berkeley
- Inco AI
- NVIDIA
arxiv_id: '2611.18562'
url: https://arxiv.org/abs/2611.18562
pdf_url: https://arxiv.org/pdf/2611.18562
published: '2026-11-13'
collected: '2026-11-16'
category: Agent
direction: 机器人使用 Agent 的模拟 RL 后训练
tags:
- Robot-Use Agent
- Reinforcement Learning
- Sim-to-Real
- Post-Training
- Reasoning Model
one_liner: 用模拟环境强化学习后训练开源27B推理模型，无需演示即可直接控制真实机器人，成功率大幅提升
practical_value: '- **用仿真环境做 RL 后训练替代 SFT**：面对 Agent 策略优化（如推荐对话、操作执行），可以搭建高吞吐模拟器，用奖励函数（点击、转化、任务成功）驱动
  RL，避免昂贵的人工演示，适合电商场景中优化长期收益。

  - **保留通用能力是后训练底线**：论文验证了 RL 后训练不会破坏推理/代码/视觉基准，业务中微调 Agent 时应同步监控通用能力，防止灾难性遗忘。

  - **CoT + 动作生成的端到端训练**：模型在链式推理后直接输出结构化动作（末端位姿），推荐系统中可类比为让 LLM 先生成推理再输出可执行操作（如调价、选品），实现更可控的决策。

  - **仿真到真实的迁移启示**：在模拟环境中训练的策略能泛化到未见任务和真实机器人，说明离线仿真训练对推荐 Agent 的上线前验证具有参考价值，可通过域随机化提升鲁棒性。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：机器人使用 Agent（RUA）目前仅靠闭源前沿模型（如 GPT-6 Astra）取得强性能，开源模型能力严重不足。

**方法**：构建 Post-training Engine for Agentic Robotics (PEAR)，在模拟环境（LIBERO、RoboDojo）中用 robot-use reinforcement learning (RURL) 训练 Qwen3.8-27B。模型像 computer-use agent 一样观察环境、链式推理，并直接生成末端执行器位姿，全程无 harness、无演示。

**结果**：在 LIBERO 上成功率从 1.6% 提升至 74.4%，接近 GPT-6 Astra 最高推理强度（80.6%）；在真实双臂机器人上达到 60% 成功率（基线为 0）；对任务变化鲁棒性远超 π0.5（57.4% vs 0.75%）；在 9 个推理、编码、视觉基准上无退化。
