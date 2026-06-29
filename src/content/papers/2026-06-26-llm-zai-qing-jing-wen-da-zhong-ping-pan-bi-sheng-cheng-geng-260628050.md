---
title: Can LLMs Judge Better Than They Generate? Evaluating Task Asymmetry, Mechanistic
  Interpretability and Transferability for In-Context QA
title_zh: LLM 在情境问答中评判比生成更难？不对称性分析
authors:
- Sambaran Bandyopadhyay
affiliations:
- Adobe Research
arxiv_id: '2606.28050'
url: https://arxiv.org/abs/2606.28050
pdf_url: https://arxiv.org/pdf/2606.28050
published: '2026-06-26'
collected: '2026-06-29'
category: Eval
direction: LLM 评判 vs. 生成不对称性 · 注意力机制
tags:
- LLM-as-Judge
- Self-evaluation
- Mechanistic Interpretability
- Attention Analysis
- LoRA Fine-tuning
- In-context QA
one_liner: 发现自评估并非总是比生成容易，注意力差异揭示评估忽略上下文与答案。
practical_value: '- 在电商搜索、Agent 反馈等依赖 LLM 自评估的场景，需警惕评估准确率常低于生成，应引入外部校验或结构化评估流程，避免错误答案被放行。

  - 评估时模型对上下文关注度低 3-5 倍，且几乎不看候选答案，可设计显式 prompt 强制其细读上下文或答案，或改用单独的评估模型。

  - 微调生成与评估会相互干扰：优化生成导致过接受（误判增多），优化评估则损害生成质量。若需两者兼具，建议分离模块或采用多任务平衡训练。

  - 在 Agent 反思机制中，单靠模型自评可能不可靠，结合检索结果验证、执行反馈等外部信号可提高稳健性。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM-as-a-Judge 与自评估管道普遍默认「评估比生成容易」。本文在可控 in-context QA 设定下，排除参数知识干扰，检验模型自判断答案是否真的比生成更简单。  
**方法**：在 SQuAD 2.0、DROP、HotpotQA、MuSiQue 四个基准上，给定上下文段落作为唯一信息源，让模型先生成答案、再评判自己的生成结果。比较生成准确率与自评估准确率；通过注意力分析对比生成与评估时模型对上下文和候选答案的关注度；再用 LoRA 分别微调生成和评估能力，观察相互影响。  
**关键结果**：三个基准上生成准确率均高于自评估（如 ChatGPT SQuAD 81.1% vs 73.4%），仅多跳推理 MuSiQue 例外（17.3% vs 31.5%）。注意力分析显示评估时对上下文关注比生成少 3-5 倍，且几乎不读候选答案。LoRA 微调证实不对称非训练假象：生成微调引致评估过接受（错判为对），评估微调则损害生成质量。结论挑战自评估管道的基础假设。
