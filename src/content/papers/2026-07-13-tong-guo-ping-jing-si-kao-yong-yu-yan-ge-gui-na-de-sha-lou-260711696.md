---
title: 'Think Through a Bottleneck: Hourglass Reasoning for Rigorous Induction'
title_zh: 通过瓶颈思考：用于严格归纳的沙漏推理
authors:
- Huan Zhu
affiliations:
- Peking University
arxiv_id: '2607.11696'
url: https://arxiv.org/abs/2607.11696
pdf_url: https://arxiv.org/pdf/2607.11696
published: '2026-07-13'
collected: '2026-07-14'
category: Reasoning
direction: 结构化推理增强 · 归纳推理
tags:
- Inductive Reasoning
- Hourglass Reasoning
- LLM
- Context Isolation
- Symbolic Representation
- Few-shot Learning
one_liner: 提出 Hourglass 推理框架，通过阶段隔离与符号化状态压缩，大幅提升 LLM 少样本归纳推理能力
practical_value: '- **Agent 推理工作流设计**：在构建推荐或广告策略 Agent 时，可借鉴 Hourglass 的阶段隔离与信息瓶颈设计，强制中间推理以紧凑的符号化状态（如规则摘要、关键变量）传递，避免前序上下文污染后期决策，尤其适用于多步逻辑推导、规则生成场景。

  - **规则归纳与验证**：电商场景下常有从少量案例中归纳业务规则的需求（如识别欺诈模式、生成选品策略），可部署类似的“归纳→演绎→实现→验证→修正”流程，用错误驱动的自修正提升规则准确性，并确保修正始终锚定在核心规则上。

  - **提升 LLM 推理可控性**：借鉴显式符号编码器-解码器思想，在用户意图理解、复杂条件文案生成等任务中，将关键信息压缩为符号化描述再逐步展开，减少长链推理中的语义漂移，增强结果的可解释性与稳定性。

  - **少样本场景下的推理增强**：如果使用 LLM 进行冷启动推荐或新品类属性补全，可采用沙漏式上下文隔离与迭代修正，从稀疏样本中更可靠地抽取泛化规律，优于直接反复追问的朴素自纠正方法。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：现有自纠正方法难以稳定提升 LLM 的少样本归纳推理能力，仅要求模型显式说出规则效果甚微。根本问题在于缺乏结构化的推理阶段隔离，导致信息混杂、修正失焦。

**方法**：提出 Hourglass 推理框架，强制不同推理阶段之间只能通过压缩的符号状态传递信息。冻结的 LLM 作为元构造器，针对每个任务构建符号化的编码器-解码器流程：
1. **归纳模块**：将支持示例压缩为模式 φ（编码器）与临时支架 z；
2. **演绎模块**：从 (φ, z) 派生出规则 T（解码器）并丢弃 z；
3. **实现器**：将 (φ, T) 编译为具体产物（如图形、代码）；
4. **修正器**：基于产物错误驱动修订 (φ, T) 并从头重新生成产物。
全程仅 (φ, T) 跨越阶段边界，保证修正始终锚定规则。

**结果**：在 ARC-AGI-2、ChipBench 和 BBEH-Linguini 三个涵盖视觉抽象、硬件综合和文本规则归纳的基准上，使用 GPT-5.5 和 Gemini 3.1 Pro 验证。ARC-AGI-2 上 best-of-5 准确率较迭代修正基线最高提升 14 个百分点；ChipBench 上 Verilog 综合准确率从 31% 翻倍至 58%；在语言学奥赛难题上，Hourglass 逆转了显式语言化反损性能的倾向。消融证实增益源于阶段隔离与初始归纳质量，而非提示词或特定符号形式。
