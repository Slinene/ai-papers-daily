---
title: 'Selection Is Retrieval, Abstention Is Not: On-Device Tool Routing over 70
  Korean-English Actions'
title_zh: 选择是检索，拒绝不是：70个韩英动作的设备端工具路由
authors:
- Janghoon Lee
affiliations:
- Redrob
arxiv_id: '2609.18672'
url: https://arxiv.org/abs/2609.18672
pdf_url: https://arxiv.org/pdf/2609.18672
published: '2026-09-16'
collected: '2026-09-17'
category: Agent
direction: 设备端工具路由 · 检索与拒绝分离
tags:
- tool routing
- on-device
- retrieval
- abstention
- BM25
- multilingual-e5
one_liner: 拆分工具路由中的“选择”与“拒绝”决策，证明选择可用检索器、拒绝需神经编码器，设备端可省去大模型
practical_value: '- 在设备端或低延迟 Agent 场景，把工具选择与“是否拒绝/委托”拆成两阶段：先用轻量检索器（如字符 3-gram BM25）选出候选动作，再用一个冻结编码器（如
  multilingual-e5）做 out-of-catalog 判断，避免让大模型同时做两件事带来的延迟和内存开销。

  - 如果业务中有“本地动作目录”或固定工具的 Agent 路由，可先基于 lexical overlap 做召回：对于规范表达或关键词命中的请求，BM25 几乎全对；转述/同义表达则丢得较多，可限制候选集到
  top-7 再做重排或接一个小型语义判别器，性价比高于直接用大模型。

  - 对“是否该本地处理还是委托给远端/大模型”的决策，不要依赖分类器在检索得分特征上做阈值：论文表明这样做 AUC 上限仅 0.697，而冻结编码器的语义得分可达
  0.806。建议直接复用轻量 sentence encoder，成本低且能显著减少误委托。

  - 工程落地时注意：neural ranker 虽然所有质量指标更好，但常因延迟和内存被拒。若需在端上引入语义模型，优先考虑量化、蒸馏或小模型，并只用于 abstention
  阶段，而非全量排序。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：设备端 AI 助手做工具调用时，通常由一个语言模型同时决定“调用哪个工具”和“是否没有适用工具”。模型主导了延迟和内存，成本高。常见替代是用检索器对本地动作目录排序，但检索器总会返回最高分候选，无法表达“目录中没有有效动作”。此前工作只约束输出语法，未改善选择质量。两个决策的代价未被分别测量。

**方法关键点**：将工具路由拆成 selection（从 70 个本地动作中选一个）和 abstention（判断是否该本地处理、询问缺失槽位、回复或委托）。构造 600 个韩英请求，半数复用目录词汇、半数转述，区分词汇重叠与实际意图。用字符 3-gram BM25 做选择，用冻结 multilingual-e5-base 编码器做拒绝判断，并对比基于检索得分特征的分类器与神经排序器。

**关键结果**：BM25 在 164 个词汇匹配请求中选对 162 个（98.8%），但在 166 个转述请求中仅对 85 个；将候选集限制到 7 后，转述准确率提升至均值 0.825。基于得分特征的分类器区分 in/out-of-catalog 的 AUC 最高仅 0.697，冻结编码器达 0.806。仅用编码器做 abstention，376/450 本地请求被正确保留，150 个需委托请求中仅误路由 9 个。结论：选择可由检索器承担，拒绝必须引入神经组件；神经排序器精度全面更优，但因延迟和内存被工程化拒绝。
