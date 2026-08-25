---
title: 'The Laws of Context Allocation: Causal Measurement and Closed-Loop Orchestration
  in Generative Search'
title_zh: 上下文分配定律：生成式搜索中的因果测量与闭环编排
authors:
- Peiyang Liu
- Xi Wang
- Di Liang
- Wei Ye
affiliations:
- Peking University
- National Engineering Research Center for Software Engineering, Peking University
- Tencent
arxiv_id: '2608.23252'
url: https://arxiv.org/abs/2608.23252
pdf_url: https://arxiv.org/pdf/2608.23252
published: '2026-08-24'
collected: '2026-08-25'
category: RAG
direction: 生成式搜索 · 推理时上下文编排
tags:
- RAG
- Causal Attribution
- Inference-time Scaling
- Submodular Scheduling
- Contrastive Decoding
one_liner: 用因果探针揭示标准相关性代理在困难负样本上失效，并证明窄上下文多轮生成比宽上下文单轮带来16.8-20.5个百分点的组合召回增益
practical_value: '- 借鉴因果归因探针：在电商搜索/RAG 场景中，用 leave-one-out 对数似然下降度量生成结果对每个上下文文档的真实依赖，避免
  query-doc 相似度等代理指标在同查询稠密负样本上的失效。工程上可对已生成响应做并行 teacher-forced 前向，绕过解码瓶颈，适合在线监控证据利用率。

  - 推理预算分配策略：若有多轮生成场景（如生成多个搜索摘要或推荐理由），优先把相同证据槽位拆成多个窄上下文轮次，而不是一次性塞入宽上下文。实验显示相同 24 个文档预算下，k=2,T=12
  比 k=24,T=1 的 portfolio recall 高 0.144（0.397 vs 0.253），且提升在 7B-32B 模型上稳定。

  - 反馈驱动的子模调度：在每轮生成后用归因信号标记已消费的知识簇，下一轮通过贪心子模最大化选择未被充分利用的文档；比盲目轮换文档的 ECR 提升显著（0.626
  vs 0.375）。该模式可直接用于多轮对话推荐或多样性商品集合生成，避免内容冗余。

  - 对比解码增强新鲜证据整合：在生成阶段用公式 ℓ'' = ℓ(·|q,C) + α[ℓ(·|q,C\O) - ℓ(·|q,O)] 减去过度使用证据的概率质量，推动模型利用新文档，同时加
  plausibility 约束防止幻觉。此 trick 可用于电商推荐理由生成中强制覆盖不同卖点。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
RAG系统在模糊查询下从单一响应转向多样组合生成，面临两个瓶颈：证据利用测量不准和上下文预算分配低效。标准相关性代理（如 BM25、embedding 相似度）在相似度上看似完美，但无法区分真正被生成利用的证据与仅主题相关的文档，特别是在同查询困难负样本上完全失效。需要因果测量工具和优化分配策略。

## 方法关键点
- **因果 leave-one-out 探针**：通过删除文档后生成文本对数似然的下降度量真实依赖，依靠固定响应和 teacher-forced 前向实现高效测量（无需重复解码）。
- **诊断幻觉揭露**：在 off-query 负样本上代理指标 AUC 接近 1.0，但在 same-query hard negatives 上崩塌至随机；只有因果探针保持鲁棒（AUC 0.824-0.876）。
- **宽度稀释定律**：校准后上下文宽度弹性为 -0.68（SE 0.02），证明宽上下文注意力稀释是固有生成行为，非硬件截断。
- **闭环子模调度器（Ascp）**：每轮生成后用归因信号聚类知识面，以单调子模目标贪心选择下一轮文档，动态削减已消费簇。
- **归因引导对比解码**：在解码中减去过度使用证据的概率质量（公式 ℓ' = ℓ(·|q,C) + α[ℓ(·|q,C\O) - ℓ(·|q,O)]），强制整合新鲜证据，并用 plausibility 约束避免幻觉。

## 关键实验
在 ASQA、QAMPARI、ELI5 和跨文化食谱适应四个基准上，冻结检索池（N=30 或 N=400），使用 Qwen2.5-7B/14B/32B、Llama-3.1-8B、Mistral-7B 等模型。对比 vanilla RAG、MMR、xQuAD、PM-2、DPP-RAG、Carriage 等 7 个 baseline。关键数字：
- 相同 k×T=24 证据槽预算下，旋转式窄上下文（k=2,T=12）相比宽上下文（k=24,T=1）portfolio recall 从 0.253 提升到 0.397（+0.144）。
- 全网格中旋转对比固定上下文增益 +0.073 到 +0.140（全部 p<0.01）。
- Ascp 调度器 ECR 达到 0.626，远超 deep rotation 的 0.375；在 frozen held-out 上比所有 baseline 的 portfolio recall 高 0.033-0.081。
- 宽度弹性 -0.68，在 7B-32B 模型上一致。

**最值得记住的一句话**：在固定证据预算下，把上下文拆成多个窄窗口并依据因果反馈迭代调度，比一次性宽上下文更有效；标准相似度指标在稠密相关负样本上不可信，必须用因果探针度量真实证据利用。
