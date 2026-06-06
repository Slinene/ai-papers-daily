---
title: Multimodal Music Recommendation System using LLMs
title_zh: 基于LLM的多模态音乐推荐系统
authors:
- Srikar Prabhas Kandagatla
- Sreehitha R. Narayana
- Chandana Magapu
- Swetha Mohan
- Shamanth Kuthpadi
- Hongjie Chen
- Ryan A. Rossi
- Franck Dernoncourt
- Nesreen Ahmed
affiliations:
- University of Massachusetts
- Dolby Laboratories
- Adobe Research
- Cisco Research
arxiv_id: '2606.00125'
url: https://arxiv.org/abs/2606.00125
pdf_url: https://arxiv.org/pdf/2606.00125
published: '2026-05-27'
collected: '2026-06-06'
category: RecSys
direction: 多模态序列推荐 · LLM增强
tags:
- Multimodal
- Music Recommendation
- LLM
- Sequential Recommendation
- E4SRec
one_liner: 在序列推荐框架中融合音频、歌词、LLM语义元数据与听歌完成率，大幅提升召回与NDCG
practical_value: '- 电商场景可借鉴多模态商品表示：用预训练模型提取商品图像、标题等特征，拼接或交叉注入序列推荐模型，简单涨点明显。

  - LLM生成结构化语义标签（如风格、场景）可作为额外的文本特征，类似商品属性扩展，在冷启或稀疏交互下尤其有效。

  - 注意多模态融合并非简单拼接就能叠加收益，文中发现朴素融合可能不增反降，实践中需探索交叉注意力或门控机制。

  - 利用行为强度信号（如停留时长、转化率）替代二元交互，能提供更丰富的用户兴趣强度信息，改进序列建模。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有音乐推荐系统仅将歌曲视为ID，忽略丰富的音频、歌词等语义内容，且缺乏统一LLM框架同时建模语义、声学和行为强度。

**方法**：基于E4SRec序列推荐框架进行扩展，在LastFM-1K数据上补充三路信号：（1）用预训练音乐和文本模型提取音频与歌词嵌入；（2）用LLM按MGPHot schema生成结构化语义元数据；（3）听歌完成比率作为交互强度。框架支持SASRec、BERT4Rec、GRU4Rec等多种ID编码器，LLM主干可选LLaMA-2-13B、Qwen2.5-7B-Instruct、LLaMA-3-70B，在zero-shot和微调两种设定下评估。

**结果**：融合内容特征后，Recall@20最高提升95%，NDCG@20最高提升79%，显著优于纯ID基线。但简单多模态拼接并非总是带来叠加提升，部分融合出现性能下降，表明跨模态集成仍需精心设计。同时发布大规模多模态音乐推荐基准数据集。
