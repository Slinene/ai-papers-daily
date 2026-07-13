---
title: Self-Guided Test-Time Training for Long-Context LLMs
title_zh: 自引导测试时训练：提升长上下文LLM推理的简单方法
authors:
- Xinyu Zhu
- Zhe Xu
- Xiaohan Wei
- Yunchen Pu
- Fei Tian
- Chonglin Sun
- Kaushik Rangadurai
- Hua Zhi
- Frank Shyu
- Sandeep Pandey
affiliations:
- Meta AI
- University of Virginia
arxiv_id: '2607.09415'
url: https://arxiv.org/abs/2607.09415
pdf_url: https://arxiv.org/pdf/2607.09415
published: '2026-07-09'
collected: '2026-07-13'
category: LLM
direction: 长文本测试时自适应训练
tags:
- Test-Time Training
- Long-Context
- Self-Guided
- Evidence Selection
- LLM Reasoning
one_liner: 模型自适应前先自选相关证据片段，只在选中的片段上做测试时训练，长上下文推理最高提升15%
practical_value: '- 在长上下文任务（如长用户行为序列建模、长文档问答）中，可借鉴自引导TTT：对每条测试样本，先用模型识别出与当前query/任务最相关的证据片段，仅在这些片段上进行语言模型微调，以低计算成本实现实例自适应。

  - 工程上，S-TTT的稀疏训练只更新少量token，适合在线延迟敏感场景，例如搜索query改写、个性化推荐理由生成时的实时自适应。

  - 借鉴“自选择证据”思想，在构建Agent的记忆或RAG模块时，可设计一个轻量级证据选择器，从长上下文历史中检索关键信息，再对此进行微调或提示增强，有效过滤噪声。

  - 该方法无需额外标注，利用模型自身输出作为监督信号，可在电商评论聚合、广告文案生成等长文本应用中以无监督方式提升证据利用率。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：长上下文LLM随着输入增长准确率下降，主要原因是模型难以有效定位和利用与问题相关的证据。测试时训练（TTT）能针对具体输入自适应，但直接在整个长上下文上训练成本过高，随机采样片段又会引入大量噪声甚至损害性能。初步实验显示，TTT对训练片段的选择高度敏感：使用oracle相关片段能大幅提升，而随机片段有害。

**方法关键点**：提出自引导TTT（S-TTT），在自适应前，模型先根据当前问题自行识别出应学习的证据片段（通过注意力或相关性评分），然后仅在这些选中的片段上应用标准语言模型训练目标，进行参数更新。这样既保留了TTT的实例自适应优势，又避免了无关噪声和计算浪费。

**关键结果**：在LongBench-v2上，S-TTT将Qwen3-4B-Thinking-2507的准确率从35.8%提升到39.2%（+9.5%），Llama-3.1-8B-Instruct从19.1%提升到22.0%（+15.2%）；在LongBench-Pro上也有显著提升，均优于随机采样TTT和基线。
