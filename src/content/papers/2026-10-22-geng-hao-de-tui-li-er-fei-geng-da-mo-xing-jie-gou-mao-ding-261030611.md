---
title: 'Better Reasoning, Not Just Bigger Models: A Structure-Grounded Framework for
  Efficient and Reliable Inference'
title_zh: 更好的推理，而非更大模型：结构锚定的高效可靠推理框架
authors:
- Amirhossein Aghaei
- Liangyan Li
- Shiyi Yang
- Shaohua Wang
- Yan Wang
affiliations:
- Huawei Research Canada
- Huawei Technologies Co., Ltd.
- Central University of Finance and Economics
arxiv_id: '2610.30611'
url: https://arxiv.org/abs/2610.30611
pdf_url: https://arxiv.org/pdf/2610.30611
published: '2026-10-22'
collected: '2026-10-23'
category: Reasoning
direction: 结构化不确定性削减 · 多轮推理
tags:
- Structure-Grounded Reasoning
- Uncertainty Reduction
- Graph Matching
- Active Information Gain
- Multi-turn Inference
- Training-Free
one_liner: 训练无关的 SGUR 框架用先验加权图匹配与主动信息增益消减多轮推理不确定性，医学诊断 Hit@3 达 92.5% 且 token 少 5 倍
practical_value: '- 可把业务知识构建成共享 schema 的异构图数据库，将用户当前行为/属性作为 query graph，再做先验加权部分图匹配，而不是对所有边等权检索；先验权重可由历史数据中的关系频率或决策增益得到，重点强化与最终决策相关的边。

  - 主动信息增益策略可迁移到对话式推荐或 Agent 客服：不要问次要属性，而是按信息增益最大的节点/属性发起下一轮询问或补特征，既减少 token 消耗，也降低用户负担，同时系统性剪枝候选空间。

  - 训练-free 框架可叠加在任意 LLM 后端上，适合业务快速上线验证；较小后端模型配合结构约束，可逼近甚至超过 10 倍规模的大模型，有助于降低线上推理成本。

  - 对 Graph-RAG 类方案有直接启示：不要把所有图边一视同仁，先验权重让检索更聚焦决策相关关系，减少噪声，提升命中率。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：模型规模提升带来流畅生成，但可靠自主 Agent 需要的不只是流利表达。多轮推理中现有系统常产生语义合理却结构失据的推理，尤其在观察不完整时。

方法关键点：提出训练无关框架 SGUR。离线阶段从专家数据构建分层专家图数据库 Gdb，并采用共享 schema；在线阶段把不完整观察表示为 query graph，通过先验加权部分图匹配与候选假设图对齐。先验来自数据库经验频率，对决策相关关系赋予更高重要性，避免所有图边等权。推理状态随后由主动信息增益策略迭代优化：每次选择信息量最大的节点发起查询，系统剪枝候选空间，形成闭环多轮推理。

关键结果：在 PrimeKG 派生的序贯医疗诊断 benchmark 上，仅从两个已观察症状出发，SGUR 达到 92.5% Hit@3，比最强 Graph-RAG 基线高 9.4 个百分点，同时 token 用量约为其 1/5。结构 grounding 还能部分替代模型规模：较小骨干模型可匹配或超过最高 10 倍规模模型的表现，说明结构化 grounding 比单纯扩大模型更稳健高效。
