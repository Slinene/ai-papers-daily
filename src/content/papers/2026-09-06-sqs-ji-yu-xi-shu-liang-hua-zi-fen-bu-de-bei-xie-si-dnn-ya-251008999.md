---
title: 'SQS: Bayesian DNN Compression through Sparse Quantized Sub-distributions'
title_zh: SQS：基于稀疏量化子分布的贝叶斯 DNN 压缩
authors:
- Ziyi Wang
- Nan Jiang
- Guang Lin
- Qifan Song
affiliations:
- Purdue University
- University of Texas at El Paso
arxiv_id: '2510.08999'
url: https://arxiv.org/abs/2510.08999
pdf_url: https://arxiv.org/pdf/2510.08999
published: '2026-09-06'
collected: '2026-09-10'
category: Training
direction: 模型压缩 · 贝叶斯变分推断
tags:
- Bayesian compression
- pruning
- quantization
- spike-and-slab
- GMM
- variational inference
one_liner: 用 spike-and-slab 先验与高斯混合模型统一贝叶斯剪枝与量化，压缩率更高且精度损失相当
practical_value: '- **统一压缩替代两阶段**：电商/广告排序塔及 LLM-based reranker 对推理延迟和内存敏感，可借鉴 SQS
  把稀疏化和量化作为同一个变分学习问题，避免先剪枝再量化带来的误差累积；对 embedding 层、FFN 层可分别设置稀疏率和码本宽度。

  - **可微的先验/近似方案**：spike-and-slab 先验天然支持非结构化剪枝，GMM 后验提供量化码本均值，整体保持可微优化；工程落地时可用更轻量的近似替代复杂积分。

  - **面向 LLM 部署可迁移**：论文在 Llama3.2、Qwen2.5 上验证，说明适合本地部署的 embedding 模型、轻量生成式推荐模型；可按层或
  token 粒度做联合压缩，降低 CPU/边缘推理成本。

  - **注意**：低 bit 量化依赖硬件算子和量化校准，需结合 TensorRT/ONNX 等推理框架；论文偏学术方法，业务收益还需线上延迟和精度实测。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：DNN 部署到资源受限设备需要压缩，但主流方法将剪枝和低 bit 量化独立执行，往往为了控制精度损失而牺牲压缩率。

**方法关键点**：提出 SQS（Sparse Quantized Sub-distributions），用 spike-and-slab 先验同时诱导权值稀疏化，并将量化权重建模为高斯混合模型（GMM），从而构建统一的贝叶斯变分学习框架。由于含 spike-and-slab 先验与 GMM 的目标不可解，作者推导了高效近似，保证压缩过程对精度影响最小；同时给出变分方法收敛到稀疏、量化 DNN 的一致性理论。

**关键结果**：在 ResNet、BERT-base、Llama3.2、Qwen2.5 等模型上实验，SQS 相比现有剪枝、量化及组合基线达到更高压缩率，同时性能下降保持在可比范围。
