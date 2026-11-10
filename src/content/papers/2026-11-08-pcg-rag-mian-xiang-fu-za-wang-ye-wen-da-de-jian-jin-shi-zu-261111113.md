---
title: 'PCG-RAG: Progressive Compositional Grounding for Retrieval-Augmented Generation
  in Complex Web Question Answering'
title_zh: PCG-RAG：面向复杂网页问答的渐进式组合证据定位 RAG 框架
authors:
- Linyao Zheng
- Xuhang Shi
- Zhifang Mao
- Chongqi Qu
- Xiuquan Hou
affiliations:
- Xi'an Jiaotong University
- Beijing University of Posts and Telecommunications
arxiv_id: '2611.11113'
url: https://arxiv.org/abs/2611.11113
pdf_url: https://arxiv.org/pdf/2611.11113
published: '2026-11-08'
collected: '2026-11-10'
category: RAG
direction: RAG · 渐进式组合证据定位
tags:
- RAG
- Complex Web QA
- Progressive Grounding
- Compositional Reasoning
- Evidence Acquisition
- Multi-hop Retrieval
one_liner: 提出 PCG-RAG，用子问题 DAG 与渐进证据获取分离候选引导检索和证据回答，在复杂网页 QA 上准确率提升超 5 个百分点
practical_value: '- 把复杂用户查询拆成子问题 DAG，先验证实体识别条件再推进检索，避免“部分证据过早锁定错误候选”。电商导购中可对应多约束商品查询（如“送母亲、无糖、适合高血压的保健品”），单靠一个属性匹配就锁定商品会跑偏。

  - 明确区分 candidate-guided retrieval 与 evidence-based answering：候选实体只用于引导下一步搜索，最终答案必须基于所有原始条件做证据核查。可借鉴到
  Agent 回复前增加“条件满足性校验”步骤，降低幻觉和错误实体绑定。

  - 渐进证据获取按“缺失属性/关系”定向搜索，每次迭代只补当前缺的证据，减少检索噪声。适合电商商品属性补全、多源商品信息聚合，或搜索系统用弱线索逐步收敛候选集。

  - 最终生成时把识别证据与关系证据分离并保留来源，提升可解释性；客服/导购 Agent 可输出“哪条证据支持哪个条件”，方便用户确认和调试。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：复杂网页问答需要从多线索描述中识别目标实体，并连接散落在长网页中的证据。单页通常只满足部分语义约束，一个页面发现的线索要引导后续搜索，但过早依赖部分证据可能让检索偏离原始信息需求。

**方法关键点**：PCG-RAG 基于渐进式组合证据定位（Progressive Compositional Grounding）。Progressive Evidence Acquisition 定向搜索候选属性或关系缺失的证据；Compositional Reasoning 沿子问题 DAG 把“候选引导检索”和“基于证据的回答”解耦，临时命名让依赖搜索更具体，回答阶段用原始问题评估已接受结果和未解决识别条件；新段落连接识别线索与请求关系；Evidence Grounding 把识别证据、关系证据与中间答案结合，在最终生成时跨页面关联到原始条件。

**结果**：在 BrowseComp-Plus 和 WebWalkerQA 上，PCG-RAG 比最强对比基线分别提升 5.43 和 5.15 个百分点的准确率。
