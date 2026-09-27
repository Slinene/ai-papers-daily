---
title: Do Audio Language Models Hear and Read Distinctive Features Alike?
title_zh: 音频语言模型听与读区分特征是否一致？
authors:
- Yuanhao Chen
- Peter Chin
affiliations:
- Thayer School of Engineering, Dartmouth College
arxiv_id: '2609.30167'
url: https://arxiv.org/abs/2609.30167
pdf_url: https://arxiv.org/pdf/2609.30167
published: '2026-09-24'
collected: '2026-09-27'
category: Multimodal
direction: 跨模态表征一致性分析 · 音频语言模型
tags:
- audio language models
- phonological features
- cross-modal representation
- multilingual speech
- representation geometry
one_liner: 通过最小音素对差分方向，发现仅 Qwen2.5-Omni 的 voicing 跨模态对齐显著，且模型家族决定表征一致性
practical_value: '- 评估多模态 LLM 的跨模态对齐时，不要只看余弦相似度的绝对值：任意音素对的基线一致性已经很高，必须构建随机配对参考做显著性检验，否则会高估对齐程度。

  - 模型家族比模型规模更能影响表征对齐，选型多模态底座时应优先评测家族特性而非参数量。

  - 最小对差分方向法可迁移到电商场景：如评测模型是否将“红色/蓝色”“棉/麻”等属性在文本与图像/语音中编码为同一方向，用于诊断多模态 embedding 的属性一致性。

  - 注意不同模型 reference 差异可达 7 倍，对齐结论不能跨模型直接比较，需要各自标定基线。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：音频语言模型（ALM）将语音和文本统一输入单一解码器，需要检验其是否在两种模态中共享同一特征方向，还是分别编码音素区别性特征。

**方法**：对只差一个区别性特征的最小音素对，取两成员平均表示的差分向量，在音频和文本两个流中分别聚合得到特征方向，计算二者余弦相似度；考虑到任意音素对在两流中已有较高一致性，将结果与随机配对的基线分布比较，做多重检验校正。覆盖 6 个模型、7 个特征、15 种语言（11 语系）。

**关键结果**：仅 Qwen2.5-Omni 系列模型中的 voicing 特征在校正后显著超过随机基线；基线水平在不同模型间可差 7 倍。在 14 种有足够最小对的语言中，6 个模型里有 3 个的 voicing 在音频流有一个跨语言一致方向，其中 2 个模型在所有语言对间一致。模型家族而非模型规模决定哪个流表征该特征。
