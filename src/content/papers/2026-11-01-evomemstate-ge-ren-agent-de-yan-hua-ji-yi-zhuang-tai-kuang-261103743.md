---
title: 'EvoMemState: Evolving Memory State for Personal Agents'
title_zh: EvoMemState：个人 Agent 的演化记忆状态框架
authors:
- Zhishang Xiang
- Yunbo Tang
- Zhongqiao Liu
- Junkai Chen
- Zerui Chen
- Qingguo Hu
- Yuxuan Zhang
- William Grant
- Qinggang Zhang
- Jinsong Su
affiliations:
- Xiamen University
- Nanyang Technological University
- University of British Columbia
- University of Waterloo
- Jilin University
arxiv_id: '2611.03743'
url: https://arxiv.org/abs/2611.03743
pdf_url: https://arxiv.org/pdf/2611.03743
published: '2026-11-01'
collected: '2026-11-06'
category: Agent
direction: 个人 Agent 长期记忆状态化建模
tags:
- Agent Memory
- Relational State
- GRPO
- Personalization
- Long-term Memory
- LLM
one_liner: 将长期记忆从事实为中心升级为状态为中心，用关系状态保留更新与冲突，用 RL 学习请求特定的推理状态
practical_value: '- 在用户画像/长期行为建模中，不要只存扁平 embedding 或最新 profile；保留历史 fact，并用关系图显式标
  SUPERSEDES/CONFLICTS_WITH/validity scope，推荐、广告排序时区分 current vs historical preference，避免旧行为带偏新决策。

  - 检索阶段用“种子召回 + 关系图双向 traversal”补全证据：电商 query/push 场景中，用户一句话命中的标签可能没有包含冲突或更新信息，沿用户画像关系边扩展，可提升上下文完整率和最终策略正确性。

  - 借鉴 GRPO 训练轻量 Memory State Evolution Policy：只训练一个小 policy 生成自然语言“如何使用用户记忆”的指导，冻结主
  LLM/推荐生成模型；可用于个性化文案、query 改写、消息推送选择，奖励直接用下游业务指标（点击/转化/答案质量）做相对 gain。

  - 用推理状态显式控制记忆 applicability/role/priority，降低 sycophancy/过度个性化；在电商导购或推荐解释中，可生成“预算约束优先于历史类目偏好”等规则，避免模型一味迎合历史偏好。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM 个人代理的长期记忆通常采用 fact-centric 范式，把用户信息抽取成独立事实并维护检索。但事实会随时间失效、更新、冲突；即使检索到全部相关事实，Agent 仍可能误判适用性、优先级，被旧偏好带偏。因此需要把“记忆内容”与“记忆状态”解耦。

**方法关键点**：
- Ontology-Guided Memory State Induction：按时间顺序抽取 Persistent Facts，增量构建个人本体图；概念层级用 PARENT_OF/CONTAINS，事实间用 SUPERSEDES/CONFLICTS_WITH，形成 Relational States（有效性、范围、关系），保留原始记录不覆盖。
- RL-Based State Evolution：用 GRPO 训练 Memory State Evolution Policy，输入请求、相关事实和关系状态，生成请求特定的 Reasoning State，说明记忆的适用性、角色和优先级。奖励是下游冻结 Agent 带/不带的得分差。
- State-Aware Reasoning：检索 top-K 种子事实后，沿关系边双向 traversal 补全更新/冲突证据；再用 policy 生成推理状态，指导冻结 Agent 生成答案。

**关键结果**：在 MemSyco-Bench 上，Qwen3-8B/GPT-4o-mini 分别达到 57.6/58.9，比最强基线高 12.2/5.9 个百分点；LoCoMo-Refined 的 LLM-judge 比最强基线高 6.1/7.0 个百分点。完整证据检索率 85.6%；完整证据下 Acc@complete 在 LoCoMo-Refined 和 MemSyco 上分别为 70.8/68.5，超过最强基线 11.5/31.2 个百分点。消融显示，移除关系状态使 MemSyco 掉 8.9、MemTrapBench 掉 6.4；移除 RL 训练掉 7.9/16.4。

**最值得记住的一句话**：个人记忆的可靠性不只取决于“召回多少事实”，更取决于显式维护事实间关系并学习“何时/如何使用”记忆。
