---
title: 'D$^3$-Subsidy: Online and Sequential Driver Subsidy Decision-Making for Large-Scale
  Ride-Hailing Market'
title_zh: 网约车司机补贴的动态扩散决策框架 D3-Subsidy
authors:
- Taijie Chen
- Rui Su
- Siyuan Feng
- Laoming Zhang
- Hongyang Zhang
- Haijiao Wang
- Zhaofeng Ma
- Jintao Ke
affiliations:
- University of Hong Kong
- Harbin Institute of Technology
- Hong Kong Polytechnic University
- Didi International Business Group
arxiv_id: '2605.20036'
url: https://arxiv.org/abs/2605.20036
pdf_url: https://arxiv.org/pdf/2605.20036
published: '2026-05-19'
collected: '2026-05-20'
category: Other
direction: 离线强化学习 + 扩散模型用于动态定价控制
tags:
- Diffusion
- Offline RL
- Subsidy Allocation
- Ride-hailing
- Constrained Optimization
- Multi-city pretraining
one_liner: 提出前缀条件扩散模型与Lagrangian-dual映射，在预算约束下实现城市级补贴的在线序列决策
practical_value: '- **前缀条件扩散用于离线决策**：部署时历史不可改变，训练时也固定历史前缀，仅扩散未来后缀，消除训练-推理 gap，可推广到任何需基于实时观测做序列决策的场景（如电商动态定价、Agent
  策略学习）。

  - **约束感知的后处理评分**：在优化目标中加入对预算上限的 soft penalty，通过调整 penalty exponent 即可控制违规容忍度，无需重训模型，适合有严格
  ROI 约束的营销或补贴分配任务。

  - **Lagrangian-dual 映射实现降维动作**：将城市级标量控制信号通过闭式映射转为订单级补贴，既保证低延迟（单次决策 20ms），又避免个性化激励的不公平，可借鉴到大规模促销额度分配中，用总预算系数自动生成细粒度折扣。

  - **多城预训练 + PEFT 冷启动迁移**：先在多城数据上预训练扩散先验和逆动力学解码器，再对目标城市仅微调解码器（冻结扩散模型），大幅提升新市场冷启动效果，对电商新品类、新区域策略复用有直接参考。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：网约车平台需实时决定司机补贴以平衡供需，但受到每日补贴率上限、低延迟及可扩展性三重约束。传统在线 RL 探索风险大，离线 RL 面临分布偏移且难以处理序列预算耦合。该工作将城市级补贴控制建模为预算受限的 MDP，并引入扩散模型以生成符合历史前缀的未来轨迹，从而学习安全且可部署的策略。

**方法关键点**：
- **前缀条件扩散**：只对轨迹的未来部分加噪/去噪，保持历史前缀固定，使训练与在线部署一致。
- **上下文条件逆动力学**：从局部状态窗口和上下文（城市 embedding、时间、预算上限、目标 KPI 偏好）解码城市级控制变量 λ。
- **约束感知分数**：每日补贴率超过上限时对得分施加乘性 penalty，可通过指数 β 调节软硬程度。
- **Mask-Normalized Denoising Loss (MNDL)**：按有效后缀步数归一化去噪损失，解决变长轨迹训练中的梯度波动。
- **两阶段训练**：多城预训练扩散先验和逆动力学模型，再对单城进行轻量 PEFT（仅微调解码器，加锚点正则），实现跨城泛化与冷启动。
- **Lagrangian-dual 映射**：从全局 λ 推导出订单级 subsidy 的闭式解，保证低延迟与一致性。

**关键结果**：
- 离线测试覆盖 3 城 7 天，D3-Subsidy 在所有城市、所有时间窗口（2/5/10 min）均优于生产在线策略及 7 种离线 RL 基线（BCQ、CQL、IQL、TD3+BC、DT、DD），整体平均 Score 提升分别达 4.3%~18.5%（相对于 Online）。
- 在线 A/B 测试（7 天，20 万+ 订单）中，Rides +1.59%，GMV +2.06%，DRV +2.31%，预算从未超标，推理延迟仅增加 20ms。
- 消融实验表明移除上下文条件、多城预训练或 PEFT 均导致 Score 下降 3%~5%，验证各模块的必要性。

**核心启示**：通过前缀条件扩散与约束感知评分，离线生成式模型可以在严格的实时预算约束下实现稳健的序列决策，且多城预训练+PEFT 使策略冷启动可行。
