---
title: 'EEVEE: Towards Test-time Prompt Learning in the Real World for Self-Improving
  Agents'
title_zh: EEVEE：面向现实世界多数据流测试时提示学习的自改进智能体
authors:
- Weixian Xu
- Shilong Liu
- Mengdi Wang
affiliations:
- Shanghai Jiao Tong University
- Princeton University
arxiv_id: '2606.11182'
url: https://arxiv.org/abs/2606.11182
pdf_url: https://arxiv.org/pdf/2606.11182
published: '2026-06-09'
collected: '2026-06-10'
category: Agent
direction: 多任务测试时提示学习与自改进智能体
tags:
- Prompt Learning
- Self-Improving Agents
- Router-Prompt Co-evolution
- Test-time Adaptation
- Multi-task Learning
one_liner: 通过路由器和提示协同进化，在异构多任务流中实现稳定的测试时提示学习，缓解跨任务干扰
practical_value: '- **多场景路由提示适配**：可借鉴 router 条件下的多 prompt 集成分思路，为电商推荐中不同业务线（如搜索推荐、直播文案、商品描述）自动分配专用
  prompt，避免统一 prompt 在任务间相互干扰。

  - **路由与提示协同更新策略**：在 Multi-Agent 系统中，可将路由器视为任务分配 Agent，提示视为执行 Agent，借鉴交替进化的训练流程（初始化→交替探索→收敛）来最小化耦合风险，实现自改进的协作模式。

  - **Pareto 前沿多样性提示初始化**：使用贪婪覆盖选择互补 prompt，可应用于生成式推荐中构建多风格文案生成器或 Semantic ID 多样性集合，确保不同
  prompt 覆盖不同的用户意图。

  - **过程性任务优先优化**：实验表明测试时提示学习对可转化为可复用规则的代码生成、公式计算等提升显著，但对领域知识密集型任务可能削弱知识利用。在电商文案生成中，可优先用于格式约束强、可模板化的任务（如自动生成标题、卖点），减少对知识密集型描述的过度干预。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有测试时提示学习方法多为单一数据集设计，但真实部署中智能体面临异构输入流（多领域、多格式），更新提示时单一 prompt 难以兼顾所有任务，导致严重的跨任务干扰。本工作旨在让自改进智能体在混合任务流中实现稳定的性能提升，并保持各任务的历史能力。  
**方法关键点**  
- **路由机制**：维护 K 个专用 prompt，并训练一个 router 将输入动态分配给最匹配的 prompt，避免共享 prompt 的跨域遗忘。  
- **路由-提示协同进化**：交替执行 router 更新和 prompt 更新，利用下游准确率、一致性、平衡性评分进化 router，用 Pareto 前沿保留互补 prompt，解决两者相互依赖的优化问题。  
- **三阶段训练**：初始化阶段通过 Pareto 池贪婪选择多样性强 prompt；探索阶段快速交替路由与提示进化，评分权重从一致性/平衡性退火至准确率；收敛阶段固定 router，为每个槽位投入更大预算精细优化 prompt。  
- **高效推理**：router 仅增加少量 token 开销，避免像 ACE 那样累积过长的上下文。  
**关键实验**  
在 GPQA Diamond、Formula、TheoremQA、HumanEval 四个基准混合训练流上评估，与 GEPA、ACE 对比。  
- 在 Qwen3-4B-Instruct 上，EEVEE 平均得分 51.75，比基线高 10.38，比 GEPA 高 14.02；DeepSeek-V3.2 上平均 64.07，比基线高 24.32。  
- 增量多任务学习中累积保留提升 +41.53，而 GEPA 和 ACE 分别降至 -15.36 和 -18.58。  
- 单基准测试仍保持竞争力，且 token 开销仅为 ACE 的 1/5。  
- 案例研究表明，提示学习擅长提取可复用过程（代码、公式计算），但可能削弱封闭域知识问答所需的领域知识。
