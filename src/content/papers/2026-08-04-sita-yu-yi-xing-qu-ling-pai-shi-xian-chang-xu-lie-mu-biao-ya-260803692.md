---
title: 'SITA: Semantic Interest Tokens for Target-Aware Compression in Long-Sequence
  Recommendation'
title_zh: SITA：语义兴趣令牌实现长序列目标感知压缩
authors:
- Rui Zhou
- Bo Chen
- Qinglin Jia
- Jiezhou Ji
- Chaoyi Ma
- Ruiming Tang
- Hao Wang
- Enhong Chen
affiliations:
- University of Science and Technology of China
- Kuaishou Technology
arxiv_id: '2608.03692'
url: https://arxiv.org/abs/2608.03692
pdf_url: https://arxiv.org/pdf/2608.03692
published: '2026-08-04'
collected: '2026-08-05'
category: RecSys
direction: 长序列推荐 · 目标感知压缩 · 语义令牌
tags:
- Long-Sequence Recommendation
- Target-Aware Modeling
- Semantic ID
- Interest Compression
- Balanced Parallel Quantization
one_liner: 通过语义码本组织兴趣令牌，在离线压缩的全局兴趣中实现目标感知选择
practical_value: '- **语义分组压缩**：用多个并行码本将商品离散化为语义组，用户侧维护每组K个兴趣令牌并离线存储，推理时仅按商品SID选取令牌，O(BNd)复杂度，适合高并发线上服务。

  - **BPQ码本设计**：利用商品多模态特征训练并行码本，加入使用平衡正则化防止码字利用不均，可作为推荐系统语义特征编码或召回索引的通用技巧。

  - **组内独立FFN+组间偏置交互**：在保持语义分组的同时，用组间自注意力生成偏置，既保留结构又支持跨组信息融合，相比全量令牌自注意力复杂度更低（O(N^2)
  vs O((NK)^2)），适合兴趣解耦与融合场景。

  - **工程部署**：用户兴趣令牌存为KV对（UID→tokens），SID映射表存为特征，在线推理仅一次查表加轻量注意力，完全脱离原始行为序列，对时延友好。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
长序列推荐的两大范式长期对立：检索式（如SIM）会丢弃大量历史，丧失全局兴趣；压缩式（如C-Former）虽保留全局信息，但压缩后的用户表示对所有候选目标相同，无法感知目标差异。理想的方案是为每个<用户, 物品>对维护专用压缩兴趣，但存储复杂度O(|U||V|)无法落地。SITA的出发点是**用组合语义空间降低存储**，同时**在压缩兴趣中植入目标感知的选择能力**。

## 方法关键点
- **平衡并行量化 (BPQ)**：用N个专家将商品多模态嵌入投影至N个平行码本（各含K个码字），得到N维语义标识符 (SID)。训练中引入**使用平衡正则化**避免码字崩溃，将O(|U||V|)存储降为O(|U|NK)。
- **结构化兴趣压缩 (SIC)**：初始化NK个兴趣令牌，分为N组（对应N个语义组），通过堆叠块压缩行为序列。每块先做交叉注意力，再进行**组内独立SwiGLU**提取细粒度兴趣，最后通过**组级自注意力生成偏置**广播，实现跨组交互同时保持分组结构。压缩后的兴趣令牌离线存储为用户表示。
- **SID指导选择 (SGS)**：给定目标商品SID，从每组选取对应位置的兴趣令牌（共N个），经目标注意力得到**目标感知的长期兴趣**。同一组存储的令牌可支持不同目标的不同选择，实现“一次压缩，多次目标感知复用”。

## 关键结果
- **公开数据集**：在Taobao-MM和XLong上，SITA相较最强基线LONGER和C-Former，AUC分别提升3.02%和3.77%，GAUC提升1.56%和3.82%。消融实验证实移除任意组件（组内SwiGLU、组间交互、SID选择）均导致性能下降。
- **工业A/B**：在日活数亿的生产场景，SITA替换原有压缩式模块，两个场景的线上AUC/GAUC相对提升0.05%~0.08%（工业环境下0.05%即显著），验证了目标感知压缩的工程可行性。

> 最值得记住的一句话：**用并行语义码本将兴趣令牌分组存储，使离线压缩的用户表示能够通过目标商品SID动态激活对应兴趣，同时解耦长序列编码于线上推理。**
