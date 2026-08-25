---
title: Risk-Aware Reranking for Agentic Tool Retrieval
title_zh: 风险感知的Agent工具检索重排序
authors:
- Qinfei Li
- Xiaoxuan Dong
- Jin Zhang
- Dexu Yu
- Wenhao Deng
- Junchen Fu
- Youhua Li
- Hanwen Du
- Chunxiao Li
affiliations:
- University of Science and Technology of China
- University of Electronic Science and Technology of China
- Lanzhou University
- Fenz.AI
- University of Glasgow
arxiv_id: '2608.22751'
url: https://arxiv.org/abs/2608.22751
pdf_url: https://arxiv.org/pdf/2608.22751
published: '2026-08-24'
collected: '2026-08-25'
category: Agent
direction: Agent 工具检索的风险感知重排序
tags:
- risk-aware reranking
- tool retrieval
- LLM agents
- retrieval safety
- dual-head ranking
- tool risk annotation
one_liner: 提出轻量双头重排序框架，在保持相关性的同时通过可调风险惩罚和规则过滤降低高风险工具暴露
practical_value: '- 在电商/广告的 Agent 工具调用或 API 选择场景，可以在召回后增加双头重排序：冻结已有 encoder，只训练两个轻量
  MLP 头（相关头 + 风险头），用 `s = f_rel - λ f_risk` 融合，λ 作为推理时旋钮控制安全-效用平衡，头部参数量仅 20 万，推理开销极小。

  - 对商品/内容候选做类似风险标注（如合规风险、敏感类目、价格操纵风险），定义 RVR@k / SRR@k 类指标监控 top-k 风险暴露，作为 NDCG/MRR
  之外的安全补充指标；该论文的标注方案（三 LLM 投票 + 人工复核）可直接复用。

  - 规则过滤器思路可迁移到严格合规场景：重排后叠加硬约束（如最多一个高风险商品、相似度去重），提供可解释的保守操作点，适合需要审计的推荐/搜索候选集。

  - ToolGraph 的分数平滑主要提升相关性而非安全，若要在业务中引入 item 关系图（如同店铺、共现、类目）做平滑，应将其定位为相关性增强模块，安全控制需依赖独立的风险头或规则。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
LLM agent 依赖外部工具执行任务，工具检索决定哪些可执行工具暴露给 agent，成为执行前的安全边界。现有工具检索方法只优化语义相关性，安全评估多发生在工具执行之后，但检索阶段形成的 top-k 候选集已经限定了 agent 可选择的动作空间，高风险工具一旦进入候选集可能引发不可逆后果。为此，论文为 6108 个工具标注五级操作风险，将工具检索形式化为相关性-安全权衡问题。

**方法关键点**
- 冻结 ToolRet-BGE 编码器，只训练两个轻量 MLP 头：query-conditioned 的相关性头 `f_rel(q,t)` 和 tool-level 风险头 `f_risk(t)`，总参数量 196,866。
- 推理时用 `s(q,t) = f_rel(q,t) - λ f_risk(t)` 融合，λ 控制安全-效用平衡，同一模型可支持不同操作点。
- 构建四种边类型的 ToolGraph（共现、语义、权限、风险共现）对分数做一步平滑，提升排序质量。
- 可选规则过滤器：最多一个高风险工具（风险≥3）、最多两个高权限工具、余弦相似度>0.9去重，提供保守部署模式。
- 风险标签由 Claude Code、Codex、Qwen 三 annotator 投票，span≥2 时人工审核。

**关键实验**
在 UltraTool（2032 工具，1000 查询）和 Seal-Tools（4076 工具，700 查询）上对比 8 个通用 reranker。UltraTool 上 core+graph 取得 NDCG@5 0.562，比最强 baseline Qwen2-1.5B 提升 11.3%，RVR@5 为 0.145；叠加规则过滤器后 RVR@5 降至 0.073，SRR@5 降至 0.019，但 NDCG@5 略降至 0.522。λ 从 0 到 0.2 可连续降低风险暴露，stress test 中规则过滤将 RVR@5 从 0.393 降至 0.111。

**最值得记住的一句话**
工具检索是 Agent 执行前的安全边界，用显式风险惩罚和可解释规则可以在保持相关性的同时大幅减少高风险工具暴露，且无需修改上游 retriever。
