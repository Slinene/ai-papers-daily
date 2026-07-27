---
title: 'Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills'
title_zh: 技能自我对弈：用可进化的技能接口突破 LLM 自我训练的数据困境
authors:
- Siyuan Huang
- Pengyu Cheng
- Haotian Liu
- Tao Chen
- Yihao Liu
- Jingwei Ni
- Shijie Zhou
- Ziyi Yang
- Gangwei Jiang
- Mengyu Zhou
affiliations:
- Alibaba
- The Chinese University of Hong Kong
- Renmin University of China
- Sun Yat-sen University
- Peking University
arxiv_id: '2607.22529'
url: https://arxiv.org/abs/2607.22529
pdf_url: https://arxiv.org/pdf/2607.22529
published: '2026-07-23'
collected: '2026-07-27'
category: Agent
direction: Agent 自我进化 · Skill 协同
tags:
- Skill-SP
- Self-Play
- Co-Evolution
- Tool-Calling
- Reasoning
- Reinforcement Learning
one_liner: 通过可进化的技能库充当任务生成的结构化接口，在工具调用与逻辑推理上显著超越无引导自我对弈
practical_value: '- **技能库即任务模板池**：电商搜索/推荐中可将高频意图、结构化的查询改写或回复模式抽象为可进化的技能模块，直接指导生成式推荐或对话模型的训练，避免无监督生成的数据坍塌。

  - **双轨训练与动态课程设计**：借鉴技能流（skill stream）与开放探索流（exploration stream）混合构建训练池的做法，在推荐模型或Query改写模型的强化学习训练中，用预定义模板确保基本质量，同时用无约束采样扩展多样性，通过前沿奖励自动筛选高价值样本。

  - **技能生命周期管理**：定期根据模型表现剪枝已饱和的技能、从成功探索中诱导新技能，可迁移到推荐系统中的新闻推送文案生成、活动主题生成等场景，自动淘汰低质模式，持续注入新鲜内容。

  - **共进化验证机制**：用同一个模型同时扮演提议者和求解者的自我对弈，可用于线上自动评估推荐解释/文案的质量，无需额外标注，适合业务中快速迭代的Agent或生成式推荐组件。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
现有LLM自我进化方法面临任务多样性（覆盖广）与验证可靠性（判断准）的根本矛盾：环境绑定的方法能得到精确反馈，但任务空间狭窄；开放式的无引导生成虽然覆盖面广，却依赖被动的后置过滤，错误积累易导致训练崩溃。本文观察到 Agent 技能（Skill）可作为解耦这一矛盾的中层抽象：每个技能封装特定场景的可验证执行逻辑，动态技能路由则维持任务开放性，从而在保持高保真验证的同时实现广阔的课程学习空间。

**方法关键点**
- **技能自我对弈框架（Skill-SP）**：由提议者（Proposer）、求解者（Solver）和技能控制器（Skill Controller）三部分组成，通过强化学习循环协同进化。
- **技能条件生成**：提议者从可进化的技能库（Skill Library）中采样技能作为结构性先验，生成具备明确契约（如单元测试、约束规则）的可验证任务，同时保留无技能约束的探索流以维持多样性。
- **前沿课程构建**：通过求解者在生成任务上的成功率计算前沿奖励（Frontier Reward），仅保留有效且难度适中的任务构建训练池，并用双重过滤确保结构完整性（模式合规、契约有效、探针一致性）。
- **技能库持续进化**：控制器根据验证失败的轨迹优化旧技能，剪枝产出平凡任务的饱和技能，并从探索流中归纳新技能，形成“生成—验证—进化”闭环。
- **优化目标**：求解者最大化环境验证奖励；提议者最大化有效任务的前沿奖励；两者均通过 GRPO 异步更新，以避免奖励黑客。

**关键实验结果**
- 在工具调用（API-Bank、BFCL）和逻辑推理（ZebraLogic）两个领域，Skill-SP 在 5 种不同基座（3B–14B）上均稳定提升。Qwen3-4B-Instruct 工具调用平均绝对提升 **+6.5** 点，推理格级准确率提升 **+3.9** 点；对初始完全无法自制有效任务的 Ministral-3-8B，工具调用大幅增长 **+42.9** 点，推理格级 **+20.0** 点，远超无引导自我对弈。
- 消融实验证实：移除技能引导（仅无引导自我对弈）导致 **-2.6** 点整体退化；静态技能路由或冻结技能库分别带来 **-1.9** 与 **-2.3** 点退化；冻结提议者或反馈求解者均显著损害效果，验证了共进化更新的必要性。
- 技能库诊断显示，技能流生成的任务平均 𝑣_solve ≈ 0.57，恰好落在模型学习前沿，且 PCA 可视化表明任务多样性远超无引导方法。

**一句话核心**：将技能抽象为可进化的任务生成接口，能同时保证自我对弈中的数据多样性与验证可靠性，为 LLM 无监督自我进化提供稳定且可扩展的引擎。
