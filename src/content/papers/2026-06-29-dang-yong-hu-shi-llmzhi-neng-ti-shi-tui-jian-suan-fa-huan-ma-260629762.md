---
title: Do Recommendation Algorithms Work When Users Are LLM Agents? A Case Study on
  Moltbook
title_zh: 当用户是LLM智能体时，推荐算法还奏效吗？Moltbook案例研究
authors:
- Daming Li
- Simeng Han
- Jialu Zhang
affiliations:
- Independent Researcher
- Stanford University
- University of Waterloo
arxiv_id: '2606.29762'
url: https://arxiv.org/abs/2606.29762
pdf_url: https://arxiv.org/pdf/2606.29762
published: '2026-06-29'
collected: '2026-06-30'
category: RecSys
direction: AI Agent环境下的推荐评估 · 结构模式替代个性化
tags:
- LLM Agents
- Recommender Systems
- Personalization
- Collaborative Filtering
- Social Platforms
- User Modeling
one_liner: 在AI智能体社交平台上，推荐因缺乏用户偏好而退化为结构匹配，简单方法胜过个性化模型
practical_value: '- 若电商或内容平台出现大量AI Agent行为（如爬取、自动测评），训练数据会被污染，个性化模型将引入噪声；应部署Agent检测与过滤机制，保护训练集纯度。

  - 在Agent混入的场景下，简单信号（物品共现、全局热门）比复杂用户表示更鲁棒，可考虑构建一套「轻量结构模型」作为兜底策略或信号补充。

  - karma加权（质量信号）使结构方法性能提升2~5倍，但对个性化模型无效，说明质量信号的利用需要与模型假设匹配——若用户无稳定偏好，质量信号只能放大结构模式，无法激活个性化。

  - 时间衰减实验表明Agent行为无偏好漂移，因此对Agent密集的日志，可降低模型重训频率，减少工程开销，重点维护结构信号而非追求时效性用户表示。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
LLM智能体正大量涌入Web平台，传统推荐系统假设用户拥有可学习的持久偏好，但Agent通常无状态、无固定兴趣，这一假设面临根本性挑战。探索Agent主导的社交网络中现有推荐算法是否仍然有效，对保护真实用户体验、防止模型退化具有紧迫意义。

## 方法
- **平台与数据**：采用Reddit式的纯Agent社交平台Moltbook，使用其公开数据集（10周内约240万帖、99万评论、17.5万Agent），过滤后约8万活跃Agent、5.4k submolts，交互矩阵密度仅0.041%。
- **推荐任务**：给定Agent历史交互，预测下一周会参与的submolt（论坛），为Top‑N推荐。
- **评估算法**：Random、TopPopular、BPR‑MF、HybridMF（ALS+MiniLM内容嵌入）、ContentBased（仅内容相似度）、ItemKNN、LightGCN、SASRec，共8种。
- **追加实验**：karma加权交互矩阵、Agent静态描述特征、训练‑测试时间间隔衰减分析。
- **指标**：Recall、NDCG、Hit Rate、MRR @5/10/20/50。

## 核心结果
- **结构方法统治**：ItemKNN整体最优，LightGCN、SASRec、TopPopular紧随其后，均显著优于依赖用户表示的BPR‑MF、HybridMF、ContentBased。
- **karma加权放大差距**：使用karma加权后，TopPopular性能提升2.2~3.2倍，ItemKNN提升2.2~2.6倍，HybridMF提升2.5~5.2倍，而BPR‑MF基本不变。
- **Agent描述无效**：利用Agent静态描述特征几乎无预测力，注入到ItemKNN或HybridMF中反而带来噪声性下降。
- **无时间衰减**：训练‑测试间隔从1周扩大到4周，所有模型性能均未退化，说明Agent行为稳定、无偏好漂移。

**一句话：LLM Agent缺乏持久偏好，推荐由个性化坍缩为结构模式匹配，简单协作过滤与流行度即达到上限。**
