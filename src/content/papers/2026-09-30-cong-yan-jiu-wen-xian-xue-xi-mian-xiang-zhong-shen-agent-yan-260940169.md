---
title: 'Learning from Research: Toward Lifelong Agent Harness Evolution'
title_zh: 从研究文献学习：面向终身 Agent Harness 演化
authors:
- Jingbo Yang
- Kwei-Herng Lai
- Xiaowen Wang
- Yaar Harari
- Evgeniy Gabrilovich
- Shiyu Chang
affiliations:
- University of California, Santa Barbara
- Microsoft
arxiv_id: '2609.40169'
url: https://arxiv.org/abs/2609.40169
pdf_url: https://arxiv.org/pdf/2609.40169
published: '2026-09-30'
collected: '2026-10-01'
category: Agent
direction: Agent harness 终身演化 · 文献驱动搜索
tags:
- Agent Harness Evolution
- Lifelong Learning
- Topic Modeling
- Literature-Guided Search
- Module Crossover
one_liner: 用论文检索、主题建模和模块化交叉重组，在冻结 LLM 下自动演化 Agent 执行层 harness
practical_value: '- 把 Agent 执行层拆成 Tool / Context / Skills / Memory / Workflow 五个模块，只演化
  harness 代码、冻结 LLM 权重。业务上可以在不重训模型的前提下快速迭代线上 Agent，尤其适合电商导购、客服、广告投放等需要频繁调整工具和上下文策略的场景。

  - 失败轨迹不要直接喂给 coding agent 改代码，先做 failure audit，把 badcase 抽象成 capability gaps，再转成
  research queries 去查论文。这样能把业务问题翻译成文献检索问题，持续引入新机制。

  - 用 TopicGPT 式主题建模把候选论文聚成正交机制族，按 round-robin 分配预算，而不是按 relevance ranking 取 top-K。可避免反复在
  workflow 里加 verifier、多 Agent 辩论等内卷操作，探索更宽的机制空间。

  - 单模块 mutation 之后再做 crossover 组合评估：先用 additive predicted gain 便宜初筛组合，再对短名单实测。注意单模块指标排名不能预测组合效果，这对应推荐系统中召回/排序/策略模块的组合搜索，值得直接复用。

  - 终身演化可以作为工程机制：定期拉取新论文，从当前 champion 启动新一轮搜索，用独立的 validation tasks 做 fitness，test
  严格隔离。适合让线上 Agent harness 跟进学术界最新 memory consolidation、skill library 等方法。'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
语言 Agent 要处理越来越复杂、长周期的任务，但反复训练大模型成本过高。近期工作转向演化 agent harness：在冻结 backbone 的情况下，修改工具调用、上下文管理、技能、记忆、工作流等执行层代码。现有方法让 coding agent 根据执行反馈改 harness，存在三个问题：探索窄，容易反复在 workflow 里加 verifier 或多 Agent 辩论；设计知识受限于 meta agent 自身能力；适应滞后，往往要等失败积累到一定程度才触发更新。因此，有必要像人类专家一样从研究文献中持续获取新的候选机制。

## 方法关键点
- **五模块化 harness**：Tool interface、Context management、Skills、Memories、Agentic workflows，模块接口隔离，支持单模块 mutation 与跨模块 crossover。
- **文献池构建**：在 Devo 轨迹上做 failure audit，抽象出 benchmark-agnostic 的 capability gaps，再生成 research queries，检索论文和代码。
- **TopicGPT 式主题建模**：把每模块的论文聚成机制 topic，合并重叠主题，再按 round-robin 跨 topic 选论文，保证探索的正交性和多样性。
- **从论文到 mutation**：研究 agent 读全文和代码，产出 mutation blueprint；coding agent 实现单模块改动，并通过 health probes 检查可导入性、接口兼容和 action 产出。
- **组合与选择**：单模块候选分别实测后，用 additive predicted gain 枚举组合并短名单实测，考虑模块交互；用 paired bootstrap 置信区间决定是否保留新 champion。
- **终身演化**：定期吸收新论文，从当前 champion 启动新一轮搜索；backbone 权重始终不变。

## 关键实验
在 AppWorld 和 τ2-Bench 上验证。Qwen3.5-27B 经 ScholarEvolve 后，AppWorld Normal TGC 从 69.0% 提升至 81.4%，Challenge 从 49.6% 提升至 63.6%；SGC 分别从 48.8% 到 69.0%、28.3% 到 44.8%。GPT-5.4-mini 在 τ2-Bench Telecom 上 pass1 从 72.7% 提升至 81.9%，pass4 从 49.2% 到 58.3%。相比 Meta Harness，Challenge TGC 高出 9.0–10.0 pp。终身演化三轮后 TGC 达 81.55%。消融显示 research guidance、module-wise mutation、topic-guided selection 逐步移除后性能持续下降；组合分析表明单模块最强的候选未必构成最强组合。

最值得记住的一句话：**把学术文献当作 harness 搜索的外部知识库，用主题建模保证正交探索，是比纯 execution feedback 更有效的持续演化信号。**
