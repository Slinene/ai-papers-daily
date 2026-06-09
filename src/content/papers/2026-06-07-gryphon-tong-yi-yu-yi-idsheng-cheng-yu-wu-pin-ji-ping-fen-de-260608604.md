---
title: 'Gryphon: A Unified Architecture for Semantic-ID Generation and Item-Level
  Scoring in Industrial Recommendations'
title_zh: Gryphon：统一语义ID生成与物品级评分的生成式推荐架构
authors:
- Daria Tikhonovich
- Oleg Sorokin
- Vladislav Dodonov
- Mariia Ulianova
- Ilya Murzin
affiliations:
- Yandex
arxiv_id: '2606.08604'
url: https://arxiv.org/abs/2606.08604
pdf_url: https://arxiv.org/pdf/2606.08604
published: '2026-06-07'
collected: '2026-06-09'
category: GenRec
direction: 生成式推荐 · Semantic ID · item-level scoring
tags:
- Generative Retrieval
- Semantic ID
- Item-Level Scoring
- Encoder-Decoder
- Collision Resolution
- Industrial Recommendation
one_liner: 在生成式检索中引入联合训练的物品级评分模块，解耦beam likelihood与最终排序，解决SID碰撞和得分失校准
practical_value: '- **用beam search做ID候选生成，再加一个轻量级评分器重排序**：工程上可复用的架构模式，beam likelihood仅用于控制候选池入口，最终排序由Item-Level
  Scoring Module（ILSM）接管，避免beam失校准影响回召；尤其适合SID碰撞严重的动态目录场景。

  - **ILSM复用编码器用户状态，成本极低**：只需一层用户-物品交叉注意力+MLP，几乎不增加推理耗时，可直接集成到现有生成式检索模型中。

  - **联合训练目标：生成损失 + 带流行度纠正的next-item prediction损失**：共享编码器，使同一用户表示同时支持SID质量与物品级相关性，训练稳定，可推广到多目标优化。

  - **在线A/B证明单一生成式模型可替代复杂多路召回**：Gryphon取代了15+候选源与预排序，候选量从3000降至1000，核心指标持平，大幅降低系统复杂度和运维成本，对电商推荐系统多路融合极有参考价值。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
生成式检索（GR）通过自回归生成语义ID（SID）进行召回，但beam search优化的序列似然**不等于**物品级推荐质量。两个典型问题：① beam搜索时前缀误差累积导致序列似然失校准，无法准确反映物品相关性；② 多个物品共享同一SID时，beam score完全一致，无法区分其真实偏好。两者共同指向同一缺陷：排序是在SID序列上完成的，而业务需要的是物品排序。  

**方法关键点**  
- **Gryphon统一架构**：编码器-解码器GR + 物品级评分模块（ILSM），二者共享编码器输出的用户状态 \\(E_u\\)。  
- **ILSM设计**：基于item-id等特征通过物品塔得到 \\(e_i\\)，再用轻量交叉注意力+MLP头输出标量分 \\(r_\phi(u,i)\\)。  
- **训练**： \\(\mathcal{L}_{gen}\\)（SID自回归交叉熵） + \\(\lambda \mathcal{L}_{NIP}\\)（采样softmax的下一物品预测，含logQ流行度纠正），迫使编码器同时支持ID生成与物品评分。  
- **推理**：beam search生成SID候选集，解析出所有对应物品，ILSM对物品打分后取TopN，完全丢弃beam likelihood用于排序。  

**关键实验**  
- 数据集：某大规模音乐推荐平台一周日志，千万级用户和物品。  
- 基线：生产级自回归双塔ARGUS、Vanilla GR、带冲突消除的Vanilla GR Resolved。参数量与推理耗时近似控制。  
- 离线结果：Gryphon在Recall@1000上达到0.8552，分别比Vanilla GR和Resolved GR提升**+3.7%**和**+2.5%**；对同一beam候选池，ILSM重排后的item-level Recall比beam likelihood排序高出**+4.2%**，且**超过了SID-level beam ceiling**（0.8404），直接证明beam失校准限制了可召回物品。  
- 7天在线A/B：Gryphon作为唯一候选源，替代15+候选生成器和预排序，候选量从10,000→1,000（传递至精排仅1,000），总听歌时长无显著变化(+0.25%)，活跃用户比+0.43%，未完成播放降低-1.3%，核心体验持平的同时大幅简化管线。  

**最值得记住的一句话**  
GR架构中，beam search仅应被看作ID级候选生成工具，最终物品排序必须交给一个联合训练的物品级评分器，才能化解beam失真与SID碰撞，同时在工业场景中安全地做减法。
