---
title: 'RippleMem: From Isolated Retrieval to Associative Recollection for Long-Term
  Agent Memory'
title_zh: RippleMem：从孤立检索到联想式回忆的长期 Agent 记忆系统
authors:
- Jingbo Ji
- Lingyi Li
- Xilong Cheng
- Yuhao Zhou
- Wenji Zhang
- Yuting Tan
- Yunxiao Qin
affiliations:
- Communication University of China
- Zhilian Yinghe Technology Co., Ltd.
- State Key Laboratory of Media Convergence and Communication
arxiv_id: '2608.13334'
url: https://arxiv.org/abs/2608.13334
pdf_url: https://arxiv.org/pdf/2608.13334
published: '2026-08-13'
collected: '2026-08-14'
category: Agent
direction: 长期 Agent 记忆 · 联想式证据补全
tags:
- Agent Memory
- Associative Recollection
- Episodic Memory
- Graph Retrieval
- Long-Term Memory
- LLM Agents
one_liner: 把已召回记忆作为 cue，沿事件图局部扩展补全缺失证据，长期记忆 QA 精度显著提升
practical_value: '- 在客服/导购 Agent 中，用户偏好、约束常分散在多轮多 session：一次检索容易只召回直接相关记忆，却漏掉安全约束（如海鲜过敏）。可借鉴「召回后把已召回记忆当
  cue，用 LLM 判断缺失证据目标，再沿语义/结构化边局部扩展」的读阶段，避免无向图全局游走。

  - 写入阶段把对话压缩为 cue-rich episodic units，结构化保存参与者/地点/时间，并建稀疏图：语义边 + 结构化边（Jaccard/时间衰减）。电商场景可把用户、商品、场景实体存为
  cue，便于跨 session 关联，且比维护完整 KG 便宜约 30 倍。

  - 工程实现上，建图采用增量式候选池（语义近邻 + 结构化倒排），每节点最多 K 条边，避免 O(N²)；证据装配用固定权重排序 + 固定 evidence budget，上下文
  token 可控。query-time 控制器额外引入 LLM 延迟，可异步或缓存。

  - 复用结论：关联/图检索只有在「evidence-conditioned」补全（有明确缺失支撑目标）时才有效，单纯加图或递归检索容易召回相关但不支持答案的记忆；业务里可用
  missing-support target 约束扩展方向。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
Long-horizon agent memory 的瓶颈不是存，而是取：答案证据常分散在多个 session、混合在常规对话里。Flat retrieval 召回孤立记录，无向图扩展又容易走到相关但不支持回答的记忆。需要把「已召回的证据」当作继续寻找缺失支撑的 cue，而不是检索终点。  

**方法关键点**  
- **写入**：把对话切分为 event-centric 的 cue-rich episodic memory units，schema 包含 canonical restatement、dense vector，以及参与者/地点/时间 cues；不强行推断未 grounded 字段。  
- **建图**：节点为 memory units，边分语义（cos）与结构化（participant/location Jaccard + 时间衰减）；增量稀疏建图，每节点最多 K 条边。  
- **读取**：先 hybrid initial recall（semantic/lexical/cue）拿初始证据；LLM 控制器做 memory-anchor planning，输出是否继续、anchors、missing-support target；只从 anchors 在 h 跳邻域内扩展，用 target 做语义/结构匹配筛选 support；证据去重后按 query alignment、provenance、anchor status 排序，控制在固定 evidence budget 内生成回答。  

**关键结果**  
LoCoMo：F1 52.49 / BLEU-1 44.05 / judge acc 87.14，judge acc 相对最强基线 RF-Mem +3.95%；LongMemEval-S：两个设置下整体 84.80 / 86.60，multi-session reasoning 较 SimpleMem 78.20 vs 60.92、较 EverMemOS 80.45 vs 73.68。消融中移除 graph expansion 跌幅最大（-4.61%）。图构建成本比 Mem0g/Zep 低约 30×，answer context 平均约 1.47k tokens。  

> 最值得记住：**可靠的长期记忆不取决于把经历存下来，而取决于如何组织它们，让部分 recall 能继续把缺失的支撑证据补全。**
