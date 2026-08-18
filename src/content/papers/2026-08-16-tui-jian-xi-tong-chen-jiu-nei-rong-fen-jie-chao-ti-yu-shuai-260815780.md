---
title: 'Decomposing Staleness in Recommender Systems: A Dual-Filter Framework for
  Supersession and Decay'
title_zh: 推荐系统陈旧内容分解：超替与衰减双过滤器
authors:
- Di Bai
- Feng Han
- Zhenwei Tang
- Jintao Liu
- Luoshu Wang
- Jialu Liu
affiliations:
- Google LLC
arxiv_id: '2608.15780'
url: https://arxiv.org/abs/2608.15780
pdf_url: https://arxiv.org/pdf/2608.15780
published: '2026-08-16'
collected: '2026-08-18'
category: RecSys
direction: 候选集陈旧度过滤 · LLM 蒸馏 + 流量预测
tags:
- staleness filtering
- LLM distillation
- multimodal PTR
- candidate pruning
- Google Discover
one_liner: 用 LLM 蒸馏的 pairwise 超替检测与多模态流量比例预测在排序前过滤陈旧内容，Google Discover 用户投诉降 54.9%
practical_value: '- 把候选集陈旧度拆成「超替」和「衰减」两类，分别用 pairwise 关系模型和内容流量预测做上游 OR 过滤，可复用到电商的促销/价格/库存更新、广告素材生命周期管理；在排序前剪枝还能直接省
  CPU/TPU。

  - 用 LLM 合成 pair 训练数据时，先聚类去冗余、再在中等相似度区间加权采样，能显著提高正样本比例；同时监督 rationale 比只监督 class
  更好，并可加入 NLI 等 pair 关系辅助任务。

  - PTR 类流量预测建议用 search-click / 主动意图信号，不用 page-view，避免 Publisher 推广 bias；多模态 early
  fusion + 多 horizon 多任务输出，比 late fusion 更省也更强，决策时取已过最大 horizon 的单调阈值即可。

  - 在线评估体验类指标可借鉴 prevalence-delta A/B：按实验组 vs 对照组的 view delta 采样 item 做人评，解决用户投诉稀疏的统计功效问题；item-level
  无个性化信号离线缓存、serving 时查表，不增加在线推理成本。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
推荐系统的时间敏感性使陈旧内容成为用户投诉的主要来源。传统 age cutoff 一刀切，engagement 启发式滞后，无法区分「被新进展取代」（超替）与「自身生命周期衰减」两种机制。Google Discover 日活数亿，需要在候选集上游提前剪掉 stale items，既提升体验又降低排序计算成本。

**方法关键点**
- 将陈旧度拆为两个互补信号：relational supersession 和 intrinsic decay，用 OR 融合作为最终 staleness 判定。
- 关系型过滤器：用 PaLM 2-L 作 teacher 合成 110 万 pair 数据；采样时聚类去冗余并在中等相似度带加权，产出 rationale+class；通过两阶段多数投票得到标签；蒸馏到 T5 11B 学生，训练时监督 rationale（CoT 式）并加入 NLI 辅助。
- 内在衰减过滤器 PTR：多模态 early fusion 输入 text/image/video，多 horizon 预测头，训练目标为 30 天窗口内各 horizon 的累计搜索点击流量占比；预测值达到阈值 θ 后过滤，决策时 mask 掉未到达的 horizon。
- 两过滤器均为无个性化、item-level 信号，离线计算缓存，在线只查时间戳，serving 无推理开销。

**关键实验**
- 关系模型 Gen+NLI 测试 F1 84.79，人类 golden set precision 83.5 / recall 95。
- PTR early fusion 80% vs late fusion 76%；θ=0.9 时的 stale-item 分类 F1 在 5/5 标注一致集上 87.5。
- 在线 prevalence-delta A/B：SDF Δstale −6.91±2.23%，显著优于 baseline −0.10±1.22% 及单过滤器。
- 两年部署：用户陈旧反馈总降 54.9%，超替降 64.0%，衰减降 34.4%；关系过滤器省 4.76% CPU/TPU，PTR 省 3.98%。

> 最值得记住的一句话：把「陈旧」拆成「被新内容取代」和「自身流量吃完」两类，分别用 LLM 蒸馏的 pairwise 判别与内容流量预测在排序前 OR 过滤，能同时拿到体验提升和成本节省。
