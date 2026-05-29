---
title: 'GradSentry: Gradient Spectral Entropy for Backdoor Sample Filtering in Large
  Language Model Fine-Tuning'
title_zh: GradSentry：基于梯度谱熵的大模型微调后门样本过滤
authors:
- Haodong Zhao
- Tianyi Xu
- Tianhang Zhao
- Zhuosheng Zhang
- Gongshen Liu
affiliations:
- School of Computer Science, Shanghai Jiao Tong University
arxiv_id: '2605.26574'
url: https://arxiv.org/abs/2605.26574
pdf_url: https://arxiv.org/pdf/2605.26574
published: '2026-05-25'
collected: '2026-05-29'
category: Training
direction: 大模型微调安全 · 后门防御
tags:
- backdoor defense
- spectral entropy
- gradient analysis
- LoRA
- sample filtering
one_liner: 利用梯度谱熵区分后门与干净样本，无需聚类，在1%-90%投毒比例下均有效
practical_value: '- 使用不可信数据微调推荐或对话模型时，可集成 GradSentry 进行数据清洗：对每个样本计算梯度谱熵，用自动阈值过滤高熵后门样本，避免模型植入后门。

  - 方法训练无关，适用于 LoRA、Adapter 等参数高效微调，无需修改现有微调流程，可直接在梯度计算后附加过滤步骤。

  - 计算开销极低（7B 模型每样本 20-50 ms），适合大规模电商语料或用户行为数据微调前的快速扫描。

  - 无需聚类且对投毒比例鲁棒，特别适合电商场景中投毒比例未知、正负样本极不平衡的真实数据。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 微调中使用不可信数据会引入后门攻击，已有过滤防御依赖聚类，在数据不足或投毒比例极端时失效。

**方法**：提出 GradSentry，核心发现是后门样本的梯度谱熵显著高于干净样本。方法利用单样本梯度频谱捕获输出改变的后门特征，避免样本间比较和聚类，通过自动阈值分离样本。

**关键结果**：
- 在 4 个 QA 数据集和 4 种攻击上，GradSentry 能有效区分后门样本，自动阈值接近最优 F1。
- 对 LoRA 和全参数微调均适用，计算开销极小（7B 模型每样本 20–50ms）。
- 在 1%–90% 投毒比例下均保持高检测率，无需调整阈值。
