---
title: 'MESH: Scaling Up Retrieval with Heterogeneous Content Unification'
title_zh: MESH：通过异质内容统一扩展检索规模
authors:
- Jiaxing Qu
- Yilin Chen
- Junpeng Hou
- Jinfeng Rao
- Olafur Gudmundsson
- Sai Xiao
- Huizhong Duan
arxiv_id: '2607.12392'
url: https://arxiv.org/abs/2607.12392
pdf_url: https://arxiv.org/pdf/2607.12392
published: '2026-07-14'
collected: '2026-07-15'
category: RecSys
direction: 异质内容统一检索 · 尺度优化
tags:
- heterogeneous retrieval
- scaling bias
- gated bias correction
- modular architecture
- fresh item retrieval
- Pinterest
one_liner: 提出模块化门控偏置校正框架MESH，缓解多内容层级检索中的扩展偏置，大幅提升稀疏内容召回能力
practical_value: '- **异质内容分域建模**：将不同曝光频次的内容（爆款、长尾、冷启动）划分独立特征域，通过域隔离减少高频信号对低频信号梯度更新的干扰。电商推荐中可针对新品、长尾商品设置专属子塔或门控单元，避免被爆品淹没。

  - **门控偏置校正单元**：在上层融合前引入可学习的门控偏置，自动校准不同域的输出置信度，缓解冷门 item 在打分时被系统性低估的问题。可直接嵌入现有双塔或多塔的融合层。

  - **稀疏 item 缩放指数提升14×**：该方法显著改善新鲜物品的长尾分布拟合，线上新鲜 repin 提升5.5%，证明长尾内容也能从模型容量增长中受益。适用于电商新品冷启、UGC内容推荐等场景。

  - **异步 Serving 提升吞吐2.87×**：模块化设计天然支持异步执行，稀疏分量可延迟更新或复用缓存，降低在线延时。对需要多路召回融合的大规模系统，可作为工程优化参考。'
score: 9
source: arxiv-cs.IR
depth: abstract
---

**动机**：大规模检索系统常维护多种专用模型来覆盖不同内容层级（新鲜、长尾、爆款），导致架构碎片化。根本挑战是“异质扩展偏置”：模型容量增长带来的收益在不同内容层级上不均衡，稀疏内容几乎无法受益。

**方法**：提出MESH框架，通过模块化架构与门控偏置校正实现统一检索。核心做法：将特征空间按内容域（如新鲜度、互动量）分割为独立子域，每个域拥有独享的参数路径，避免高曝光特征的梯度主导；在各域输出后引入门控偏置单元，动态校准置信度，再聚合为通用表征。这种结构归纳偏置有效保护了稀疏信号的梯度路径，缓解扩展偏置。

**结果**：离线实验中，新鲜物品的幂律缩放指数提升14倍。在Pinterest十亿级物品-物品推荐系统上线后，新鲜物品 repin 提升+5.5%，漏斗效率提升55%，用户留存+0.46%；异步服务策略使系统吞吐提升2.87倍。
