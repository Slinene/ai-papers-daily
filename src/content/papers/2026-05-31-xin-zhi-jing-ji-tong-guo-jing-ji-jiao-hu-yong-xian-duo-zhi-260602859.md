---
title: 'Economy of Minds: Emerging Multi-Agent Intelligence with Economic Interactions'
title_zh: 心智经济：通过经济交互涌现多智能体集体智能
authors:
- Zhenting Qi
- Huangyuan Su
- Ao Qu
- Chenyu Wang
- Yu Yao
- Han Zheng
- Kushal Chattopadhyay
- Guowei Xu
- Zihan Wang
- Weirui Ye
affiliations:
- Harvard
- MIT
- 2077AI
- Kempner Institute
arxiv_id: '2606.02859'
url: https://arxiv.org/abs/2606.02859
pdf_url: https://arxiv.org/pdf/2606.02859
published: '2026-05-31'
collected: '2026-06-05'
category: MultiAgent
direction: 多智能体经济协作与自进化
tags:
- Multi-Agent Systems
- Economic Coordination
- LLM Agents
- Self-Evolution
- Credit Assignment
- Decentralized Intelligence
one_liner: 仅用拍卖、交易和财富的经济信号就使一群受限智能体自组织、自进化，在多个任务上超越完整单一智能体。
practical_value: '- **去中心化协调替代集中编排**：在电商多Agent场景（如协商、客服、供应链）中，可借鉴拍卖选择动作 + 财富驱动的生存机制，避免中心协调器瓶颈，实现自组织协作，尤其适合流式任务。

  - **隐式信用分配**：Bucket-brigade交易规则（获胜者向前一Agent支付出价）自动将价值反向传播，无需全局奖励分解或稠密过程奖励，适合难以定义子任务奖励的长链任务（如多步对话或推荐管线）。

  - **经济驱动的群体进化**：用财富积累与破产作为自然选择压力，剥削成功Agent并通过突变传播其策略，探索则利用破产Agent的修正版本；这种方法可替代手工设计提示或架构，使Agent群体在持续任务流中自适应。

  - **鲁棒性与通用专家**：实验表明增加一个全能Agent不会垄断市场，市场仍偏好局部精细的专业Agent，这为构建可扩展的多专业Agent生态提供了信心；可应用在生成式推荐中，让多个领域专家Agent通过经济信号竞争，避免单一模型退化。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**：集中式多智能体系统存在协调瓶颈和扩展困难。受Hayek市场理论启发，研究如何通过简单的经济激励，让一群局部有限的LLM Agent在没有全局规划或通信协议的情况下，自发形成更强的集体智能。

**方法关键点**：
- Agent定义：每个Agent包含触发谓词（何时可行动）、行动策略、固定出价和当前财富，均基于共享冻结LLM，仅通过系统提示区分。
- 拍卖规划：每步环境中，符合条件的Agent根据最高出价竞得行动权；获胜者向前一步获胜Agent支付其出价，并获取环境奖励，形成Bucket-brigade信用分配，使价值沿成功轨迹反向流动。
- 群体进化：财富积累的Agent被剥削（通过突变产生后代，保留成功模式），破产的Agent被移除，并通过探索（基于失败提示的修正）补充新Agent；出价遵循新手规则（保证新Agent首次获胜），形成持续的自选择与自适应。
- 训练仅用最终结果奖励，无稠密过程奖励；评估时冻结经济动态，仅用拍卖进行动作选择。

**关键实验结果**：
- 在5类任务上（数学推理、金融研究、科学研究、加速器设计、分布式系统优化），EOM均显著改善弱约束群体性能，并超越完整单Agent基线：数学从15.9%提升至57.0%（Llama-3.1-8B），金融研究从45.0%至60.0%，加速器EDP降至39.3（vs. 完整Agent 43.1，领域专用80.2），分布式成本降低28%。
- 消融证明经济组件（拍卖、剥削、探索）不可或缺，参数扰动导致性能下降。
- 经济体展现出易到难的泛化、课程依赖性、以及专业Agent对通用Agent的竞争优势，表明市场选择能挖掘可复用的领域结构（如输出稳定数据流模式）。
- 分析显示，经济动态逐步塑造Agent提示策略、交互拓扑和专业化角色，无需中央设计。
