---
title: 'One Framework to Diagnose Them All: A Stratified Benchmark for Bengali LLM
  Hallucination'
title_zh: 面向孟加拉语 LLM 幻觉的分层诊断基准
authors:
- Asif Shahriyar Sushmit
- Shefayat E Shams Adib
- Abdullah Al Jubaer Gem
- Ahmed Shafin Ruhan
- MD. Nazmuddoha Ansary
- Biplab Kumar Sarkar
- Syed Rifat Raiyan
- Ajwad Abrar
- Abdullah Bin Hasan
- Adib Sakhawat
affiliations:
- Islamic University of Technology
- Bengali.AI
- North Dakota State University
- Bangladesh University of Engineering and Technology
- BRAC University
arxiv_id: '2611.26336'
url: https://arxiv.org/abs/2611.26336
pdf_url: https://arxiv.org/pdf/2611.26336
published: '2026-11-19'
collected: '2026-11-22'
category: Eval
direction: LLM 幻觉评估 · 分层诊断基准
tags:
- hallucination detection
- stratified benchmark
- LLM-as-judge
- calibration
- low-resource NLP
one_liner: 构建按文化距离、任务类型与32种幻觉模式分层的孟加拉语幻觉基准，发现LLM判别器跨层F1差超30且过度自信
practical_value: '- 把「分层切片评估」用于 LLM 生成商品文案、推荐理由、客服回答：按文化距离、任务类型、幻觉模式切分测试集，报告切片 macro-F1，而不只看整体指标，能暴露「流畅但漏掉关键属性」的失败模式。

  - LLM-as-judge 用于线上幻觉拦截时，应输出概率并校准：文中判别器 ROC-AUC 0.74–0.95 但 ECE 高；工程上可加温度缩放或 conformal
  prediction，并用 negative controls 测误杀率，避免过度拦截正常内容。

  - 公共榜单/单阶段 holdout 不可靠：Phase1 排名与 Phase2 排名 Spearman ρ=0.35，24/25 队回退；内部选型需要多阶段金标或时间外样本，并关注
  slice 级排名稳定性，防止过拟合开发集。

  - 话语级遗漏（omission）对 judge 和团队都难：对推荐解释、搜索摘要、广告文案，建议引入结构化 grounding/RAG 与逐属性 checklist，显式检测‘应提未提’，不能只依赖端到端
  LLM judge。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：低资源语言幻觉研究碎片化，每个失败模式各建数据集，标注资源不可比；目标是用一个基准统一诊断。

方法：Alikbachan 是按三个交叉轴分层的孟加拉语幻觉检测基准：人工校验的文化距离带、6 种任务类型、5 族 32 模式幻觉分类。数据包含 Phase 1 采集的 2,516 条测试集与 Phase 2 配额构建的 5,000 条金标集。

关键结果：4 个零样本 LLM 判别器在不同分层上 macro-F1 相差超 30 点；99 个 Phase1 与 32 个 Phase2 参赛系统的逐项预测复现同一画像——话语级遗漏挫败判别器和多数队伍，仅少数系统误杀负对照。判别器预测概率排序能力好（ROC-AUC 0.74–0.95），但过度自信（ECE 0.04–0.29）。竞赛吸引 222 队、3,566 次提交，单 prompt 32B 判别器达第 57 百分位。两阶段都参加的 25 队中 24 队 Phase2 平均下降 17.6 分，而所有零样本判别器都提升；Phase1 排名与 Phase2 排名仅 Spearman ρ=0.35，单一阶段榜单会选出不同冠军。
