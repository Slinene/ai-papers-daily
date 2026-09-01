---
title: 'Hi-Q: Hierarchical Evidence-guided Query Refinement for Multi-Hop Question
  Answering'
title_zh: Hi-Q：面向多跳问答的层级证据引导查询细化
authors:
- Jueun Kim
- Sungho Park
- Wook-Shin Han
affiliations:
- POSTECH
arxiv_id: '2608.30468'
url: https://arxiv.org/abs/2608.30468
pdf_url: https://arxiv.org/pdf/2608.30468
published: '2026-08-31'
collected: '2026-09-01'
category: QueryRec
direction: 多跳问答的 query 粒度控制
tags:
- Multi-hop QA
- Query Refinement
- RAG
- Evidence-conditioned
- Hierarchical Decomposition
- Granularity Control
one_liner: 将query粒度作为控制变量，用检索证据支持信号决定是否分解，构建依赖有序的查询树，在全语料多跳QA上显著超过图RAG与迭代检索
practical_value: '- 在电商多跳 query（如“送妈妈生日礼物”）召回中，不要预先固定拆成 N 步；先让 reader 基于召回商品判断当前 query
  是否可由证据支持，不可答才触发分解。这种“证据条件触发”比按复杂度静态 Routing 更抗漂移，且无需训练分类器。

  - 分解时强制依赖顺序：左分支先解析前提实体/属性（品牌、品类、用户特征），把结果写入 history，再生成右分支 query；工程上用 append-only
  history 保证下游检索可见前置答案，降低召回干扰。

  - 增加一个语义覆盖 verifier：每次二元分解后检查左右子 query 是否完整保留父 query 意图，最多修复一次；在营销活动规则拆解、多条件商品匹配中可减少意图丢失。

  - 成本工程：采用短 rationale + 限制递归深度（dmax=1 或 2）的 cost-matched 版本，可在几乎同数量 LLM call 下比迭代检索更准且
  API 成本低近一个数量级；优先在 root 节点先试答，可避免大部分不必要展开。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：多跳问答中，自然语言 query 通常把多个推理步骤压缩成粗粒度句子，而证据语料中的可检索事实是细粒度；固定图结构、迭代改写、代码执行等方案未显式判断“当前 query 单元是否已被检索证据支持”。论文将其形式化为可检索粒度发现，提出 Hi-Q。

方法关键点：
- 每个查询节点先经过 resolution operator：改写 query → top-k 检索 → reader 基于证据尝试回答；若 resolved 则停止，否则进入分解。
- 停止/展开决策是成本敏感阈值；用 reader 输出 a=⊥ 作为无训练的 unresolved 信号，触发分解。
- 二元分解保持依赖顺序：左分支先解析桥接事实/前置实体，结果写入 history 后右分支再执行；语义覆盖 verifier 校验并修复拆分，防止意图丢失。
- 搜索树最大深度 dmax=4，保证有限递归成本。

关键实验：在 MuSiQue、HotpotQA、2WikiMultiHopQA 三个基准上，以全语料检索为主设置（139k–5.2M passages）。全语料平均 52.3 EM / 64.0 F1，比 IRCoT 高 15.1 EM / 18.2 F1，在 MuSiQue-full 上比 PropRAG 高 11.5 EM / 12.0 F1；控制池设置平均 57.9 EM / 69.3 F1，优于 PropRAG 5.6 EM / 3.9 F1、IRCoT 13.7 EM / 15.8 F1。成本匹配配置在相同 LLM call 下比 IRCoT 准确 +10.4 EM / +11.6 F1，API token 成本低 8.6 倍。触发诊断中，clean MuSiQue 的 gold 覆盖从 root@5 的 7.9% 提升到 leaf@5 的 42.7%，false trigger 率约 10%。

最值得记住的一句话：多跳检索应把 query 粒度当作控制变量，用检索证据支持信号决定何时分解、何时停止，而不是预先固定图结构或分解模板。
