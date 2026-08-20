---
title: 'Harness the Memory: A Holistic Evaluation of Memory Substrates in Memory Agents'
title_zh: 驾驭记忆：记忆智能体中记忆基质的整体评估
authors:
- Wei-Chieh Huang
- Weizhi Zhang
- Yuchen Wu
- Yankai Chen
- Eric Hanchen Jiang
- Wooseong Yang
- Yiwei Yang
- Henry Peng Zou
- Hanrong Zhang
- Ying Nian Wu
affiliations:
- University of Illinois Chicago
- University of Washington
- McGill University
- MBZUAI
- University of California, Los Angeles
arxiv_id: '2608.15008'
url: https://arxiv.org/abs/2608.15008
pdf_url: https://arxiv.org/pdf/2608.15008
published: '2026-08-14'
collected: '2026-08-20'
category: Eval
direction: Agent 记忆基质评测与自适应路由
tags:
- Memory Agents
- Memory Substrates
- Evaluation
- LLM Agents
- Retrieval
- Adaptive Routing
one_liner: 统一评测多种记忆基质，发现无单一最优，需按任务类型与历史长度做自适应路由
practical_value: '- 记忆基质选型不是检索越强越好：在事实性 QA（如客服问答、商品知识库）中，dense/sparse 广泛检索有增益；但在多步决策（如导购
  Agent、谈判流程）中，过度检索会挤占动作关键上下文，建议控制检索数量或设置相关性阈值。

  - 长历史下中等长度表现好的基质可能成本激增或变脆：用户长期偏好存储不宜直接套用现有结构，需设计分层、压缩、refinement 机制，或按会话长度、任务类型动态路由到不同存储介质。

  - 评测要同时看效率与任务指标：在自己的 Agent 评测 harness 中加入 memory 读写的 token 成本、延迟、检索命中率等，避免只优化下游准确率而忽略工程可行性。

  - 把 memory substrate 抽象为可替换组件并统一接口，方便在推荐对话、个性化搜索等场景中快速对比 dense/sparse/structural/parametric
  等不同存储方案。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：长程 LLM agent 依赖持久记忆，但现有评测对“用哪种记忆基质（memory substrate）在什么运行条件下最优”缺乏指导。不同任务对记忆读写、检索广度、成本敏感度差异很大，需要系统化实证。

**方法关键点**：构建统一评测 harness，覆盖 dense/sparse indices、text records、structural stores、hierarchical stores、refinement-based memories、parametric updates、activation-compatible context mechanisms 等记忆基质。在 3 个 backbone 模型、4 个 benchmark suites（用户为中心 QA 与 agent 决策）上，测量 26 个性能和效率指标。

**关键结果**：没有任何单一基质全面领先。广泛检索对长上下文事实 QA 有帮助，但过度检索会损害序列决策——注意力被从动作关键上下文移开。可扩展性引入新的路由维度：在中等历史长度表现好的基质，在更长历史上可能成本过高或变得脆弱。结论支持 substrate routing 作为自适应 agent memory 系统的必要组件，并给出分 regime 的选型经验。
