---
title: The Compaction Cliff in Long-Running AI Agent Memory
title_zh: 长运行AI Agent记忆中的压缩悬崖
authors:
- Saber Zerhoudi
- Jelena Mitrovic
- Michael Granitzer
affiliations:
- University of Passau, Passau, Germany
- IT:U, Linz, Austria
arxiv_id: '2608.22752'
url: https://arxiv.org/abs/2608.22752
pdf_url: https://arxiv.org/pdf/2608.22752
published: '2026-08-24'
collected: '2026-08-25'
category: Agent
direction: Agent 长期记忆压缩与安全规则保留
tags:
- Context Compaction
- Agent Memory
- Safety Rules
- Knowledge Triage
- Long-Running Agents
- LLM
one_liner: 提出 Knowledge Triage 框架，通过分类与确定性算子避免安全规则在长上下文压缩中快速丢失
practical_value: '- 将 Agent 上下文知识分为需逐字保留的安全/合规规则与可粗粒度压缩的日志/经验，不同类别走不同压缩策略，避免生产 Claude
  /compact 这类统一 summarization 造成规则坍塌。

  - 在电商/推荐 Agent 中，价格上下界、库存状态、平台政策、prompt 约束等规则适合用 TypeCompact 按类型保真度压缩，并附加确定性验证器检查规则是否完整，防止多轮任务后策略漂移。

  - TypeRetrieve 的“规则 pinned ahead of relevance”思路可直接用于 RAG/长期记忆：先返回适用规则，再按相关性补充内容，保证召回合规边界。

  - AgentArtifactCorpus 可作为测试压缩/检索策略的外部基准，尤其适合评估长流程 Agent 在不同压缩轮次下的安全规则 retention。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：长运行 Agent 的上下文窗口有限，安全规则与场景日志竞争 token；预算溢出时统一 summarization 会丢掉需要精确措辞的规则。生产环境 Claude Code /compact 在 Sonnet 4.6 上一轮压缩后仅保留 53% 安全规则，五轮后只剩 10%。

**方法**：提出 Knowledge Triage 框架，将每行知识分类，按类型路由到不同保留策略。三个确定性算子：TypeCompact 按 per-type 保真度原地压缩；TypeDecompose 将大 topic 分区并复制跨分区安全规则；TypeRetrieve 检索外部存储时把适用规则钉在相关性之前。分类器+验证器确保约束未被丢失。

**结果**：五个公开语料上，TypeCompact 在任意压缩比下比最强单次 LLM 压缩器多保留 2–4 倍安全规则，五轮 recall 达 96%；TypeDecompose 局部性违规 0%（uniform 分区为 93%）；TypeRetrieve recall@50 100%（最强 LLM retriever 为 73%）。下游医疗合规 p<10^-8、零售任务通过率 p<0.01、航空领域 p=0.024。发布 AgentArtifactCorpus。
