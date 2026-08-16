---
title: 'Knowledge Synthesis Review Framework: Task-Level Benchmarking of LLM-Based
  Systems for Multi-Source Evidence Synthesis'
title_zh: 知识综合评审框架：多源证据综合LLM系统的任务级基准测试
authors:
- Wafa Shafqat
- Mark Patterson
- Steven N. Liss
affiliations:
- Toronto Metropolitan University
- Queen's University
- Stellenbosch University
arxiv_id: '2608.12741'
url: https://arxiv.org/abs/2608.12741
pdf_url: https://arxiv.org/pdf/2608.12741
published: '2026-08-13'
collected: '2026-08-16'
category: Eval
direction: LLM证据综合任务级评测与路由
tags:
- LLM benchmark
- evidence synthesis
- human-in-the-loop
- task routing
- multi-source synthesis
one_liner: 提出KSR人机协同框架，将证据综合拆解为筛选、抽取、分析、综合四任务并基准测评与路由，无单一系统全任务领先
practical_value: '- 将复杂智能流程拆解为可独立评测的子任务（筛选/抽取/分析/综合），再按任务挑选最优模型或系统路由，可迁移到电商平台的商品评论分析、竞品报告生成、广告素材合规筛查等多源文档处理场景。

  - 建立人工标注金标并报告 inter-rater reliability（如 Kappa=0.80）作为 LLM 效果上限参考，同时做数据污染检查，可避免模型评测被训练集泄漏或过度拟合金标误导。

  - 多源异构信息（电商评论、社媒、政策、行业报告）的综合分析中，采用任务路由而非单一模型端到端生成，能暴露单源视角的盲点，例如论文发现 worker well-being、small
  firms、Global South 等跨源不对称问题，对市场洞察和风险识别有参考价值。

  - 在业务中构建 LLM 驱动的知识管理或研究助手时，可借鉴其 human-in-the-loop 治理思路：将专家验证嵌入每个任务节点，保持流程透明可审计，降低模型在推理分析类任务上的不可控输出风险。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：快速演变领域的证据分散在学术论文、行业报告、政策文件和媒体等异构多源文档中，LLM 有望加速综合，但其在不同认知任务上的可靠性未知。

方法关键点：提出 Knowledge Synthesis Review (KSR) 框架，将证据综合显式分解为 screening、extraction、analysis、synthesis 四个任务；在 244 篇文档基准集（采样自 1,893 篇 AI 与工作主题语料，覆盖四类来源）上评测 GPT-5、Claude Sonnet 4、Gemini 2.5 Pro、NotebookLM，对照高一致性的专家金标（一致率 92.2%，Kappa=0.80），并按任务将工作流路由到最佳系统，持续接受专家验证。

关键结果：无单一系统在所有任务上领先。Claude Sonnet 4 获得最高筛选准确率 82.8%，GPT-5 获得最高召回 91.8% 但特异性较低。抽取任务对标题和来源的准确率超过 90%，但在作者和参考文献字段明显退化。在解释性分析和跨源综合任务上性能下降最严重，专家判断仍不可或缺。污染检查未发现训练截止后文档的评分虚高，排除了数据泄漏影响。应用到全文库时，路由工作流揭示了单源综合会遗漏的跨源不对称和盲点，如 worker well-being、small firms 和 Global South。KSR 提供透明、可审计且模型无关的框架，用于治理 LLM 辅助科研综合并保留人类责任。
