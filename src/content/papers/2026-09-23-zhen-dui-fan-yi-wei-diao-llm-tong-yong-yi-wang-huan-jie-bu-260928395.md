---
title: 'Fine-Tuning LLMs for Translation: General Forgetting Mitigation Does Not Preserve
  MT-Specific Instruction Following'
title_zh: 针对翻译微调LLM：通用遗忘缓解不保护MT特定指令遵循
authors:
- Niklas Scholz
- David Thulke
- Abdallah Nasir
- Will Allred
- Evgeny Matusov
- Hermann Ney
affiliations:
- AppTek GmbH, Aachen, Germany
- Machine Learning and Human Language Technology, RWTH Aachen University, Germany
- Applied Science Private University, Amman, Jordan
arxiv_id: '2609.28395'
url: https://arxiv.org/abs/2609.28395
pdf_url: https://arxiv.org/pdf/2609.28395
published: '2026-09-23'
collected: '2026-09-24'
category: Training
direction: LLM 微调与灾难性遗忘缓解
tags:
- fine-tuning
- catastrophic forgetting
- machine translation
- instruction following
- EWC
one_liner: 比较微调中的遗忘缓解方法，发现EWC保留通用能力最好，但只有混合控制任务数据可保留MT特定指令遵循，且泛化有限
practical_value: '- 在电商/推荐场景微调LLM（如生成推荐文案、query改写、对话Agent）时，建议添加EWC正则化：实现简单，能显著减缓通用基准能力下降（本文8B模型仅降1.7分
  vs 标准微调11.0），同时不影响领域任务性能。

  - 若需要保留多种控制能力（如文案语气、长度、格式），仅靠通用遗忘缓解不够，应在微调数据中混合少量控制任务示例，但需注意对未见过的指令模板泛化有限，因此要持续扩充控制任务的数据多样性。

  - 评估微调模型时必须同时监控通用能力和任务特定指令遵循，不能只看单一指标，因为通用能力保留不代表特定控制能力保留。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：指令微调LLM在低资源语言/领域翻译质量不佳，微调平行数据可大幅提升（如Amharic-to-English COMET从45.6升至71.5），但会引发灾难性遗忘。现有遗忘缓解方法只在通用基准上评估，未考察MT特定指令遵循（MT-IF：语气、语法性别、长度控制）是否被保留。

**方法**：比较三类遗忘缓解方法——基于辅助数据、基于模型输出、基于基模型参数。先在Llama 3.2 1B Instruct上筛选，再在Llama 3.1 8B Instruct上微调双向阿拉伯语-英语或西班牙语-英语数据。

**关键结果**：Elastic Weight Consolidation (EWC)在两个阶段均最好地保留通用能力；8B西班牙语模型通用基准平均分仅下降1.7，而标准微调下降11.0。然而，EWC对形式化和语法性别控制的得分仍接近标准微调，说明通用遗忘缓解不自动保护MT-IF。只有数据混合控制任务示例能保留这些控制，但其增益不能泛化到未见过的同任务prompt。
