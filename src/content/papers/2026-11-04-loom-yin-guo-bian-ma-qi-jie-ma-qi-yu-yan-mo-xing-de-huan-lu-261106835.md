---
title: 'LooM: Loop-Invariant Memory for Causal Encoder-Decoder Language Models'
title_zh: LooM：因果编码器-解码器语言模型的环路不变记忆
authors:
- Lele Yang
- Muxi Diao
- Zhonghao Yan
- Jiankang Chen
- Bin Wen
- Tingting Gao
- Wentao Zhang
- Kongming Liang
- Zhanyu Ma
- Weiran Xu
affiliations:
- Beijing University of Posts and Telecommunications
- Zhongguancun Academy
- Peking University
- Kling Team
arxiv_id: '2611.06835'
url: https://arxiv.org/abs/2611.06835
pdf_url: https://arxiv.org/pdf/2611.06835
published: '2026-11-04'
collected: '2026-11-05'
category: LLM
direction: LLM循环架构与推理预算控制
tags:
- Looped Transformers
- KV cache
- Causal Encoder-Decoder
- Dynamic Depth
- Language Modeling
one_liner: 提出LooM，在因果编码器-解码器中循环解码器层并复用一次写入的KV缓存，缓存不随循环增长，单模型覆盖3-21层执行预算
practical_value: '- 在线推理部署中，可借鉴LooM的“循环层+共享KV缓存”设计：对LLM的解码器部分层做循环复用，保持固定KV缓存，实现推理时动态扩展计算深度而不增加显存，便于在电商搜索/推荐服务中按流量压力调整算力。

  - 训练时随机采样循环次数（budget sampling）使单一模型支持多个推理深度，无需为每个深度单独训练；推荐系统中的生成式模型（如query生成、文案生成）可采用类似策略，用一个模型覆盖不同延迟/效果权衡。

  - 将深度作为部署时预算的思想可用于需要动态降级或升级的场景，例如大促期间减少循环次数保底可用，或对高价值query增加循环提升效果，而缓存和参数不变。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：Looped Transformers通过反复执行共享层增加有效深度，但存在三个限制：KV缓存随循环次数线性增长、计算只能以整块步长调整、训练后循环次数难以改变。

**方法关键点**：提出LooM，在因果编码器-解码器（CED）中仅循环第一层之后的解码器层；这些层读取每个token仅写入一次的全局记忆，每个token的KV仅在首次访问时发布，因此缓存大小与循环次数无关。各层独立循环，提供从3到21层执行预算；使用随机采样的预算训练单一模型，无需路由器即可覆盖所有预算。

**关键结果**：在相同缓存大小下，具有足够循环次数的LooM在语言建模、零样本准确率和长上下文困惑度上均超过单次基线；分析表明训练预算分布决定额外深度的收益。结论是CED是循环的自然位置，深度可视为部署时选择的预算。
