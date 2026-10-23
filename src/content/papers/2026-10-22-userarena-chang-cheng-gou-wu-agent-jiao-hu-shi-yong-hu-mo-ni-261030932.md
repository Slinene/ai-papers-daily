---
title: 'UserArena: Benchmarking Interactive User Simulation for Long-Horizon Shopping
  Agents'
title_zh: UserArena：长程购物 Agent 交互式用户模拟基准
authors:
- Jujia Zhao
- Jiakai Tang
- Jing Yu
- Wen Chen
- Jian Wu
- Han Zhu
- Fei Sun
- Suzan Verberne
- Zhaochun Ren
affiliations:
- Leiden University
- Renmin University of China
- Alibaba Group
- Institute of Computing Technology, Chinese Academy of Sciences
arxiv_id: '2610.30932'
url: https://arxiv.org/abs/2610.30932
pdf_url: https://arxiv.org/pdf/2610.30932
published: '2026-10-22'
collected: '2026-10-23'
category: RecSys
direction: 用户模拟器 · 长程购物 Agent 基准
tags:
- User Simulator
- Benchmark
- On-Policy Distillation
- Long-Horizon Shopping
- Recommendation
- LLM
one_liner: 构建真实电商长程交互基准与五级评估协议，并提出 on-policy trajectory distillation 提升用户模拟器保真度
practical_value: '- 借鉴五级评估协议（L0-L4）构建业务用户模拟器验收流程：从动作解析有效率、下一步行为准确率、到序列分布和群体分层保真，最后对比策略
  A/B 效果；尤其关注不平衡动作（如滚动占38%）用宏观 F1 而非微平均。

  - OPTD 的训练策略可迁移到序列决策模型的离线训练：用 trajectory-level intent 作为 teacher 的 privileged context，在
  student 自己的 rollout 上做 token-level 蒸馏（JSD），并用 trust region 限制意图影响，可减少 exposure bias
  和稀疏监督，提升长程一致性。

  - 建立模拟器-线上校准闭环：将相同策略对在模拟器中对比效果，与生产 A/B 效果比较（如 effect ratio 和 error），确保模拟器结论可指导业务决策；OPTD
  达到 0.713× effect ratio，远好于通用大模型。

  - 数据层面：整合用户跨会话长期行为（平均 10+ 会话）来训练和评估模拟器，比单会话更能揭示行为惯性；可结合用户属性、视觉上下文、完整动作空间来提升模拟器保真度。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
现有推荐系统用户模拟器缺乏长程、细粒度真实用户轨迹，且评估多为下一步动作一致，难以反映长期行为保真和与线上策略效果的一致性。本文构建 USERARENA 基准，解决训练高保真用户模拟器的问题。

**方法关键点**
- **数据**：USERARENA 包含 11,010 用户、64,729 个会话、577,670 次动作的真实电商交互轨迹，覆盖 566,102 个商品和 13 种动作，每步对齐用户画像、视觉观察、商品上下文和动作；跨会话子集连接同一用户多次会话（平均 10.29 个会话、86.36 次动作），支持长程评估。
- **评估协议**：五级 L0-L4，从输出合法性（L0）、局部动作保真（L1，Macro-F1/Acc）、序列动态（L2，DM-JSD/TE）、个性化群体保真（L3，PF，按历史活跃度、购买倾向、品类广度分组）、结果保真（L4，∆CTR/∆ACR/T-JSD）。
- **OPTD 方法**：针对 SFT 的 exposure bias 和稀疏监督，采用 on-policy 采样（在 student 自己 rollout 上训练）；用 LLM 提取 trajectory-level intent 作为 teacher 的特权上下文；teacher 在 student 每个 token 上提供稠密分布目标，并通过 trust region（KL 散度预算）限制 intent 条件分布与无条件分布的差异；总损失为 JSD 蒸馏损失 + 记录响应接地损失。
- **生产验证**：用同一策略对在模拟器中比较，与线上 A/B 结果对比。

**关键实验**
- 对比 8 个 text/GUI 模拟器（统一用 Qwen3.5-2B 控制模型规模），OPTD 在单会话设置 L1-L4 八项指标全部第一；跨会话八项中五项第一、两项第二。
- 生产 A/B 验证中，OPTD 的 effect ratio 达到 0.713×（最接近 1），通用大模型（如 GPT-6）反而过估计。
- 消融显示去除 on-policy、intent、trust region、grounding 或 SFT 初始化均导致性能下降，去 SFT 退化最严重。
- 图灵测试中 OPDT 的 Human win rate 最低（2.0%），Model win rate 最高。

**最值得记住的一句话**：通过 trajectory-level intent 引导的 on-policy distillation，在真实长程电商数据上训练的用户模拟器不仅能高保真复现行为，还能较准确预测生产 A/B 策略效果。
