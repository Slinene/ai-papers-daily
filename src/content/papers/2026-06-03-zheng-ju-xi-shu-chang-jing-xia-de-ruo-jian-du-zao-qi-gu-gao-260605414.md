---
title: 'When Evidence is Sparse: Weakly Supervised Early Failure Alerting in Dialogs
  and LLM-Agent Trajectories'
title_zh: 证据稀疏场景下的弱监督早期故障告警
authors:
- Avinash Baidya
- Xinran Liang
- Ruocheng Guo
- Xiang Gao
- Kamalika Das
affiliations:
- Intuit AI Research
- Princeton University
arxiv_id: '2606.05414'
url: https://arxiv.org/abs/2606.05414
pdf_url: https://arxiv.org/pdf/2606.05414
published: '2026-06-03'
collected: '2026-06-07'
category: Agent
direction: 对话/Agent轨迹早期故障告警
tags:
- Early Failure Alerting
- Weak Supervision
- Multi-turn Dialog
- LLM Agents
- Multiple Instance Learning
- Preference-Conditioned RL
one_liner: 利用MIL从轨迹级标签中学习稀疏故障证据，结合偏好条件触发策略实现推理时可控的准确-提前性权衡
practical_value: '- 利用 MIL 从轨迹级标签中自动挖掘稀疏的故障证据轮次，无需人工标注 turn 级标签，直接改善前缀故障预测的准确性，适合客服对话和
  Agent 执行监控。

  - 融合“naive 前缀预测”与基于 MIL 的稀疏证据信号：前者反应快但噪声大，后者延迟但准确，简单 MLP 融合即可显著提升准确-提前性 Pareto 前沿，该模式可直接推广到需早期决策的序列监控场景。

  - α-STOP 策略让单一模型通过改变标量 α 在推理时覆盖整个准确-提前性权衡曲线，无需为每个运营点重新训练；部署后可根据业务需要（如高精准告警 vs. 尽早干预）动态调节，大幅降低运维成本。

  - 模块化设计（故障预测器 + 触发策略分离）优于端到端 RL，预测器提供可靠风险信号，触发策略专注决策偏好，且预测器升级不影响触发策略，工程上更灵活易维护。'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

**动机**
交互对话和 LLM Agent 轨迹越长，早期发现失败风险越关键，但往往只有轨迹级成功/失败标签。现有方法将终端标签广播到每个前缀，迫使模型在大量无故障证据的早期轮次上学习虚假正例，导致过早告警且最高精度受限。本文观察到故障证据高度稀疏（仅占 4.7–11.3% 的轮次）且延迟出现（首个关键轮次平均在 59–83.6% 轨迹长度后），因此需要从弱标签中挖掘稀疏证据并实现可控的早期告警。

**方法关键点**
- **注意力故障预测器**：先用注意力 MIL 从轨迹标签学习 turn 级风险得分，并训练在线门控网络近似全局注意力，得到在线证据向量 \(E_t\)；再将传统前缀预测 \(b_t\) 与 \(E_t\) 通过轻量 MLP 融合为最终故障概率 \(\hat{p}_t\)，理论上可严格提升对数损失。
- **α-STOP 停止策略**：构建状态 \(s_t = (\hat{p}_t, b_t, E_t, \tau_t, z_t)\)，训练单个偏好条件（α）策略网络，使用 BC→PPO 训练范式；推理时仅改变 α 即可无重训练地扫掠准确-提前性 Pareto 前沿，且 α 对停止时间呈单调控制。

**关键结果**
在 5 个数据集（客户支持 PCS、任务对话 BETOLD、劝捐 P4G、工具使用 AppWorld、具身规划 ALFWorld）上：
- 注意力预测器比 naive 预测器的 Pareto 超体积（HV）提升 1–10%，最大准确率提高显著（如 PCS 上 0.813 vs 0.695）；
- α-STOP 相比 SOTA 触发策略（ALERT*、FIRMBOUND）HV 提升 3–42%，且 GPU 时/运营点降低 1–3 个数量级；
- 单一 α 条件策略相比单 α 独立训练策略，不仅效率更高，且 α 与停止时间的秩相关性 > 0.94，控制更可靠。

**一句话总结**
“在弱监督早期故障告警中，分离预测与决策、利用 MIL 挖掘稀疏证据、并通过偏好条件实现单策略多权衡点，是提升准确–提前性效率的关键。”
