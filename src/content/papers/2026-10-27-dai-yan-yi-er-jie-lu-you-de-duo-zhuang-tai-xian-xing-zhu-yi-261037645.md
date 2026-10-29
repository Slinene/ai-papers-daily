---
title: Multi-State Linear Attention with Generalized Second-Order Routing
title_zh: 带广义二阶路由的多状态线性注意力
authors:
- Hee Seung Hwang
- Sanghyuk Chun
- Xindi Wu
- Olga Russakovsky
- Zhiwei Deng
affiliations:
- Princeton University
- Google DeepMind
arxiv_id: '2610.37645'
url: https://arxiv.org/abs/2610.37645
pdf_url: https://arxiv.org/pdf/2610.37645
published: '2026-10-27'
collected: '2026-10-29'
category: LLM
direction: 多状态线性注意力长上下文聚合路由
tags:
- Multi-State Linear Attention
- Linear Attention
- Second-Order Routing
- Long-Context
- Gated DeltaNet
- Mamba-2
one_liner: 提出MERLIN，用段内keys的一/二阶矩恢复query-段对齐的均值与方差，提升多状态线性注意力聚合路由
practical_value: '- 长期用户行为序列建模：若用分段线性注意力/记忆状态压缩用户历史（按会话、时间窗分段），可借鉴二阶矩路由。当前均值pooling只捕捉平均兴趣，二阶矩能捕捉段内兴趣峰值与多样性，对定位“某一次强购买意图”更准，有助于CTR/CVR预估或召回。

  - RAG/LLM生成推荐理由或广告文案：在长上下文多文档、多商品描述中，用query与段落keys的一阶+二阶矩计算相关性权重，可缓解仅基于位置或均值导致的近因偏差，让模型更均匀地利用中前段关键信息，适合检索增强生成中的证据选择。

  - 工程落地：额外缓存每段keys的一阶/二阶矩开销很小（dr=128时约4–13%内存增量，参数增量与meanpooling相当）。建议为路由使用独立的key/query投影（shared-KQ会明显掉点），并采用可学习gate混合均值/方差项，而非固定系数。

  - 注意该方法需要mid-training将单状态backbone转为多状态，无法即插即用；如果业务已有长序列记忆或State Space模型，可将其作为继续预训练阶段加入。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
自注意力二次复杂度限制长序列LLM扩展。线性注意力将KV cache压缩为固定状态，但单状态容量有限。多状态线性注意力（MSLA）分段压缩，但现有聚合权重仅使用位置或mean alignment（一阶矩），忽略对齐的方差。方差能区分“少数尖锐相关key”和“普遍弱相关”，对定位关键段至关重要。

**方法关键点**
- 将上下文均匀分段（m=256），每段维护主记忆状态S_{C_i}（Gated DeltaNet或Mamba-2 SSD recurrence）。
- 额外维护每段keys的一阶矩μ_i（均值向量）和二阶矩Σ_i（未中心外积均值），使用独立投影k'、q'（维度d_r=128，远小于主d）。
- 对当前token，计算每段对齐均值r_μ=μ_i^T q'_t 和方差r_Σ=q'^TΣ_i q' - (r_μ)^2。
- 聚合权重λ_t,i = γ_t softmax_i(τ_μ r_μ) + (1-γ_t) softmax_i(τ_Σ r_Σ)，γ_t由hidden state投影，τ为可学习温度。
- 与softmax attention的段级分组证据：log-evidence的cumulant展开中前两项正是均值和方差，所以该路由近似段级softmax。
- 训练：将预训练单状态模型（Gated DeltaNet-1.3B, Mamba-2-780M）继续预训练/mid-training 2B tokens（LDC + RULER NIAH/QA增强）转为多状态。

**关键结果**
- RULER 16K NIAH/QA：GDN平均62.7（vs Meanpool 57.9, Position 54.6），Mamba-2 76.2（vs 71.2, 69.6）。
- LongBench 16K：GDN 21.9（+13.5% vs Meanpool），Mamba-2 20.6（+12.0%）。
- 在HELMET TriviaQA上，位置控制检索显示MERLIN保持高准确且几乎不受gold passage位置影响，消除recency bias。
- m=256时MERLIN超过m=64（4x内存）的Meanpool/Position；额外缓存开销GDN≤12.6%，Mamba-2≤4.2%。

**最值得记住的一句话**：路由聚合的权重应同时编码query-段对齐的均值与方差，用独立低维key/query投影维护每段一/二阶矩即可在极小开销下显著提升长上下文检索与理解。
