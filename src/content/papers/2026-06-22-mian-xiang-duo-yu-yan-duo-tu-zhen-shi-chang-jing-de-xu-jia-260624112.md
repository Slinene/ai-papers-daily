---
title: 'ReMMD: Realistic Multilingual Multi-Image Agentic Verification for Multimodal
  Misinformation Detection'
title_zh: 面向多语言多图真实场景的虚假信息检测基准与持久记忆Agent
authors:
- Chenhao Dang
- Dantong Zhu
- Jun Yang
- Conghui He
- Weijia Li
affiliations:
- Shanghai Jiaotong University
- Shanghai Artificial Intelligence Laboratory
- Tsinghua University
- Central South University
- China Electronics Technology Group Corporation 15th Research Institute
arxiv_id: '2606.24112'
url: https://arxiv.org/abs/2606.24112
pdf_url: https://arxiv.org/pdf/2606.24112
published: '2026-06-22'
collected: '2026-06-25'
category: Other
direction: 多模态虚假信息检测与Agent验证
tags:
- misinformation detection
- multimodal
- agentic verification
- multilingual
- persistent memory
- benchmark
one_liner: 提出包含多语言多图基准和持久记忆Agent的验证框架，五类真实性判别最优且成本降低17.5–79.9%
practical_value: '- 在广告/商品内容审核中，可借鉴 ReMMD-Agent 的“原子主张分解+证据集构建”策略，将多模态内容拆解为独立可验证点，并行收集证据，提升复杂虚假信息的检出效率。

  - 持久记忆设计（reusable evidence set）可避免对同一证据重复搜索，适合需持续校验的大规模商品库或 UGC 内容，显著降低大模型 API 调用成本。

  - 结构化输出 L1/L2/L3（真实性/失真类型/理由）可直接作为风控或搜索排序的中间特征，为推荐系统过滤低质或不实内容提供可解释信号。

  - 多语言与交叉语言支持可直接应用于跨境电商场景，统一处理不同语言下的商品图文真实性验证，无需为每种语言单独开发模型。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有虚假信息检测基准大多局限于单图、短文本、二分类标签，不匹配真实社交媒体帖子的多语言、多图、混合出处与细微图文错位等复杂场景，而且基于 Agent 的验证在现实证据检索下成本过高。

**方法关键点**：
- 构建 ReMMDBench 基准，含 500 个真实样本、2756 张图片，覆盖 5 种单语言及跨语言设定、三档文本长度（短/中/长）、五类真实性标签和八类失真标签，附带证据来源与推理理由。
- 提出 ReMMD-Agent 验证器，采用持久记忆机制：将帖子分解为原子事实点，对每个点搜索证据并存储在可复用证据集中，最后综合预测三层结构化输出（L1 真实性、L2 失真类型、L3 理由），避免重复搜索降低成本。

**关键结果**：用 GPT‑5.2 驱动时，ReMMD‑Agent 在五类真实性判别上准确率达 41.80%，宏 F1 为 39.12%，相比 MMD‑Agent 和 T2‑Agent 成本分别下降 17.5% 和 79.9%。
