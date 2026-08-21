---
title: 'Eureka: Task-Conditioned Meta-Agent Orchestration for Scientific Discovery'
title_zh: Eureka：面向科学发现的任务条件化元智能体编排
authors:
- Alizer Wong
- Heng Cui
- Yi Tan
- Xiongchao Zhan
- Liang Lin
- Yuxiang Guo
- Zhaorong Dai
- Zixin Zeng
- Wenyuan Li
affiliations:
- ManXis
- Guangdong University of Technology
- South China Normal University
- Shanghai Jiao Tong University
- Duke University
arxiv_id: '2608.19047'
url: https://arxiv.org/abs/2608.19047
pdf_url: https://arxiv.org/pdf/2608.19047
published: '2026-08-19'
collected: '2026-08-21'
category: MultiAgent
direction: Meta-Agent 任务条件编排与自演化
tags:
- Meta-Agent
- Multi-Agent Orchestration
- Scientific Discovery
- Self-Evolving Agents
- Receding-Horizon Planning
- Task-Conditioned Architecture
one_liner: 提出任务条件的 Meta-Agent 架构，动态编译义务图并形成专门代理，通过治理式演化完成长程科学发现
practical_value: '- **动态义务图 + ready frontier 调度**：在电商多 Agent 场景（如大促策划、商品打标、广告文案生成）中，避免一次性完整规划，改为维护有依赖关系的义务图，仅执行前置条件已满足的节点，减少规划浪费和上下文膨胀。

  - **架构热点识别与 Macro-Agent 封装**：根据子任务间状态共享、依赖密度、操作复用等遥测，将高频协作的子任务封装为拥有私有状态和工具集的专门子
  Agent，减少重复状态加载和通信 token；父编排器只通过类型化接口查看已验证产物。

  - **治理式自演化（governed evolution）**：不盲目循环优化，而是用 cost-benefit gate 判断是否值得修改架构；对低风险局部变异（如
  prompt/工具接口）给予有限租约，结构性变更升级到高层，避免长程任务中过度搜索。

  - **接受证书机制**：对关键节点输出附带可回放收据和验证器契约，确保在复杂流程（如推荐策略生成、数据管道）中每个环节可审计，避免置信错误。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：长程任务（如科学发现、开放数学猜想）对任务分解、状态维护、验证、工具使用和长期自适应提出综合要求。固定架构必须同时满足多种异构认知结构，导致架构错配和协调开销。仅靠扩大模型规模无法消除因状态复制、串行化、缺失验证语义等产生的结构开销，因此需要根据任务本身的认知结构动态形成并维持合适的智能体架构。

**方法关键点**：
- 将长程任务编译为动态义务图（obligation graph），节点包含目标语义、依赖、读写集、接受契约；采用 receding-horizon planning，仅展开当前信息可确定的部分，通过 ready frontier 背压驱动规划。
- 通过状态共享、依赖密度、操作/验证器复发、剩余时长等遥测识别架构热点，执行 architecture promotion，将局部子树封装为 Macro-Agent，拥有专门状态、记忆、操作符、工具、验证器和拓扑。
- 通过 typed subtree interface 对外暴露已验证导出产物、显式假设、未解决债务和重开条件，父编排器只观察这些接口。
- 对复发瓶颈实施 cost-benefit-gated governed evolution，仅在预期收益能摊销诊断、评估和迁移成本时修改架构；架构修改分层级进行，低风险局部变异在 EvolutionLease 内执行，结构性变更升级到 Meta-Agent。

**关键实验**：
- 170/170 递归长程任务全部完成，产出 3,948 个接受证书，无未认证接受或错误终端状态。
- 编译主动上下文将中位模型输入从 9,490 tokens 降至 4,005，同时保持成功率。
- 12,000 个增量依赖任务中避免 65.38% 重复计算。
- 16,000 个并发执行与有效串行执行一致，0 个不安全提交。
- 同一 Meta-Agent 形成 Theory-Discovery Agent 和 Math/Conjecture Agent，分别取得量子过程/时空理论结构结果和黎曼猜想相关进展，后者将 Suzuki 局部 Weil 二次型的全向量正性证书推进至 0 < a ≤ 69/200 = 0.345，约为第一素数阈值的 99.55%。

**最值得记住的一句话**：长程任务的智能体能力不仅取决于底层模型，还取决于能否根据任务本身的认知结构动态形成并维持合适的智能体架构。
