---
title: Personal-Agent Mediated Recommendation with Cross-Platform User History
title_zh: 跨平台用户历史驱动的个人代理中介推荐
authors:
- Yu Xia
- Jiangfan Zhang
- Jun Xiao
- Julian McAuley
- Xiangjun Fan
affiliations:
- University of California San Diego
- Meta AI
arxiv_id: '2610.07588'
url: https://arxiv.org/abs/2610.07588
pdf_url: https://arxiv.org/pdf/2610.07588
published: '2026-10-05'
collected: '2026-10-07'
category: GenRec
direction: Personal Agent 中介推荐 · 跨平台历史
tags:
- Personal Agent
- Cross-Platform
- LLM4Rec
- PAMO
- MediateRec
- GRPO
one_liner: 用反事实掩码估计跨平台历史归因，在 LLM 重排平台榜单时做价值保序的优势再分配
practical_value: '- 在电商/广告推荐中，平台强排序通常已编码 population evidence，Agent 直接重排容易产生 harmful
  override。可借鉴论文的 rescue–harm 双指标：评估 LLM 重排时只报 HR/NDCG 不够，要同时监控 rescue rate 和 harmful
  override rate，尤其关注 top-K 中被替换掉的原始命中。

  - PAMO 的反事实归因思路可迁移到跨域推荐：训练 agent 时，mask 跨域/跨平台上下文后对同一 rationale 重新打分，得到 context
  dependence score；再将该 score 注入 RL advantage 分配，避免模型仅凭 outcome reward 学到 generic rerank，而不是真正用上外部用户行为。

  - 价值 floor 约束值得工程化：不要只用上下文依赖度分配 advantage，要求重分配后的平均 platform-relative NDCG 不下降。这能抑制“高依赖但低价值”的
  intervention，适合平台上做生成式重排时保护强排序基线。

  - 成本上，PAMO 只增加一次 masked teacher-forced 前向，不增加 rollout，无推理时开销；用 4B 开源模型即可在多个场景超过闭源
  LLM。对搜索/推荐 Agent 训练有直接复用价值。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**

推荐正在从平台中心化走向用户治理：个人 LLM agent 可以持有跨平台用户历史，并在平台排序之上做中介。但平台排序包含个人 agent 看不到的群体协同证据，agent 用跨平台历史修正平台结果时，既可能 rescue 平台漏掉的真实偏好，也可能 harmful override 平台原本正确的强项。现有 agent 推荐大多把 LLM 放在平台侧，较少研究用户侧 agent 如何选择性改写一个已经很强的平台榜单。

**方法关键点**

- 形式化 Personal-Agent Mediated Recommendation：平台给出 proposal `(C, ρP, M)` 和默认 top-K slate `P`；agent 生成 rationale 和最终 slate `S`。核心指标是 rescue 与 harmful override 的差值。
- 提出 MediateRec benchmark：用 Amazon Reviews 四个 category 构造 proxy 平台，目标类别为 within-platform history，其他类别为 cross-platform history；OpenPlay 提供真实跨平台 Steam/Nintendo/Xbox 外测。平台排名由 SASRec + Claude Sonnet 冻结，保证强基线。
- 提出 PAMO 训练方法：采样 rollout 后，mask 跨平台历史，对同一 rationale 计算 personal mediation support `c_g`，即 full-history 与 within-only 下 likelihood 的对数比；把 NDCG 分解为 `K` 个 cutoff 的边际贡献，在平台 disagreement 集合内做 support-tilted 权重分配，同时用 value floor 约束不降低平均 platform-relative NDCG。
- 理论证明 PAMO 保留 cutoff-level advantage mass，并在所有保序一阶再分配中局部最优。

**关键结果**

在 Movie/Toy 两个 seen 平台、Grocery/Beauty 两个 unseen 平台，以及 OpenPlay 真实跨平台测试上，PAMO 均优于匹配的 GRPO 基线：例如 Movie HR@10 从 GRPO 61.2 提到 62.2，OpenPlay HR@10 从 47.4 提到 47.9，同时 harmful override 率下降。消融显示，只给跨平台历史而不训练，基座模型反而低于平台；移除 value floor 后 PAMO 明显变差。对 PAMO 成功 rescue 的 900 个 episode 标注显示，72% 的干预由跨平台上下文驱动，说明模型确实学会何时用外部证据覆盖平台排序。

**最值得记住的一句话**

有效中介不是拥有更多用户历史，而是学会何时让跨平台证据覆盖平台群体证据，并在不能覆盖时保持克制。
