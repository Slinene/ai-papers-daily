---
title: 'One Hierarchy, Two Systems: Semantic Product IDs for Discovery-Surface Ranking
  and Search-Page Query Reformulation'
title_zh: 一个层级，两个系统：语义商品ID用于发现面排序与搜索页查询改写
authors:
- Steven Xu
- Sanjyot Thete
- Saathvik Dirisala
- Raghav Saboo
- Nimesh Sinha
- Leo Shao
- Elyse Winer
- Sudeep Das
- Martin Wang
- Kyle MacDonald
affiliations:
- DoorDash Inc.
arxiv_id: '2608.20640'
url: https://arxiv.org/abs/2608.20640
pdf_url: https://arxiv.org/pdf/2608.20640
published: '2026-08-21'
collected: '2026-08-24'
category: RecSys
direction: 语义ID 跨推荐搜索共享层级
tags:
- Semantic ID
- ranking
- query reformulation
- e-commerce
- residual quantization
one_liner: 一次性构建的分层语义商品ID同时支撑个性化排序与查询改写，排序聚合前缀特征、改写基于商品概念转移
practical_value: '- 用 RQ-KMeans 从商品文本 embedding 构建三层语义 ID（L=3, K=512）作为跨商家商品概念层级；排序中按
  L1/L2/L3 前缀聚合消费者、区域、全局行为统计得到多粒度 dense 特征，再用 SentencePiece BPE 对 (position, code)
  符号串学出子词，构建 item/user 序列 embedding，比直接用前缀更互补。

  - 查询改写不要直接 LLM 生成：先把 query 通过关联加购商品映射到 L2/L1 语义前缀，在概念空间用 NPMI 构建转移图；需要细化时从 L2 下降到
  L3 子节点，用 query-specific 加购证据排序；LLM 仅负责最后将概念渲染成用户可见 query，保证可控性和可解释性。

  - 服务时必须恢复上下文：用 merchant 当前可用商品过滤概念候选，避免推荐无货意图；排序保留 listing ID 和 taxonomy，SID 只作为补充，防止量化边界问题。

  - 共享表示不共享模型：推荐和搜索各自独立使用同一语义层级，无需联合训练；排序在多个前缀深度同时消费，查询改写则 L2 横向导航、L3 纵向精化，适合低成本迁移到现有系统。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
多商家电商目录中，相同/相关商品分散在不同商家 listing ID 下，行为信号碎片化；专家 taxonomy 又太粗，难以支撑细粒度个性化。需要一种能跨商家聚合证据、同时保留细粒度区分、并且能同时支持推荐排序和查询改写的商品表示。分层语义 ID（SID）通过残差量化 embedding 形成嵌套商品概念，恰好提供多分辨率层级。

**方法关键点**  
- 商品文本 profile 经 gemini-embedding-001 得到 3072 维 embedding，用 RQ-KMeans（L=3，K=512）构建三层 SID；前缀 L1/L2/L3 形成嵌套商品概念。  
- 排序侧：设计两种 SID 特征——按前缀聚合消费者、区域、全局行为统计的 dense 特征，以及将 SID 转为 (position, code) 符号串训练 SentencePiece BPE，item 与用户历史池化 embedding 共享表的序列特征。  
- 查询改写侧：query 通过关联加购事件映射到 L2/L1 前缀，在业务垂类内用 NPMI 构建概念转移图；从 L2 下降到 L3 子节点做细化；LLM 只用于将概念渲染成 query；候选经过 merchant 当前商品类目过滤。  

**关键实验数字**  
排序离线：完整 SID 特征相对无 SID 特征 MRR@5 +6.98%、NDCG@5 +6.76%；在线首位/次位 ATC rate 分别 +8%、+16%，subtotal +0.31%，首位平均历史 popularity 下降 18.1%。  
查询改写离线：SID 意图坍缩率 10.9% vs taxonomy 18.8%；LLM judge 质量分 0.734 vs 原始 query-string 图 0.522；在线 ATC position −1.571%，scroll depth −1.866%，Purchase MRR +0.558%。  

**最值得记住的一句话**  
SID 层级作为可转移语义先验：排序同时消费多个深度，查询改写 L2 做横向导航、L3 做纵向精化；每个应用在行动前恢复自己的任务上下文，而不是直接使用共享表示。
