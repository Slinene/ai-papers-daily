---
title: 'SePO: Self-Evolving Prompt Agent for System Prompt Optimization'
title_zh: SePO：自演进提示代理优化系统提示
authors:
- Wangcheng Tao
- Han Wu
- Weng-Fai Wong
affiliations:
- National University of Singapore
- City University of Hong Kong
arxiv_id: '2606.04465'
url: https://arxiv.org/abs/2606.04465
pdf_url: https://arxiv.org/pdf/2606.04465
published: '2026-06-02'
collected: '2026-06-05'
category: Agent
direction: 自演进提示代理优化框架
tags:
- System Prompt Optimization
- Self-Evolving Agents
- Evolutionary Search
- Self-Referential
- Prompt Engineering
one_liner: 通过自指涉设计，使提示代理在进化搜索中同步优化自身与任务代理的系统提示，突破手工设计瓶颈。
practical_value: '- **动态优化多智能体系统**：在电商多智能体（如推荐、客服、运营）中，可引入 SePO 式自演进提示代理，自动迭代各 Agent
  的系统提示，替代手工调参，持续适应变化的业务场景。

  - **低成本跨任务泛化**：预训练-微调两阶段设计，先在多任务池上进化出通用提示优化能力，再快速适配具体推荐任务（如生成式推荐、Query 改写），大幅降低重复优化成本并提升新任务冷启动效果。

  - **失败-成功平衡采样避坑**：提示优化时按 1:1 同时输入失败与成功案例，避免代理过拟合单一失败模式，这一技巧可直接用于推荐提示词迭代或用户意图理解的
  Prompt Engineering 中。

  - **archive 进化搜索防止早熟**：基于存档的开放演进保留历史上性能较好的提示作为“垫脚石”，可借鉴到推荐策略的自动化调优中，防止搜索陷入局部最优。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有系统提示优化方法（如 TextGrad、MetaSPO）只自动优化任务代理的提示，而负责生成提示的“提示代理”自身的系统提示仍由人工编写且固定不变，这导致优化能力受限于人的设计水平，且无法从任务经验中持续提升。  
**方法**  
提出 SePO，将提示代理自身的系统提示也纳入优化目标，形成一个自指涉闭环：提示代理像优化任务代理一样优化自身提示。采用基于存档的开放进化搜索，维护候选提示种群，将早期优质提示作为“垫脚石”推动后续改进。训练分为两阶段：  
- **预训练**：在多任务混合池上进化提示代理自身的系统提示，获得通用的提示优化技能；  
- **微调**：复用训练好的提示代理，在具体目标任务上优化任务代理的系统提示，此时提示代理固定。  
任务选择上，使用贪婪启发式算法平衡目标任务相关性和任务间多样性。  
**关键结果**  
在数学（AIME’25）、抽象推理（ARC-AGI-1）、研究生级科学（GPQA）、代码生成（MBPP）和逻辑谜题（Sudoku）五个基准上，SePO 平均准确率比 Manual-CoT 高 4.49 个百分点，全面超越 TextGrad 和 MetaSPO。SePO-Generalist 通过泛化的提示优化技能，即使对未见于预训练的任务（如 Sudoku）也能带来增益。消融证实自改进和开放进化的必要性。成本上，SePO-Generalist 通过分摊预训练成本，使每个微调任务成本与 TextGrad 相近或更低。  
**核心洞见**：让提示代理自己也能进化，是打破人工设计上限的关键。
