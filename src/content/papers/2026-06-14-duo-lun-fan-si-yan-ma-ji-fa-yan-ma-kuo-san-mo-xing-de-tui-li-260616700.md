---
title: Multi-Turn Reflective Masking Elicits Reasoning in Mask Diffusion Models
title_zh: 多轮反思掩码激发掩码扩散模型的推理能力
authors:
- Yanming Zhang
- Yihan Bian
- Jingyuan Qi
- Yuguang Yao
- Lifu Huang
- Tianyi Zhou
affiliations:
- University of Maryland
- Virginia Tech
- Intuit
- UC Davis
- MBZUAI
arxiv_id: '2606.16700'
url: https://arxiv.org/abs/2606.16700
pdf_url: https://arxiv.org/pdf/2606.16700
published: '2026-06-14'
collected: '2026-06-23'
category: Reasoning
direction: 掩码扩散模型 · 多轮反思推理
tags:
- Mask Diffusion Models
- Reflective Masking
- Test-time Scaling
- Local Edits
- History Reference
- Reasoning
one_liner: 为掩码扩散模型引入轻量后训练和免参数历史参考机制，实现原生多轮局部修改与测试时推理缩放
practical_value: '- **文案/Query生成场景**：若你的场景使用掩码扩散模型（如文本生成），可直接迁移Reflective Masking多轮修正机制，让模型根据上下文反复局部修改初始输出，提升文案或搜索Query的生成质量，减少全量重生成开销。

  - **Agent反思模式借鉴**：Agent多步推理中常需局部修正错误，RM的“先预测再动态掩码高error区域”策略可嵌入自回归Agent的反思环，避免丢弃所有前文，只重写有问题的片段，降低推理token消耗。

  - **推荐列表迭代优化**：生成式推荐（如Semantic ID逐位生成）可引入test-time scaling：初次生成后，根据约束（多样性、业务规则）掩码部分ID位，多轮去噪生成更优列表，实现可控的局部编辑。

  - **工程实现**：方法无需修改模型结构，仅需轻量后训练即可激活推理能力；直接应用到现有MDM框架中，成本低，可作为固定范式插入现有流程。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：自回归模型通过链式思维和反思进行推理，但修正错误仍需从头生成全文，即使只需局部修改。掩码扩散模型（MDMs）天然支持基于掩码的局部编辑，但现有MDM不支持多轮迭代去噪。本文旨在唤醒MDM内在的多轮推理能力，实现类似人类的“局部反复修正”。

**方法**：
- **Reflective Masking (RM)**：轻量后训练方案，将MDM的生成过程从单轮扩展为多轮。每轮基于前一轮输出和当前上下文，预测需修改的位置并掩码，然后去噪重写，实现迭代改进。
- **History Reference**：免参数的跨轮信息传递机制，利用前一轮中间去噪状态，为当前轮提供历史推理线索，避免推理断裂。
- 无需结构改动，直接应用于任何MDM。

**结果**：在文本生成、数独、图像编辑等多模态任务上，RM一致优于标准掩码基线。例如，文本生成任务中，RM将困惑度（Perplexity）显著降低；数独准确率提升近10个百分点；图像编辑保真度和局部一致性明显改善。展现强泛化性，为MDM推理提供基础范式。
