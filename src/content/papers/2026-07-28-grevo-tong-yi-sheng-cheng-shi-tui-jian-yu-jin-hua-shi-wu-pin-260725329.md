---
title: 'Grevo: A Unified Generative Recommendation Framework with Evolutionary Item
  Indexing'
title_zh: Grevo：统一生成式推荐与进化式物品索引
authors:
- Huanjie Wang
- Liwei Guan
- Zekai Sun
- Hongwei Zhang
- Honghui Bao
affiliations:
- 北京邮电大学
- 伊利诺伊大学芝加哥分校
arxiv_id: '2607.25329'
url: https://arxiv.org/abs/2607.25329
pdf_url: https://arxiv.org/pdf/2607.25329
published: '2026-07-28'
collected: '2026-07-29'
category: GenRec
direction: 生成式推荐 · 进化式语义ID索引
tags:
- Generative Recommendation
- Semantic Identifiers
- Evolutionary Indexing
- Multitask Learning
- Posterior-driven Editing
- Semantic-Behavioral Alignment
one_liner: 用统一多任务吸收tokenizer角色，通过后验驱动的离散索引进化持续缩小语义-行为鸿沟，无需额外模型或交替优化
practical_value: '- **直接丢弃tokenizer，将SID视为可进化的离散变量**：在已上线的生成式推荐系统中，可将初始RQ-VAE量化后的SID作为热启动，后续通过后验反馈迭代修改部分SID，无需保留或重训tokenizer，大幅降低部署复杂度。

  - **BSG+SSG多任务训练可复用**：让同一个seq2seq模型同时学习“从行为序列预测物品ID”和“从物品语义嵌入重建自身ID”，两个任务共享token表征，能在不增加推理成本的前提下强化推荐效果，适用于任何基于T5或类似架构的生成式推荐模型。

  - **基于后验的离散候选生成与风险预算**：利用训练好的推荐模型计算行为似然、语义似然和跨任务一致性作为打分，从混淆邻居和低负载码本令牌中构建候选，按预算比例只修改最有风险的SID标签，工程上实现轻量、可控的索引更新，适合周期性离线优化或流式场景。

  - **进化轮次与参数设置经验**：实验表明仅需修改最后两层码本、预算比0.05、λ1=0.25、λ2=0.15 即可在3轮内收敛到最优，这些参数可直接作为电商搜索推荐中语义ID索引进化的默认起点。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：生成式推荐（GR）将召回转化为自回归生成语义标识符（SID），但主流的两阶段协议先用RQ-VAE量化内容得到冻结的SID，再训练生成式Transformer，这导致SID仅为内容重建优化，忽视用户行为模式，形成语义-行为鸿沟。端到端联合训练tokenizer和推荐器能部分弥补该鸿沟，但需要第二个可学习模型、交替优化和额外的对齐损失，训练不稳定且工程复杂。Grevo重新思考了tokenizer的角色：在GR中，tokenizer只是初始化索引的“一次性启动器”，索引本身比tokenizer更重要。因此提出将SID分配视为可进化的离散变量，利用推荐器自身的后验信号进行有预算的迭代修正，无需保留tokenizer、无需交替优化。

**方法关键点**：
- **统一多任务模型**：基于T5，同时进行行为SID生成（BSG：用户历史序列→下一物品SID）和语义SID归位（SSG：物品语义嵌入→自身SID），两个任务共享解码器和token嵌入，SSG仅激活浅层，计算开销小但能丰富token表征。
- **进化索引生命周期**：每轮先预训练BSG+SSG模型，再依次收集后验信号、枚举候选SID、评分并按预算提交最佳重分配，形成“预训练→收集→枚举→进化→重训”的闭环。
- **后验信号收集**：利用训练好的模型对每个物品计算BSG似然（在用户上下文中的平均log概率）、SSG似然（从物品语义还原的概率）以及跨任务逐层一致性分数。
- **候选生成**：只对最后两层码本中的高风险物品生成候选，候选令牌来自当前令牌、行为上混淆的邻居令牌和码本中低负载令牌，保持原词汇表和SID长度不变。
- **贪婪预算进化**：根据行为增益、语义增益和一致性增益的加权和打分，按硬预算（如ρ=0.05）选取最高分的SID进行更新，每物品每轮最多改一次，实现稳定的离散坐标下降。

**关键实验**：在Amazon Beauty/Sports/Toys三个数据集上，Grevo在TIGER和LETTER两种骨干上Recall@5/10、NDCG@5/10均稳定提升。以Beauty为例，TIGER+Grevo的R@10从0.0648升至0.0778，N@10从0.0336升至0.0412；即使仅用进化后的SID训练LC-Rec（不加入Grevo训练），也能带来明显增益，验证了索引质量本身可跨模型迁移。消融实验表明移除行为信号或语义信号均下降，去除混淆邻居候选或低负载候选也使性能显著变差。超参分析建议可变层数2、预算率0.05、SSG权重0.25、一致性权重0.15，且迭代3轮后接近收敛。

**值得记住的一句话**：**生成式推荐的瓶颈不是tokenizer，而是索引对行为信号的适配程度；通过后验驱动的离散索引进化，可以将一个固定的语义索引逐步改造成行为友好的推荐索引，无需额外模型，更简单且更稳定。**
