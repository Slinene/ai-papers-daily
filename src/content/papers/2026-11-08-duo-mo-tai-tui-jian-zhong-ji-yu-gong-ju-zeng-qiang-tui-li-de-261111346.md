---
title: 'IntentLens: Grounding Underspecified Multimodal Queries for Recommendation
  via Tool-Augmented Reasoning'
title_zh: 多模态推荐中基于工具增强推理的意图澄清框架
authors:
- Xiao Chen
- Dong Fang
- Haitao Li
- Qing Li
affiliations:
- The Hong Kong Polytechnic University
- LightSpeed
arxiv_id: '2611.11346'
url: https://arxiv.org/abs/2611.11346
pdf_url: https://arxiv.org/pdf/2611.11346
published: '2026-11-08'
collected: '2026-11-10'
category: RecSys
direction: 多模态推荐 · 工具增强意图澄清
tags:
- Multimodal Recommendation
- Tool-Augmented Reasoning
- MLLM
- GRPO
- Intent Grounding
- Underspecified Queries
one_liner: 通过 ground-then-rank 和 MLLM 工具增强推理，把欠指定多模态 query 澄清为结构化证据再做轻量排序
practical_value: '- **可借鉴的架构：ground-then-rank 分离**：MLLM 只负责 query 侧工具规划与意图澄清，item
  侧工具采用确定性缓存批量执行，排序交给轻量双塔。适合电商大规模候选池，避免逐候选 MLLM 调用带来的时延与成本。

  - **视觉工具弥补 VLM 表示不足**：颜色直方图、主色、色温、crop/zoom 等确定性工具，把“氛围类似、更亮、更暖”这类模糊视觉偏好转化为可比数值特征。可迁移到“找同款/相似风格/相似氛围”商品推荐，尤其适合穿戴设备或拍照搜同款场景。

  - **RFT 奖励设计对齐下游排序**：用 frozen ranker 计算 counterfactual ranking reward（有工具 vs 无工具），再叠加
  tool selection F1 奖励和 observation-masked GRPO。这比只监督工具调用正确性更贴近业务指标，可借鉴到 Agent 工具规划器的强化训练中。

  - **双层用户记忆**：episodic + semantic 记忆分离，长期偏好摘要与交互级证据解耦，并通过紧凑检索 API 暴露。可直接用于电商用户理解，减少
  prompt 上下文膨胀，同时保留可解释的偏好证据。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
智能助手和可穿戴设备带来多模态 query：用户只给一张参考图加一句模糊需求，如“找一家像这样的、氛围温暖、我之前去过的、现在营业的咖啡馆”。这类 query 的视觉偏好、个性化历史约束、商品属性约束都高度欠指定。传统多模态推荐依赖历史交互融合特征，或假设 query 完整，难以直接匹配。

**方法关键点**  
- 提出 ground-then-rank 两阶段框架。Stage 1 用 MLLM 做工具增强推理，只负责 query 澄清和工具选择；item 侧工具解耦批量执行，不增加 MLLM 调用。Stage 2 用轻量双塔 ranker（BGE-M3 backbone）对 grounded query 和 enriched item 打分。  
- 工具分三类：视觉工具（crop/zoom/主色/颜色直方图/色温）提取可比较的感知特征；用户记忆工具（episodic + semantic 双层记忆）检索历史偏好；商品属性工具补齐候选侧细粒度证据。  
- 训练采用 ranker-aligned RFT：用 frozen ranker 给出 counterfactual ranking reward，比较有工具 vs 无工具的排名提升；再加 tool selection F1 奖励和 format reward；GRPO 只对 policy 生成 token 算 loss，mask 掉工具返回观测。

**关键结果**  
在构造的 GOOGLEREVIEW-MMTOOL 和 YELP-MMTOOL 上，IntentLens-7B 达到 GR Hit@10 62.1、MRR 40.2；Yelp Hit@1 33.8、Hit@10 70.4、MRR 46.7，超过 GPT-4o、GPT-5.4 等强 baseline。消融显示去掉 query grounding 后 MRR 从 40.2 掉到 33.5；去掉 RFT 掉到 33.1；去掉 counterfactual reward 或 observation masking 也明显下降。人类手写 query 上仍比 BGE 高 7.3 MRR，端到端延迟约 4 秒（Stage1 3.59s + Stage2 515ms）。

**最值得记住的一句话**  
把 MLLM 从“直接排序器”降级为“意图澄清器 + 工具规划器”，排序交给轻量双塔，既获得工具证据增益又控制在线时延。
