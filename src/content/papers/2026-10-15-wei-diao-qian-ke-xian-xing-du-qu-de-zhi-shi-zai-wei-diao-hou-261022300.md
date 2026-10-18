---
title: Knowledge That Is Linear Before Fine-Tuning Generalizes After It
title_zh: 微调前可线性读取的知识在微调后更能泛化
authors:
- Faridoun Mehri
- Hinrich Schütze
affiliations:
- Center for Information and Language Processing, LMU Munich
- Munich Center for Machine Learning (MCML)
arxiv_id: '2610.22300'
url: https://arxiv.org/abs/2610.22300
pdf_url: https://arxiv.org/pdf/2610.22300
published: '2026-10-15'
collected: '2026-10-18'
category: LLM
direction: LLM 线性可读性与微调泛化
tags:
- linear probing
- fine-tuning
- generalization
- interpretability
- knowledge representation
one_liner: 预训练表示中原关系的线性可读性越强，新构造关系微调后的泛化越好，模型内 Pearson r=0.87–0.92
practical_value: '- 微调电商/搜索领域的实体属性映射前（如品牌→类目、商品→属性、query→品类），先用线性探针测量预训练表示中该映射是否线性可读；可读性高时，小样本微调更可能泛化到长尾实体，可节省标注和算力。

  - 若要做生成式推荐或 Semantic ID 映射等新任务，可构造“原属性→任意新标签”的代理任务，快速预判模型能否在新实体上泛化，避免在不可泛化的监督信号上做无效微调。

  - 线上模型出现错误标签时，可将错误标签映射回原答案，并通过线性探针的 top 预测辅助诊断：错误可能不是模型没记住事实，而是共享结构没有被线性编码；这能指导后续是继续微调还是补充预训练/表示学习。

  - 对 Agent 或 LLM4Rec 中需要模型进行规则归纳、实体聚类、属性补全的场景，优先选择预训练表示中已线性可分的特征作为监督目标，能显著提高微调后的
  held-out 泛化。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：语言模型能回忆的事实不一定都能支撑下游泛化。作者区分 active facts（能支持新样本泛化）与 inert facts（仅能回忆但无助于当前任务泛化），并研究预训练表示中何种性质能预测这一差异。

方法关键点：在已有关系（如城市→大洲）基础上，给原答案随机分配无意义新标签（如 Europe→crab, Asia→zebra），构成新关系。仅对部分 subject 微调模型，不告知原始关系和标签映射，随后测试模型对 held-out subject 能否预测对应新标签。这样隔离了“原关系知识”对泛化的影响。用线性探针测量预训练表示中原始关系的线性可读性，并分析其与新关系泛化效果的相关性。

关键结果：在 11 个语言模型、70 个关系上，预训练表示中原关系的线性可读性与微调后泛化呈强相关，模型内 Pearson r 为 0.87–0.92。控制微调样本数、答案数、模型在原关系上的准确率、subject 在预训练文本中的频率后，仍稳健；更换标签语义类别、随机标签分配和微调 seed 也不改变结论。错误标签映射回原答案后，得到的答案更多出现在线性探针的 top 预测中，而不是预训练模型自身输出中。说明新关系能否泛化，更取决于其共享结构是否可被线性读出，而非事实能否被回忆。
