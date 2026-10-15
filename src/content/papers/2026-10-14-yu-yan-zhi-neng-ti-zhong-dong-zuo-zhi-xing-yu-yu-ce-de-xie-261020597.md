---
title: Co-Evolving Acting and Forecasting for Language Agents
title_zh: 语言智能体中动作执行与预测的协同进化
authors:
- Haofei Yu
- Yixing Chen
- Yining Zhao
- Xuyan Ye
- Yuxiang Liu
- Zhigang Hua
- Yan Xie
- Shuang Yang
- Jiaxuan You
affiliations:
- University of Illinois Urbana-Champaign
- University of California San Diego
- Meta AI
arxiv_id: '2610.20597'
url: https://arxiv.org/abs/2610.20597
pdf_url: https://arxiv.org/pdf/2610.20597
published: '2026-10-14'
collected: '2026-10-15'
category: Training
direction: 语言智能体 RL 训练 · 动作预测辅助目标
tags:
- Language Agents
- Reinforcement Learning
- Auxiliary Targets
- Sample Efficiency
- Action Forecasting
one_liner: 在成功轨迹上以未来动作序列为多步辅助目标，让策略骨干同时执行与预测并共同进化，提升样本效率且无推理开销
practical_value: '- **长链路 Agent 训练可直接复用**：在电商导购、搜索比价、下单等多步任务中，可只对成功会话构造“从中间历史预测未来动作序列”的辅助损失，同一动作在不同历史位置反复监督，能显著压缩所需的成功轨迹数量；适合在
  WebShop 类仿真环境先跑通再迁到真实场景。

  - **无推理侧负担，适合在线部署**：该方法不增加额外模型、不改变单步推理流程，可在现有 policy 模型上直接加辅助 loss 训练；对推荐/搜索 Agent
  的服务架构几乎零侵入。

  - **比 value/observation 辅助目标更稳定**：若业务中 agent 奖励稀疏，且页面日志、终端输出长且嘈杂，可优先尝试这种多步动作预测目标，而不是拟合下一步观测或单标量价值。

  - **时间集成可迁移到生成式推荐**：同一 item 从不同用户历史前缀反复预测，等价于多步预测正则，或可缓解长序列生成中的 exposure bias，值得在
  Semantic ID 或生成式重排任务中试验。'
score: 8
source: arxiv-cs.LG
depth: abstract
---

**动机**：语言智能体长程 rollout 成本高，标准 agentic RL 只用终局标量奖励，中间监督利用不足；常见价值目标与观测目标分别存在同质标量、长噪声单步等问题。
**方法**：COPE 在成功 on-policy 轨迹上，从每个历史位置训练策略骨干生成其后继动作序列；同一动作会被前面不同历史反复预测，形成时间集成，由共享骨干吸收，使 acting 与 forecasting 共同进化。推理仍单步执行，无额外模型或开销。
**结果**：在 ALFWorld、ScienceWorld、WebShop、tau^2-bench、AppWorld 五个基准上，综合性能超过 GRPO 与带预测辅助目标的 RL 基线；ScienceWorld 上样本效率比 ECHO 高 1.9 倍、比 GRPO 高 2.0 倍；仅需单一策略骨干，无需单独预训练或推理开销。
