---
title: Mellum2 Technical Report
title_zh: Mellum 2：面向高效代码助手的12B MoE模型训练与架构
authors:
- Marko Kojic
- Ivan Bondyrev
- Aral de Moor
- Joseph Shtok
- Petr Borovlev
- Kseniia Lysaniuk
- Madeeswaran Kannan
- Ivan Dolgov
- Nikita Pavlichenko
affiliations:
- JetBrains
- Constructor University, Bremen, Germany
arxiv_id: '2605.31268'
url: https://arxiv.org/abs/2605.31268
pdf_url: https://arxiv.org/pdf/2605.31268
published: '2026-05-28'
collected: '2026-06-02'
category: LLM
direction: 代码生成与推理LLM · MoE架构与训练
tags:
- MoE
- Code Generation
- Training Recipe
- Long Context
- Speculative Decoding
- RLVR
one_liner: 开源12B/2.5B活跃MoE代码模型，通过架构与训练设计在2.5B算力下达成7B级性能
practical_value: '- **MoE部署经济学**：通过64选8专家架构，总参数量12B但单token仅2.5B，推理成本可比拟7B密集模型。若在推荐系统中使用MoE，可参考其GQA+SWA+MTP的组合设计，压缩KV
  cache并利用推测解码加速。

  - **三阶段课程学习**：预训练数据从通用网页逐步切换到高质量代码/数学（代码比例23%→42%→59%），在lr decay阶段集中最干净的数据。推荐模型训练中也可借鉴：初期用大规模行为数据，后期用精选交互序列，并在lr衰减期引入高标准标注数据。

  - **长上下文扩展的层选择性YaRN**：仅对全局注意力层应用频率重映射，滑动窗口层保持原样，节省计算且有效保持长短文本性能。对于需要长序列建模的推荐场景（如用户长期行为），可尝试类似分层扩展策略，避免全量RoPE调整。

  - **RLVR避免奖励模型噪声**：用可验证奖励直接优化策略，省去奖励模型训练。在推荐中，若存在确定性的正负反馈（如购买、跳过），可构造程序化的reward函数，减少RLHF的工程成本和不确定度。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现有代码LLM分成两块——4-14B密集模型部署便宜但处理复杂任务乏力，超大MoE模型性能好但成本高。Mellum 2 希望在2.5B活跃参数的算力预算下，达到7B级别的代码与推理能力，取代自家仅做代码补全的4B密集Mellum。

**方法关键点**：
- **架构**：12B总参数，64选8 MoE，28层Transformer，隐藏维度2304，GQA（32查询头/4 KV头），在3/4的层上使用滑动窗口（窗口1024），带单个多token预测头（作为辅助任务和推测解码的草稿模型）。
- **预训练**：10.6T tokens三阶段课程→代码比例逐步上升（23%→42%→59%），Muon优化器+FP8混合精度，Warmup-Hold-Decay调度且线性衰减至零。
- **长上下文扩展**：采用层选择性YaRN，仅对全局注意力层做频率重映射，训练至117B tokens，上下文从8K升至128K。
- **后训练**：SFT+RLVR两个阶段，分出Instruct（直接回答）和Thinking（带推理轨迹）两版。RL部分使用GRPO改进版，奖励来自可验证的代码执行、数学比对等，无需奖励模型。

**关键结果**：在同类开源模型中，Mellum 2以2.5B活跃参数量，在MMLU-Pro（59.3%）、BBH（74.9%）、GSM8K（81.7%）等基准上超越部分7B密集模型，且服务时延与Qwen2.5-7B相当或更优。MTP头在105B ablation中提升HumanEval pass@1 +10.4，预示推测解码的实际加速潜力。
