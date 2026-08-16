---
title: Mitigating Gender Bias in English to Romanian Machine Translation
title_zh: 缓解英语到罗马尼亚语机器翻译中的性别偏见
authors:
- Ioana Grigore
- Sergiu Nisioi
affiliations:
- Human Language Technologies Research Center, Faculty of Mathematics and Computer
  Science, University of Bucharest
arxiv_id: '2608.08606'
url: https://arxiv.org/abs/2608.08606
pdf_url: https://arxiv.org/pdf/2608.08606
published: '2026-08-08'
collected: '2026-08-16'
category: Other
direction: 机器翻译 · LLM 性别消歧与标签注入
tags:
- Gender Bias
- Machine Translation
- LLM
- NMT
- Debiasing
- Romanian
one_liner: 用微调 LLM 插入性别提示标签配合标签感知 NMT，将英罗翻译性别准确率提升超 40 个百分点
practical_value: '- 在生成式推荐或文案生成中，借鉴“LLM 分类 + 标签注入”的控制方式：用轻量分类器（或 LLM）识别目标属性（如性别、人群、品牌调性），向生成模型输入插入特殊
  token 或标签，实现可控生成，无需重新训练大模型。

  - 多阶段流水线（分类器与生成器解耦）便于单独评估和迭代，尤其适合电商场景中需要对特定属性（如性别、年龄、价格带）进行精准控制的文案或标题生成任务。

  - 构建针对特定偏见的标注数据集，用于微调下游小模型（如 NMT 或文案生成模型），可有效降低推理时对大规模 LLM 的依赖，平衡效果与成本。

  - 若业务涉及多语言翻译（如跨境电商商品描述本地化），可借鉴性别提示标签方案提升目标语言语法正确性和用户感知。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：英语到罗马尼亚语机器翻译中性别偏见严重，缺乏性别信息的英语输入常导致译文默认阳性或强化刻板印象。  
方法关键点：  
- 混合流水线：用微调 LLaMA 对英语句子中目标词做性别分类，插入内联性别提示标签（如 `<tgF>teacher</tgF>`）；  
- 将带标签句子输入微调的 Transformer NMT 模型，生成形态正确的罗马尼亚语翻译；  
- 引入三个新数据集支持性别消歧与翻译训练。  
结果：在 WinoMT 和 WinoGender 基准上，性别准确率相比基线 MT 系统提高超过 40 个百分点；首次显式解决英-罗 MT 性别偏见问题。
