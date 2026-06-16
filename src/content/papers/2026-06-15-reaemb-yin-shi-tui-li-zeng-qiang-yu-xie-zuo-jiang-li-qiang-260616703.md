---
title: 'Harmonizing Semantic and Collaborative in LLMs: Reasoning-based Embedding
  Generator for Sequential Recommendation'
title_zh: ReaEmb：隐式推理增强与协作奖励强化学习的两阶段LLM嵌入生成框架
authors:
- Qidong Liu
- Mingyao Huang
- Moranxin Wang
- Wenxuan Yang
- Haiping Zhu
affiliations:
- 西安交通大学
arxiv_id: '2606.16703'
url: https://arxiv.org/abs/2606.16703
pdf_url: https://arxiv.org/pdf/2606.16703
published: '2026-06-15'
collected: '2026-06-16'
category: GenRec
direction: LLM生成式推荐Embedding · 隐式推理+RL协作注入
tags:
- LLM Embedding
- Sequential Recommendation
- Latent Reasoning
- Collaborative Reward
- RL-based Collaborative Injection
one_liner: 通过隐式推理增强对比学习与协同奖励强化学习，让LLM生成的物品嵌入同时捕获深层语义和共现关系，提升序列推荐效果。
practical_value: '- **两阶段核心理念可复现**：先做语义增强（隐式推理+对比学习），再做协同信号注入（RL奖励优化），解耦训练，可在自己的LLM推荐embedding场景中直接参照。

  - **隐式推理token的轻量化设计**：仅增加一个轻量attention模块生成多个推理token，然后送入LLM二次前向得到embedding，训练和推理成本低，可离线缓存。适用于需要LLM理解物品属性多义的电商场景（如商品标题、品类、品牌组合）。

  - **基于共现的奖励函数简单有效**：用互作用序列统计物品共现次数，设计奖励让高共现物品对嵌入更近，无需昂贵的标注或用户反馈。这直接对标推荐系统中的协同过滤思想，可快速应用到广告或推荐系统的物品向量生成。

  - **RL的batch级优势估计稳定训练**：舍弃组内归一化，改用噪声-free样本的batch均值作基线，解决了噪声扰动下的训练震荡，该trick可移植到其他RL优化embedding的场景。

  - **长尾与热门兼顾**：实验表明，该方法在整体和长尾推荐上都显著优于现有LLM2Emb、LLM2Vec等方法，且不同LLM架构（Qwen、Llama）下均可稳定提升，适合处理物品冷启动问题。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：序列推荐（SRS）依赖物品嵌入，但传统ID-based方法受长尾问题困扰，LLM虽可提供语义知识，却存在两大不足：一是现有方法只用LLM单次前向编码，未利用模型内部推理能力；二是协作信号（物品共现）多通过有监督微调隐式注入，缺乏显式引导，导致语义与协同空间错位。

**方法关键点**：
- **两阶段框架**：第一阶段 LRCL，通过隐式推理增强对比学习强化语义表示；第二阶段 CRRL，通过协同奖励强化学习显式注入共现信号。
- **隐式推理（Latent Reasoning）**：在LLM输入后添加k个可学习的推理占位token，经注意力模块生成k步推理向量，再替换占位token，二次前向得到语义增强的嵌入。
- **属性级对比学习**：随机丢弃物品文本属性，对比同一物品的两个增强视图，训练LLM进一步关注语义。
- **协同奖励函数**：基于交互统计，以物品共现频率为权重，奖励使高共现物品对嵌入更近的采样样本。
- **GRPO式批量策略优化**：对推理模块参数加噪声采样G个嵌入，以噪声-free样本的batch平均奖励为基线计算优势，进行裁剪的优化，仅更新轻量推理模块，保持LLM冻结。
- **推理完全离线**：训练后所有物品嵌入预计算并缓存，SRS推理时无需LLM在线参与，延迟为零。

**关键结果**：
- 在Yelp、Amazon CD、Amazon Games三个数据集上，ReaEmb在SASRec、GRU4Rec、BERT4Rec三种骨干上均优于LLM2Vec、TSLRec、SAID、LLMEmb、LLM2Rec等5个baseline。
- Yelp数据集SASRec + ReaEmb的 H@10 0.7862（最佳baseline LLMEmb仅0.6752），长尾H@10达0.6504（比LLMEmb提升约35%）。
- 消融实验表明，去除第一阶段对比学习性能显著下降，去除RL阶段或替换为组内优势均造成下降。
- 推理步数k=1即已达稳定，正样本数M=3时NDCG最优。
