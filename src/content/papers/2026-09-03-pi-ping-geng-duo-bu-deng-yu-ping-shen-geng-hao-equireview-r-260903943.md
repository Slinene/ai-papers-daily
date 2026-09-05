---
title: 'More Criticism Does Not Make a Better Review: EquiReview-R'
title_zh: 批评更多不等于评审更好：EquiReview-R
authors:
- Zexing Zhang
- Jichao Li
- Tianyang Lei
- Yude Fu
- Yang Kewei
affiliations:
- College of Systems Engineering, National University of Defense Technology
arxiv_id: '2609.03943'
url: https://arxiv.org/abs/2609.03943
pdf_url: https://arxiv.org/pdf/2609.03943
published: '2026-09-03'
collected: '2026-09-05'
category: Eval
direction: AI 辅助评审 · 证据引导精炼
tags:
- AI-assisted peer review
- evidence-guided refinement
- overcritique
- omission
- selective risk control
one_liner: 将 AI 审稿建模为证据引导的结构化问题集精炼，分离遗漏与过度批评，显著降低过度批评并控制遗漏风险
practical_value: '- 将生成式任务（如推荐理由、商品亮点总结、搜索 query 推荐）重构为「结构化 concern set 精炼」：先校验已有候选点是否有证据支撑（降低
  overcritique/幻觉），再从独立视角补充缺失点（降低遗漏），最后输出 stop/continue/defer 决定是否继续推理或转人工。

  - 证据定位与 provenance：为每个 claim 绑定具体文档片段或用户行为证据，无法定位的候选点直接标记为不充分，可复用到 RAG 式推荐文案生成，减少无依据描述。

  - 设置 stop/defer 机制：用 selective risk control 对 omission/overcritique 分别设定容忍上限，达到阈值即停止迭代或转人工审核，避免
  Agent 过度调用 LLM 增加成本。

  - 评估指标分离：不要只看 overall score，把「漏了重要点」和「说了没证据的话」分开度量，这在评估推荐理由、客服回答、商品描述质量时更利于定位问题。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：AI 审稿虽能生成大量具体批评，但“更多批评”不等于更好。常见两类对立失败：遗漏重要弱点（omission）与保留证据不支持的指控（overcritique）。现有生成导向系统和聚合指标无法区分二者，导致优化方向含混。

方法关键点：将 AI 辅助评审重构为证据引导的结构化 concern set 精炼。EquiReview-R 先对现有 concern 做局部证据校验与解决（revision），再从独立视角和 review-conditioned 视角搜索缺失问题（search），最后给出 stop/continue/defer 决策。构建 evidence-linked 轨迹语料 ReviewTrace，回顾分析显示高召回 review 中几乎所有 concern 缺乏决定性证据，必须先 revision 再 search。

关键结果：在未见论文冻结队列上，major omission 满足预设非劣效标准；major overcritique 从 15.5% 降至 8.1%；omission 单侧上界 9.9%，52.4% 论文可停止。计算匹配对照、控制配对和消融表明收益来自 revision 而非额外推理或更短输出。
