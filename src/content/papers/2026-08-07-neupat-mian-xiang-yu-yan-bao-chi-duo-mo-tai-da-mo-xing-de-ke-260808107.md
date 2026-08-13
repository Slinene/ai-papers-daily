---
title: 'NeuPAT: Neuron-aware Plasticity Allocation Tuning for Language-Preserving
  MLLMs'
title_zh: NeuPAT：面向语言保持多模态大模型的神经元可塑性分配调优
authors:
- Jiayue Jin
- Jingwei Zhang
- Chen Wang
- Jing Liu
- Longteng Guo
affiliations:
- Fudan University
- Zhongguancun Academy
- Institute of Automation, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- Tianjin University
arxiv_id: '2608.08107'
url: https://arxiv.org/abs/2608.08107
pdf_url: https://arxiv.org/pdf/2608.08107
published: '2026-08-07'
collected: '2026-08-13'
category: Multimodal
direction: 多模态大模型 · 神经元可塑性约束
tags:
- MLLM
- Neuron Plasticity
- Language Preservation
- Multimodal Instruction Tuning
- Parameter-Efficient Tuning
one_liner: 用神经元级更新约束保护语言敏感神经元，在多模态微调中恢复94.5%语言能力下降且保持多模态性能
practical_value: '- 在微调多模态推荐/搜索模型时，可用小规模 probe 任务识别对文本理解敏感的神经元/参数，对其实施低学习率或正则，防止原
  LLM 的文本召回/相关性下降。

  - NeuPAT 的 neuron-wise 约束是轻量、架构无关的，可叠加在 LoRA/Adapter 等参数高效微调方案上，适合线上迭代：只增加少量探测成本，避免多模态训练后语义排序能力退化。

  - 类似思想可用于多任务训练（如商品文本描述生成 + 图像理解）：区分不同任务敏感神经元群体，动态分配更新幅度，缓解跨任务遗忘。

  - 若业务以纯文本 LLM 为底座接入多模态商品数据，建议在指令微调阶段加入语言能力回归目标或约束，保持语言泛化能力，防止线上 query 理解/改写质量下降。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 扩展为多模态大模型（MLLM）时常造成预训练语言智能下降，现有工作多从数据配比或参数高效微调切入，缺乏对模型内部适应动态的理解。作者发现预训练 LLM 神经元在多模态学习中呈现异质性可塑性：部分神经元对保持语言能力至关重要，另一部分则更易适应多模态知识。

**方法关键点**：提出 NeuPAT（Neuron-aware Plasticity Allocation Tuning），一个轻量、架构无关的框架。先用小规模 probing 阶段估计神经元的适应模式，区分语言敏感神经元与多模态可塑神经元；在多模态指令微调中按神经元分配更新约束：选择性保护语言敏感神经元，降低其更新幅度，同时鼓励多模态可塑神经元充分更新。该方法可叠加在任意微调架构上，不依赖特定模块。

**关键结果**：在多个 LLM 家族上，NeuPAT 在 11 个语言基准上恢复 vanilla tuning 造成的 94.5% 语言能力下降，同时保持可比的（comparable）多模态性能，验证了能力保持的有效性。
