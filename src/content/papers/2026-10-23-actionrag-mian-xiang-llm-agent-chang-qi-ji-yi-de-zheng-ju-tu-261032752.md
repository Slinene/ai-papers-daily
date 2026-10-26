---
title: 'ActionRAG: Evidence-Refining Graph Diffusion for Long-Term Memory in LLM Agents'
title_zh: ActionRAG：面向 LLM Agent 长期记忆的证据精炼图扩散
authors:
- Navyansh Mahla
- Sashank Vandrangi
affiliations:
- Actioneer
arxiv_id: '2610.32752'
url: https://arxiv.org/abs/2610.32752
pdf_url: https://arxiv.org/pdf/2610.32752
published: '2026-10-23'
collected: '2026-10-26'
category: Agent
direction: LLM Agent 长期记忆 · 图扩散检索
tags:
- graph diffusion
- memory-augmented LLM agents
- knowledge graph
- RAG
- entity resolution
- triple retrieval
one_liner: 结合谨慎图索引与查询时接收者归一化图扩散，在 MemoryAgentBench 上以 55.1 平均分刷新检索式记忆 agent 表现
practical_value: '- 查询时把向量召回视为 proposal 而非最终结果：用双通道（实体+三元组）召回后在局部图上做 receiver-normalized
  diffusion 重排序，能恢复多跳关联且不引入 LLM 调用；适合电商会话中“用户问某商品是否适用于某场景”这类需要跨事实推理的 query。

  - 索引阶段做标签调和 + 分层实体消解（精确名+类型匹配优先，模糊匹配仅限唯一候选）能显著降低商品/类目/属性图中的实体碎片，避免后续图检索被重复节点稀释。

  - 冲突消解与事实更新：将时间短语归一化为绝对日期并存入事实描述而非节点，保留 source chunk 指针，可支撑价格/优惠/状态变更等需要区分新旧事实的场景。

  - seed protection 与 hub-penalized flux 两个参数化 trick 可直接借鉴：保护原始高分证据不被图扩散淹没；对高连接度实体（爆款商品/热门类目）施加惩罚，避免
  flux 补全被 hub 主导。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：LLM agent 长期记忆需要从增长交互史中恢复精确且一致的证据，特别是跨事实推理与冲突消解。现有 dense RAG 对 chunk 独立评分，丢失多跳和 superseded 事实区分；图方法如 HippoRAG-v2 依赖查询时 LLM 提取实体，可能遗漏谓词线索。索引错误也可能造成实体碎片或错误合并。

**方法关键点**：
- 离线索引：LLM 提取 typed triples；标签调和；分层实体消解（精确名+兼容类型优先，模糊匹配仅限唯一候选，同组归一建节点）；时间短语归一化为绝对日期存入描述；定期摘要但保留 source chunk 指针。
- 查询时：双通道检索 top-K 实体与具体三元组；hop-capped 扩展构建有界局部图；query-conditioned 接收者归一化扩散 x = α(I-(1-α)P)^{-1}s，A 由最短路径和相关三元组构成；seed protection 保留 top-S raw-score 项；ε 阈值修剪；hub-penalized flux 恢复最多 L 条未见三元组；检索阶段无 LLM 调用。

**关键实验**：在 MemoryAgentBench 八个确定性列上，ActionRAG 平均 55.1，比 HippoRAG-v2 高 5.4，六列最高。MCC 上 82.0 接近 long-context 的 82.4，超过 HippoRAG-v2 20.6 点。消融显示完整管道（reconciled + summarized + diffusion）55.1，基础检索仅 45.0。每查询合成成本 <$0.001，检索 p99 组件 440.7ms。

**最值得记住**：把初始语义检索当作 proposal 而非 final，用局部图扩散 retroevaluate 并 materialize 遗漏关系，是低成本提升多跳/冲突记忆检索的关键路径。
