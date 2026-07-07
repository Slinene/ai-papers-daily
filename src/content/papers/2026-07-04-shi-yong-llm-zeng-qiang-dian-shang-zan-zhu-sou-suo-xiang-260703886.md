---
title: Enhancement of E-commerce Sponsored Search Relevancy with LLM
title_zh: 使用 LLM 增强电商赞助搜索相关性
authors:
- Md Omar Faruk Rokon
- Andrei Simion
- Weizhi Du
- Musen Wen
- Hong Yao
- Kuang-chih Lee
affiliations:
- Walmart AdTech
arxiv_id: '2607.03886'
url: https://arxiv.org/abs/2607.03886
pdf_url: https://arxiv.org/pdf/2607.03886
published: '2026-07-04'
collected: '2026-07-07'
category: RecSys
direction: LLM 助力搜索广告相关性判别
tags:
- LLM
- LoRA
- sponsored search
- relevance classification
- LLaMA2
- e-commerce
one_liner: 用 LoRA 微调 LLaMA2 7B 做 <query, ad title> 三分类，准确率 89.43% 优于 GPT-4 和 BERT
practical_value: '- 用 **LoRA 微调开源 LLM（LLaMA2 7B）** 构建相关性模型，成本和隐私都优于依赖 GPT-4 API，适合公司内部部署。

  - 将相关性定义为 **三分类（Relevant / Partially Relevant / Irrelevant）** 更贴合实际排序需求，可据此设计差控策略或加权打分。

  - 直接使用 **<query, ad title> 文本对** 作为输入，无需手工构造特征，可快速迁移到商品搜索、内容推荐等其他文本匹配场景。

  - 标注时采用 **3 人投票取多数** 保证质量，后续可搭配 **模型自动标注 + 人工抽检** 缩短迭代周期，降低标注成本。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：电商赞助搜索中，广告相关性直接影响点击率和转化率。传统关键词匹配难以捕捉查询意图的细微差别，BERT 类模型效果有限，GPT-4 成本高且存在隐私风险。本文探索用开源 LLM 高效构建高精度、低成本的相关性分类器。

**方法关键点**：
- **基座模型**：LLaMA2 7B 自回归解码器，具备强文本理解能力。
- **微调方法**：Low‑Rank Adaptation (LoRA)，在注意力和前馈网络的投影层注入低秩矩阵，只训练新增参数，大幅降低显存和计算开销。
- **任务设计**：三分类——Irrelevant、Partially Relevant、Relevant，直接输入“用户查询”和“广告标题”文本对，输出概率。
- **训练配置**：250K 训练样本，56K 验证/测试，使用交叉熵损失、Adam 优化器，学习率 1e‑5，batch size 16，4×V100 训练 3 轮后取验证准确率 89.44% 的检查点。

**关键结果**：
- 在 56K 测试集上准确率 **89.43%**，显著优于 Cross‑Encoder BERT（86.27%）、Bi‑Encoder BERT（74.42%）和 GPT‑4 few‑shot（63.02%）。
- NDCG@4 达 **0.7142**，超过 Cross‑Encoder BERT 的 0.6939，表明排序质量更高。
- 模型对“Irrelevant”类别仍有提升空间，但已在主流方案中达到最佳平衡。

**核心一句话**：将 LLaMA2 7B + LoRA 用于电商广告相关性三分类，在保证数据私密性与较低推理成本的前提下，准确率提升至 89.43%，成为替代 GPT‑4 和传统 BERT 方案的有效路径。
