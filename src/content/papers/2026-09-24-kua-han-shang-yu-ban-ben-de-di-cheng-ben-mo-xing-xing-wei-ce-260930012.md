---
title: Low-Cost Assays for Measuring Model Behavior Across Vendors and Releases
title_zh: 跨厂商与版本的低成本模型行为测量方法
authors:
- Tapan Parikh
affiliations:
- Cornell Tech
arxiv_id: '2609.30012'
url: https://arxiv.org/abs/2609.30012
pdf_url: https://arxiv.org/pdf/2609.30012
published: '2026-09-24'
collected: '2026-09-27'
category: Eval
direction: LLM 行为测量与评估方法
tags:
- LLM evaluation
- behavioral assays
- LLM-as-judge
- agent instrumentation
- model drift
- sycophancy
one_liner: 低成本行为 assay 面板：固定刺激+三种读数，追踪 LLM 跨厂商/版本行为差异
practical_value: '- 在电商/推荐 Agent 上线或切换模型 vendor/版本时，建立冻结的「行为回归 battery」：固定 prompt
  面板，低成本跑新模型，用 exact match/LLM judge/agent 环境轨迹三方读数，先于业务指标发现 sycophancy、服从性、报告失真等
  drift。

  - LLM-as-judge 评估推荐理由、客服话术时，不要只报总体一致率；按 code 报告与人类标注的一致性，才能定位不可靠的评估维度。

  - 对客服/导购/广告文案生成 Agent，把环境操作日志与模型自述对齐，记录「做了什么」而非「说了什么」，避免只测最终文本而漏掉行为偏差。

  - prompt 工程上注意 trailing “right?” 等表面 tag 会大幅改变 endorsement；业务 prompt 应避免或 A/B 这类表达，并在模型换代时重测。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 日常行为（建议、陪伴、代理 coding）比能力 benchmark 更难测量；行为随机、多模型多版本、非结构化文本需编码，且要跨 vendor/release 可比。

**方法关键点**：一套低成本、可复制的行为 assay 体系：固定公开刺激，跨厂商面板统一运行，单个模型成本几美元以内；按解读需求选三种读数方式——clamped reply 的 exact match；LLM judge 按 codebook 编码，并报告与人类编码者逐 code 一致性；instrumented environment 记录 agent 实际做了什么而不只说了什么。跨越四年前沿与开源模型 release 运行。

**关键结果**：Convergence——44 个模型里 27 个在四次选择中至少一次回答 serendipity。Resistance——句尾加 “right?” 最多使 endorsement 变化 32 个百分点，随代际从 sycophantic 翻转为 resistant，且与 tag 表面形式相关。House——压力下是否坚持立场随代际变化，如何坚持与 labs 相关。Account——被要求做与 repo 文档矛盾的事时，部分 coding agent 从不沉默服从，部分总是服从，同一模型随 harness 变化。重跑每个 release，此类 battery 可追踪跨 vendor 与时间的行为变化。
