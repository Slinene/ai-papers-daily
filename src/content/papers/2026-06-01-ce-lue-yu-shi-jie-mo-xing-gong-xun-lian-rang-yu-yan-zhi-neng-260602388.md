---
title: Policy and World Modeling Co-Training for Language Agents
title_zh: 策略与世界模型共训练：让语言智能体在 RL 中学会预测动作后果
authors:
- Ning Lu
- Baijiong Lin
- Shengcai Liu
- Jiahao Wu
- Haoze Lv
- Yanbin Wei
- Lingting Zhu
- Shengju Qian
- Xin Wang
- Ying-Cong Chen
affiliations:
- Southern University of Science and Technology
- Hong Kong University of Science and Technology
- Hong Kong University of Science and Technology (Guangzhou)
- Hong Kong Polytechnic University
- LIGHTSPEED
arxiv_id: '2606.02388'
url: https://arxiv.org/abs/2606.02388
pdf_url: https://arxiv.org/pdf/2606.02388
published: '2026-06-01'
collected: '2026-06-02'
category: Agent
direction: 语言智能体 · 世界模型与强化学习共训练
tags:
- World Modeling
- On-policy RL
- Co-Training
- LLM Agent
- MAE Loss
one_liner: 将 on-policy RL 的 rollout 同时用作世界模型的下一观测监督，通过动作熵过滤、裁剪 MAE 损失和奖励自适应权重实现稳定共训练，无需额外模型或推理开销
practical_value: '- **复用现有 rollout 作为世界模型监督**：在电商对话 Agent 或推荐交互 Agent 中，用户与系统的多轮交互（如搜索-浏览-下单）天然包含状态转移样本，可将每步动作对应的下一页面内容作为预测目标，无需额外构造模拟器。

  - **动作熵过滤冗余样本**：只保留策略熵较高的决策点（如用户提问模糊、候选商品多）的转移样本进行世界建模，避免大量确定性动作（如翻页）造成的低效训练，可显著提升样本效率。

  - **用裁剪 MAE 替代 CE 应对噪声观测**：在电商页面等富含随机 ID、产品名的文本环境中，MAE 损失能抑制不可预测 token 的梯度，配合置信度裁剪（pt,i
  >ρ 的 token 不训练）可防止过拟合表面形式，使世界模型抓住核心动态。

  - **奖励自适应权重平衡多任务**：根据 rollout 组成败调整世界模型 loss 权重，低成功率组强化环境理解，高成功率组侧重策略优化，这种简单启发式可直接用于客服
  Agent、推荐对话 Agent 的多目标 RL 训练。'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：标准 RL 训练的语言智能体只优化动作以最大化奖励，缺乏对动作后果（环境动态）的理解，这导致智能体在长链路任务中脆弱，容易犯错或陷入不可逆状态。传统世界模型（WM）方法需要独立模拟器、额外训练阶段或推理时规划，成本高。本文观察到 on-policy RL rollout 已天然包含动作-下一观测配对，可直接作为 WM 监督信号，于是提出策略与世界模型共训练框架 PaW，在不改变推理范式的前提下，为 RL 智能体注入环境动态知识。

**方法关键点**：
- **数据复用**：将每个 rollout transition (h_t, a_t, r_t, o_{t+1}) 中的 o_{t+1} 作为世界模型自回归预测目标，在同一次前向传播中同时计算 RL loss 和 WM loss，因果注意力避免下一观测影响动作 logit。
- **动作熵过滤**：仅对当前策略动作熵较高的 transition 施加 WM 监督，因为高熵动作对应不确定性大的决策点，其观测更富含动态信息；通过保留 top-α 比例（α=0.75）减少冗余。
- **裁剪 MAE 损失**：面向噪声化的文本观测（如 WebShop 中随机产品 ID），用 token 级 MAE (1−p_{t,i}) 替代 CE，避免低概率 token 梯度爆炸；并引入置信度掩码（p_{t,i} > ρ 的 token 停止训练），聚焦于未充分掌握的动态。
- **奖励自适应权重**：λ_WM,g = 1−ar{R}_g/R_max，使低奖励 rollout 组获得更强的 WM 监督，高奖励组则专注策略精调。

**关键实验**：
- 环境：ALFWorld（具身文本）与 WebShop（网页购物）的交互决策，以及搜索增强 QA（单跳/多跳）。
- 基线：GRPO、GIGPO 等 strong RL 基线与 ReAct、Reflexion 等提示方法。
- 结果：在 ALFWorld 上 GRPO + PaW 将成功率由 70.0% 提至 77.9%（1.5B），GIGPO 由 87.6% 提至 90.4%；WebShop 上 GRPO + PaW 成功率从 60.6% 升到 68.6%，GIGPO 从 66.2% 升到 75.3%。对 Llama3.2-3B 在 WebShop 上，PaW 将成功率从 4.0% 大幅提升至 62.2%，展现出在稀疏奖励场景下的拯救能力。训练额外开销仅 2% 左右。

**核心一句话**：on-policy RL rollout 天然可作世界模型监督，配合动作熵过滤、裁剪 MAE 和奖励自适应权重，就能几乎零成本地让语言智能体学会预测动作后果，全面提升长链路任务表现。
