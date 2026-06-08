---
title: 'Agentopia: Long-Term Life Simulation and Learning in Agent Societies'
title_zh: Agentopia：长期智能体社会模拟与生命奖励学习
authors:
- Xintao Wang
- Sirui Zheng
- Hongqiu Wu
- Weiyuan Li
- Jen-tse Huang
- Minghao Zhu
- Can Zu
- Qi Deng
- Jiawei Wang
- Qianyu He
affiliations:
- Fudan University
- Independent Researcher
- Johns Hopkins University
- University of Science and Technology of China
arxiv_id: '2606.07513'
url: https://arxiv.org/abs/2606.07513
pdf_url: https://arxiv.org/pdf/2606.07513
published: '2026-06-05'
collected: '2026-06-08'
category: MultiAgent
direction: 多智体社会模拟 · 生命奖励训练
tags:
- Multi-Agent Simulation
- Life-Long Learning
- Role-Playing
- Social Intelligence
- LLM Fine-tuning
- Rejection Sampling
one_liner: 实现10年规模的智能体生活模拟，通过生命奖励训练提升LLM的社交智能与角色扮演能力
practical_value: '- 长期多agent模拟可作为训练数据工厂：在虚拟社会中生成海量交互轨迹，无需人工标注，可用于训练客服、导购等角色扮演型对话模型，降低数据成本。

  - 生命奖励的多维设计（社会+主观+经济）可用于优化推荐或对话agent：定义复合奖励并采用拒绝采样挑选高质量轨迹微调，比直接RL更稳定，适合业务中的离线策略优化。

  - 记忆文件系统（Memory Files）提供轻量级长期记忆方案，agent自主管理读写，可借鉴到电商个性化推荐中持续积累用户长期偏好，避免上下文窗口膨胀。

  - 环境模型作为生成式引擎替代硬编码规则，可降低构建复杂模拟环境（如购物决策、多轮协商）的开发成本，利用LLM灵活提供反馈和编排。'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：LLM能否通过模拟社会经验提升拟人化能力？现有智能体社会模拟通常仅持续数天，无法探索长期社会动态与成长，且训练依赖昂贵的人类数据。Agentopia旨在构建长达10年的智能体生活模拟，让LLM从模拟经历中学习社交智能。

**方法关键点**：
- **模拟流程**：100个智能体在三个虚构世界（公寓、魔法学院、中国高中）中生活10年，每周经历计划、联系、活动、回顾四阶段，年末更新档案、申请职位、计算奖励。
- **智能体设计**：包含档案（背景、性格）、社会关系（通过记忆文件自主管理）、动态状态（活力、需求满足度等），并配备了文件系统式的长期记忆，智能体可读写、更新。
- **生命奖励**：从社会（基于他人尊重/喜欢程度的加权PageRank）、主观（多维需求满足度与低值惩罚）、经济（资产变化）三个维度衡量智能体福祉，奖励由环境计算而非自报。
- **生命奖励训练**：采用拒绝采样，选择每年优势（回报相对自身过去提升）前25%的智能体轨迹，过滤低质量回复后微调LLM，并混入通用指令数据防止遗忘。
- **环境模型**：一个独立的LLM作为生成式引擎，负责活动反馈、事件编排、响应过滤、档案更新等，替代大量硬编码规则。

**关键结果**：
- 单次10年模拟消耗13.7B token、567K次调用，约186小时。
- 训练后智能体在模拟中经济奖励+2.5%，主观奖励+1.8%，被尊重人数+24.2%，被喜欢人数+15.9%，社交需求满足度+9.7%；公共活动参与度+7.1%，单人活动减少，显现奖励导向的行为转变。
- 在下游角色扮演基准CoSER Test上，总平均得分从42.51提升到49.16（+15.6%），拟人化维度+23.7%，角色忠实度+16.4%，超过部分闭源模型。

**核心结论**：首次在十年尺度的智能体社会中证实，利用模拟经验通过生命奖励训练可以显著提升LLM的社交智能与拟人化能力，完全无需人类数据。
