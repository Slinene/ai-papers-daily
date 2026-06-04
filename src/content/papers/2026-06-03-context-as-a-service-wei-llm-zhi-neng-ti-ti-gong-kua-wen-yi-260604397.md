---
title: 'Context-as-a-Service: Surfacing Cross-File Dependency Chains for LLM-Generated
  Developer Documentation'
title_zh: Context-as-a-Service：为 LLM 智能体提供跨文件依赖链检索层
authors:
- Ameya Gawde
- Vyzantinos Repantis
- Harshvardhan Singh
- Lucy Moys
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2606.04397'
url: https://arxiv.org/abs/2606.04397
pdf_url: https://arxiv.org/pdf/2606.04397
published: '2026-06-03'
collected: '2026-06-04'
category: Agent
direction: Agent 工具增强 · 跨文件依赖检索
tags:
- LLM Agent
- Retrieval-Augmented Generation
- Code Documentation
- Cross-File Dependencies
- Tool Use
one_liner: 提出 CaaS 检索层，让 LLM 代理通过混合搜索追踪跨文件依赖，提升文档审查质量并节省 22-34% 时间
practical_value: '- **检索增强代理设计模式**：在电商推荐系统中，为 Agent 构建专用检索索引（如商品知识图谱、接口文档、历史实验记录），使用「关键词+语义」混合搜索作为工具，让
  Agent 自主查询跨模块依赖，避免将所有上下文塞入 prompt，能显著提升复杂任务（如推荐链路排障、AB 报告生成）的准确性和效率。

  - **增量评估方法**：论文采用基线已具备常规仓库工具（文件读取、关键词搜索）再叠加检索层的对比方式，可迁移到评估推荐 Agent 增强方案，确保效果归因于新增的检索能力而非基础工具完善。

  - **减少 token 开销的工程技巧**：通过有目标的检索索引，Agent 无需加载大量上下文，输入 token 使用量下降，节省成本。这在调用大模型生成推荐理由、商品描述等高频任务中可直接复用。

  - **依赖链追踪对多智体协作的启示**：电商多 Agent 系统中，各 Agent 处理不同领域（商品、用户、营销），CaaS 的思路可用来构建跨 Agent
  知识检索总线，使 Agent 能按需查询其他 Agent 的输出依赖，避免信息孤岛。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM 智能体越来越多用于编写和维护开发者文档，但文档准确性常取决于代码库中隐式的跨文件依赖链。即使提供更多上下文文件，智能体仍需自主决策追踪哪些依赖，常遗漏关键关系。

**方法**：提出 Context-as-a-Service (CaaS)，作为智能体的检索层。CaaS 提前索引源代码、API 参考和上游文档；智能体在审查或生成文档时，通过工具调用以「关键词+语义」混合搜索查询索引，获取跨文件依赖证据。基线智能体已具备文件读取、关键词搜索和符号导航等常规仓库工具，CaaS 仅增加额外检索能力，用于隔离评估。

**结果**：在两个生产 SDK 案例中，使用 Claude Sonnet 4.5，CaaS 增强的智能体在 API 参考评论审查任务中不仅复现了基线发现的 5 处缺失文档，还额外找出 2 个跨文件事实错误和 2 个表述不清晰的 API 注释。在教程验证任务中，CaaS 发现了 1 个可执行 bug、1 个 API 用法改进和 2 个缺失前置条件，均被基线遗漏。这些发现需追踪工具文件、框架内部、使用示例和测试中的非显式依赖。五次重复实验中，引入 CaaS 使墙钟时间减少 22%~34%，输入 token 使用量显著降低。
