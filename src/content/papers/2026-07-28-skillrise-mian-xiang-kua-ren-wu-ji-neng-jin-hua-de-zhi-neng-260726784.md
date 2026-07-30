---
title: 'SkillRise: Agentic Reinforcement Learning for Cross-Task Skill Evolution'
title_zh: SkillRise：面向跨任务技能进化的智能体强化学习
authors:
- Zhiyuan Yao
- Yuxin Chen
- Zhengxi Lu
- Zishan Xu
- Yueqing Sun
- Yifu Guo
- Yuquan Lu
- Zhengzhou Cai
- Kangning Zhang
- Zhuowen Han
affiliations:
- Zhejiang University
- National University of Singapore
- Shanghai Jiao Tong University
- Meituan
arxiv_id: '2607.26784'
url: https://arxiv.org/abs/2607.26784
pdf_url: https://arxiv.org/pdf/2607.26784
published: '2026-07-28'
collected: '2026-07-30'
category: Agent
direction: Agent 多任务技能进化与文档迭代
tags:
- AgenticRL
- Cross-Task
- SkillEvolution
- DecoupledCredit
- Curriculum
one_liner: 将相关任务序列化并用单一策略交替执行任务解决与技能文档演化，以解耦信用分配实现跨任务技能迁移
practical_value: '- **跨任务技能积累范式**：对于电商搜索/推荐Agent，可将不同商品类目下的搜索/推荐任务视为同一任务族，按难度递增构造序列，使Agent在解决简单任务后沉淀通用策略，再迁移到复杂任务，减少重复探索。

  - **演化文档作为记忆载体**：在投放策略优化或多轮对话中，让Agent维护一份技能文档（例如“高价商品推荐要点”），每次任务后自动更新，替代外部记忆库的复杂维护，降低工程复杂度。

  - **解耦信用分配**：将“执行当前任务”与“为后续任务总结经验”的奖励分离，执行用即时反馈，总结用后续任务折扣回报，避免两者相互干扰，适合广告出价、查询改写等需要平衡即时效果与长期学习的场景。

  - **测试时持续提升**：SkillRise展现的随着相关任务序列增加性能递增的特性，可应用于在线服务中持续积累跨请求的经验，无需重新训练即可利用历史交互不断优化策略。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
LLM Agent经常遇到共享潜在规律的相关但不同任务，标准Agentic RL将每个任务视为独立episode，丢弃了可从经验中抽取的可复用技能。现有技能学习方法要么反复尝试同一任务（得到的知识难以跨实例迁移），要么依赖多阶段流水线（技能抽取、存储、检索耦合，难以归因组件效果）。因此需要一个端到端框架，让Agent在解决任务的同时从交互中提炼可迁移技能，并用下游任务表现直接监督技能质量。

**方法关键点**  
- **跨任务序列构建**：将同一任务族的不同实例按难度递增排列（如WebShop按属性数量），形成由简到繁的序列，早期技能可支持后期任务。  
- **单一策略双阶段交替**：同一策略在任务间切换角色：先基于当前技能文档进行任务解决，完成后进入技能整理阶段，根据轨迹改写技能文档（抽象、剔除实例细节、记录失败教训），仅传递更新后的文档给下一任务。  
- **解耦信用分配**：任务解决直接使用当前任务奖励，技能整理使用后续任务的折扣累积奖励，从而分离“完成任务”与“为未来提供帮助”的学习信号。  
- **角色感知的组相对优势**：在同一序列位置和阶段内计算优势，避免解决与整理相互干扰，优化时对两者应用相同的PPO式裁剪损失。

**关键结果**  
在ALFWorld、WebShop、ScienceWorld三个交互式文本环境中，SkillRise（Qwen3-4B）取得最优Pass@1：85.9%、84.4%、54.6%，分别超出最强基线GiGPO 2.3、7.1、8.5个百分点。即使其在训练时从未在相同任务上重复尝试，Pass@2/3也全面领先，说明学会的技能迁移策略可泛化至同一任务的重试场景。测试时，随跨任务序列长度从2增至6，成功率从83.6%提升至87.5%，展现跨任务外推能力。消融表明技能整理阶段贡献约3个点提升。与多阶段流水线RetroAgent、SkillRL相比，SkillRise仅需1/6的运行时间且性能相当或更优，验证了端到端精简设计的有效性。

**核心要义**：跨任务技能学习无需复杂的外部记忆流水线，通过序列化相关任务、演化文本技能文档及解耦信用分配即可让Agent持续自我改进。
