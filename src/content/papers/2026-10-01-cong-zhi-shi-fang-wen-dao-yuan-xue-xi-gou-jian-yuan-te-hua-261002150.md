---
title: 'From Knowledge Access to Source Learning: Developing Source-Specific Competence'
title_zh: 从知识访问到源学习：构建源特化能力
authors:
- Lucheng Fu
- Kejing Xia
- Yiyang Wang
- Yiqiao Jin
- Jinjin He
- Xiyuan Yang
- Haoxin Liu
- Ye Yu
- Haibo Jin
- Yijia Xiao
affiliations:
- Georgia Institute of Technology
- University of Illinois at Urbana-Champaign
- University of California, Los Angeles
arxiv_id: '2610.02150'
url: https://arxiv.org/abs/2610.02150
pdf_url: https://arxiv.org/pdf/2610.02150
published: '2026-10-01'
collected: '2026-10-03'
category: Agent
direction: Agent 长期源能力学习
tags:
- Source Learning
- Source Model
- LLM Agents
- RAG
- Self-Directed Learning
- Task-Guided Learning
one_liner: 提出SourceLearn，用自指导+任务指导学习持续构建可复用源模型，在13/15设置中超越RAG与记忆基线
practical_value: '- 在电商/广告 Agent 中，类目规则、活动规则、API 文档、售后政策等是反复访问的持久权威 source。可以维护一个与实时
  RAG 并列的 source model：source model 固化可复用的结构、条件、规则与关系，RAG 继续提供精确证据；任务时按预算激活相关 region，减少每次从零推理。

  - 自指导源学习采用 Inspect–Study–Consolidate 的 read-many write-once 模式：先对照现有源模型找出未解释清的机制/条件，再规划有限
  DEEPEN/CONNECT 动作，最后才提交一次持久更新。适合离线周期性沉淀业务知识库，避免频繁写坏记忆。

  - 任务指导学习不要把失败答案或经验本身存入记忆；只用失败定位源模型缺失的 requirements，然后回到权威 source 做 grounded reconstruction。跨任务可抽象成
  representation lesson，只存“应显式区分条件/不要合并/应同置”等表示偏好，再对 source 做 recalibration，能把经验迁移到未见区域。

  - 源模型实体槽位可参考 attributes/mechanisms/distinctions/decisive_details，优先结构和条件而非低层事实；论文显示条件显式度从约
  30% 升到 65–82%，未来任务覆盖从 23.2% 升到 40.0%，覆盖越高准确率越高。检索失败时，source model 也能单独维持与完整检索 RAG
  相当的水平，适合兜底降级。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

动机：现有 LLM Agent 反复使用同一外部 source 时，通常仍是重复访问，RAG 优化的是访问方式，记忆系统保存的是任务经验，都没有持续提升对 source 本身的理解。Source learning 把持久权威 source 作为学习对象，目标是建立可复用的 source-specific competence。

方法关键点：
- 源模型 M：以实体为中心，槽位化表示 attributes、mechanisms、distinctions、decisive_details，保留结构、规则、条件和关系；低层细节留给原始 source。
- 初始构建 M0：按实体阅读 source，生成 provisional 模型。
- 自指导源学习：Inspect–Study–Consolidate 循环，观察当前模型仍有缺口的地方，规划 DEEPEN/CONNECT 学习动作，read-many write-once，最终通过 grounded reconstruction 提交持久更新。
- 任务指导源学习：用 guidance tasks 诊断 source requirements；failure-guided local refinement 只对模型中缺失的 requirements，回到 source 重建；cross-task representation learning 聚合 representation lessons 成 policy，再对 source 做 recalibrate。
- 推理时：source model 超过预算则按 region 激活，与 retrieval evidence 互补；学习信号只决定要重新看什么，权威 source 决定什么能成为持久知识。

关键实验：在 MultiDoc2Dial、NarrativeQA、SWE-QA、APIBench、AppWorld 五个 benchmark、三个 LLM backend 上，SourceLearn 在 15 个 setting 中 13 个最优；相比 Hybrid RAG 平均提升 +14.3/+4.9/+13.4 points，最大提升 +22.6；消融显示 self/task 学习互补，两种任务指导路径都必要。分析表明模型从孤立事实转向规则和程序，条件显式度从约 30% 升到 65–82%，未来任务覆盖从 23.2% 升到 40.0%，且覆盖越高准确率越高；检索证据缺失时性能下降更慢。

最值得记住：学习信号决定要重新看什么，权威 source 决定什么能进入持久记忆；任务经验只用来暴露缺口，不直接写入。
