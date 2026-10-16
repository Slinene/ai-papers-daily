---
title: Aligning LLMs with Sparse Retrieval via Adaptive Sparse Supervision
title_zh: 自适应稀疏监督下的LLM稀疏检索对齐
authors:
- Tongna Chen
- Minghan Li
- Guodong Zhou
affiliations:
- Soochow University
arxiv_id: '2610.21877'
url: https://arxiv.org/abs/2610.21877
pdf_url: https://arxiv.org/pdf/2610.21877
published: '2026-10-15'
collected: '2026-10-16'
category: RecSys
direction: LLM稀疏召回 · 自适应稀疏对齐
tags:
- Neural Sparse Retrieval
- LLM
- SPLADE
- LoRA
- Knowledge Distillation
- Efficiency
one_liner: 用动态α-truncation对齐SPLADE词表，1B LLM稀疏检索在L0=182时接近Lion-sp效果且延迟降11倍
practical_value: '- 在搜索/广告召回中若要用LLM做稀疏召回，可复用「投影到SPLADE词表 + max-pooling + log(1+ReLU)」结构，用1B模型+LoRA即可与倒排索引兼容，避免在线生成式开销

  - 训练阶段用SPLADE作为anchor，对每个输入按累积激活质量动态选取监督support（α-truncation），比固定Top-K更稳：在消融中MRR@10从α-mean的0.303提升到0.322

  - 两阶段训练值得借鉴：先做稀疏对齐预训练，再做对比学习+KL蒸馏+FLOPS正则，可让索引条目减少40.7%，同时MRR@10从0.3619提升到0.3998

  - 推理时无需额外truncation，只靠训练获得的稀疏性；对query和document分别设置FLOPS正则系数，可把L0从1170压到182，避免83GB索引和>1s查询延迟'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
神经稀疏检索（如SPLADE）高效且兼容倒排索引，但骨干编码器较小，语义容量受限；LLM语义建模强，但直接投影到稀疏词表会产生不可控的密集激活，导致存储与查询延迟不可接受（Lion-sp的L0=1170、索引83GB、延迟>1s）。该工作希望保留LLM语义表达能力，同时维持稀疏检索的效率和可解释性。

**方法关键点**
- 采用LLaMA-3.2-1B双向注意力作为编码器，将hidden states投影到SPLADE词表维度，经max-pooling和log(1+ReLU)得到非负稀疏向量。
- 提出动态α-truncation：对每个输入，在SPLADE anchor向量上按累积激活质量占比选取最小Top-K词作为监督support；对齐损失在support内做MSE，support外用L2惩罚低激活。该方法不依赖固定support budget，能抑制长尾噪声并保留显著词。
- 两阶段训练：Stage 1用LoRA做稀疏对齐预训练；Stage 2结合对比学习、MiniLM cross-encoder蒸馏和FLOPS稀疏正则（query/doc分别λ=0.05/0.04）进行检索微调。

**关键实验**
- MS MARCO Dev MRR@10=0.408，接近Lion-sp的0.410，超过SPLADE++的0.383；BEIR六数据集平均NDCG@10=50.3，优于SPLADE++的48.2，ArguAna等数据集有统计显著提升。
- 效率：最终平均L0=182，索引13GB，端到端延迟约90ms/query；相比Lion-sp存储降6.4倍、延迟降11倍以上，与BERT稀疏模型保持同一数量级。
- 消融：Stage 1让索引条目减少40.7%（72.10M→42.72M），平均每篇激活词从355.46降到210.62，MRR@10从0.3619提升到0.3998。

**最值得记住的一句话**：用SPLADE anchor的动态α-truncation作为监督，可以让LLM在保持强效果的稀疏约束下，将L0压到182，索引和延迟数量级降至可生产部署水平。
