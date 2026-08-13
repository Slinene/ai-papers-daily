---
title: Reference-Free Post-Training of Open Large Language Models for Multilingual
  Machine Translation
title_zh: 开放大语言模型多语机器翻译的无参考后训练
authors:
- Chris Han
- Pengzhi Gao
- Pei Fu
- Jian Luan
affiliations:
- Xiaomi Inc.
arxiv_id: '2608.10812'
url: https://arxiv.org/abs/2608.10812
pdf_url: https://arxiv.org/pdf/2608.10812
published: '2026-08-10'
collected: '2026-08-13'
category: Training
direction: LLM 多语翻译 · 强化后训练
tags:
- GRPO
- reference-free reward
- checkpoint interpolation
- multilingual MT
- on-policy distillation
- LLM post-training
one_liner: 用GRPO加语言门控无参考质量奖励与SFT-RL权重插值，46语翻译12B模型超越多个闭源系统
practical_value: '- 无参考奖励设计：在缺乏成对标注的生成任务（商品文案、搜索query改写、Agent回复）中，可组合多个可学习质量模型打分，并用规则门控（目标语言/格式/长度）过滤无效高分，避免错误输出获得奖励。

  - SFT-RL参数插值：训练完成后把SFT与RL权重按α线性混合，无需额外训练即可调节指标trade-off（如相关性 vs 多样性、BLEU vs 神经指标），推荐默认尝试α=0.5作为起点。

  - RL数据筛选：对每个prompt采样一组rollout，只保留reward均值和标准差符合条件的样本，能显著提升GRPO训练信号效率，适合从线上日志或无标注语料构造后训练数据。

  - 小模型继承大模型增益：用on-policy distillation可以接近RL+插值模型的性能，资源受限时可只对大模型做RL然后蒸馏到线上小模型。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
开放LLM通过SFT已能胜任多语翻译，但高质量平行语料稀缺且分布不均，尤其低资源语言和非英语方向。源语言文本远比对齐目标句易获取，因此探索仅用源端数据的无参考后训练具有实际价值。

**方法关键点**  
- 从MiLMMT-46-v0.1（1B/4B/12B）出发，用GRPO优化无参考奖励：reward为XCOMET2与COMETKiwi得分均值，并用OpenLID-v3做语言识别门控，输出语言与目标语言不匹配时reward置0，抑制错误语言奖励黑客。
- RL数据来自SFT数据去掉参考译文，保留26.4万源句；对每个源句采样G=8候选，仅保留组内reward均值0.30~0.95且标准差≥0.05的样本，最终得到31572条训练数据，提高训练信号。
- 训练后将SFT与RL checkpoint进行线性参数插值，选α=0.5得到MiLMMT-46-v1.0，兼顾神经质量指标与lexical overlap。

**关键结果**  
在46语言、WMT24++和FLORES+上，v1.0相比v0.1：WMT24++无参考XCOMET/COMETKiwi平均提升2.75/2.44点；FLORES+参考XCOMET提升1.17，无参考XCOMET提升1.41，spBLEU下降1.21。12B-v1.0在无参考指标上领先所有评估系统，包括Google Translate、Gemini 3 Pro、GPT-5；1B-v1.0在多数指标上超过TranslateGemma-4B。插值α=0.5恢复spBLEU 2.79/3.70/4.21点（1B/4B/12B），而参考XCOMET仅损失0.53/0.56/0.54点。OPD蒸馏可接近但不超越RL+插值的前沿。

最值得记住：无参考质量模型打分+语言门控+checkpoint插值，是低成本提升多语LLM翻译质量且避免reward hacking的实用组合。
