---
title: Fine-Tuned LLM as a Complementary Predictor Improving Ads System
title_zh: 微调LLM作为补充预测器改进广告系统
authors:
- Hui Yang
- Daiwei He
- Kevin Jiang
- Taejin Park
- Kungang Li
- Jiajun Luo
- Yuying Chen
- Xinyi Zhang
- Sihan Wang
- Haoyu He
affiliations:
- Pinterest, Inc., USA
arxiv_id: '2605.27856'
url: https://arxiv.org/abs/2605.27856
pdf_url: https://arxiv.org/pdf/2605.27856
published: '2026-05-27'
collected: '2026-05-28'
category: RecSys
direction: 生成式推荐 · 广告辅助预测
tags:
- LLM
- Ad Prediction
- Candidate Generation
- Semantic ID
- GRPO
- Pinterest
one_liner: 用微调LLM预测潜在转化广告商，注入检索与排序，线上广告回报提升4.94%-6.69%
practical_value: '- **LLM补全弱信号用户**：对行为稀疏的用户，用LLM基于跨域特征（站外搜索/URL）预测可能转化的广告商，作为检索候选补充，显著提升覆盖与转化。

  - **Semantic ID增强LLM**：将多模态内容（PinCLIP嵌入量化后的SID）拼入prompt并通过多阶段继续预训练注入模型，可大幅提高广告商预测召回率（Recall@20
  +7.2pp），是低成本引入视觉/协同信号的实用路径。

  - **渐进式训练与奖励设计**：先SFT学单目标，再GRPO扩展到多输出并利用位置奖励与长度惩罚，这种简单到复杂的两阶段方案适合工业广告预测，GRPO的格式奖励保证了结构化输出直接可用。

  - **工程化部署要点**：通过用户分层降低推理量、增量更新只处理活跃用户、vLLM+Ray分布式批量推理配合前缀缓存和连续批处理，可在成本可控下实现天级全量推断，适配推荐系统的时效约束。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
在广告推荐中，LLM直接替代工业级Ranker面临ID稀疏、推理延迟等瓶颈。现有LLM在推荐中的应用集中在生成式检索、重排序或信号富集，大规模广告场景的实践较少。本研究探索一种新范式：用微调LLM作为**补充预测器**，基于用户画像和行为历史预测最可能转化的广告商，将结果注入检索和排序，在不改变主排序架构的前提下提升系统效率。

**方法关键点**
- **数据构建**：选取有90天转化记录的活跃用户，特征包括用户画像、站内外搜索/转化/URL序列、历史转化广告商池与预设高收入广告商池；标签为未来7天首个转化广告商。
- **阶段化训练与提示**：SFT阶段预测单个广告商（自由文本）；GRPO阶段预测20个广告商+5个用户兴趣（XML结构化输出），奖励函数包含位置匹配奖励和长度惩罚；推理复用GRPO格式保证一致性。
- **Semantic ID增强**：通过三阶段继续预训练将PinCLIP多模态嵌入量化为20248码表的5级SID融入LLM，SID作为prompt额外输入，显著提升召回。
- **下游集成**：检索端以LLM预测的广告商作为过滤，通过双塔模型生成候选；排序端将预测广告商和兴趣特征化，输入ctcvr/vtcvr转化率模型。
- **服务架构**：vLLM+Ray分布式推理，利用前缀缓存、连续批处理；用户选择与增量更新降低日推理量。

**关键实验与结果**
- 广告商预测：V1数据集（贴近生产）上，SFT (1-ad) + GRPO + SID 的Recall@20达0.755，较零样本高出33个点。
- 特征消融：历史转化广告商贡献最大，站外URL/搜索次之，用户画像影响微弱。
- 下游转化模型：vtcvr PR-AUC提升1.64%，ctcvr PR-AUC提升0.71%。
- 线上A/B：仅对opt-in用户展示LLM候选生成器，美国购物广告ROAS提升6.69%（p=0.029）。

**核心结论**
“ 微调LLM作为补充预测器，可以有效地将异构用户信号合成为可操作的广告商先验，提升工业广告系统。”
