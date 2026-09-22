---
title: 'The Copy Ceiling: An Input-Exposure Control for Ontology-Grounded Generation
  over Curated Corpora'
title_zh: 复制天花板：本体生成中的输入暴露控制
authors:
- John J. O'Hare
affiliations:
- DreamLab AI
arxiv_id: '2609.24885'
url: https://arxiv.org/abs/2609.24885
pdf_url: https://arxiv.org/pdf/2609.24885
published: '2026-09-21'
collected: '2026-09-22'
category: Eval
direction: RAG 评估 · 输入暴露控制
tags:
- RAG
- Evaluation
- Exposure Accounting
- Copy Ceiling
- Grounded Generation
- LLM
one_liner: 提出曝光记账与复制天花板基线，证明RAG/本体生成增益主要来自上下文复制而非推理，且超出暴露恢复稀少且常为假阳性
practical_value: '- 在构建 RAG / 知识库问答 / 本体驱动对话的评测集时，添加“是否已暴露在输入上下文”字段：统计模型输出中与上下文重叠的
  gold item，避免把复制能力当作推理能力。可计算 copy ceiling（直接复制检索块中目标答案的 recall）作为 judge-free 基线，任何
  grounding 提升都要报告 signed gain over copy。

  - 对生成式推荐/文案生成评估，尤其基于 Semantic ID 或知识图谱的生成，若评测指标依赖目标 ID 或关键词是否出现在输出中，务必检查这些 ID/词是否已在检索上下文或
  prompt 中出现；否则会严重高估模型。可通过 rephrasing 系统性问题、避开高频标题词来测试真实泛化。

  - 对少量“超出暴露的恢复”保持警惕：自动评分器给出的少量 unexposed credits 很可能为假阳性，需用 stratified audit + 引用验证（quote-gate）复核。电商场景中，模型“举一反三”的推荐解释可借鉴此方法：对声称的推理链路要求引用出处，否则视为无效。

  - 阴性对照设计：在 A/B 评估生成质量时，除了对比“无上下文”和“有 scaffold”，还要加入一个“格式良好但与任务无关的语料块”作为对照，否则无法证明特定
  scaffold 的内容贡献。这个思路可用于评估推荐理由生成或商品卖点提炼的模型。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：RAG 或基于知识图谱的 grounded generation 评估通常报告显著提升，但无法区分模型是基于输入复制还是真正推理。当 gold answer 已出现在检索上下文中时，grounding uplift 可能只是复制粘贴，而非结构化推理。

**方法关键点**：提出 exposure accounting——对每个 gold item 按“上下文是否暴露”和“模型答案是否恢复”四分类。copy ceiling 定义为逐字复制上下文能达到的 recall，作为无需 judge 的确定性基线；signed gain over copy 衡量模型 recall 相对该基线的净增益（通常为负）。还采用 rephrasing 问题、stratified audit + quote-gate 人工验证来交叉检验自动评分。

**关键结果**：10 个模型，裸 recall 平均 0.26，grounded recall 0.92，但 gain over copy 全部为负（-0.067 至 -0.022）。11,360 个 gold-item 观察中仅 3 个 unexposed 项目被自动评分恢复，人工审计全部失败；在未暴露目标上，词法恢复从裸 0.121 降至 grounded 0.004。重述问题使暴露率从 0.964 降至 0.328。这些结果支持将 exposure accounting 作为语料衍生评估的标准控制。
