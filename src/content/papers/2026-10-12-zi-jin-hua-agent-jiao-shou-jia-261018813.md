---
title: Self-Evolving Agent Harness
title_zh: 自进化 Agent 脚手架
authors:
- Chuyang Wei
- Haoxiang Guan
- Minghang Zhu
- Kexin Zhou
- Jiyan He
- Xiren Zhou
- Huanhuan Chen
- Yifei Shen
affiliations:
- Zhongguancun Academy
- Zhongguancun Institute of Artificial Intelligence
- University of Science and Technology of China
arxiv_id: '2610.18813'
url: https://arxiv.org/abs/2610.18813
pdf_url: https://arxiv.org/pdf/2610.18813
published: '2026-10-12'
collected: '2026-10-16'
category: Agent
direction: Agent 自我进化与持续学习理论
tags:
- Agent
- Self-Evolution
- Harness
- PAC-Learning
- Software Scaffolding
one_liner: 保持模型权重固定，仅修订 prompt/memory/workflow/代码实现 Agent 自我进化，并给出持续 PAC 学习保证
practical_value: '- 在推荐/电商 Agent 中，将 prompt、memory、workflow、工具代码作为可独立版本化与验收的资产；更新时强制走“提案-准入”流程，用独立的线上验证集或影子流量做高概率准入决策，避免直接热更引发事故。

  - 对生成式推荐/QueryRec 系统中调用 LLM 的 agent，可借鉴“解释态（如语义 ID 映射、标签）低风险快速更新，可执行代码/工具高风险慢更新”的分层更新策略，控制回归预算。

  - 多智能体协作或 RAG 工作流可引入持续 PAC 式监控：每次 harness 修订后记录历史回归与泛化误差，基于预算决定是否保留更新，保证长期稳定性。

  - 注意组织层面：harness 不断进化会改变团队知识共享与工作流，建议保留修订审计日志、权限隔离和回滚机制，与模型权重更新流程区分开。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Agent 部署后任务和环境持续变化，固定权重模型需要不断调整。现有方法多聚焦模型权重更新，但频繁重训练成本高；harness 自我进化只修订软件脚手架（prompt、memory、workflow、可执行组件），保持权重固定，提供更轻量、可审计的适应路径。

**方法关键点**：将自我进化形式化为反馈驱动闭环，接受的修订跨运行持久化；框架分离“更新目标”与“提案/准入机制”，并区分四类更新：解释态、工具与代码修订、仓库级控制逻辑、插件组合。搜索过程建模为演化优化，用持续 PAC 学习给出可靠性分析：期望泛化界、基于历史回归预算的保留界、基于独立新验证数据的高概率准入规则。还讨论了持久 harness 修订对知识共享、组织工作流、安全性、问责的影响。

**关键结果**：在明确假设下，得到上述三个理论保证；提供 66 页相关研究、算法、评估与应用讨论，代码与补充材料持续更新。
