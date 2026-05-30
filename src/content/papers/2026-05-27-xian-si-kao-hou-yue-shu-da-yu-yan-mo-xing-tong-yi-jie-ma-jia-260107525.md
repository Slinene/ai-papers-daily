---
title: 'Thinking Before Constraining: A Unified Decoding Framework for Large Language
  Models'
title_zh: 先思考后约束：大语言模型统一解码框架
authors:
- Ngoc Trinh Hung Nguyen
- Alonso Silva
- Laith Zumot
- Liubov Tupikina
- Armen Aghasaryan
- Mehwish Alam
affiliations:
- Télécom Paris, Institut Polytechnique de Paris
- Nokia Bell Labs
- Nokia
arxiv_id: '2601.07525'
url: https://arxiv.org/abs/2601.07525
pdf_url: https://arxiv.org/pdf/2601.07525
published: '2026-05-27'
collected: '2026-05-30'
category: LLM
direction: LLM解码：自由推理与结构化生成统一
tags:
- Structured Decoding
- Trigger Token
- Chain-of-Thought
- Constrained Generation
- In-Writing
one_liner: 通过先自由推理后触发约束解码的单步框架，消除过早触发，在多个推理任务上准确率提升高达27%，并保证100%解析率。
practical_value: '- 在需要LLM同时进行推理并输出结构化指令（如API调用、数据库查询参数）的场景中，采用先自由推理再触发约束（如特殊标记）的模式，可避免过早格式限制打断心智链。

  - 使用单个<eos>作为唯一触发token，能有效解决premature triggering问题，提升推理完整性。

  - 结构化解码可充当天然的后处理解析器和语法修正器，无需额外模型，降低管线复杂度，尤其适合多字段结构化提取（如电商商品属性、Agent工具调用参数）。

  - 方法仅需增加5-20个token开销，适合追求低延迟和高吞吐的工业系统，可直接集成到现有LLM推理管线中。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：大语言模型自由生成具有丰富推理，但难以保证输出结构；约束解码可确保格式却往往因过早施加限制而破坏推理链条。现有方案如NL-to-Format需要额外解析模型，代价高且不能保证正确解析；CRANE虽交替生成，但推理仍受限于语法空间。为此需要一种能保持推理自由、同时确保格式正确的方法。

**方法关键点**：
- 提出In-Writing解码框架，在单次生成中分离推理与格式化：先生成无约束的推理步骤，一旦产生触发token（如`<eos>`或`{`），立即切换到基于有限自动机的约束解码，输出符合预设正则或JSON schema的结果。
- 将约束解码重新定位为推理后的解析器和语法修正器，而非全程约束，从而避免在推理阶段剔除有效但表面不一致的路径。
- 通过仅使用`<eos>`为触发token的策略（In-Writing*），几乎完全消除“过早触发”（premature triggering）导致推理截断的失败模式。

**关键实验与结果**：
- 在GSM8K、Last Letter、Shuffled Objects等推理任务和多个分类任务上，与自然生成、约束解码、NL-to-Format、CRANE进行全面对比。
- In-Writing*相比自然生成最高准确率提升27%（GSM8K，Qwen3-1.7B）；相比CRANE在GSM-Symbolic上最高提升32%。
- 所有测试中保持100%解析成功率，而NL基线解析率波动大（22%-100%），NL-to-Format也未能达到100%。
- 额外token开销极小：仅增加5-20个token，且不依赖外部解析模型。

**最值得记住的一句话**：将约束解码推迟到推理完成后，既保留了推理完整性，又实现了零失误的结构化输出，是LLM应用中的廉价但高效的提升手段。
