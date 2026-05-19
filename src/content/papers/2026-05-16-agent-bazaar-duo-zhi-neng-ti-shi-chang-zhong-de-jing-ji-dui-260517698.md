---
title: 'Agent Bazaar: Enabling Economic Alignment in Multi-Agent Marketplaces'
title_zh: Agent Bazaar：多智能体市场中的经济对齐仿真与强化学习训练
authors:
- Seth Karten
- Cameron Crow
- Chi Jin
affiliations:
- Princeton University
arxiv_id: '2605.17698'
url: https://arxiv.org/abs/2605.17698
pdf_url: https://arxiv.org/pdf/2605.17698
published: '2026-05-16'
collected: '2026-05-19'
category: Agent
direction: 多智能体经济对齐 · 市场仿真 · RL训练
tags:
- Economic Alignment
- Multi-Agent Simulation
- LLM Agents
- REINFORCE++
- Market Crash
- Sybil Attack
one_liner: 提出多智能体市场仿真框架，揭示LLM代理在B2C/C2C市场的崩溃与欺诈失败模式，并通过REINFORCE++训练9B模型实现经济对齐，性能超越前沿模型。
practical_value: '- **电商市场防护Sybil攻击的买家审核策略**：可借鉴Skeptical Guardian模式，在买家决策时注入对卖家声誉、价格区间与描述一致性的交叉验证逻辑，尤其是当多个账户可能被同一主体操控时，通过行为聚类识别Sybil集群。

  - **价格战市场的稳定性设计**：限制消费者可见信息并不总能改善市场，过度提高搜索可见性反而加速恶性降价（dlc增大导致崩溃更难抑制）。在电商推荐系统中可考虑动态调整商品曝光度，避免陷入无利润的价格内卷。

  - **EAS标量指标用于智能体系统健康评估**：结合稳定性、诚信度、福利与盈利四个维度的经济对齐分数，可直接迁移到评估电商智能体（如自动定价、自动客服）的整体市场影响，取代纯效率指标。

  - **RL训练使小模型获得经济对齐能力**：用REINFORCE++加自适应课程（根据生存/检测率调整对手难度）和平方log-ratio正则化，仅需1.3%参数LoRA微调，9B模型即可在稳定性与反欺诈上超越大得多的模型。这种方法可用于训练电商中的自动议价或选品Agent，使其在优化自身收益的同时维护全局市场健康。'
score: 10
source: huggingface-daily
depth: full_pdf
---

**动机**：随着LLM开始作为经济代理直接参与市场交易，其集体行为可能引发系统性风险，如2010年闪崩式的价格螺旋和利用虚假身份进行大规模欺诈。传统的“对齐”只关注单代理的助人、无害等，却无法捕捉多代理市场中的稳定性与诚信性。本文定义“经济对齐”为代理系统保持市场稳定、保护参与者福利的能力，并构建仿真框架Agent Bazaar来暴露和缓解两种典型失败模式。

**方法关键点**：
- **两个市场环境**：B2C市场“Crash”模拟五家LLM厂商定价竞争，消费者随机采样可见厂商，价格战可能跌破成本触发破产连锁；C2C市场“Lemon Market”中，一个欺诈主控者可创建多个Sybil卖家身份，每个身份独立评价，当评价降低时弃用并新建身份，买家无法直接区分诚实与欺诈卖家。
- **经济对齐评分（EAS）**：融合破产率、价格波动、Sybil检出率、欺诈购买率、市场存活率和代理利润的标量指标，用于跨模型比较。
- **对齐引导策略**：Stabilizing Firm引导厂商保持价格高于成本，不跟随恶意降价，并进行上下文反思；Skeptical Guardian引导买家交叉检验价格与质量层级、卖家评价，并反思历史决策。
- **强化学习训练**：基于Qwen 3.5 9B，用REINFORCE++和LoRA微调，采用平方log-ratio惩罚防止策略坍塌，对手为冻结的基础模型拷贝，课程难度随代理表现自适应调整（稳定厂商占比或Sybil集群大小）。

**关键结果**：
- 前沿模型在无干预时普遍失败：Gemini 3 Flash在Crash中破产率87%，GPT 5.4为67%，仅Sonnet 4.6无需干预即可稳定；Lemon Market中Sybil收入份额随欺诈卖家比例增大而上升，至K=9时达10-17%。
- 对齐策略有所改善但脆弱：消费者可见厂商数增多时，稳定厂商策略仍会失败（dlc=5时破产率>65%）。
- RL训练后的9B模型EAS达0.79，超越所有参评的前沿和大尺寸模型（如Hermes 3 405B的0.72，Sonnet 4.6的0.60），且模型大小与经济对齐无明显相关性。

**一句话结论**：经济对齐是一种与通用能力正交的特性，可通过目标明确的RL训练让小模型习得，并作为市场锚点惠及未训练代理。
