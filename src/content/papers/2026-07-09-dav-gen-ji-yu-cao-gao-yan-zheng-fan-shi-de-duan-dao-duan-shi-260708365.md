---
title: 'DaV-Gen: End-to-End Generative Retrieval via Draft-and-Verify'
title_zh: DaV-Gen：基于草稿-验证范式的端到端生成式检索
authors:
- Meng Zhao
- Chunmei Liu
- Qinyong Wang
affiliations:
- Alibaba Group
- HUJING Digital Media & Entertainment Group
arxiv_id: '2607.08365'
url: https://arxiv.org/abs/2607.08365
pdf_url: https://arxiv.org/pdf/2607.08365
published: '2026-07-09'
collected: '2026-07-10'
category: GenRec
direction: 生成式推荐 · Semantic ID · 稀疏稠密混合表征
tags:
- Generative Retrieval
- Draft-and-Verify
- Semantic ID
- Hybrid Sparse-Dense
- Latency Reduction
- Industrial Search
one_liner: 将生成式检索重构为向量召回 + 并行验证，打破自回归解码的延迟瓶颈
practical_value: '- **用向量检索代替逐 token 生成做候选召回**：训练时通过对比损失优化用户-物品混合表征，线上用 ANN 快速产生固定大小的候选集，彻底绕过自回归解码的
  O(L) 延迟，可落地到搜索/推荐的粗排甚至精排一体化

  - **混合稀疏-稠密物品表征融合 trick**：将 RQ-VAE 的连续编码向量（保存细粒度语义）与 Semantic ID 的均值池化向量（保存层次结构）经
  LayerNorm+MLP 融合为一个向量，同时用于 MIPS 召回和后续打分，比纯 Semantic ID 或纯稠密向量更稳健

  - **广播式前缀缓存实现批量化验证**：训练和推理时把用户上下文编码成 KV cache 只算一次，再广播给所有候选物品并行计算生成分数，上下文长度不再随候选量线性增长，可直接用于大规模召回-精排合并场景

  - **复合损失联合优化解决多阶段目标不一致**：对比损失（召回导向）+ 生成损失（语义合理性）+ 两两排序损失（点击与未点击的细粒度校准）同模型训练，能让同一套参数同时做好召回和排序，避免传统级联系统的误差传播'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：工业级搜索与推荐系统常用多阶段级联架构，但召回、粗排、精排间优化目标不一致，导致早期错误不可逆传播。生成式检索（GenIR）虽能将全链路统一为序列生成，但自回归解码的逐 token 生成引入极高延迟，且缺乏对列表长度的精确控制。为此，需要一种既能保持端到端表达能力，又能满足线上毫秒级响应要求的新范式。

**方法关键点**：
- **草稿-验证双阶段架构**：训练单一模型同时掌握候选生成与精排能力；线上先通过向量相似度做 ANN 检索得到候选集，再对候选做并行评分排序，替换掉自回归生成。
- **混合稀疏-稠密物品表征**：将 RQ-VAE 编码前的连续向量（保留细粒度语义）与 Semantic ID 经 Transformer 后取均值（保留层次结构）融合为统一向量，支撑高效向量召回和后续精细验证。
- **联合训练损失**：① 对比损失在批次内拉近正例、推远负例，组织语义空间供向量检索；② 生成损失预测物品 Semantic ID 序列的似然，建模物品的层次语义；③ 两两排序损失基于点击/未点击对优化最终融合打分，实现从召回目标到排序目标的对齐。
- **广播前缀缓存**：训练与推理时，将用户上下文的 KV Cache 计算一次后广播至所有候选物品，实现候选并行打分，延迟几乎独立于候选数量。

**关键结果**：
- 在 Amazon Beauty、Sports、Yelp 三个推荐基准上，Recall@10 较最强基线 OneRec 最高提升 2.89%，NDCG@10 最高提升 3.44%。
- 在工业级视频搜索数据集 Ind-Search 上，召回率@50 从对照组的 44.7% 提升至 77.4%，NDCG@10 和 MRR@10 均显著优于线上 MoE 精排模型。
- 线上 A/B 测试：用户平均停留时长 +2.09%，用户转化率 +0.47%，人均成功搜索次数 +0.31%。
- 推理延迟：纯生成式模型约 3s，传统级联系统约 130ms，DaV-Gen 降至约 70ms，实现 2.5 倍加速。
- 消融实验表明：移除稠密向量部分导致最大性能下降，验证了混合表征的核心作用。

**一句话**：用一次向量搜草稿 + 一次并行打分替代逐 token 生成，让生成式推荐首次在工业级延迟下提供比传统级联系统更强的排序效果。
