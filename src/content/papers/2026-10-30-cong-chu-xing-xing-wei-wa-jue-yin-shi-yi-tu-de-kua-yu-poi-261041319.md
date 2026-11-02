---
title: 'MILES-Rec: Uncovering Implicit Intents from Mobility Behaviors for Cross-Domain
  POI Recommendation'
title_zh: 从出行行为挖掘隐式意图的跨域 POI 推荐 MILES-Rec
authors:
- Yi Zou
- Wei Luo
- Xuewen Zhang
- Zhuang Yan
- Pengjie Wang
affiliations:
- AMAP, Alibaba Group
arxiv_id: '2610.41319'
url: https://arxiv.org/abs/2610.41319
pdf_url: https://arxiv.org/pdf/2610.41319
published: '2026-10-30'
collected: '2026-11-02'
category: QueryRec
direction: 生成式 query 推荐 · LLM 跨域意图推理
tags:
- LLM
- GRPO
- Cross-Domain POI Recommendation
- Intent Inference
- Query Generation
- Mobility Behavior
one_liner: 用 LLM 将地图出行行为与画像推理为有序自然语言 query，再用 GRPO 双层 credit assignment 对齐后续服务交互
practical_value: '- 跨域推荐可用「自然语言 query 列表」作为语义桥：当行为域与商品/服务域无直接 ID 重叠时，不直接预测 item，而让
  LLM 先输出多条有序意图 query（primary/expansion），再复用现有检索/召回。可迁移到从站内浏览、搜索、收藏、加购等异质行为生成导购 query，接商品/POI
  检索。

  - 两阶段训练可落地：先用大模型+人工校验合成三段式推理 SFT 数据（situation understanding → intent expansion →
  query prioritization），要求证据引用并去重；再用后续点击/下单做 GRPO。相比直接 SFT，能显著提升下游 Hit/NDCG，冷启与稀疏历史也受益。

  - 奖励设计值得复用：用后验交互按细类聚合后，计算 query-category 匹配概率 × query-目标内容 embedding 相似度，one-to-one
  最大权匹配 + rank discount 量化列表覆盖；重复 query 和超长惩罚可抑制冗余。适合只有隐式反馈、无逐 query 标签的列表生成任务。

  - two-level credit assignment 是关键 trick：list-level advantage 管整体覆盖，query-specific
  advantage 只加在对应 query token 上，不能广播到所有 query；这能同时优化单 query 相关性和列表多样性。在生成广告文案、搜索推荐词、多意图
  query 时可直接借鉴。

  - 完整 60 天历史好过 7 天窗口；画像在行为稀疏时更补益。实际系统可将轨迹/行为窗口放大，并对冷启动保留画像与城市上下文。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
地图平台高频出行行为（搜索、路线、导航、保存）与服务消费行为高度异质，传统 next-POI 预测只预测下一地点，无法捕获伴生消费意图。MILES-Rec 让 LLM 将画像和历史行为推理为有序自然语言意图 query，作为 mobility → local-service 的显式语义桥，再由 query 检索 POI。

**方法关键点**  
- 输入含三类画像（基础/生活/车辆）、历史行为（时间、动作、文本）和时空上下文；输出为最多 10 个带 primary/expansion 标签的有序 query。
- 两阶段训练：SFT 用 19,006 条教师生成 + AI 反馈 + 人工复核的三段式推理演示，阶段为 situation understanding → intent expansion → query prioritization；GRPO 用 3,000 用户后续服务交互做策略优化。
- 行为奖励：将后续交互按 263 细类归组，query 分数 = 服务匹配概率 × 与目标 POI 的语义相似度；one-to-one 最大权匹配 + rank discount 奖励列表覆盖，重复和超长扣分。
- two-level credit assignment：list-level advantage 作用于全响应，query-specific advantage 只作用于对应 query token，避免同一响应内 query 共享同质信号。
- 跨 4B/9B/27B/122B-A10B 骨干；检索用 200 万 POI 池的空间混合检索。

**关键结果**  
- GRPO 相对 SFT 一致提升：4B Rich Hit@50 1.50→3.40，NDCG@50 0.171→0.325；Sparse NDCG@50 0.276→0.282，SIA@10 14.41→18.20，SDA 15.77→25.80。
- 27B GRPO 在 Rich 上取得最高 SIA@10 42.45、SDA 72.19。
- 对比 Content-ComiRec-SA，MILES 4B Rich NDCG@50 0.325 vs 0.212；Sparse 0.282 vs 0.183。
- 将 query 替换为粗类目后 NDCG 几乎归零（0.325→0.004），说明自然语言意图表达对检索价值不可替代。

**一句话**：把跨域隐式需求显式化为有序自然语言 query，并用 list coverage + query relevance 双层 credit assignment 的 GRPO 对齐后续行为，是稳定提升检索与语义对齐的核心。
