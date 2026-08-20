---
title: 'SIDScope: A Diagnostic Resource for Semantic-ID Interfaces in Generative Recommendation'
title_zh: SIDScope：生成式推荐中 Semantic-ID 接口的诊断资源
authors:
- Jiandong Ding
- Huijie Qin
- Tiandeng Wu
- Yi Cao
affiliations:
- Huawei Technologies Co., Ltd., Shanghai, China
arxiv_id: '2608.18779'
url: https://arxiv.org/abs/2608.18779
pdf_url: https://arxiv.org/pdf/2608.18779
published: '2026-08-19'
collected: '2026-08-20'
category: GenRec
direction: 生成式推荐 · Semantic ID 接口诊断与生命周期
tags:
- Semantic ID
- Generative Recommendation
- Evaluation
- Artifact
- Reproducibility
- Trace Accounting
one_liner: SIDScope 把 Semantic-ID 映射做成可复用接口诊断资源，发现路径存活与唯一命中间存在 1.2–3.0pp 缺口
practical_value: '- 在电商/生成式推荐落地 Semantic ID 前，先用 D1–D5 做 artifact 准入：检查 full-code
  collision item rate（D2）、tail unique-SID ratio（D4）、prefix co-occurrence recall（D3）与
  trie fan-out（D5）。不要只看下游 NDCG；collision-free 但 prefix 行为弱时，生成器可寻址但曝光差。

  - 若召回/打分逻辑直接消费 SID prefix，可用论文的 prefix-candidate protocol 做免训练曝光检查：用历史 item 的共享
  prefix 生成候选集，评估 held-out target 是否被覆盖；D3 对这种 prefix-based operation 校准度高（ρ≈0.96），但换成
  co-occurrence/popularity/metadata scorer 后关联显著下降，所以 prefix 无关评分需单独评估。

  - 训练束解码后必须区分 path survival 与 unique-item hit；约束解码可以消除 invalid path，但 collision 导致的
  ambiguous path 仍会幸存。监控 ambiguous row rate 与“目标路径存活−唯一命中”差距，尤其在 collision 率高的映射（如
  GRID/P5 上 2.0–3.0pp）上，否则线上会出现多个商品共享同一生成 SID 导致无法唯一召回。

  - SID 映射刷新/重建后，不要假设旧 generator 可继续复用；执行 D6 风格 paired diff 和单独 handoff check。对内部
  artifact 治理，可借鉴 C0–C5 源追溯、hash、license 与 manifest 机制，把 mapping 版本与模型版本绑定审计。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
Semantic-ID 已成为生成式推荐的核心接口，但已发布的 item-to-code 映射通常缺少系统诊断：是否可寻址、前缀是否暴露行为结构、生成路径能否唯一解析、刷新后需要重验什么。单一排序指标无法回答这些 artifact 层问题，容易导致后续 generator 在坏接口上训练。

**方法关键点**
- 定义统一 artifact 记录 `R=(I,c,P;M,X,R,T)`，把映射、来源、交互、刷新对与生成束路径绑定为同一对象。
- 设计 C0–C5 准入契约，逐层校验来源身份、schema、join、诊断执行、可复现性与矩阵角色。
- 提供 D1–D5 映射诊断：D1 码空间利用率，D2 full-code/prefix collision item rate，D3 prefix 与交互共现的加权召回，D4 头/中/尾 unique-SID 比例，D5 trie 结构与 fan-out。
- D6 做 paired refresh diff；D7 做生成束的路径到 item 解析，区分 path survival、unique-item hit 与 ambiguous path。
- 基于 9 个源追溯导出（8 个可执行 C0–C5 route + 1 个可审计快照），跨 Amazon 与 Yelp，覆盖 ReSID、GRID、CARD、DIGER、ReSOT、LETTER、LC-Rec 等 7 个方法家族。

**关键实验与数字**
- D3 与 prefix-candidate recall 在 per-artifact aggregate 上 Spearman ρ=0.958；去掉控制行后 ρ=0.976（exact p=0.0004）；按 catalog collapse 后 ρ=0.900（p=0.083）。
- 当 scoring 变为 co-occurrence/popularity/metadata-category 等 prefix-independent 方式时，D3–NDCG@20 关联明显减弱甚至到 0.001（random-negative pool）。
- 在 trained trie-constrained beam 上，GRID/P5 两个 split 的 target-path survival 比 unique-item hit 分别高 3.0pp 与 2.0pp，DIGER sensitivity route 高 1.2pp；GRID/P5 的 ambiguous row rate 达到 34.0% 与 37.1%。
- DACT refresh 案例显示，修复映射本身不会自动恢复继承的 generator，模型复用需要单独 handoff check。

**最值得记住的一句话**
Semantic-ID 映射是接口状态而非单一质量分数；生成路径能存活不代表能唯一命中目标 item，映射修复也不等于模型可复用。
