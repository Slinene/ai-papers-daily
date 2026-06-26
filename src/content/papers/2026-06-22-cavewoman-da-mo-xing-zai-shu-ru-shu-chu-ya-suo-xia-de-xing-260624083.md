---
title: 'CAVEWOMAN: How Large Language Models Behave Under Linguistic Input and Output
  Compression'
title_zh: CAVEWOMAN：大模型在输入输出压缩下的行为研究
authors:
- Morayo Danielle Adeyemi
- Ryan A. Rossi
- Franck Dernoncourt
affiliations:
- Independent
- Adobe Research
arxiv_id: '2606.24083'
url: https://arxiv.org/abs/2606.24083
pdf_url: https://arxiv.org/pdf/2606.24083
published: '2026-06-22'
collected: '2026-06-26'
category: LLM
direction: LLM 推理成本与语义保真度评估
tags:
- input compression
- output compression
- cost efficiency
- accuracy
- semantic divergence
- evaluation protocol
one_liner: 输入压缩反而增加成本并损害准确性，输出压缩能省钱但导致语义偏离基线
practical_value: '- 在电商/搜索等依赖 LLM 生成文案、推荐理由等的场景中，**不要通过压缩用户输入（如缩写查询词、省略语法）来节省成本**，实验证明这会迫使模型输出更长回复，总成本反而上升，且准确性显著下降。

  - **输出压缩（如限定模型简短回答）能有效降低 API 调用成本**，尤其在使用开放权重模型时；但需注意，即使答案正确，其表面文本可能与无压缩基线产生语义偏离，因此需额外监控生成内容与原始风格的一致性。

  - 实现时可将输出压缩作为**成本控制手段**，结合**语义对齐度指标**（如 entailment 检测）确保压缩后内容不违背原意，适合高频生成场景（如自动回复、消息推送）。

  - 如果使用自建模型，可按 token 计费时优先压缩输出；若模型输出长度不可控，可设置最大 token 数来硬性限制，但需权衡准确性和语义偏移。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**

业界常建议用“穴居人式”压缩语言（如“Talk short. Drop grammar. Save token.”）来降低 LLM 推理成本，但缺乏系统评估：压缩输入（用户提示）和输出（模型回复）的效果是否相同？实际成本与准确性如何变化？

**方法**

提出 **CAVEWOMAN** 双通道评估协议，同时测量：
1. 任务准确性
2. 每样本实际推理成本（token 数 × 对应通道单价）
3. 生成文本与无压缩参考文本的语义一致性（基于 NLI 的 entailment 指标）

在 8 个模型（含 API 与开放权重模型）、5 个数据集、5 个压缩等级上进行控制实验，确保输入和输出压缩在相同样本上测量。

**关键结果**

- **输出压缩**显著降低实际成本：API 模型通常节省 1.4–2.4 倍，开放权重模型节省更明显，最佳情况可达 3 倍。
- **输入压缩**反而是 strict lose-lose：平均净成本增加约 **15%**，在部分数据集上高达 **1.8 倍**，强压缩时甚至 **2.7 倍**；原因是模型为弥补信息缺失而生成长回复，同时准确性大幅下降。
- **语义偏离严重**：即使答案正确，非推理模型中约半数生成文本不再蕴含其无压缩基线生成的内容，这一偏离在长度控制、多重检验及不同语义指标下均稳健存在。

结论：压缩策略必须区分输入与输出通道，输入压缩有害无益，输出压缩虽省钱但需警惕语义保真度。
