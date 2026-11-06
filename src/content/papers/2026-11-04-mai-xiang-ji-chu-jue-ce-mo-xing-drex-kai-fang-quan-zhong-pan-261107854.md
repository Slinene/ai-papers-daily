---
title: 'Towards Foundation Decision Models: Drex'
title_zh: 迈向基础决策模型：Drex 开放权重判别式决策模型
authors:
- Nischay Dhankhar
- Alisher Amantay
- Zhanibek Datbayev
- Darkhan Akhmetov
- Yash Shah
- Nurmukhamed Ubaidullayev
- Raman Saparkhan
- Dos Baha
- Abulhair Saparov
affiliations:
- Nace.AI Research Team
arxiv_id: '2611.07854'
url: https://arxiv.org/abs/2611.07854
pdf_url: https://arxiv.org/pdf/2611.07854
published: '2026-11-04'
collected: '2026-11-06'
category: LLM
direction: 判别式决策模型 · 概率校准与顺序鲁棒
tags:
- decision model
- calibration
- pointer head
- readout head
- RLAF
- option order
one_liner: Drex 系列用 pointer/readout 头直接输出选项概率分布，替代自回归解码，在决策基准上逼近前沿 LLM 且延迟更低
practical_value: '- **把高频判别任务改成决策接口**：商品审核、客服意图、广告合规、搜索相关性等可由 LLM 生成+解析改为“state+questions+options→概率分布”。Drex
  这类模型 183ms 返回，概率可直接做阈值/置信度路由；适合对延迟和成本敏感的生产决策。

  - **同 context 多问题用 pointer 架构**：state 只编码一次并缓存，后续问题仅做短前向，适合同一用户/会话/商品详情下打多个标签；若精度优先且上下文不长，则改用
  readout head + 双向 attention 的 Dense 模型。

  - **训练时加一致性 loss 和 RLAF**：SFT 加入选项置换 KL 和 state 字段 shuffle KL，可把 flip rate 从 6.3%
  降到 4.2%；RLAF 用 verified answer + judge 分布构造 proper scoring rule 目标，并加 KL 到 SFT，提升
  Decision Index 2 点且改善校准。此思路可迁移到 CTR/CVR 概率输出和相关性打分。

  - **上线前把校准和选项顺序作为必测指标**：作者在 230k decisions 上做 ECE/selective accuracy；并证明 multi-order
  averaging 只改善 log loss 不提升 top-1 accuracy。因此不建议为 top-1 做 permutation ensemble，但应训练时加固顺序鲁棒性。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
自回归 LLM + 长 CoT 在判别任务上准确率高，但生产中存在输出不稳定、解析成本高、延迟和费用高。Drex 的目标是用非自回归“决策模型”直接对用户提供的 option 集合输出概率分布，兼顾闭集输出、问题独立性、顺序鲁棒、校准和多模态。

**方法关键点**
- 接口：请求由 state（文本/JSON/可选图片）+ 多个 question 组成；题型为 choice / noul / score，选项数 K≤255，返回 softmax 概率、置信度和期望分值。
- 两种 head：pointer 模型（DLM/v1.5/v2.0）用 <opt>/<decide> token 的 hidden state 做点积，状态只编码一次并跨问题缓存；Drex Max 用 readout head，把最后隐藏态映射到 255 个 option code logits，逐问题重新编码，16 层全局双向 attention。
- 训练：1.15M 条 verified 文本决策记录，覆盖商业/金融/工具路由等 11 个领域；SFT 加选项置换 KL、state shuffle KL 和 NONE/distractor 选项；pointer 模型用 RLAF（proper scoring rule + adjusted target），Max 用 KL 正则化 RLAF，奖励由 verified answer + judge 概率组成；Max 再 SFT image encoder。

**关键实验**
在 Decision Index 0.4.1 上，Drex Max public suite 67.52，超过 Jev 1.14.0 的 60.70 和 v2.0 的 61.25；full score 66.60。Decision Bench v4 上 Max 94.0，接近 GPT-6 Sol 94.7，优于 d3-turbo 93.7 和 Jev 92.3；延迟 183ms vs GPT-6 Sol 2.0s。RLAF 带来 +2.0 Decision Index；一致性 loss 将 flip rate 从 6.3% 降到 4.2%。

**最值得记住的一句话**：决策任务不必自回归解码，用 pointer/readout head 直接对候选选项做 softmax，是同时拿到精度、校准、稳定性和低延迟的关键。
