---
title: Gradient-free Task-Conditioned Retrieval for On-Device In-Context Learning
title_zh: 面向端侧上下文学习的无梯度任务条件检索
authors:
- Xinyu Luo
- Hui Liu
- Yihua Shao
- Junyi Yang
- Arindam Basu
- Haoliang Li
affiliations:
- City University of Hong Kong
- Institute of Automation Chinese Academy of Sciences
arxiv_id: '2607.27766'
url: https://arxiv.org/abs/2607.27766
pdf_url: https://arxiv.org/pdf/2607.27766
published: '2026-07-30'
collected: '2026-08-02'
category: RAG
direction: 输出条件化的无梯度检索对齐
tags:
- In-Context Learning
- Retrieval
- Gradient-free
- Low-rank
- Multimodal
- On-device
one_liner: CoRA 利用输出信息构建条件空间，无需微调即可将冻结编码器转为任务导向检索器，支持端侧多模态示例选择
practical_value: '- **无梯度任务适配**：在推荐或搜索中，可用少量任务样本（如高转化 item 的标题或图像）构建条件空间，将已有编码器快速适配为任务专用检索器，无需重新训练或反向传播，适合快速
  A/B 测试。

  - **端侧高效检索**：低秩压缩将检索索引缩小至原始表示的 1/50~1/100，且查询时仅需输入编码和预计算索引，适合移动端或边缘设备的实时个性化推荐。

  - **多模态扩展**：可将商品图、详情描述等视觉特征纳入条件空间，直接检索多模态示例，为图文推荐或广告创意优选提供轻量方案。

  - **离线构造与双通流式处理**：采用闭式岭回归和双通算法避免储存完整拟合矩阵，可处理百万级候选集，适合大规模电商场景下构建任务条件索引。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：端侧上下文学习需要在推理前检索示例，但现有方法通常需微调检索器或依赖反向传播，计算与存储开销大，且无法充分利用任务输出信息。设备端内存和算力受限，亟需轻量、可任务适配的检索框架。

**方法**：提出 CoRA，一种无梯度框架，将冻结编码器转为任务条件检索器。核心步骤：(1) 从候选记忆中选择互补编码器层，提取输入特征；(2) 利用候选输出（如标签、回答）构建输出导出的条件空间；(3) 通过闭式岭回归将候选输入表示对齐到条件空间；(4) 对拟合矩阵做低秩分解，生成紧凑检索基，在线查询时仅需输入编码和预计算索引。推导出秩约束基是输出条件拟合表示的最优低秩压缩，并给出不实体化拟合矩阵的双通流式构建算法。框架可扩展至多模态，将视觉表示融入条件空间。

**结果**：在10个文本数据集和4个多模态基准上，搭配 Llama-3.2-1B、MobileLLM-Pro 等模型，CoRA 的检索效果媲美或超越需微调的检索器，且在树莓派 5 上成功部署。低秩分解使索引尺寸缩减至 1/50 以下，同时保持检索质量。
