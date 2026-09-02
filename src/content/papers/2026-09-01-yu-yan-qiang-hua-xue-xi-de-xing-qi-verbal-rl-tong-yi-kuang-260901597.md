---
title: The Rise of Verbal Reinforcement Learning
title_zh: 语言强化学习的兴起：Verbal RL 统一框架与三大支柱
authors:
- Kshitij Tayal
- Arun Sharma
- Genta Indra Winata
- Anirban Das
- Sambit Sahu
affiliations:
- AI Foundations, Capital One
- University of Minnesota
arxiv_id: '2609.01597'
url: https://arxiv.org/abs/2609.01597
pdf_url: https://arxiv.org/pdf/2609.01597
published: '2026-09-01'
collected: '2026-09-02'
category: Agent
direction: Agent 语言反馈驱动学习统一框架
tags:
- Verbal RL
- LLM Agents
- Feedback Taxonomy
- Self-Refine
- Alignment
one_liner: 提出 Verbal Reinforcement Learning 统一框架，按语言反馈介入时机分为 grounding、deliberative
  feedback、learning signal 三大支柱
practical_value: '- 在电商推荐 Agent 中，把用户自然语言任务描述（如“推荐适合夏天通勤的连衣裙”）作为 **grounding signal**，定义目标、商品属性状态和可执行动作（过滤、排序、解释），而不是硬编码规则。

  - 推理阶段引入**外部工具反馈**（库存 API、价格校验、评价摘要）作为 grounded critique，修正推荐结果和解释文案，避免模型自说自话的盲区。

  - 将用户对推荐结果的文字反馈（“太贵了”“风格不喜欢”）收集为偏好对，压缩成标量信号用于 DPO/PPO 训练，持续改进推荐策略；同时保留原始文本用于 feedback-conditioned
  SFT，保留更丰富的纠错信号。

  - 训练一个专门的 **feedback-tuned critic** 来评估推荐解释质量或商品匹配度，替代通用 LLM 自评，能显著提升反馈可靠性和校准性，减少
  sycophancy 偏差。

  - 对用户反馈做 **provenance 追踪**，区分真实偏好、噪声和对抗注入，防止恶意反馈操纵推荐策略，尤其在 UGC 电商场景中。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
传统强化学习依赖人工设计奖励函数，成本高且难以覆盖开放场景中的模糊目标。自然语言作为反馈通道能传递意图、偏好和因果结构，且能被现代 LLM 直接解释和执行。但已有方法分散在自我修正、偏好对齐、语言 grounding 等不同子领域，缺乏统一视角，难以系统比较和迁移。

**方法关键点**  
论文提出 Verbal Reinforcement Learning (VRL) 统一框架，以“语言何时进入 agent 生命周期、修改什么”为轴，划分三大支柱：
- **Language as Grounding Signal**（问题定义期）：用语言定义 MDP 的 goal、state、action、reward。例如 Eureka 将自然语言描述编译为可执行奖励代码，Eureka 后续工作扩展到离线偏好优化和视频演示。
- **Language as Deliberative Feedback**（推理期）：不更新参数，用语言反馈修正当前 episode 的输出或推理轨迹。包括 self-critique（Self-Refine）、外部工具 grounded critique（CRITIC）、多智能体辩论、经验记忆（Reflexion, Voyager）、搜索引导的 deliberation（Tree of Thoughts）。
- **Language as Learning Signal**（训练期）：将语言反馈蒸馏为梯度更新，按压缩程度从保留全文（feedback-conditioned modeling）到过滤自生成轨迹（self-improvement）、步骤级评分（process supervision）、最终压缩为偏好标量（DPO/PPO）。

**关键结果数字**  
论文综述了代表性工作的关键增益：Reflexion 通过语言自反思在 HumanEval 上达到 91% pass@1；InstructGPT 用 1.3B 参数模型基于口头偏好判断训练，性能超过 175B GPT-3 基线，参数差距 130 倍；Eureka 在机器人奖励设计上达到人类水平；CriticGPT 等专用反馈模型比通用 LLM 批评更可靠。

**最值得记住的一句话**  
语言反馈正在取代手工奖励成为定义、更新和改进 agent 的主要媒介，瓶颈将从生成反馈转向验证反馈——反馈的来源可信度、质量评估和对抗鲁棒性将成为基础设施要求。
