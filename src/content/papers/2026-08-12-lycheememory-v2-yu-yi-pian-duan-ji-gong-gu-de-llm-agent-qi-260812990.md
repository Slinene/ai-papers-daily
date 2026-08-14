---
title: 'LycheeMemory V2: Efficient Long-Term Memory for LLM Agents via Semantic Segment-Level
  Consolidation'
title_zh: LycheeMemory V2：语义片段级巩固的 LLM Agent 长期记忆框架
authors:
- Dongfang Li
- Zixuan Liu
- Junmai Wang
- Jiahe Huang
- Fuhao Li
- Bonian Jia
- Baotian Hu
- Min Zhang
affiliations:
- Harbin Institute of Technology, Shenzhen
arxiv_id: '2608.12990'
url: https://arxiv.org/abs/2608.12990
pdf_url: https://arxiv.org/pdf/2608.12990
published: '2026-08-12'
collected: '2026-08-14'
category: Agent
direction: LLM Agent 长期记忆构建与检索
tags:
- LLM Agent
- Long-Term Memory
- Semantic Segmentation
- Memory Consolidation
- Structured Retrieval
- Efficiency
one_liner: 将逐轮记忆巩固改为语义片段级批量编码，写侧 token 降最多 86% 且 LoCoMo/LongMemEval-S 精度 SOTA
practical_value: '- 在对话式推荐/导购 Agent 中，不要每轮都调 LLM 写画像；改成按语义完整片段批量生成 typed memory records（偏好/事实/约束/事件），写侧
  token 可降低 75%–86%，适合长期用户画像积累。

  - 分段触发别用固定窗口，可用 embedding 相似度 + cohesion drop 在线检测语义边界，保留事件和话题结构；固定窗口在消融中精度掉 6.8pp，语义分片能提升多跳和开放域问答。

  - 把非结构化对话提炼为 typed records，并建立 entity/topic/temporal/event-frame 结构化索引；查询时 planner
  一次性规划多路召回（record/节点/时间/原始 turn），再用 RRF 融合，能有效处理多跳、时序、偏好追踪类查询，且避免多轮 LLM 检索带来的 query
  token 上升。

  - 评估记忆系统时，把 construction tokens 和 query tokens 分开核算，不要只比精度；该方法在精度提升 20pp 以上的同时，query
  tokens 反而比 A-Mem 低 28%–43%。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
长期 LLM Agent 需要外部记忆，但现有 eager consolidation 每轮调用 LLM 提取总结，写侧成本随对话线性增长；粗粒度摘要会丢失细粒度证据，而大上下文或多跳推理又把开销转到查询侧。核心挑战是：在保留足够细粒度证据的同时，控制写侧和查询侧 token。

**方法关键点**  
- 用语义片段级巩固替代逐轮巩固：对话先进入缓冲，通过语义惊喜度、cohesion drop、token 压力和轮次压力计算边界分数，只在片段完成时触发一次 LLM 编码；平均 5.8 轮编码一次。
- 片段编码成上下文无关的 typed records：包含事实、偏好、事件、约束、过程、失败模式等类型，并带实体、话题、时间范围和原始 turn 溯源。
- 跨片段通过轻量消歧状态（实体别名、指代关系）保持连续性，避免重读全部历史。
- 记录进入 append-only 结构化存储，建立向量索引 + entity/topic/temporal/event-frame 结构化索引；查询时 planner 一次性分解为多条 recall route，执行 direct record / evidence-node / temporal / raw-turn 四通道召回，RRF 融合 + rerank + 多样性选择。

**关键结果**  
GPT-4.1-Mini 下，LoCoMo 总体准确率 89.22%、LongMemEval-S 92.20%，均为 SOTA；对比 A-Mem，construction tokens 分别降 86.0% 和 75.9%，query tokens 分别降 27.9% 和 42.6%。消融显示：eager 固化精度掉 7.3pp 且写侧 token 增 316%；固定窗口精度掉 6.8pp；移除融合/rerank/多样性选择精度掉 22.6pp；阈值鲁棒性良好。

**最值得记住的一句话**  
长期 Agent 记忆的精度-成本权衡不只取决于保留什么信息，更取决于在什么粒度上做语义巩固。
