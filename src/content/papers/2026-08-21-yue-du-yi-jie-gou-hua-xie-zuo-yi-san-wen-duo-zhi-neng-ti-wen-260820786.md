---
title: 'Structure for Reading, Prose for Writing: Asymmetric Structural Conditioning
  in Multi-Agent Document Authoring'
title_zh: 阅读宜结构化，写作宜散文：多智能体文档创作中的非对称结构条件化
authors:
- Cheng Yu
- Nikhil Mathew
- Zhengjie Wang
affiliations:
- ML Research Labs, Canberra, Australia
arxiv_id: '2608.20786'
url: https://arxiv.org/abs/2608.20786
pdf_url: https://arxiv.org/pdf/2608.20786
published: '2026-08-21'
collected: '2026-08-24'
category: MultiAgent
direction: 多智能体文档生成与结构条件化
tags:
- Multi-Agent
- Document Authoring
- Structured Conditioning
- XML
- LLM Judge
- Evaluation
one_liner: 部署招标应答系统发现：结构化标记利于读取抽取，但嵌套 XML 条件化生成质量从 74% 降至 48%
practical_value: '- 生成式推荐/Agent 中，用于抽取解析的 JSON Schema/XML 不应直接作为生成约束条件；在 prompt 里用自然语言描述输出要求，比嵌套结构化标签更稳定。尤其做对话式推荐或商品描述生成时，模板别过度结构化。

  - 负面约束（“不要生成 XX 结构/词”）只命名禁止形式易让模型集中生成该形式；建议配套正面示例、自检清单或后校验器，而不是仅列禁止项。

  - 评估生成质量时，若对照的 ground truth 包含模型输入源没有的知识，应拆分“信息可得性”和“模型能力”两类指标，否则会低估系统；在电商文案/搜索改写评估中同样要区分。

  - 抽取和生成两阶段应使用不同表示：读取端用结构化解析提升召回，写入端回归自然语言指令和自检，这是可复用的架构选择。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：多智能体文档撰写系统必须读取申请方表单并按其格式作答，同时满足主权约束。论文部署了一个招标应答系统，开源权重模型，并与同组织实际提交的人工标书做盲评。

**方法关键点**：LLM judge 对 55 个 ground-truth sections 评分，系统无任何示例可用。结果：40/55 至少与人类答案持平，4 个更好，无遗漏，仅 1 处无依据声明。对差距分类发现 68% 因源材料中缺失知识（人类已知但 pipeline 未给到），15 个不利判定中仅 6 个是系统可避免的缺陷。随后报告条件化不对称：从文档抽取阶段，结构化标记（XML/Markdown）优于 prose；但在生成条件化阶段，将指令材料从 prose 转为嵌套 XML 使答案质量从 74% 降至 48%。另外，显式命名禁止构造反而集中缺陷：96% 的幸存缺陷落在 prompt 命名的两种形式上；随机标注与确定性窗口函数耦合，使同一文件的需求抽取数从 68 降至 51。

**关键结果**：结构标记利于阅读/抽取，但不利于写作条件化；prose 指令与自检更适合生成端。
