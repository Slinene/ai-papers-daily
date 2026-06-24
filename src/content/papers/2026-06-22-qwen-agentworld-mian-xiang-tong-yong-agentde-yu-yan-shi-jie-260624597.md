---
title: 'Qwen-AgentWorld: Language World Models for General Agents'
title_zh: Qwen-AgentWorld：面向通用Agent的语言世界模型
authors:
- Yuxin Zuo
- Zikai Xiao
- Li Sheng
- Fei Huang
- Jianhong Tu
- Yuxuan Liu
- Tianyi Tang
- Xiaomeng Hu
- Yang Su
- Qingfeng Lan
affiliations:
- Qwen Team
arxiv_id: '2606.24597'
url: https://arxiv.org/abs/2606.24597
pdf_url: https://arxiv.org/pdf/2606.24597
published: '2026-06-22'
collected: '2026-06-24'
category: Agent
direction: 语言世界模型增强Agent训练与规划
tags:
- Language World Model
- Agent Simulation
- Reinforcement Learning
- World Model
- Controllable Simulation
- Agent Training
one_liner: 首个覆盖7个交互域的语言世界模型，通过三阶段训练实现高保真环境仿真，并验证世界建模可提升Agent策略与任务表现
practical_value: '- **三阶段训练管线可迁移**：CPT注入世界知识、SFT激活“下一状态预测”推理模式、RL强化仿真精度。此范式可用于训练电商场景的环境模拟器（如模拟价格变化、库存波动、用户行为反馈），为Agent提供安全训练环境。

  - **信息论损失掩蔽**：根据动作-观测的统计特征（重叠率、新颖度、Jaccard等）判定信息量，对低价值turn（如API回声、纯确认）屏蔽损失但保留上下文。推荐系统训练中可借鉴此方法，自动过滤低质量点击/曝光序列中的无信息step，提升学习效率。

  - **世界模型作为Agent预训练任务**：世界建模训练（预测环境反馈）可作为Agent策略学习的前置warm-up，显著提升下游任务表现。在电商Agent（如对话式购物助手）设计时，可先训练其预测用户回复或系统状态变化，再微调至目标任务，获得更强基座。

  - **可控仿真暴露长尾风险**：通过simulation instruction人为制造干扰（如部分返回结果、隐藏关键信息），迫使Agent学习处理罕见边缘情况，最终超越纯真实环境训练的效果。适用于电商高风险操作（大额退款、自动调价）的仿真训练，低成本覆盖长尾异常场景。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：当前LLM Agent研究几乎全部聚焦于策略（状态→动作），而缺少通用世界模型（状态+动作→下一状态），这限制了Agent在复杂环境中的泛化与稳健性。理论表明，具备世界模型的Agent在原理上更强。本文旨在构建能模拟多种现实环境的语言世界模型（LWM），并探索如何通过世界建模增强Agent。

**方法**：
- 统一7个交互域（终端、MCP、搜索、软件工程、Android、Web、OS）的环境轨迹模式，将GUI状态表示为可访问性树或视图层级。
- **三阶段训练**：持续预训练（CPT）注入状态转移动态与专业世界知识，并采用信息论损失掩蔽滤除低信息量turn；有监督微调（SFT）通过拒绝采样激活长链推理产生下一状态预测思维模式；强化学习（RL）使用五维度评分（格式、事实性、一致性、真实感、质量）与规则验证的混合奖励提升仿真保真度，解决奖励坍缩与自誉攻击问题。
- 构建AgentWorldBench基准，基于5个前沿模型在9个现有基准上的真实交互轨迹，采用参照真实环境的开放式评分。

**关键结果**：
- Qwen-AgentWorld在AgentWorldBench上全面超越现有前沿模型。
- 作为**环境模拟器**，可模拟4000个真实OpenClaw环境用于Agent强化学习，在Claw-Eval和QwenClawBench上带来显著提升；可控仿真在Tool Decathlon、MCPMark等基准上的增益超过纯真实环境训练。
- 作为**Agent基础模型**，世界建模预热训练在Terminal-Bench 2.0、SWE-Bench Verified、BFCL v4等7个基准上全面提升下游Agent表现。

**核心洞察**：世界建模提供了一种互补于策略优化的路径——通过解耦仿真或统一训练，都能显著增强Agent能力。
