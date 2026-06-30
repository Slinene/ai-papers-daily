---
title: 'From Extraction to Navigation: Progressive Retrieval with Indirectly Infinite
  Depth'
title_zh: 从抽取到导航：间接无限深度的渐进式检索
authors:
- Linxiao Che
- Shanshan Huang
- Haitao Lu
- Yijia Sun
- Qiang Luo
- Ruiming Tang
- Han Li
- Kun Gai
- Guorui Zhou
affiliations:
- Kuaishou Technology
- Unaffiliated
arxiv_id: '2606.29970'
url: https://arxiv.org/abs/2606.29970
pdf_url: https://arxiv.org/pdf/2606.29970
published: '2026-06-29'
collected: '2026-06-30'
category: RecSys
direction: 图导航召回 · 间接无限深度探索
tags:
- Graph Navigation
- Stateful Retrieval
- Search Drift
- Multi-hop
- Cross-request State
- Hard Negative Sampling
one_liner: 将推荐召回建模为跨请求状态演化的图导航过程，突破单次查询的深度限制，缓解搜索漂移
practical_value: '- **用状态接力绕过延迟天花板**：将召回视为有状态的多轮探索，通过Redis缓存上一请求的搜索前沿节点，注入下一次请求的种子集，在用户多次交互中累积探索深度而不增加单次延迟。电商/广告场景中，可对同一会话内的翻页、重搜、换词请求复用图游走状态，逐步渗透长尾商品。

  - **图硬负采样对抗搜索漂移**：在训练时从协同图与语义图中采样拓扑接近但无正交互的邻居作为硬负例，结合pairwise margin loss，让判别器学会区分“结构近但意图远”的节点，抑制多跳导航中的累积误差。在自身召回模型里可直接引入图结构硬负例，提升检索精度。

  - **意图锚点融合近期与遗忘兴趣**：初始化触发集时，将用户近期曝光项与历史中出现但近期缺失的品类项合并，避免兴趣窄化。广告推荐中可借鉴，用关键品类标签补齐近期未覆盖类目，确保召回起点同时兼顾实时意图与沉睡兴趣。

  - **双图异构导航实现互补探索**：同时构建协同图（Swing i2i）和语义图（多模态LLM embedding），融合行为相似性与内容相似性路径。电商场景下，协同图保证物理关联，语义图通过画像/标题/视觉相似性发现跨类目商品，适合新品冷启动与跨域推荐。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
现代大规模推荐系统正从静态相似抽取转向动态导航，但传统i2i启发式方法受限于“兴趣隧道”效应，无法探索深层兴趣；基于结构化索引的方法则因静态入口和刚性拓扑而出现“搜索漂移”，多跳后召回质量大幅下降。单次请求的延迟预算严格限制了图遍历的物理跳数，导致系统难以穿透稀疏的兴趣区域。为此，本文提出间接无限深度（IID）理论，将检索形式化为有状态、自主探索的过程，使系统能在不增加单次延迟的情况下跨请求累积深度。

## 方法
- **异构导航环境**：分别构建基于Swing算法的协同图（行为关联）和基于多模态LLM提取embedding的语义图（内容关联），为意图驱动的多跳遍历提供互补的路径基础。
- **目标导向导航策略**：采用target-aware cross-attention打分网络作为判别器，替代被动近邻扩展，根据用户历史与候选的交互决定搜索方向，实现主动路由。
- **轨迹感知学习**：训练中从图邻居中采样拓扑接近但无正交互的“图硬负例”，结合InfoNCE与margin ranking的混合损失，强制模型在整条导航轨迹上对抗搜索漂移，维持意图对齐。
- **动态锚点唤醒**：每次请求的触发集由近期兴趣（最近L个不重复曝光项）和“缺失记忆兴趣”（最近未充分出现的品类中的历史项）融合而成，避免兴趣固化并引入长期记忆多样性。
- **递归状态演化（IID核心）**：将上一请求搜索前沿的高分节点通过Redis缓存注入下一次请求的初始触发集（E_u(t+1)=A_u(t+1)∪S_u^t），使逻辑探索深度随时间线性增长，却不受单次延迟约束。

## 结果
在MovieLens-20M、淘宝用户行为以及一个日活亿级的短视频工业数据集上进行评测。IID-Nav在工业数据集上Recall@500达0.2408，相较Kuaiformer提升36.35%，NDCG@500提升36.98%，且QPS维持在910（基准DSSM为1300，NANN为384），满足线上延迟要求。在线A/B测试中，总使用时长提升0.33%~0.40%，视频观看时长提升0.55%以上。消融表明去除图硬负样本后Recall@500下降8.26%，去除缺失记忆锚点后下降21.2%，验证了各组件的关键作用。
