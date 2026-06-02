---
title: 'SIRI: Self-Internalizing Reinforcement Learning with Intrinsic Skills for
  LLM Agent Training'
title_zh: 'SIRI: 自我内化强化学习与内在技能'
authors:
- Zhongyu He
- Yuanfan Li
- Fei Huang
- Tianyu Chen
- Siyuan Chen
- Xingyang Li
- Meng Hsuan Yu
- Xiangrong Liu
- Leyi Wei
- Lu Pan
affiliations:
- Xiamen University
- Meituan
- Macao Polytechnic University
arxiv_id: '2606.02355'
url: https://arxiv.org/abs/2606.02355
pdf_url: https://arxiv.org/pdf/2606.02355
published: '2026-06-01'
collected: '2026-06-02'
category: Agent
direction: LLM Agent 强化学习 · 自我技能内化
tags:
- LLM Agent
- Reinforcement Learning
- Skill Internalization
- Self-supervised Skill Mining
- Long-horizon Task
- Advantage Weighting
one_liner: 通过三阶段自监督技能挖掘与优势加权内化，让LLM智能体在长程任务中摆脱推理期技能库依赖并取得最优性能。
practical_value: '- **自动技能提取**：借鉴自我技能挖掘（Phase 1），可从电商客服或购物Agent的成功交互轨迹中自动总结可复用策略（如处理缺货、比价），无需外部大模型生成，降低人工成本。

  - **在线效用验证与技能生命周期管理**：采用配对rollout的效用差（Δ_g）动态评估技能质量，并设置候选→激活→退役的进化机制，可确保线上使用的技能始终有效，避免技能库污染。

  - **优势加权内部化实现检索自由**：通过轨迹级效用门控与动作级优势加权，仅将正向技能引导的动作token蒸馏到基础策略，彻底移除推理期的技能检索、提示注入，显著降低上线延迟与工程复杂度，适合高并发电商推荐与对话系统。

  - **训练框架的兼容性**：SIRI可与现有RL算法（如GiGPO、GRPO）无缝衔接，作为增量模块提升现有Agent训练流水线，且自我挖掘的技能可逐步逼近外部强模型生成的质量，适合在模型自主进化中逐渐摆脱对昂贵外部API的依赖。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
长程LLM智能体训练面临稀疏奖励与探索效率低下问题，技能（skills）作为可复用的行为抽象能有效缓解这一困境。然而现有技能增强方法依赖外部技能生成模块或推理时技能检索，引入了工程复杂性、额外延迟与上下文长度。SIRI旨在回答一个核心问题：能否让智能体在RL训练中自行发现并内化技能，使最终策略在推理时完全摆脱技能库？

**方法关键点**  
SIRI是一个三阶段课程框架：  
1) **Phase 0（策略热身）**：用GiGPO对原始策略进行预热，收集足够多的高质量无技能轨迹，避免从低水平策略中挖掘出虚假技能。  
2) **Phase 1（自我技能挖掘与利用）**：智能体冻结快照从自己成功的无技能轨迹中自动提炼技能（条件-策略对）；通过配对 rollout（有/无技能）计算技能宏效用 Δ_g，用 EMA 更新技能效用并动态管理技能库（候选→激活→退役），确保只保留能给任务带来正向增益的技能。  
3) **Phase 2（优势加权技能内化）**：以有技能提示的轨迹作为教师，原始无技能上下文作为学生，仅当轨迹级效用 Δ_g > 0 且 token 属于动作部分时，利用 GiGPO 的轨迹级与步级复合优势进行加权蒸馏，将有用的技能引导行为吸收进策略参数。训练完成后丢弃技能库，推理仅用原始 prompt。

**关键实验结果**  
在 ALFWorld 和 WebShop 两个长程智能体基准上，用 Qwen2.5-7B-Instruct 进行评估：  
- SIRI 将 GiGPO 的 ALFWorld 平均成功率从 0.908 提升至 **0.930**，WebShop 成功率从 0.728 提升至 **0.813**（得分从 0.844 到 0.899），均优于 SkillRL、PPO 等记忆增强及 RL 基线。  
- 消融实验表明，移除预热或跳过内部化均导致显著性能下降，且自我挖掘的技能质量随训练持续提升，最终可接近外部强模型（Gemini-3-Flash）的挖掘效果，验证了自采矿的有效性。

**核心启示一句话**  
SIRI 证明了智能体能够“自我教学”：通过在线效用药取高质量技能并选择性内部化，彻底去除推理期对外部技能库的依赖，为部署高效、低延迟的 LLM Agent 提供了实用路径。
