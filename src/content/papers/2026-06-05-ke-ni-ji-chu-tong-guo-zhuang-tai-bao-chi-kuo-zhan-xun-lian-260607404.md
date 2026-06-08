---
title: 'Reversible Foundations: Training a 120B Sparse MoE through State-Preserving
  Scaling'
title_zh: 可逆基础：通过状态保持扩展训练120B稀疏MoE模型
authors:
- Rohan Shravan
affiliations:
- The School of AI, Bengaluru, India
arxiv_id: '2606.07404'
url: https://arxiv.org/abs/2606.07404
pdf_url: https://arxiv.org/pdf/2606.07404
published: '2026-06-05'
collected: '2026-06-08'
category: Training
direction: 大规模MoE训练与模型扩展
tags:
- MoE
- Reversible Architecture
- State-Preserving Growth
- Quantized Training
- Single-Node Training
one_liner: 在单8GPU节点上，结合可逆堆叠与状态保持增长，端到端训练出120B稀疏MoE，优化器状态缩减45倍。
practical_value: '- **可逆设计用于长序列推荐**：电商用户行为序列往往很长，可逆层可将激活内存降至常数，适合在有限显存下扩展推荐模型的序列长度，例如用于用户长期兴趣建模。

  - **渐进式模型扩容**：从种子模型出发，通过状态保持增长逐步扩大专家数量，这一思路可直接借鉴到生成式推荐模型的迭代：先训练小规模Semantic ID生成器，再逐阶段增加专家，避免冷启动训练的高成本。

  - **TQP量化训练策略**：对基础专家权重量化，仅对低秩适配器保留优化器状态，显著降低显存占用。在电商多模态Agent微调或生成式推荐模型部署时，可用类似方法在大参数量下保持低资源推理与训练。

  - **施工级工程报告**：文中详细记录了扩展中的失败模式，如“静默失败”导致假性收敛，这对实际构建大规模推荐系统时有警示意义，能帮助团队提前规避类似陷阱。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**  
训练千亿参数稀疏MoE通常需要数百张GPU，作者试图在单个8-GPU节点上完成从种子模型到120B规模的完整训练，目的是写出一份可复现的“操作食谱”，把模型扩展中常被隐藏的系统原理和失败经验公开。  

**方法关键点**  
- **可逆堆叠**：使用可逆递归骨干，反向传播时重建激活值而非存储，使激活内存不随深度和专家数量增长，保证长上下文下单节点可行。  
- **状态保持增长**：将模型增长视为“接口保持”：从密集种子模型（1.78B）逐步扩展为MoE（5B、9B）再到120B（460专家、top-12路由）。每次扩展都给出可复现原则，并明确指出错误做法导致的静默失败（如假性收敛）。  
- **单节点经济性**：提出TQP策略——量化基础专家权重，同时训练低秩适配器，将优化器状态集中在适配器的2.26B参数上，而非100B+的专家全量，使优化器状态占用缩减约45倍。  

**关键结果**  
- 在单8-GPU节点上，端到端训练出120B稀疏MoE（活跃参数仅5.93B，占总参数118.67B的5%）。  
- 训练损失达到1.78，模型在目标领域（多语言印度语、代码）上通过构造学习到相应能力。  
- 完整发布模型家族、分词器与训练代码。
