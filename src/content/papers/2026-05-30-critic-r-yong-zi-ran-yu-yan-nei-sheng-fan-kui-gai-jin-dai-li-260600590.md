---
title: 'Critic-R: Improving Agentic Search using Instruction-tuned Retrievers with
  Natural Language Introspective Feedback'
title_zh: Critic-R：用自然语言内省反馈改进代理搜索中的检索瓶颈
authors:
- Md Zarif Ul Alam
- Alireza Salemi
- Hamed Zamani
affiliations:
- University of Massachusetts Amherst
arxiv_id: '2606.00590'
url: https://arxiv.org/abs/2606.00590
pdf_url: https://arxiv.org/pdf/2606.00590
published: '2026-05-30'
collected: '2026-06-02'
category: Agent
direction: Agentic Search · 推理时检索反馈优化
tags:
- Agentic Search
- Critic Model
- Inference-Time Scaling
- Contrastive Learning
- Retrieval-Augmented Generation
- Multi-Hop QA
one_liner: 引入批评模型判断检索是否满足推理需求，结合推理时查询重写与无标注对比学习，显著提升多跳问答性能
practical_value: '- **推理时检索质量修复**：无需修改现有检索模型，仅引入一个独立的批评模型判断检索结果是否满足当前推理步骤，并基于不满足的反馈重写查询。在电商搜索或对话推荐中，当检索结果不相关或信息不足时，可直接使用此机制动态改进查询，提升最终答案准确性。

  - **无标注检索器微调**：利用代理轨迹中的正例（被推理模型接受的文档）和硬负例（被拒绝的文档）构建对比学习数据，无需人工相关度标注。该方案可用于训练电商领域的稠密检索器，尤其适用于缺乏标注数据的场景，且能显著超越端到端联合训练的检索器。

  - **内省反馈作为关键监督信号**：批评模型必须基于推理模型的思考过程（而非仅查询-文档对）来判断检索质量。在应用时，应保留推理链中的自然语言反馈，将其作为后续模型优化或数据筛选的重要输入，能大幅提升训练信号纯度。

  - **解耦判断与改进**：将“检索引擎是否满足需求”的判断与“如何改进查询”分开为两个独立的提示步骤，可提高稳定性并避免不必要的外部调用。实现类似系统时可复用这种解耦设计，减少推理开销并提升灵活性。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机

在代理搜索（Agentic Search）中，推理智能体通过多次检索和推理来回答复杂问题，但现有工作大多将检索模型视为黑盒，仅通过改进推理策略来补偿检索失败。这导致检索成为性能瓶颈。 Critic-R 认为推理智能体的内省思考（introspective reasoning）天然蕴含对检索质量的反馈，可以借此显式建模检索充分性，并同时用于推理时修复和检索模型训练。

### 方法关键点

- **Critic-R-Zero（推理时查询优化）**：在每次检索后，先让推理智能体基于检索结果进行“投机”思考（不提交到历史），再由一个独立的批评模型（critic）根据原始问题、当前子查询、检索文档和智能体的内省思考，判断检索是否充分。若否，批评模型会生成新的查询和检索指令，重新检索（最多K次）。整个过程无需梯度更新，可适配任意冻结的检索器。
- **Critic-Embed（自监督检索微调）**：利用 Critic-R-Zero 在多跳问答训练集上收集的轨迹，将最终被接受的文档作为正例，被拒绝的文档作为硬负例，结合批量内负例进行 InfoNCE 对比学习，微调 Stella-400M 稠密检索器。此过程不需要任何人工相关度标注。特别重要的是，批评模型在判断时必须看到推理智能体的内省反馈；去除该反馈会导致训练信号质量大幅下降。
- **Critic-R（联合系统）**：将微调后的 Critic-Embed 用作检索器，并仍启用推理时的查询优化循环，二者互补，进一步提升性能。

### 关键实验

在 HotpotQA、2WikiMultihopQA、MuSiQue 和 Bamboogle 四个多跳 QA 数据集上，使用 Search-R1（基于 Qwen2.5 的多尺度版本）作为推理智能体，Qwen2.5-72B 作为批评模型。主要结果：
- **Critic-R-Zero**（冻结 Stella-400M 检索器）将 14B 推理智能体的多跳平均 EM/F1 从 0.3472/0.4470 提升至 0.3903/0.4855，相对提升约 12.4%。
- **Critic-Embed**（静态检索，无推理时循环）在 top-1 设置下多跳平均 EM/F1 为 0.3794/0.4806，显著优于同基座下的 Stella-400M（0.3472/0.4470）和端到端联合训练的 Agentic-R（0.3670/0.4564）。
- 全系统 **Critic-R** 达到最佳多跳平均 0.3957 EM / 0.4959 F1，相对静态基线提升 10.9%。
- 去除内省反馈的训练会使 Critic-Embed 在 top-1 下平均 EM/F1 跌至 0.3614/0.4521，证实了推理智能体的思考反馈是监督信号的核心来源。
