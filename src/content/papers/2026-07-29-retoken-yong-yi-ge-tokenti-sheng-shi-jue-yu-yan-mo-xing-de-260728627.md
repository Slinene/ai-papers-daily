---
title: 'ReToken: One Token to Improve Vision-Language Models for Visual Retrieval'
title_zh: ReToken：用一个Token提升视觉语言模型的长视觉检索
authors:
- Yao Xiao
- Reuben Tan
- Zhen Zhu
- Yuqun Wu
- Jianfeng Gao
- Derek Hoiem
affiliations:
- University of Illinois at Urbana-Champaign
- Microsoft Research
- Google DeepMind
arxiv_id: '2607.28627'
url: https://arxiv.org/abs/2607.28627
pdf_url: https://arxiv.org/pdf/2607.28627
published: '2026-07-29'
collected: '2026-07-31'
category: Multimodal
direction: 多模态视觉检索 · 稀疏Token选择
tags:
- Vision-Language Models
- Visual Retrieval
- KV Cache
- Sparse Token Selection
- Long Video Understanding
one_liner: 用单个可学习Token从视觉KV缓存中检索稀疏相关token，大幅提升长视觉上下文中的问答准确率
practical_value: '- 电商场景中处理商品多图或视频描述时，可利用可学习检索Token从大量视觉特征中快速定位与用户查询相关的帧/区域，提升问答或推荐理由生成的质量。

  - 利用预填充的KV缓存和稀疏选择机制，避免每次查询都重新处理所有视觉token，大幅降低多模态推荐的推理延迟和显存占用，适合线上服务。

  - 轻量级设计（单个token，单卡训练）表明，小型Query-Image数据集即可训练出有效的检索能力，可迁移到商品视觉问答或视觉搜索中。

  - 该方法本质是条件特征选择，可扩展到用户行为序列（如视频浏览记录）中，用学习到的Token从长序列中检索相关历史行为，增强推荐模型而无需输入完整序列。'
score: 7
source: huggingface-daily
depth: abstract
---

## 动机
长视觉上下文（如图集、长视频）中，多模态大模型的性能随干扰增加而严重退化，全量处理所有视觉token在GPU内存上不可行。现有注意力机制无法有效定位查询相关的帧（图1a Recall@1仅5.1%）。

## 方法
提出**ReToken**，一个可学习嵌入向量，作为显式检索目标。它从预填充的视觉KV缓存中，通过计算与查询token的相似度，选择每个注意力头前k个最相关的视觉token，形成稀疏子集。后续层仅处理这些选中token，大幅减少计算量和无关干扰。ReToken仅在一个小型图像QA数据集（约140万样本）上对比学习训练，要求检索结果与真实相关帧一致。

## 结果
在Visual Haystacks基准上，Qwen3VL-8B提升13.4点，InternVL3.5提升12.4点（相对提升>20%）。在LVBench长视频理解上零样本迁移带来8.0点增益。训练和推理均在单张H100完成。ReToken在最后一层的检索召回率是注意力方法的3倍以上（图1b 18.4% vs 5.1%），有效解决长序列关键帧定位问题。
