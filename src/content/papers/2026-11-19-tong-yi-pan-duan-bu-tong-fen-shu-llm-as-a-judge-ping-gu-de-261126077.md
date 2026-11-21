---
title: 'Same Judgement, Different Scores: Numerical Scoring Topology in LLM-as-a-Judge
  Evaluation'
title_zh: 同一判断，不同分数：LLM-as-a-Judge 评估中的数值评分拓扑
authors:
- Doyun Kim
- Chanwoo Kim
- Jiwoo Kum
- Minsoo Song
- Chanjun Park
affiliations:
- Soongsil University
arxiv_id: '2611.26077'
url: https://arxiv.org/abs/2611.26077
pdf_url: https://arxiv.org/pdf/2611.26077
published: '2026-11-19'
collected: '2026-11-21'
category: Eval
direction: LLM-as-a-Judge 评分方案设计
tags:
- LLM-as-a-Judge
- scoring topology
- evaluation
- calibration
- robustness
- prompting
one_liner: 系统揭示数值评分拓扑对 LLM-as-a-Judge 评分、校准与鲁棒性的系统性影响
practical_value: '- 在电商/推荐/Agent 场景用 LLM-as-a-Judge 做离线评估时，不要把 1-5、0-10 或带偏移的分数看作是同一量纲：幅度宽度、粒度、偏移、对称性、边界位置都会系统性改变分数，需要在
  prompt 中显式固定 scoring topology，并记录到实验配置。

  - 论文发现 shifted 和 narrow range 会导致最大分数偏差，因此建议优先采用对称、锚点明确、宽度足够大的评分区间；避免使用 1-5 这类窄范围去比较不同模型或版本。

  - 更强更大的 judge 模型对拓扑变化更鲁棒、判别效度更高，因此若用 LLM 评估搜索/推荐/Agent 输出，预算允许时应选更强 judge，且不要轻易更换
  judge 模型或评分协议，否则跨实验分数不可比。

  - 对重要 offline 指标，可以做 scoring-topology sensitivity analysis：固定 prompt 和输出，只改变评分拓扑，观察结论是否翻转；若翻转，说明结论不可信，需要改用
  pairwise 比较或标准化协议。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM-as-a-Judge 已成为降低人工标注成本的主流评估范式，但评分方案设计对其可靠性的影响长期未被系统研究。

**方法关键点**：论文引入 numerical scoring topology，将评分方案的结构拆为 scale width（幅度宽度）、granularity（粒度）、offset（偏移）、symmetry（对称性）、boundary placement（边界位置）五维；在多个 benchmark 和 judge model 上做 zero-shot 评估，固定 evaluation prompt、模型输出、评估标准和 judge model，仅改变数值评分拓扑，比较标准化后的分数。

**关键结果**：数值评分拓扑会系统性改变 judge 分数、校准与鲁棒性，且在判断密集型评估中影响更明显；shifted 和 narrow range 会带来较大分数偏差；更强更大的 judge 模型通常具有更高的判别效度，对评分拓扑变化也更鲁棒。因此，数值评分拓扑应被视为 LLM-as-a-Judge 评估的组成部分，需要更原则化、标准化的评分协议。
