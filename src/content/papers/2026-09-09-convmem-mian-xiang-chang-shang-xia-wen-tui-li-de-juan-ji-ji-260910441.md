---
title: 'ConvMem: Convolutional Memory for Long-Context Reasoning'
title_zh: ConvMem：面向长上下文推理的卷积记忆框架
authors:
- Hongming Zhang
- Zhaozhen Gu
- Fengshuo Bai
- Ming Hao
- Qingyang Zhang
- Yuanyuan Wang
- Shiyang Tang
- Yanna Wang
- Bo Xu
affiliations:
- Institute of Automation, Chinese Academy of Sciences
arxiv_id: '2609.10441'
url: https://arxiv.org/abs/2609.10441
pdf_url: https://arxiv.org/pdf/2609.10441
published: '2026-09-09'
collected: '2026-09-10'
category: Reasoning
direction: 长上下文推理 · 卷积记忆
tags:
- Long-context
- Reasoning
- LLM
- Memory
- Parallelization
- Training-free
one_liner: 将长上下文推理重构为分层卷积，训练免费、高度并行，缩短推理链为对数树
practical_value: '- 超长用户行为序列建模：可借鉴其分层卷积思路，将用户长期行为、浏览/点击序列分段，用 LLM 以当前 query 为卷积核做树状摘要，降低顺序读取延迟。

  - 多意图查询分解：Multi-Kernel Convolution 把复杂 query 拆成多个语义通道并行处理，适合电商搜索中多意图识别与召回融合。

  - 训练免费外挂记忆：无需强化学习微调，可作为独立 memory 组件接入现有 LLM API，避免在特定数据集上过拟合，利于快速落地。

  - 工程并行优化：Configurable Strides 和 Skip Connections 支持对多个文本段批量 summary，适合长文档 RAG、商品详情/评论聚合等场景的
  GPU 并行加速。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：LLM 处理超长上下文受固定窗口限制，自注意力二次复杂度带来高延迟；顺序更新 memory 的方法（如 MemAgent）需昂贵 RL 训练且易过拟合特定数据集。

方法：ConvMem 训练免费，把长上下文推理重构成分层卷积。LLM 以特定 query 为卷积核，对文本段进行分层摘要，将线性推理链缩短为对数树。引入 Configurable Strides 和 Skip Connections 增强证据捕获与传播，Multi-Kernel Convolution 将复杂 query 分解为解耦语义通道。该设计降低错误累积，并在文本段和推理线程两个维度实现大规模并行。

结果：在 RULER-HotpotQA 和 RULER-2WikiMultiHopQA 上，ConvMem 优于训练免费基线，且在分布外任务上避免了 RL 训练模型的参数先验过拟合风险。
