---
title: 'Causal Chain of Thought: Mitigating Attention Leakage via Context Isolation'
title_zh: 因果思维链：通过上下文隔离缓解注意力泄漏
authors:
- Gabriele Dominici
- Teague McMillan
- Fazl Barez
- Marc Langheinrich
- Martin Gjoreski
affiliations:
- Università della Svizzera Italiana
- ETH Zurich
- University of Oxford
arxiv_id: '2610.31639'
url: https://arxiv.org/abs/2610.31639
pdf_url: https://arxiv.org/pdf/2610.31639
published: '2026-10-22'
collected: '2026-10-23'
category: Reasoning
direction: 因果推理 · 上下文隔离 CoT
tags:
- Causal Inference
- Chain-of-Thought
- Attention Leakage
- Context Isolation
- Explainability
- DAG
one_liner: 提出 CausalCoT 推理框架，将问题拆成 DAG 原子子问题并在隔离上下文中求解，提升因果敏感度与解释忠实度
practical_value: '- 在电商推荐/广告的 LLM 解释生成或 Agent 多步决策中，可借鉴 DAG 分解：把复杂任务拆成原子子问题，每个节点只喂直接依赖的上下文，降低无关信息通过注意力污染推理路径的风险。

  - 对于多步 query 改写、选品推理等场景，用隔离上下文能减少模型“直接查答案再补理由”的虚假解释，使中间步骤对局部输入更敏感，便于定位错误节点。

  - 可复用 test-time intervention 机制：线上发现某个推理节点输出错误时，只需修正该节点即可按依赖图向下游传播，无需重新生成整条推理链，利于实时策略调整。

  - 架构上可采用结构化依赖图作为推理骨架，与现有 CoT 或 ReAct 类流程兼容，额外成本主要在子问题拆解和上下文裁剪，适合对可信度和可审计性要求高的推荐解释或风控审核逻辑。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：标准 CoT 虽然生成看似合理的逐步推理，但自回归生成中的稠密注意力允许每步访问全上下文，模型可能直接查找到答案，再生成事后合理化解释，导致解释不忠实、中间步骤缺乏因果驱动。

**方法关键点**：CausalCoT 将问题分解为有向无环图（DAG）的原子子问题，每个节点在仅包含其直接因果父节点的隔离上下文中评估。这种马尔可夫结构切断了到非父节点的注意力路径，使下游预测依赖局部推理而非全局上下文泄漏。具体实现包括问题图构建、逐节点隔离生成、以及支持测试时干预的依赖传播机制。

**关键结果**：在多个推理基准上，CausalCoT 保持与强基线相当的预测性能，同时显著提升解释忠实度；中间推理步骤的因果敏感度平均比最强基线提高 12 个百分点，最高提升 21 个百分点。结构化依赖图还允许局部修正按图传播，验证了可干预性。
