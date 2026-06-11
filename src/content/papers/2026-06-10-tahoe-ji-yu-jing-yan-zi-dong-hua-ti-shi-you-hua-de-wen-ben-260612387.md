---
title: 'TAHOE: Text-to-SQL with Automated Hint Optimization from Experience'
title_zh: TAHOE：基于经验自动化提示优化的文本到 SQL 系统
authors:
- Zhiyi Chen
- Jie Song
- Peng Li
affiliations:
- ByteDance Inc.
- Georgia Institute of Technology
arxiv_id: '2606.12387'
url: https://arxiv.org/abs/2606.12387
pdf_url: https://arxiv.org/pdf/2606.12387
published: '2026-06-10'
collected: '2026-06-11'
category: LLM
direction: Text-to-SQL · 持久化提示管理
tags:
- Text-to-SQL
- Hint Optimization
- Persistent Memory
- Agent
- LLM
one_liner: 将提示优化重构为持久化的数据管理问题，通过错误驱动的提示学习构建结构化提示库，实现高效、可迁移的 Text-to-SQL 生成。
practical_value: '- **错误驱动的结构化记忆范式**：在电商搜索、推荐查询改写等场景，可将编译/执行/用户反馈提炼为可复用的提示规则，避免每次重复试错，显著降低线上推理延迟和成本。

  - **冲突策略显式建模**：面对多义的用户意图（如“爆款”需包含并列），将不同解释存储为同一触发词下的竞争策略，并用成功/有害/惰性统计做运行时排序，这直接可迁移至生成式推荐中的目标锚定与意图消歧。

  - **语法与语义解耦 + 分层作用域**：在跨业务（多国多语言）的电商平台上，可分离通用逻辑与特定数据库/用户偏好，实现模型无关的热更新，无需微调即可适应新方言或新用户习惯。

  - **两阶段推理（逻辑规划 + SQL 合成）**：可借鉴到复杂生成任务中，先利用轻量检索整理冲突策略、形成连贯逻辑方案，再生成最终输出，有效缓解大型 prompt
  的上下文噪声和注意力衰减问题。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：工业级 Text-to-SQL 面临严格方言约束、海量 schema 和动态用户意图三大挑战。现有方法要么依赖高成本的测试时扩展（agentic loop），要么因 SFT 导致僵化，抑或简单 RAG 引入上下文噪声，都无法在效率与适应性上取得平衡。TAHOE 的核心洞察是：与其重复在线纠错，不如将提示优化转化为一个离线的、持久化的数据管理问题。

**方法关键点**：
- **Hint Bank**：结构化的外部知识库，解耦为 Syntax Hints（方言规则，如双引号引用）和 Semantic Hints（触发词→多个竞争策略），每条策略配有学习时间戳和事后归因统计（成功/有害/惰性）。
- **错误驱动的提示学习流水线**：对每个训练样本，执行多样本推理 → 顺序语法/语义反馈 → 原子 diff 提取 → 簇化建议 → 更新临时提示库，成功或改善则合并至全局库，无效则丢弃。
- **两阶段推理**：逻辑规划阶段根据检索策略的置信度排序、消歧，形成统一方案；SQL 合成阶段注入完整方言语法提示，生成最终可执行 SQL。
- **覆盖保证**：为防止提示库偏向错误案例，筛选首次就成功的样本，提取其所用的“常规策略”并入库，保持公平竞争。

**关键结果**：在 Spider 2.0–Snow 的 113 条开发集上，基于 GPT-5.5 的通过率从 61.95% 提升至 79.42%，pass@4 从 72.57% 升至 87.61%，方言语法通过率达 100%，平均编译器反馈轮次从 2.79 降至 0.12。同一 Hint Bank 直接用于更弱的 Doubao-2.0-lite 模型，仍带来 +19.7pp 的通过率增益，验证了跨模型迁移性。在留出样本上语法迁移稳健，语义提升依赖于开发集对目标工作负载的覆盖度。
