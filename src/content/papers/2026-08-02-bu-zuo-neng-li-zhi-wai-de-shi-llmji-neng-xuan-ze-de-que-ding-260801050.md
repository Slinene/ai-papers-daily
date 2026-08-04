---
title: 'Don''t Offer What Can''t Be Done: Deterministic Executability Gating for LLM
  Skill Selection at Scale'
title_zh: 不做能力之外的事：LLM技能选择的确定性执行门控
authors:
- Ortal Ashkenazi
- Vitalii Kloz
- Mykhailo Ulianchenko
affiliations:
- Wix
arxiv_id: '2608.01050'
url: https://arxiv.org/abs/2608.01050
pdf_url: https://arxiv.org/pdf/2608.01050
published: '2026-08-02'
collected: '2026-08-04'
category: Agent
direction: Agent 技能路由 · 确定性执行门控
tags:
- LLM agent
- tool selection
- deterministic gating
- executability
- skill routing
- production deployment
one_liner: 在LLM技能路由中，用技能内部退出条件做确定性过滤，避免推荐不可执行的技能，节省59%的上下文token并减少7.8%的错误选择
practical_value: '- 在LLM工具选择/技能路由pipeline中，将语义相关性与执行可行性解耦：先用recall-oriented的语义检索召回复候选，再通过确定性代码检查业务状态（如用户权限、账户配置）过滤不可执行的技能，可大幅减少prompt中技能描述token（本案例减少59.1%）并降低模型选择不可用操作的风险。

  - 门控谓词应直接复用技能内部的退出条件（exit conditions），通过工程手段保持与技能逻辑的parity，而非训练一个分类器；这样在谓词等价且状态一致的前提下，过滤掉的技能必定无法成功执行，可避免“虚假过滤”。

  - 需建立谓词生命周期维护机制：当技能逻辑变更时，同步更新门控谓词，并用回归测试确保parity；监控门控决策与实际执行结果的一致性，防止谓词漂移或状态陈旧导致过block或漏block。

  - 对电商/推荐Agent（如导购助手、客服），可将此思路应用于过滤不可操作的商品/服务（如缺货、无权限、不满足优惠条件），避免LLM生成无法兑现的推荐，提升信任度和任务完成率。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
LLM代理在从大型技能库中选择工具时，语义相关性匹配的技能可能因当前账户状态（如缺失权限、已有冲突配置）而无法实际执行。若仅依靠检索或模型判断，会暴露出大量“明知不可为”的选项，浪费提示词token，并可能误导用户进入死胡同。因此需要一种与语义无关的执行可行性检查，在候选集进入模型上下文前进行确定性过滤。

## 方法
- **三阶段管线**：① 状态无关的语义匹配（recall-oriented），识别与某领域相关的消息，并输出该领域全部技能；② 确定性门控，读取权威业务状态，评估每个技能的硬退出条件（exit conditions），移除条件为真的技能；③ LLM agent仅从剩余的可执行技能中决策是否调用。
- **门控谓词构建**：直接从每个技能内部实现中的退出条件反推得到门控谓词，保持与技能执行时检查逻辑的等价性。在谓词等价且状态一致的前提下，被阻挡的技能在任何相同状态下必定无法完成，从而保证“soundness by construction”。
- **不涉及学习**：门控完全由确定性代码实现，无需标注数据，不依赖模型判断。

## 实验
- **数据集**：Wix客服助手Helpmate的在线对话，包含756,641条消息、267,612个会话，聚焦一个domain skill family（10个技能）。
- **指标**：技能-消息对数量、技能描述token数、技能阻塞率。
- **关键结果**：
  - 语义阶段匹配了23.1%的消息，产生1,749,270个候选对；门控移除了其中的59.4%（1,039,462对），节省了59.1%的技能描述token（2.288亿token），与向所有消息暴露10个技能的基线相比，总token减少90.5%。
  - 在1,000个高风险的counterfactual回放中，去除门控后，模型在7.8%的对话中选择了一个被生产环境门控阻挡的技能，说明门控有效防止了不可执行选项影响模型决策。
- **技能间差异**：不同技能的阻塞率从28.1%到94.1%不等，token节省分布不均，表明需按技能粒度管理。

**最值得记住的一句话**：将执行可行性从模型选择中剥离，用技能的自身退出条件做确定性门控，让基础设施保证“能做什么”，而让LLM处理“想做什么”。
