---
title: 'Little Brains, Big Feats: Exploring Compact Language Models'
title_zh: 小模型大作为：探索紧凑语言模型在 RAG 生成阶段的潜力
authors:
- Dari Baturova
- Elena Bruches
- Ivan Chernov
- Roman Derunets
- Arsenii Fomin
- Andrey Kostin
affiliations:
- Siberian Neuronets LLC, Novosibirsk, Russia
arxiv_id: '2606.30062'
url: https://arxiv.org/abs/2606.30062
pdf_url: https://arxiv.org/pdf/2606.30062
published: '2026-06-28'
collected: '2026-07-02'
category: RAG
direction: 小型语言模型 RAG 生成器基准与设备端部署
tags:
- SLM
- RAG
- on-device
- benchmarking
- efficiency
- generation
one_liner: 系统评估小型语言模型在 RAG 生成器的表现，证明其可在无 GPU 的设备端合理时间运行
practical_value: '- **低成本 / 边缘端 RAG 部署**：在电商客服、商品问答等场景，可用 SLM 替代 LLM 作为生成器，直接运行在智能终端或本地服务器，避免
  GPU 成本，保障数据隐私。

  - **生成器选型 benchmark 方法**：复用其多数据集（开放/专有、不同主题与问题类型）评估框架，为业务中的 RAG  pipeline 快速筛选合适的轻量生成模型。

  - **延迟优化参考**：论文验证了 SLM 在无 GPU 硬件下的推理时间仍在可接受范围，可指导搜索推荐系统中实时类 RAG 应用（如解释性生成）的时延可行性评估。

  - **检索与生成能力解耦测试**：聚焦仅更换生成器模型的效果，类似思路可应用到推荐理由生成、广告文案自动改写等模块，独立评估不同 SLM 的文本生成质量。'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
RAG 系统通常依赖大模型（LLM）作为生成器，计算开销大，难以在预算受限或需要设备端运行的场景落地。小型语言模型（SLM）在生成阶段的实际效果与效率缺乏系统评估。

### 方法
基于开源的领域数据集和专有数据集，覆盖多种问题类型与主题，构建 RAG 基准测试。固定检索模块，仅更换不同规模的 SLM 作为生成器，评估回答质量、推理速度与资源消耗。实验关注端到端 RAG 系统在无 GPU 的普通硬件上运行的可行性。

### 关键结果
- 多个 SLM 在 RAG 生成中可获得有竞争力的回答质量。
- 整个 RAG 系统可完全运行在无 GPU 的设备上（如普通 CPU），推理时间处于秒级，满足可交互场景的需求。
- 为不同资源预算下的模型选型提供了明确的性能-效率权衡数据。
