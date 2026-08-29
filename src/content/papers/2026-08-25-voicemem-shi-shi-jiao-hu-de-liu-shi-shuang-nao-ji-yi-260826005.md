---
title: 'VoiceMem: Streaming Dual-Brain Memory for Real-Time Interaction'
title_zh: VoiceMem：实时交互的流式双脑记忆
authors:
- Zhifei Xie
- Jiaqi Lang
- Ze An
- Yifan Zhao
- Dongchao Yang
- Kai Li
- Ziyang Ma
- Mingbao Lin
- Chunyan Miao
- Shuicheng Yan
affiliations:
- Nanyang Technological University
- National University of Singapore
- Tsinghua University
- The Chinese University of Hong Kong
- Open Interaction Lab
arxiv_id: '2608.26005'
url: https://arxiv.org/abs/2608.26005
pdf_url: https://arxiv.org/pdf/2608.26005
published: '2026-08-25'
collected: '2026-08-29'
category: RAG
direction: 实时语音 Agent 记忆 · 流式 RAG
tags:
- Voice Memory
- Streaming RAG
- Dual-Brain Memory
- Persona Modeling
- Affective Attribution
- Speech Agent
one_liner: 双脑流式记忆：左脑管信息、右脑管情感人格，top-5 检索 134ms 达到实时语音交互记忆 SOTA
practical_value: '- 用 schema-entity 两层索引替代扁平向量召回：先把候选池按实体/类目路由到小集合，再做 top-5/10 精排；适合电商导购/会话推荐里把用户长期行为、商品类目、偏好实体做成可寻址索引，低
  token 预算下保持高准确率。

  - 借鉴“让候选池更密而不是把 K 调大”的结论：通过 query 共现和 LLM judge 自动让兴趣簇/商品簇跨预设类目重组，可迁移到用户兴趣聚类、促销主题挖掘、Semantic
  ID 层级构建。

  - 把事实行为与情感/偏好分开建模：独立节点记录长期偏好，跨实体节点记录对具体商品/事件的态度，避免把一次情境反应误判为长期兴趣；适合个性化推荐理由、卖点文案和售后
  Agent 的情绪感知。

  - 上层图路由与底层向量/记忆引擎解耦，四阶段流式检索拆分到固定静音/请求窗口内；在电商语音助手或实时推荐 Agent 中可异步执行召回/粗排/精排，保证延迟不随
  K 线性增长。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：实时语音 agent（duplex SLM）与长期记忆系统尚未打通：文本记忆常用 top-100 召回和 2-3 秒检索，超出语音对话 500ms 与 token 预算；同时情感/人格与事实信息需要不同建模方式，不能只做语义相似度。

方法关键点：
- 双脑并行：左脑用 schema–entity 二级索引组织事实，实体归属 schema、一跳邻域扩展候选；右脑维护独立人格节点与跨实体情感节点，做短/长程情感归因。
- 流式四阶段检索：在用户说话期间持续 ASR/实体/情感/说话人识别，200-400ms 静音窗口做图扩展和 embedding，最后仅后端搜索；检索 134ms，不增加额外延迟。
- 集群涌现：对反复共同检索的实体子图计算 query coherence ρ(H)，通过 LLM judge 提升为新 schema，跨预设类目重组。
- 解耦部署：上层 graph-on-graph 路由 + 底层可替换 MemSearch，当前用 Mem0；训练走 black-box OPD 蒸馏，产出 ChatMem-400K 与 ChatMem-Bench。

关键结果：
- 文本信息记忆平均 76.39，比 Mem0 高 +24.12，比 full-context 高 +15.90；LoCoMo 上 K=5 拿到 91.2，仅 430 memory tokens、134ms，比 EverMemOS 高 8.1 且 token 少 4.4×。
- 人格记忆平均 74.16/76.56，比最强 MemOS 高 +1.89。
- 长音频 ChatMem-Bench：316 题/53 小时音频，平均 68.73，领先 MemOS 14.78；声学环境类无文本证据时优势最明显。
- 消融：去掉上层索引损失最大（-9.9/-5.3/-6.7/-4.4）；schema 路由不提高上限但降低达到高准确率所需的 K；同一上层索引迁移 Mem0/LangMem/Zep 分别 +29.5/+15.8/+22.9。

最值得记住的一句话：在实时对话里，与其扩大 top-K，不如把候选池做密；候选池的语义结构决定小预算下的召回质量。
