---
title: When Does Selection Replace Extraction? A Pre-Registered Test of Agent Memory
  with a Typed Decision Model
title_zh: 何时用选择取代提取？一项基于类型决策模型的智能体记忆预注册测试
authors:
- Rishabh Sharma
- Rishika Lall
affiliations:
- Independent Researcher
arxiv_id: '2609.34227'
url: https://arxiv.org/abs/2609.34227
pdf_url: https://arxiv.org/pdf/2609.34227
published: '2026-09-27'
collected: '2026-10-07'
category: Agent
direction: Agent 记忆选择与重排序
tags:
- Agent Memory
- Selection vs Extraction
- Reranking
- Typed Decision Model
- LLM
one_liner: 预注册实验表明：在紧凑预算下，用类型决策模型单次选择原始对话轮次，效果非劣于 LLM 提取记忆且成本极低；重排序增益随预算增大而减弱
practical_value: '- 对话式推荐 / 客服 Agent 的记忆模块可优先采用「原始对话轮次选择 + 轻量判别模型（typed decision model）」，不必先做
  LLM 事实提取，写入成本可降低几个数量级，在预算紧张时效果非劣，适合高吞吐场景。

  - 重排序的投入应视最终保留的上下文预算而定：如果 context window 只能容纳少量候选（如 3/30），重排序收益显著（+17.4 / +9.1）；如果预算充裕，收益递减（+1.5
  / +1.1），可省去该环节降本增效。

  - 在匹配上下文长度下，轻量 typed decision model 可作为 LLM reranker 的低延迟替代（约 1/3 延迟），用于召回后的候选筛选，尤其适合对时延敏感的在线推荐服务。

  - 实验采用预注册 + 非劣性检验，这种评估范式适合迁移到业务算法替换场景：证明新策略「不差」而非「更优」，可加速低成本方案的灰度上线。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：对话记忆是否需要 LLM 提取事实，还是仅选择正确的原始轮次即可？已发表结果存在分歧：提取系统报告蒸馏事实带来增益，而近期研究发现排序良好的原始历史同样有效，但对排序是否重要仍有争议。

**方法**：作者进行预注册研究，在 LoCoMo 和 LongMemEval 的留出集上比较两种记忆构建方式：LLM 提取记忆 vs 使用类型决策模型 Jev 单次调用从原始对话中选择相关轮次。在不同上下文预算下测试重排序效果，并进行盲评人类评估。

**关键结果**：在 LoCoMo 紧凑预算下，Jev 选择的原始轮次非劣于 LLM 提取记忆（单侧 95% 界 -3.0，非劣边距 -5），写成本低 3061 倍，换用第二个答案模型结果一致。重排序增益随预算增大而缩小：从 30 个候选中保留 3 个时，LoCoMo 提升 17.4 分，LongMemEval 提升 9.1；预算充足时仅提升 1.5 和 1.1，且提取系统更准确。匹配上下文时，Jev 选择准确性与 LLM reranker 非劣（界 -2.0），延迟仅三分之一，优于多调用图遍历。重排序会降低正确弃权。
