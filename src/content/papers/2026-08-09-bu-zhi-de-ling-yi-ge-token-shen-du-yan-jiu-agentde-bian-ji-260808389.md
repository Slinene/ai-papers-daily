---
title: 'Not Worth Another Token: Marginal Value Estimation for Efficient Deep Research
  Agents'
title_zh: 不值的另一个Token：深度研究Agent的边际价值估计与高效剪枝
authors:
- Harshitha Kolukuluru
- Reshma Ashok
- Kirat Arora
- Evan William Ciccarelli
- Nischal Ashok Kumar
- Lunyiu Nie
- Franck Dernoncourt
- Samyadeep Basu
- Ryan A. Rossi
- Nedim Lipka
affiliations:
- University of Massachusetts Amherst
- University of Texas at Austin
- Adobe Research
arxiv_id: '2608.08389'
url: https://arxiv.org/abs/2608.08389
pdf_url: https://arxiv.org/pdf/2608.08389
published: '2026-08-09'
collected: '2026-08-11'
category: Agent
direction: Agent上下文管理 · 边际价值剪枝
tags:
- Marginal Value Pruning
- Deep Research Agent
- Stage-aware Pruning
- LLM Efficiency
- Heuristic Pruning
one_liner: 针对长程深度研究Agent，系统对比多阶段剪枝策略，发现剪枝位置比规则更关键，早期剪枝可减少73% token
practical_value: '- **多阶段剪枝理念可迁移至推荐Agent**：在生成式推荐或多步检索Agent中，可借鉴 Pre-Retrieval（过滤低价值子查询/召回请求）、Post-Retrieval（根据已收集上下文淘汰冗余召回结果）、Pre-Synthesis（最终排序前压缩上下文）的三阶段剪枝框架，在不显著损失质量的前提下大幅降低
  token 消耗与延迟。

  - **轻量启发式即可有效**：MMR（最大边际相关性）等简单规则在早期剪枝中性价比极高，无需额外的 LLM 调用或复杂学习，适合线上高吞吐场景，尤其在召回阶段过滤冗余物品或搜索词候选时可直接复用。

  - **剪枝位置远比具体公式重要**：实验表明 Post-Retrieval 剪枝能消除下游扩展成本，而 Pre-Synthesis 剪枝仅压缩最终输入，无法挽回上游开销；在电商
  Agent 流程中应优先在搜索/召回早期介入，而非只在排序前做上下文压缩。

  - **质量与证据保留需联合评估**：论文发现报告质量与引用召回率可能背离，压缩可能提升合成质量但丢失支撑证据；在广告文案生成或推荐理由合成时，应同时监控生成文本的支撑度和事实准确性，避免过度剪枝导致信息缺失。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
长程深度研究 Agent 通过多步检索、聚合与合成回答复杂问题，但累积上下文快速增长，新增信息的边际价值却逐渐下降，产生大量冗余 token，导致高成本、高延迟且最终报告噪声增多。现有方法多依赖 LLM 提示进行上下文管理，开销大且行为不一致，缺乏对流式剪枝阶段与策略的系统分析。

## 方法关键点
- **三阶段剪枝框架**：在 Pre-Retrieval（检索前滤除低价值子查询）、Post-Retrieval（检索后过滤冗余上下文以阻止分支膨胀）、Pre-Synthesis（最终合成前压缩上下文）三个位置进行边际价值评估，支持单阶段、两阶段和三阶段组合。
- **多种剪枝策略对比**：覆盖启发式（MMR、几何残差新颖性、质心漂移、DPP、次模覆盖）、词汇级（TF‑IDF + Bigram）、LLM 裁判及学习型控制器，在同一执行框架下公平比较。
- **边际价值定义统一为打分函数** V(x|C,Q)，高于阈值则保留，允许不同阶段侧重不同目标（相关性、新颖性、覆盖度）。

## 关键实验
- **数据集与基线**：使用 DeepResearchGym 基准中的 100 个复杂查询，基于 GPT‑Researcher 树的搜索流水线，无剪枝基线消耗 375.4k token、29.0 个节点、3422.6s。
- **核心结果**：
  - 单阶段 Post‑Retrieval 的 MMR 将 token 降至 114.6k（-69.5%），节点降至 8.84，质量仅微降（97.9% 基线水平）；Pre‑Synthesis Hybrid 获得最佳单阶段质量（60.68），但成本仅小幅下降。
  - 两阶段（Post‑Retrieval + Pre‑Synthesis）中 CD + SC 达到最高质量（59.47），同时减少 63.4% token；MMR 保持最强压缩（114.6k token）。
  - 三阶段 MMR 进一步将 token 降至 100.1k（-73.3%），节点 7.82，但质量略降至 55.90。
- **跨阶段发现**：剪枝阶段对效率影响远大于具体评分规则；早期剪枝（尤其 Post‑Retrieval）收益最大；两阶段提供最佳质量‑效率权衡；混合方法（如 CD+SC）在质量优先时更具竞争力；学习型控制器尚未显著超越最好启发式。

## 核心结论
剪枝位置比剪枝公式更重要：早期剪枝可大幅回收下游搜索成本，后期剪枝仅优化合成输入。没有单一方法在所有指标上均最佳，实际部署时应根据质量、效率、忠实度目标联合选择剪枝阶段与策略，轻量启发式已能满足多数工程需求。
