---
title: 'NGM: A Plug-and-Play Training-Free Memory Module for LLMs'
title_zh: NGM：即插即用、无需训练的LLM记忆模块
authors:
- Yuwen Qu
- Wenhui Dong
- Chenyang Si
- Caifeng Shan
affiliations:
- Nanjing University
arxiv_id: '2605.16893'
url: https://arxiv.org/abs/2605.16893
pdf_url: https://arxiv.org/pdf/2605.16893
published: '2026-05-15'
collected: '2026-05-20'
category: LLM
direction: LLM记忆增强 · 训练无关即插即用
tags:
- N-gram Memory
- Training-Free
- Plug-and-Play
- LLM
- Cosine Gate
- Knowledge Injection
one_liner: 提出训练无关的N-gram记忆模块，通过平均token嵌入构建表示并用余弦门控注入，显著提升代码和知识密集型任务性能。
practical_value: '- 电商搜索/推荐中，商品标题、品牌、规格等高频短语可利用N-gram缓存跳过大量计算，直接注入LLM的表示层，提升推理速度与事实准确性。

  - 在多轮对话Agent中，可将用户重复提到的实体或结构化信息（如订单号、地址）通过NGM快速恢复，减少遗忘和重复生成。

  - 完全无训练，即插即用，无需修改骨干模型权重或增加可学习参数，适合快速A/B测试和已有模型的无损增强。

  - 余弦相似度+ReLU的门控机制简单高效，可作为其他知识注入场景（如检索增强生成）中轻量级融合模块的设计参考。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM在处理命名实体、重复短语、固定搭配等局部模式时，仍需通过完整的注意力与FFN计算，效率低下。现有条件记忆模块虽能显式存储知识，但依赖可学习的记忆嵌入，需要额外训练且灵活性受限。

**方法**：提出 **N-gram Memory (NGM)**，一个无训练、即插即用的模块，包含两个组件：
- **因果N-gram编码器**：直接对骨干模型的预训练token嵌入取滑动窗口平均，动态构建N-gram表示，无需额外记忆表或检索流程，完全基于已有嵌入。
- **余弦门控记忆注入器**：用当前上下文与N-gram表示的余弦相似度计算门控值，经ReLU截断后，将检索到的N-gram嵌入调制进原始表示，实现非参数化的自适应融合。

**关键结果**：在Qwen3系列（0.6B~14B）的8个基准上，NGM使平均性能提升0.5~1.2个点，尤其对代码生成（LiveCodeBench +3.0）和知识密集型任务（GPQA +3.03）增益显著；多模态模型Qwen3-VL-2B在MMStar上提升1.53个点。
