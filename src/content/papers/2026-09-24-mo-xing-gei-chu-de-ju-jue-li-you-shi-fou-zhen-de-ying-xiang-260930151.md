---
title: Does a model's stated reason for rejecting a candidate do any work?
title_zh: 模型给出的拒绝理由是否真的影响决策？
authors:
- Archit Rastogi
affiliations:
- Independent Researcher
arxiv_id: '2609.30151'
url: https://arxiv.org/abs/2609.30151
pdf_url: https://arxiv.org/pdf/2609.30151
published: '2026-09-24'
collected: '2026-09-27'
category: Eval
direction: LLM 可解释性 · 反事实检验
tags:
- explainability
- faithfulness
- contrastive explanation
- LLM
- measurement validity
one_liner: 通过插入缺失事实的反事实检验，发现模型拒绝理由对选择有显著影响，但混杂因素使效应难以确立
practical_value: '- 在推荐/排序解释中，模型给出的“缺失属性”理由可通过反事实编辑验证：将该属性补回候选物品，重跑模型看决策是否翻转，用于评估生成解释是否忠实于决策。

  - 构建对照时需分离内容与位置效应：同时加入长度匹配的无关句子作为对照，以及把同一事实加到其他选项，避免把注意力/格式变化误判为文本内容效应。

  - 若用 LLM 自由文本输出做选择或排序，务必对字符串解析规则进行验证：本文解析规则错误率高达 17.1%，纠正后结论数量从 6 减为 4；应留存原始响应并人工抽检。

  - 强制概率读数和自由文本选择可能方向相反，提示解码策略与度量方式影响归因结论；业务中应报告多种度量并谨慎解释。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM 在做候选选择并解释时，常以候选缺失的事实为由拒绝，例如“没有导演”“没有去世日期”。这类表述是关于输入文本的断言，可无需外部裁判直接验证：补上缺失事实，看模型选择是否改变。

**方法**：在 2WikiMultihopQA 上，用 6 个开源模型，将真实语料句子插入被拒绝候选的 profile，greedy decoding 重问。设两个对照：同一位置插入长度匹配的无关句子；同一事实插入模型从未提及的第三个选项。所有测量用字符串规则，并对每条规则验证，捕捉到 8 个缺陷，包括选择解析规则错误返回刚拒绝选项（错误率 17.1%）。

**关键结果**：在最大规模实验中，提供缺失事实比无关对照更能改变选择，OR=3.57 [1.54,8.26]，Holm p=0.0210，去掉任一模型仍成立。但核心对比——同一事实加到无人提及的第三选项——未通过多重校正，Holm p=0.2428。最强效应竟是无内容差异：相同无关句子在命名候选比第三选项移动更多，Holm p=0.0008。修复与对照还在共现候选、关系模板、流畅性上有差异，事后匹配前两者保留内容效应方向，匹配流畅性削弱其一；因此内容对比只能界定效应而非确立。强制单 token 概率读数与自由文本选择方向不一致，三个候选解释均无支持。
