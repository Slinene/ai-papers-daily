---
title: 'RATED: Reliability-Aware AI Agent Tool Retrieval via Execution Dynamics'
title_zh: RATED：基于执行动态的可靠性感知 AI Agent 工具检索
authors:
- Weiliang Chen
- Song Liao
affiliations:
- Texas Tech University
arxiv_id: '2610.13889'
url: https://arxiv.org/abs/2610.13889
pdf_url: https://arxiv.org/pdf/2610.13889
published: '2026-10-09'
collected: '2026-10-12'
category: Agent
direction: Agent 工具检索 · 在线可靠性适应
tags:
- Tool Retrieval
- Contextual Bandit
- Contrastive Learning
- Reliability-Aware
- Execution Feedback
one_liner: 融合对比微调双塔检索与 discounted LinUCB 在线重排，将工具故障选择率从 86% 降至 3%
practical_value: '- **解耦语义与可靠性**：用冻结的语义检索器（DRAGON）产出 top-K 候选，再做轻量在线重排，避免每次工具故障都重训大模型；电商
  Agent 中大量 API/下游服务频繁上下线，这种架构能快速响应。

  - **discounted LinUCB per tool**：为每个工具维护独立线性模型，用折扣因子 γ=0.95 下权旧反馈，快速适应工具失效；协方差矩阵保持对角，更新和推理都是
  O(d)，单步开销 <0.2ms，适合高并发在线服务。

  - **冷启动先验**：从工具目录元数据（名称-描述一致性、来源可信度、文档质量）自动计算静态可靠性分数，初始化 bandit bias，新工具上线无历史数据也能合理排序；电商工具库也可用类似信号（如
  API 文档完整度、供应商信誉）做初始质量分。

  - **融合权重默认值**：语义 0.75、bandit 0.15、静态先验 0.10 在 20% 故障率下效果最佳，可直接作为业务调参起点。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
AI Agent 依赖外部工具执行真实动作，但真实工具生态高度不可靠：作者爬取 LangChain、CrewAI 等平台发现超过 50% 的工具存在坏链、缺认证等问题。传统方法（ToolLLM、ToolRL 等）只优化语义相关性或批量更新策略，无法在运行时动态躲避故障工具，导致 Agent 频繁选择不可用的 API，严重影响可靠性。

## 方法关键点
- **EcoAgent 基准**：聚合 5,172 个真实工具，构建 **EcoAgent-Syn**（69,501 条合成 query-tool 对，用 Gemma-3-1b 生成并过滤）和 **EcoAgent-Real**（6,379 条真实查询，9,946 个经人工抽检的 query-tool 对），同时为每个工具自动计算 0-1 的元数据可靠性分数。
- **语义感知模块**：基于 DRAGON 双塔编码器，在 EcoAgent-Syn 上用 InfoNCE 对比损失微调，部署时冻结；新工具只需编码文档即可加入，无需重训。
- **可靠性重排**：每个工具维护一个独立的 **discounted LinUCB** 模型，以查询 embedding 为上下文，结合静态先验（名称-描述一致性、来源权重、文档质量）和 bandit 置信上界，线性融合最终分数。更新时对协方差矩阵采用对角近似，保持 O(d) 计算。
- **融合公式**：S_final = 0.75·S_sem + 0.15·S_bandit + 0.10·r_static，权重在验证集上选定。

## 关键实验
- 在 EcoAgent-Real 上，**RATED (Full) 的 MRR 为 0.618**，比 ToolLLM API retriever 的 0.406 提升 52.2%，但低于 OpenAI Ada-002（0.670）和 SPLADE-v3（0.626），说明静态检索精度高不等于故障场景可靠。
- 动态故障注入（20%/30% 失败率）：RATED (Full) 的 **故障选择率 FSR 分别降至 2.5% 和 2.9%**，而 ToolLLM 为 79.6% 和 86.2%；适应步数 AS 在 20% 失败率下为 1603，30% 时为 0。
- 延迟开销：RATED (Full) 平均 3.395ms，仅比纯编码多 0.172ms，远低于 ToolRL-like batch GRPO 的 17.839ms。

## 最值得记住的一句话
把执行反馈作为一阶信号，用轻量在线 bandit 重排冻结语义检索结果，是在不重训模型的前提下大幅降低工具故障选择率的实用路径。
