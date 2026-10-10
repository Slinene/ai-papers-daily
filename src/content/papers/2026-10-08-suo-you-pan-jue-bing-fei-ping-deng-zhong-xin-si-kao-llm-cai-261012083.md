---
title: 'All Verdicts are Not Equal: Rethinking LLM Judge Reliability'
title_zh: 所有判决并非平等：重新思考 LLM 裁判可靠性
authors:
- Vineet Kumar
- Darshita Rathore
- Anindya Moitra
affiliations:
- PayPal
arxiv_id: '2610.12083'
url: https://arxiv.org/abs/2610.12083
pdf_url: https://arxiv.org/pdf/2610.12083
published: '2026-10-08'
collected: '2026-10-10'
category: Eval
direction: LLM-as-a-Judge 可靠性审计
tags:
- LLM-as-a-Judge
- Reliability
- Evaluation
- Position Bias
- Prompting
- Rubric Scoring
one_liner: 对 LLM-as-a-Judge 进行系统可靠性压力测试，提出可信判决率 T，并发现 rubric 打分比成对胜负更可信
practical_value: '- 在电商/搜索评估链路中不要用单次 LLM 成对判定作为 ground truth：至少交换待比较项顺序、重复采样多次、记录一致性；可引入类似可信判决率
  T 的联合概率作为上线门槛。

  - 位置偏差对 pairwise 评估影响严重，尤其是困难样本；推荐策略 A/B 对比、query 改写/生成质量评估应优先使用整体 rubric 打分（分维度评分），而不是直接问法官谁赢。

  - temperature=0 不等于确定性；若业务依赖 LLM 自动打分生成训练信号（如 RL reward），必须显式固定 seed、多轮采样并丢弃不一致样本，防止错误信号被误认为稳定标签。

  - 可靠性是 item-specific 的，不适合只看模型级平均准确率；对高价值场景（大促文案、头部商品推荐理由）按 item/类目统计置信度，低可信样本人工复核。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：LLM-as-a-Judge 已成为 NLP 评估标准范式，被当作确定性 ground truth 来提供奖励信号、模型对比和 benchmark 打分，但系统可靠性缺乏审计。

方法关键点：对六个前沿模型在四个 benchmark 上压力测试，覆盖五种 prompt 格式、两种呈现顺序、三个采样温度、每个条件重复十次。提出可信判决率 T，定义为判决可复现、顺序不变且准确的联合概率，并推导位置偏差对准确率的上界。

关键结果：温度 0 下相同输入重复仍产生不同判决；困难任务上交换顺序翻转多数判决；最确定性的法官能完美一致但只是重复错误判决，与 ground truth 一致率仅 51%；可靠性是 item-specific，而非 model-level；从 pairwise win-rate 改为 holistic rubric scoring 对可信度的提升超过任何单一 prompt 干预。
