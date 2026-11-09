---
title: Generative Search and Recommendation at Shopify
title_zh: Shopify 生成式搜索与推荐：语义 ID 统一建模
authors:
- Juhana Kangaspunta
- Khalil Hajji
- Darshan Fofadiya
- Kyumin Park
- Michael Garner
- Anthony Maltsev
- Ryan Synk
- Jose Sepulveda
- Joshua Crisologo
- Shuying Sun
affiliations:
- Shopify
- Liquid AI
arxiv_id: '2611.08804'
url: https://arxiv.org/abs/2611.08804
pdf_url: https://arxiv.org/pdf/2611.08804
published: '2026-11-05'
collected: '2026-11-09'
category: GenRec
direction: 生成式推荐 · Semantic ID
tags:
- Semantic ID
- Generative Retrieval
- LLM4Rec
- Multi-token Prediction
- Task Distillation
- Industrial Scale
one_liner: 用 RQ-KMeans 生成语义 ID，LLM 统一生成式搜索与推荐，在 Shopify 生产环境落地
practical_value: '- **商品 ID 离散化**：用 RQ-KMeans 对内容 embedding 量化成多级码本，比 RQ-VAE 更优；behavioral
  coherence 与下游质量正相关，可借鉴用于构建商品语义 ID 做生成式召回。

  - **统一搜索与推荐**：任务专家蒸馏（routed distillation）能避免联合 SFT 的“统一税”，在提升推荐 Recall +1.76% 的同时不损失搜索质量，适合多任务统一模型落地。

  - **推理加速**：搜索用 multi-token prediction（并行预测整个 SID）+ 轻量 ranker 重排，以质量换延迟但靠 ranker
  反超 AR；推荐用 AR + joint-probability 解码处理语义 ID 碰撞问题。

  - **数据配比与发现流**：加入“新产品/新商家/新类目首次购买”发现流，可提升 discovery Recall ~10%；压缩旧交互噪声，提升新商品发现能力。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：电商搜索和推荐需在海量商品目录下快速检索，传统检索/推荐分离，两塔模型将用户压缩为固定向量，生成式检索用语义 ID 统一表示商品，可共享表示和学习目标。Shopify 提出 SID-LLM，将搜索（非个性化/个性化）和推荐统一为根据上下文生成商品语义 ID 的任务。

**方法关键点**：
- 商品内容 embedding 经 RQ-KMeans 量化为三级 8192-8192-8192 语义 ID；预训练 LLM 扩展 SID tokens，先做 embedding alignment 再继续预训练。
- 数据混合包括商品属性、搜索会话/LLM 判断样本、用户交互序列和发现流；搜索质量后训练用 CE/DPO/GRPO。
- 统一搜索推荐用任务专家蒸馏（KL 蒸馏）；推理上搜索用多 token 预测 + 轻量 ranker，推荐用 AR + 联合概率解码。

**关键结果**：
- 搜索全栈加入 SID-LLM 后 OneDCG@10 相对提升 6.5%（combined）和 7.7%（personalized）；单模型 SID-LLM 与多模型搜索栈接近。
- 推荐上蒸馏学生比 joint SFT 提升 Recall@50 +1.76%，discovery Recall@50 +10.03%，搜索无统计显著损失。
- MTP+ranker 在搜索指标上超过 AR（OneDCG@10 0.3365 vs 0.3083）且延迟更低，p95 在 100 rps 下 36.6ms。

**最值得记住的一句话**：用内容量化语义 ID 让 LLM 生成式检索统一搜索与推荐，并通过任务蒸馏和并行解码满足工业级延迟。
