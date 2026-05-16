---
title: Quantifying and Mitigating Premature Closure in Frontier LLMs
title_zh: 量化与缓解前沿大语言模型的过早闭合行为
authors:
- Rebecca Handler
- Suhana Bedi
- Nigam Shah
affiliations:
- Stanford University
arxiv_id: '2605.15000'
url: https://arxiv.org/abs/2605.15000
pdf_url: https://arxiv.org/pdf/2605.15000
published: '2026-05-14'
collected: '2026-05-16'
category: Eval
tags:
- Premature Closure
- Medical LLMs
- Eval
- Prompt Engineering
- Abstention
- Safety
one_liner: 在医疗场景中，前沿LLM普遍在信息不足时给出不安全答案，安全提示可部分缓解但无法根除
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
过早闭合（premature closure）是临床诊断中常见的认知错误，指在信息不足时过早锁定结论。随着大语言模型（LLM）进入临床决策支持，能否识别“何时不该回答”变得与回答正确同样关键。现有医学基准多奖励正确答案，难以评估这种不当承诺行为，亟需专门衡量LLM在不确定场景下的安全边界。

**方法关键点**
- 将LLM过早闭合定义为“在不适当承诺下的不确定性响应”：应澄清、弃权、升级或拒绝时却给出答案或建议。
- 设计两类评估任务：结构化多选题与开放式交互。
  - 结构化任务：对MedQA和AfriMed-QA的题目进行修改，移除正确选项（NOTA），将“false action”（仍选答案）作为过早闭合指标。
  - 开放式任务：使用861题HealthBench子集（涵盖信息不足、紧急等类型）和191道医生撰写的对抗性红队查询，用医生制定的评分准则和二元标签衡量不当回答。
- 评估五种前沿模型：GPT-5.4、Claude Opus 4.7、Grok 3、Gemini 2.5 Pro、DeepSeek R1，在基线提示和安全提示（明确要求弃权、表达不确定性）下对比表现。

**关键结果**
- 在NOTA多选题上，baseline下模型false action率在MedQA达55–81%，AfriMed-QA达53–82%。安全提示使该指标平均下降22个百分点，但残留率仍约48%。
- 在861题HealthBench开放式任务中，baseline下过早闭合整体发生率为20.7%–44.6%，其中信息不足但低风险场景最为严重（73–96%），而紧急场景较低（5–36%）。安全提示使整体率下降4–8个百分点。
- 在191道对抗性查询中，baseline下过早闭合率达59–91%，甚至出现负分（Grok 3：-10.3%），安全提示将其降低9–20个百分点，但残余率仍超50%（Claude Opus 4.7为50.8%）。
- 多数模型的安全提示仅轻微降低回答正确题目的准确率（约1个百分点），表明未过度拒答。但Grok 3出现较大权衡：安全提示下false action大幅下降，同时正确率显著降低。
- 模型对显式紧急信号敏感，对缺失上下文不敏感，提示meta-reasoning能力不足。

**核心结论**：提示级护栏能有效减少但无法根除过早闭合，尤其在对抗性场景下残余风险仍高。未来需从训练目标、不确定性校准和评估范式入手，将“知道何时不答”作为核心能力。
