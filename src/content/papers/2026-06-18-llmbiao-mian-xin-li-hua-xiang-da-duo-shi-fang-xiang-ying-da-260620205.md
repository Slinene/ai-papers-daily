---
title: Apparent Psychological Profiles of Large Language Models are Largely a Measurement
  Artifact
title_zh: LLM表面心理画像大多是方向应答偏差的假象
authors:
- Jelena Meyer
- David Garcia
- Dirk U. Wulff
affiliations:
- Max Planck Institute for Human Development
- University of Konstanz
- Barcelona Supercomputing Center
- University of Basel
arxiv_id: '2606.20205'
url: https://arxiv.org/abs/2606.20205
pdf_url: https://arxiv.org/pdf/2606.20205
published: '2026-06-18'
collected: '2026-06-22'
category: Eval
direction: LLM评估方法论批判
tags:
- response bias
- psychometrics
- LLM evaluation
- personality assessment
- measurement artifact
one_liner: 量化证明LLM心理测评差异81-90%由方向应答偏差驱动，而非真实心理特质
practical_value: '- 在将LLM作为用户模拟器或评估其“类人”特质时，避免直接套用人类心理量表，因为模型响应主要由方向性偏差（总是偏向某极或某标签）驱动，不反映真实倾向。

  - 设计推荐理由生成、用户意图理解等任务时，需通过正交化项目设计或指令校准控制LLM的应答偏差，否则可能得到系统性偏向的推荐结果。

  - 评估LLM驱动的Agent时，不应将量表得分直接解释为稳定人格，应考虑测量工具本身的偏差结构，否则会误判Agent行为风格。

  - 若利用LLM生成多样化的用户画像或偏好标签，可借鉴“响应正交性”概念，构建平衡偏差与目标维度的题目池，提高标签有效性。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：越来越多研究直接使用人类心理量表为LLM赋予稳定心理画像，用于可用性、安全评估或人类代理，但这些画像是否真实反映模型特性存疑。

方法：对56个指令微调LLM施测一套人格和风险偏好量表（包含自陈式问卷与行为任务），并与大规模人类样本对比。利用方差分解区分特质与方向性应答偏差（模型倾向于选择量表某一端或某一标签，与题目内容无关）的贡献，并新定义“响应正交性”——题目中目标特质方向与偏差方向相反的比例。

关键结果：
1. 模型间变异81-90%由方向偏差解释，而人类仅9-16%，说明LLM的回答主要受偏差驱动而非真实心理特质。
2. 偏差随模型能力提升而降低，但未消失，即使是强模型仍保留显著偏差。
3. 量表的表面信度几乎完全由响应正交性预测：正交性越低，信度越高，因为偏差放大了内部一致性。
4. 通过选择性删除题目，可以制造出任何期望的心理画像，画像完全取决于所选题目。

结论：LLM的表面心理画像是测量工具产生的假象，呼吁开发以响应正交性为核心的专用评估方法。
