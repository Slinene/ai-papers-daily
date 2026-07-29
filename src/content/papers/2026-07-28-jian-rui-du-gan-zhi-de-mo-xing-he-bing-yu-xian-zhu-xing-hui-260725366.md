---
title: Sharpness-aware Model Merging with Salience Recovery for LLM-based Cross-Domain
  Sequential Recommendation
title_zh: 尖锐度感知的模型合并与显著性恢复：面向LLM跨域序列推荐
authors:
- Huwei Ji
- Jiajie Su
- Yuyuan Li
- Xiaohua Feng
- Chaochao Chen
affiliations:
- Zhejiang University
- Hangzhou Dianzi University
arxiv_id: '2607.25366'
url: https://arxiv.org/abs/2607.25366
pdf_url: https://arxiv.org/pdf/2607.25366
published: '2026-07-28'
collected: '2026-07-29'
category: GenRec
direction: 生成式跨域推荐 · Sharpness-aware模型合并
tags:
- Sharpness-aware
- Model Merging
- Cross-Domain Sequential Recommendation
- LoRA
- Salience Recovery
- Flat Minima
one_liner: 提出SharpRec，用平坦最小值对齐和重尾分布恢复解决LLM跨域推荐的参数干扰与性能饱和
practical_value: '- **跨域LoRA合并的“平坦化”训练**：在电商多场景（如服饰→美妆）做LoRA微调时，引入sharpness-aware目标（式7），让各域权重主动趋向平坦损失盆地，可大幅减少合并后的负迁移，避免异购场景相互覆盖。

  - **后融合非线性重参数化**：合并多个领域LoRA后，对聚合参数施加元素级非线性变换（式12）恢复重尾分布，能有效激活被平均化淹没的领域专家特征，适用于多域融合后性能天花板被线性聚合锁定的业务。

  - **轻量级实现**：SharpRec无需改动推理架构，只需在微调和合并阶段加入SGA正则化和PSA变换，计算开销小，可直接嵌入现有LoRA微调流水线，适合大规模推荐系统快速迭代。

  - **鲁棒的非重叠用户场景**：在稀疏重叠用户（低至20%）下仍显著优于传统CDSR方法，为电商冷启动或新域扩展提供了更可靠的跨域知识迁移方案。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
现有LLM跨域序列推荐（CDSR）虽通过语义推理缓解了对重叠用户的依赖，但流行的模型合并范式（如直接平均LoRA参数）暴露两大瓶颈：① 跨域知识冲突——异购领域合并时参数几何不相容导致负迁移；② 多域融合性能饱和——线性聚合使参数分布趋于高斯，抹平了关键偏好信号。该工作通过实验证实，冲突源于微调后模型陷入尖锐极小值且参数向量非正交，饱和源于统计均值化。

**方法关键点**
- **Sharpness-aware Geometric Alignment (SGA)**：在单域LoRA优化中加入对抗扰动，迫使模型收敛到平坦极小值，使各域参数处于几何连通的低损盆地，从根源消除合并时的参数干扰（Ch1）。
- **Preference Salience Activation (PSA)**：对线性合并后的参数先注入噪声解耦，再通过带非线性因子的重参数化（式12）将分布从高斯重塑为重尾，恢复被平均化的高幅值显著参数，突破多域融合的性能上限（Ch2）。
- 理论证明：合并干扰误差上界由域差异与损失尖锐度相乘决定（定理4.1），PSA能增大函数空间覆盖度（定理4.2）。

**关键结果**
- 在Amazon 7个域的双域/多域实验中，SharpRec显著超越SOTA：如Book→Movie HR@3达80.13（LLM4CDSR为62.34），Sport→Toy NDCG@3达63.88（WeaveRec为43.52）。
- 多域扩展实验：在Food域，合并7个源域后NDCG@5持续增长至0.52+（WeaveRec仅0.38且饱和），提升超+51.4%。
- 消融显示，去除SGA导致Sport→Toy NDCG@3骤降至0.4564（完整0.6388），去除PSA亦有明显下降。
- 对用户重叠比例鲁棒：20%重叠下NDCG@5仍领先，传统方法则大幅滑坡。
