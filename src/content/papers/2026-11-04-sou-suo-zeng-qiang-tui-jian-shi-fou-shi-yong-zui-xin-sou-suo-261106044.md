---
title: Do Search-Augmented Recommenders Use the Latest Search Episode?
title_zh: 搜索增强推荐是否使用最新搜索片段？
authors:
- Jiandong Ding
affiliations:
- Huawei Technologies Co., Ltd.
arxiv_id: '2611.06044'
url: https://arxiv.org/abs/2611.06044
pdf_url: https://arxiv.org/pdf/2611.06044
published: '2026-11-04'
collected: '2026-11-05'
category: RecSys
direction: 搜索增强推荐 · 反事实归因评估
tags:
- Search-Augmented Recommendation
- Counterfactual Evaluation
- Attribution
- Ranking Diagnostics
- RecSys
- Evaluation
one_liner: 提出FocalSwap审计，用中性掩码与匹配观察搜索替换对比，发现最新搜索贡献证据不足
practical_value: '- 做搜索增强推荐或Agent上下文融合时，不要只看“去掉搜索特征后指标下降”或中性mask收益；要加一组用真实历史搜索序列替换的对照，否则可能把“有搜索这个槽位/非中性ID”的收益误读为“模型用了最新检索意图”。

  - 评估模块贡献可用FocalSwap思路：固定target/candidates/pre-search history/scorer，只换关注输入槽，分别配中性掩码和匹配真实样本替换，记录rank
  change和RR gap，能得到更干净的归因。

  - 在业务中若要上线“实时搜索信号/最新query”作为模型输入，先做这类单槽替换审计；若最新slot在匹配替换下不能稳定提升rank，可能需要重新设计特征注入方式或明确其仅作为训练监督信号而非运行时强特征。

  - 该方法可复用于Agent+推荐系统中对检索上下文、工具输出、用户query等输入的真实依赖审计，帮助决定哪些上下文值得进prompt/模型。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：搜索增强推荐（SAR）模型常用搜索行为提升推荐，但聚合增益和模块消融无法定位是哪个搜索输入起作用，最新搜索episode与早期搜索/累积状态的贡献难以区分。

方法关键点：提出FocalSwap审计，对每次推荐仅替换最新搜索槽或全部搜索输入，固定目标、候选、搜索前历史和打分器；对比中性掩码与匹配的观察搜索替换，记录rank变化、相对对照的RR增益、对真实焦点搜索的偏好；用植入信号和GenSAR current-query任务验证审计能检测已知输入依赖。

关键结果：在3个独立训练的UniSAR checkpoint、同一66,139行上，全部搜索输入换中性ID得到正贡献，但换成类别/画像匹配的观察搜索序列后估计变小，一个checkpoint区间下界低于0；配对RR gaps为+2.770e-3到+6.604e-3，调整区间均高于0；中性掩码改变59.7-61.7%目标rank，匹配替换改变44.1-44.8%；控制对比在5种替代donor分配下稳定；在SESRec和UniSAR的主要中性掩码和类别匹配控制下，最新slot正贡献未被确立。结论：归因更广搜索状态或最新episode时，掩码证据应与观察搜索替换对比。
