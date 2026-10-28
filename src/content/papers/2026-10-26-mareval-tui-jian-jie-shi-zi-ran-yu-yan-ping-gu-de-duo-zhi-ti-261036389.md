---
title: 'MAREval: A Multi-Agent Framework for Evaluating Natural Language Recommendation
  Explanations'
title_zh: MAREval：推荐解释自然语言评估的多智能体框架
authors:
- Reza Yousefi Maragheh
- Jayesh Uddhav Kudase
- Aysenur Inan
- Ramin Giahi
- Kai Zhao
- Parth Parikh
- Jianpeng Xu
- Jason Cho
- Evren Korpeoglu
- Sushant Kumar
affiliations:
- Walmart Global Tech
arxiv_id: '2610.36389'
url: https://arxiv.org/abs/2610.36389
pdf_url: https://arxiv.org/pdf/2610.36389
published: '2026-10-26'
collected: '2026-10-28'
category: Eval
direction: 多智能体 LLM-as-a-judge 评估推荐解释
tags:
- Multi-Agent
- LLM-as-a-Judge
- Recommendation Explanation
- Evaluation
- Monte Carlo Sampling
- Chain of Debate
one_liner: 规划者-主持者-仲裁者多智能体+Monte Carlo 采样提升推荐解释评估的人工对齐和稳定性
practical_value: '- 将单智能体 LLM-as-a-judge 改造为 planner→evaluator→moderator→arbitrator
  流水线，planner 先生成各角色同步步骤，能显著减少 prompt drift 和辩论噪声，适合电商推荐解释的质量审核。

  - moderator 用动态摘要代替全量上下文，过滤冗余、保留关键分歧，可在长文本或多轮评估中降低 token 成本和上下文污染，类似 trick 可复用到商品文案或
  push 文案自动评估。

  - 对黑盒 LLM 用 pipeline-level Monte Carlo 采样（N=5 次取平均）降低输出方差；实验显示 4 个 evaluator、5 次采样是成本/性能折中点，边际收益递减。

  - 上线前将自动评估作为硬约束门禁，辅以少量人工抽检，可实现硬标准 100% 通过；骨干模型选择显著影响评估质量，Gemini 2.5 Pro / Claude
  3.5 Sonnet 明显优于 GPT-3.5，实际选型需先在自有数据上验证与人工标注的相关性。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
推荐解释质量评估传统依赖人工标注，昂贵且难以规模化；单智能体 LLM-as-a-judge 存在 prompt 敏感、输出不一致、自我修正退化问题；现有多智能体辩论缺乏结构化协调，易出现 prompt drift 和噪声。业务需要一个稳定、可上线、与人工判断对齐的自动评估框架。

### 方法关键点
- **Chain of Debate (CoD)**：引入 planner agent，根据评估标准、上下文和 pipeline 流程，一次性生成所有轮次 evaluator、moderator、arbitrator 的同步计划，避免各 agent 独立规划导致的不协调。
- **Context Moderation**：moderator agent 对每轮评估做摘要蒸馏，作为动态记忆机制，减少冗余和上下文过载，同时保留分歧点。
- **Arbitration**：arbitrator agent 根据 moderator 摘要和仲裁计划做最终判定，统一输出格式。
- **Monte Carlo 采样 (MAMCS)**：对黑盒 LLM 跑 N 次完整多智能体流水线取平均，或在 token 概率可获取时计算期望输出，抑制采样随机性。

### 关键实验
在两个数据集上验证：TopicalChat 公共对话数据集和 Walmart 私有电商推荐解释数据集（108 条解释，相关性/措辞质量二分类）。基线包括 Vanilla-gpt、CoT、Self-Refine、G-Eval、ChatEval。
- TopicalChat Overall Chat Quality：MAREval ρ=0.548, τ=0.478，优于 G-Eval 的 0.487/0.431 和 ChatEval 的 0.455/0.390。
- 私有电商 Relevance：MAREval ρ=0.338, κ=0.334，ChatEval 为 0.238/0.225，多数单智能体方法 κ 低于 0.05。
- 稳定性：MAREval 平均标准差 0.0197，低于 G-Eval 的 0.0227，Self-Refine 高达 0.1563。
- 人工门禁：G-Eval 过滤样本硬标准 91.0%、软标准 76.1%；MAREval 过滤 5000 样本硬标准 100%、软标准 98.6%。
- 线上 A/B：MAREval 过滤解释后 ATC +1.18% (p=0.05)，GMV +1.36% (p<0.01)。
- 骨干模型影响：Gemini-2.5-pro ρ=0.728/τ=0.632，Claude-3.5-sonnet 0.658/0.564，GPT-3.5 Turbo 0.548/0.478。

### 最值得记住的一句话
用 planner 做同步计划、moderator 压缩上下文、arbitrator 汇总，再叠加 Monte Carlo 采样，能让 LLM 评估推荐解释从不可靠的随机判断变成可上线质量门禁，在电商线上直接带来 GMV 和 ATC 提升。
