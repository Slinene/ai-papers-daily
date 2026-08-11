---
title: 'Zero Gap Is Not Restoration: Stratified Per-Question Probability Evaluation
  and Step-wise Mitigation of Benchmark Contamination'
title_zh: 分层概率评估与逐步缓解基准污染：SA-PPG 与 RailCap
authors:
- Ruijie Hou
- Yueyang Jiao
- Zhao Wang
- Yingming Li
affiliations:
- Zhejiang University
arxiv_id: '2608.07341'
url: https://arxiv.org/abs/2608.07341
pdf_url: https://arxiv.org/pdf/2608.07341
published: '2026-08-06'
collected: '2026-08-11'
category: Eval
direction: 基准污染评估与缓解
tags:
- benchmark contamination
- evaluation metric
- decoding intervention
- SA-PPG
- RailCap
- memorization
one_liner: 提出分层每问题概率差距指标SA-PPG与解码干预方法RailCap，更准确评估并缓解基准污染。
practical_value: '- 在生成式推荐或 query 推荐场景中，当训练数据可能被曝光交互污染时，可借鉴 SA-PPG 的分层概率评估思路：按干净模型求解概率分组统计，避免平均化掩盖过抑制与欠抑制。

  - RailCap 的实时解码干预可迁移至生成式推荐的解码阶段：若生成结果接近训练样本的贪婪轨迹，则裁剪概率次高 Token，强制分散分布，提升多样性并减少直接记忆。

  - 对电商 Agent 或 LLM 驱动的筛选/对话系统，在评测生成质量时，应警惕传统 accuracy 指标因 benchmark 污染而虚高，建议补充基于采样概率的细粒度评估。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：公开基准数据泄露至预训练语料，导致模型记忆并虚高评测分数。现有缓解评估指标 G-AP（聚合性能差距）存在三大缺陷：二元正确/错误无法刻画每题的求解概率；先平均后差分使过抑制与欠抑制相互抵消；等权加权易被策略利用。

方法：(1) 提出 SA-PPG（分层每问题概率差距）：对每个问题通过采样估计求解概率，逐题与干净模型差分，再按干净模型求解概率分组聚合，更精确衡量恢复真实能力。
(2) 提出 RailCap 缓解策略：不依赖预先估计污染位置，而在生成过程中实时判断——当采样回退到贪婪轨迹时，将后续 Token 限制为概率次高的，累积抑制直至响应分布充分分散，从而在解码时直接抑制记忆。

结果：在多个污染模型与基准上，SA-PPG 揭示先前策略的恢复效果被大幅高估；RailCap 在所有方法中取得最低的 SA-PPG，表明更有效地恢复模型真实能力。
