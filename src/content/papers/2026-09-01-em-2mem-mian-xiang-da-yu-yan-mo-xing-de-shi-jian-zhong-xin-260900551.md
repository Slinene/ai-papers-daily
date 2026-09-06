---
title: 'EM^2Mem: Event-Centric Multimodal Memory for Large Language Models'
title_zh: EM^2Mem：面向大语言模型的事件中心多模态记忆
authors:
- Yijun Chen
- Yaqi Zheng
- Yanya Li
- Boyi Xiao
- Buqiang Xu
- Shuofei Qiao
- Jizhan Fang
- Xinle Deng
- Yunzhi Yao
- Xuehai Wang
affiliations:
- Zhejiang University
- South China University of Technology
- Lenovo Group Limited
arxiv_id: '2609.00551'
url: https://arxiv.org/abs/2609.00551
pdf_url: https://arxiv.org/pdf/2609.00551
published: '2026-09-01'
collected: '2026-09-06'
category: RAG
direction: 多模态 RAG · 事件索引
tags:
- Multimodal Memory
- Event-Centric
- Long-Video QA
- RAG
- LLM
- Evidence Retrieval
one_liner: 以事件为中心组织多模态记忆，将异构证据绑定到事件锚点，提升长视频 QA 精度并大幅降低推理成本
practical_value: '- 直播/商品视频问答：按业务事件（商品讲解、优惠发放、试用对比）建立事件索引，把对应帧、ASR、OCR、商品卡片绑定到事件 cell；检索时直接返回完整事件单元，避免
  agent 在推理时拼接零散多模态片段，降低延迟与 token 开销（论文减少 63.66% tokens、4.67× 延迟）。

  - 召回/证据评测：引入 strict event-level Top-K evidence recall，评估检索结果是否覆盖关键事件而非只看最终答案准确率，可用于商品知识库、直播切片或广告素材检索的离线评测。

  - 用户行为记忆：将 session 内行为序列按事件（搜索、点击、加购、下单）聚合为 memory cell，绑定跨通道特征、时间与商品关系，为 LLM 推荐/导购
  Agent 提供紧凑、可溯源的上下文，减少推理时的对齐成本。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
长视频 QA 需要外部多模态记忆，但现有方法把 captions、frames、transcripts、summaries 或图事实当作孤立片段检索。虽然可搜索，但 LLM 在推理时仍需重建跨模态与时间对齐，上下文有限、归因困难，不是 generation-ready 的记忆。

### 方法关键点
EM^2Mem 在记忆构建阶段就把异构证据绑定到事件锚点，形成事件索引的 memory cell。每个 cell 对齐多模态记录、时间上下文、图链接关系、语义事实和 provenance，使证据读取以紧凑且可归因的事件单元进行，而非按模态拆散的片段。

### 关键结果
在三个长视频 QA 基准上，平均准确率比最强记忆基线提升 2.0、2.4、3.7 分；严格事件级 Top-5 证据召回提升 7.0 分；单查询延迟降低 4.67 倍，总推理 tokens 减少 63.66%。代码将集成到 LightMem。
