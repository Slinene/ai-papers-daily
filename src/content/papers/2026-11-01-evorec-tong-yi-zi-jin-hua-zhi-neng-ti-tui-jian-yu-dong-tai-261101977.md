---
title: 'EvoRec: A Unified Self-Evolving Agentic Recommender with Dynamic Reflection
  Trees'
title_zh: EvoRec：统一自进化智能体推荐与动态反思树
authors:
- Mengting Li
- Long Zhang
- Hao Jiang
- Sheng Yu
- Fei Pan
- Peng Jiang
affiliations:
- Kuaishou
arxiv_id: '2611.01977'
url: https://arxiv.org/abs/2611.01977
pdf_url: https://arxiv.org/pdf/2611.01977
published: '2026-11-01'
collected: '2026-11-03'
category: Agent
direction: Agentic 推荐 · 反思树自进化
tags:
- Agentic Recommendation
- Dynamic Reflection Tree
- Self-Evolving Recommender
- LLM Planning
- Industrial A-B Test
one_liner: 提出统一 agentic 推荐框架，通过动态反思树定位失败并生成可复用修复策略，实现无参数更新的自进化推荐
practical_value: '- **离散化 Agent 决策空间**：Planning Agent 只从 {0.1,...,0.9} 中选择检索预算比例和融合权重，而不是任意连续值。这既降低
  LLM 输出不确定性，又便于在线校验和回退，适合直接迁移到需要稳定性的广告/推荐系统。

  - **可验证的反思树 + 工作记忆**：失败被定位到 ERROR-NEED / ERROR-PLAN / ERROR-MEMORY 三类，修复策略必须通过 replay
  验证后才进入 working memory，避免错误经验污染后续决策。业务上可借鉴这一闭环：只对高意图用户（有搜索/咨询行为）做反思，控制成本并提升反馈质量。

  - **近线生成、在线竞争架构**：LLM 推理完全离线，预计算需求、计划和 query 向量，候选人异步发布到 Kafka，与现有召回通道并列进入统一排序。用户侧与物品侧独立刷新，索引更新后无需重跑
  LLM。这种架构可让 Agent 决策不阻塞实时请求，适合工业落地。

  - **策略抽象为“调参指令”而非具体 item**：修复策略只规定调整方向、条件和大致的数值范围（如提高 Need Satisfaction 预算），不推荐具体物品，避免退化为记忆个别反馈，能跨用户复用。推荐系统做反思时宜采用这种参数化修复，而非实例级记忆。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
传统级联推荐由预定义召回、粗排、精排构成，离线优化后固定部署，无法根据用户变化和实际反馈自主调整决策。近期 agentic 推荐引入推理和工具调用，但多局限于单阶段，缺乏端到端决策控制，也缺少对推荐失败的定位和可复用修复。由于转化失败可能源于需求漏判、计划不当或之前学到的错误策略，仅看最终反馈很难将失败转化为经验。

**方法关键点**  
EvoRec 将推荐建模为“需求理解 → 规划 → 执行 → 反馈 → 反思 → 修复”闭环。  
- **Need Agent** 从长期、短期和工作记忆中推断结构化需求（描述、证据、优先级、来源）。  
- **Planning Agent** 在 Behavior Continuation 与 Need Satisfaction 两条路径间分配检索预算比例，选择检索工具和排序融合权重；取值限制在 {0.1,...,0.9} 离散网格，降低动作空间复杂度。  
- **Acting Executor** 确定性执行计划，多路检索结果按 snake-order 合并，Base / SASRec / Two-Tower 通过加权 RRF 融合，并记录完整决策与执行 trace。  
- **Dynamic Reflection Tree** 将错误层级定位到 ERROR-NEED、ERROR-PLAN 或 ERROR-MEMORY：系统级节点保存通用错误模式和修复策略，用户级节点保存个性化修复和验证状态。修复策略只调整需求推断和规划的方向与幅度，不指向具体 item；策略通过 replay 验证后写入工作记忆，后续推理时注入对应 Agent。随着验证经验累积，系统级节点进行 merge / split / reparent 演化，形成跨用户可复用知识。整个过程不更新任何 Agent 参数。

**关键实验**  
在快手本地服务广告数据集上，28,227 个用户、355,163 条候选池，离线 Hit@50 比最强 baseline InteRecAgent 提升 15.7%；即使去掉反思，EvoRec 仍以相同工具和 4B 模型（对方 32B）超出 InteRecAgent 12.9%，说明自适应决策本身贡献显著。在 18.5% 获得工作记忆的用户上，反思使 Hit@50 再提升 13.1%。在线七天 A/B 测试中，广告收入 +4.6%，CTCVR +3.5%；高意图用户收入 +14.5%，CTCVR +5.6%。

**最值得记住的一句话**  
让 Agent 通过可验证的反思树把失败定位到需求、计划或记忆，并将修复策略作为工作记忆在推理时复用，可以在不更新模型参数的情况下实现推荐系统持续自进化。
