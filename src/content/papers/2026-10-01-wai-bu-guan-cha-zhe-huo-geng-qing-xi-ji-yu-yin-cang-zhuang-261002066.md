---
title: 'External Observers May See More Clearly: Cross-Model Span-Level Hallucination
  Detection in Large Language Models via Hidden State Probing'
title_zh: 外部观察者或更清晰：基于隐藏状态探测的大模型跨模型跨度级幻觉检测
authors:
- Kingshuk Gupta
- Davide Buscaldi
affiliations:
- LIX, École Polytechnique
- LIPN, Sorbonne Paris Nord
- School of Electrical and Electronic Engineering, Nanyang Technological University
arxiv_id: '2610.02066'
url: https://arxiv.org/abs/2610.02066
pdf_url: https://arxiv.org/pdf/2610.02066
published: '2026-10-01'
collected: '2026-10-04'
category: LLM
direction: LLM 幻觉检测 · 隐藏状态探测
tags:
- Hallucination Detection
- Hidden State Probing
- Cross-Model
- Span-Level
- Internal Representations
- LLM
one_liner: 提出用隐藏状态探针定位幻觉起始与延续 token，并发现外部小模型观察者可匹敌生成模型自检测
practical_value: '- 在生成式推荐或 Agent 链路中，可用隐藏状态探针做**幻觉 onset 实时检测**：不必等整段生成完成，发现 onset
  token 就触发回退、改写或检索，用于商品描述、广告文案等高价值生成场景。

  - **跨模型监控**架构值得借鉴：用一个小模型作为外部观察者读取大模型生成时的 hidden states，成本低且可独立部署，适合做大模型生成内容的在线质量守门。

  - 相比 RAG 外部检索，内部探针没有额外网络延迟，适合隐私受限、需要本地推理的搜索/推荐场景；可把探针作为轻量插件挂在 Transformer 特定层输出上。

  - 训练检测头时建议从 token 级升级到 span 级标注，业务上更对应“哪一句开始跑偏”，便于精确定位和修复；可构造自己的 span 标签（如商品属性不一致片段）来训练。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

动机：LLM 越来越多作为推理引擎使用，幻觉仍是关键风险。现有内部状态探针虽比外部 RAG 检索快，但大多把幻觉检测简化成 token 级二分类，无法捕捉语义漂移的结构化边界；外部检索又带来高延迟，不适合本地隐私部署。

方法：提出基于内部隐藏状态的细粒度 span 级幻觉检测框架，逐层检查激活模式，定位生成中幻觉的起始 token 和延续 token。进一步提出跨模型检测框架：用一个模型观察另一个模型生成时产生的内部表示，判断后者是否开始幻觉。

结果：实验显示方法能有效分离幻觉 onset，在极端类别不平衡下仍比随机基线取得显著 PR-AUC 提升；外部观察者可以匹配甚至超过生成模型对自身幻觉 onset 的检测能力，即使观察者模型更小，说明自检测并非 onset 定位的上限。
