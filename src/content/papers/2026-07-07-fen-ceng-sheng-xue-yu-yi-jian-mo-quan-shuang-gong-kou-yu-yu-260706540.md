---
title: 'Hierarchical Acoustic-Semantic Modeling: Modality Separation and Semantic
  Coherence for Full-Duplex SLMs'
title_zh: 分层声学-语义建模：全双工口语语言模型的模态分离与语义一致性
authors:
- Zhenyu Liu
- Yunxin Li
- Xuanyu Zhang
- Qixun Teng
- Shenyuan Jiang
- Haolan Chen
- Minjun Zhao
- Fanbo Meng
- Yu Xu
- Yancheng He
affiliations:
- Harbin Institute of Technology, Shenzhen
- Center for Language, Intelligence and Machines, Shenzhen
- The Chinese University of Hong Kong, Shenzhen
arxiv_id: '2607.06540'
url: https://arxiv.org/abs/2607.06540
pdf_url: https://arxiv.org/pdf/2607.06540
published: '2026-07-07'
collected: '2026-07-08'
category: Multimodal
direction: 多模态学习 · 梯度冲突解耦
tags:
- modality interference
- gradient conflict
- full-duplex SLM
- hierarchical parameter separation
- semantic coherence
- speech-language model
one_liner: 揭示全双工语音模型中声学与语义的梯度冲突，并提出分层参数分离策略以消除模态干扰
practical_value: '- **多模态搜索/推荐中的梯度冲突诊断**：当商品文本、图像、用户行为等多模态信息共享底层参数时，可借鉴论文的梯度冲突分析方法，定量评估不同模态梯度方向的余弦相似度，定位干扰源，避免盲目调整结构。

  - **分层参数分离策略用于多模态融合**：在深层网络中将不同模态的参数解耦，仅浅层共享，同时引入轻量语义对齐通道（如对比损失或跨注意力），既能保持模态特异性，又能防止语义割裂，适用于多模态排序或召回模型。

  - **语音购物助手的全双工流畅性提升**：构建对话式推荐Agent时，采用类似分层声学-语义解耦的架构，可减少语音识别与语义理解之间的干扰，提升交互的自然度和响应速度，类似方法也适用于实时多轮对话场景。

  - **高效推理兼顾模态专化**：通过仅在深层分离参数而非独立训练整个双塔，能维持推理效率，适合对延迟敏感的业务场景，如在线推荐、语音搜索等。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：全双工口语语言模型（SLM）同时处理声学信号和语义理解，但共享参数导致严重的模态干扰，造成语义知识退化和交互不自然。本文通过细粒度优化动态分析，首次揭示其根因：声学与语义建模在深层共享参数时存在固有的梯度冲突。

**方法**：提出Lychee-FD框架，核心是分层参数分离策略——在浅层保留共享参数以提取通用特征，在深层将声学和语义模块解耦，消除梯度冲突；同时设计专用的语义对齐通道（如跨注意力或对比学习），维持模态间的语义一致性，避免完全分离导致的信息断裂。

**结果**：在多个全双工基准上，Spoken QA准确率提升7.4%，FullDuplexBench 1.5交互流畅度提升28.5%，且推理效率无损失。首次从梯度冲突角度阐明干扰机制并给出优雅解决方案。
