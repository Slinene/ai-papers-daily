---
title: 'HABIT-Bench: Evaluating Habit Induction from Longitudinal Weak Evidence in
  Agent Memory'
title_zh: HABIT-Bench：评估智能体从长期弱证据中归纳用户习惯
authors:
- Junming Zhang
- Rubin Wei
- Xu Cheng
- Hao Sun
- Jiarui Wang
- Ruoxi Cheng
- Xiquan Wang
- Peisong Wu
- Mingsong Chen
- Zhouhan Lin
affiliations:
- LUMIA Lab, School of Artificial Intelligence, Shanghai Jiao Tong University
- Shanghai Artificial Intelligence Laboratory
- Fudan University
arxiv_id: '2610.24520'
url: https://arxiv.org/abs/2610.24520
pdf_url: https://arxiv.org/pdf/2610.24520
published: '2026-10-19'
collected: '2026-10-28'
category: Eval
direction: Agent 记忆评估 · 隐式习惯归纳
tags:
- Agent Memory
- Long-term Memory
- Habit Induction
- Personalization
- RAG
- Evaluation
one_liner: 四域基准显示现有 Agent 记忆方法准确率仅约 33%，复杂记忆流程不优于简单检索或历史压缩
practical_value: '- **不要默认复杂记忆 pipeline 更优**：在需要跨会话状态重构的长用户轨迹上，BM25/Dense RAG 等简单检索基线与
  A-MEM、Mem0、MemOS、Letta 等记忆方法准确率接近，GLM 下 Full Memory 压缩历史甚至达到 41.98%，超过全部记忆方法。业务落地前应先验证
  RAG/压缩历史强基线，避免过度设计。

  - **区分“证据访问”和“决策正确性”**：Oracle Evidence 提供标注证据后准确率仍只有 39.26%–58.25%，而 Oracle Habit
  State 可达 98%+。意味着即使召回相关行为，模型仍常错误应用习惯。电商/广告中需显式建模行为有效期、例外、边界和用户确认，不能把任意历史点击/对话当长期偏好。

  - **记忆构建成本与查询成本高度不对称**：A-MEM 构建 54.59 小时、107.80M tokens，查询仅 13.24 分钟、3.39M tokens。工程上要把历史预处理与在线推理分离，按记忆复用频率和更新需求评估
  ROI，必要时用增量更新或压缩历史替代全量记忆抽取。

  - **可迁移的负样本设计思想**：将临时期外、已过期选择、未接受的建议、边界情况作为干扰项，能有效测出模型是否“过度个性化”。推荐系统评估可借鉴四选一 probe，测试模型在
  scope、exception、temporal drift 下是否仍正确推荐。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
长期交互中的 LLM Agent 需要从用户大量会话里推断隐式行为习惯，但单条观察往往只提供部分证据，且习惯存在适用范围、临时例外、时间漂移和用户是否确认等问题。现有记忆基准多关注召回、推理或选择性遗忘，缺少对“弱证据归纳 + 条件化应用”的联合评估。HABIT-Bench 正是为量化这一能力而构建。

**方法关键点**
- 定义 habit memory：从跨会话不完整证据推断行为默认值，并根据 scope、exceptions、temporal validity、user endorsement 决定是否应用。
- 构建 114 个合成用户、37,152 个会话、3,328 个探针，覆盖 Food、Finance、Software、Travel 四个领域，分别侧重上下文对比、工作流重构、状态漂移、规则迁移。
- 每个 probe 为四选一任务：给定当前请求、候选动作、可见历史截止点和目标时间，要求选出唯一符合用户习惯的动作。错误选项包含过时选择、扩大默认范围、把未接受建议当作已确认偏好等。
- 人工审核：两位评审独立根据标注证据包选择答案并做八项质量评价，不一致由第三位裁决；仅在证据足以唯一支持时才计为有效。

**关键实验与结果**
- 对比 8 种记忆方法（A-MEM、Mem0、MemOS、MemRL、LightMem、SeCom、Letta、MIRIX）以及 Recency、BM25、Dense、Temporal Hybrid RAG、No/Full Memory 控制组。
- 最强记忆方法 macro accuracy 为 33.06%（Qwen3-235B-A22B）和 33.61%（GLM-5.3-Flash），仅略高于随机 25%；简单 BM25/Dense RAG 达到 32.50%/33.21%，而 GLM 的 Full Memory 压缩历史达 41.98%。
- Oracle Evidence 下准确率仅 39.26%–58.25%，相比 Oracle Habit State 的 98%+ 差距明显，说明给出相关证据仍不足以解决条件化决策。
- 证据命中 Hit@5 约 37.77%–41.44%，annotated evidence recall 仅 11.17%–13.89%，Joint A+E 为 12.92%–16.20%，表明检索到部分相关会话远不等于正确决策。

**最值得记住的一句话**：长期记忆系统的瓶颈不在“存了多少”，而在是否同时保存了默认行为、适用条件、例外和时效，并在决策时按这些边界使用。
