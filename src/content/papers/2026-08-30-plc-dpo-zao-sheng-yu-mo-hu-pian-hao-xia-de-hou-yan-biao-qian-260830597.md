---
title: 'PLC-DPO: Posterior Label Correction in Noisy and Ambiguous Preference Optimization'
title_zh: PLC-DPO：噪声与模糊偏好下的后验标签校正 DPO
authors:
- Boryeong Cho
- Sumyeong Ahn
- Se-Young Yun
affiliations:
- KAIST AI
- KENTECH
arxiv_id: '2608.30597'
url: https://arxiv.org/abs/2608.30597
pdf_url: https://arxiv.org/pdf/2608.30597
published: '2026-08-30'
collected: '2026-09-14'
category: Training
direction: LLM 偏好优化 · 标签修正
tags:
- DPO
- preference optimization
- label noise
- LLM alignment
- robust training
one_liner: 利用校准的策略-参考边际把偏好对路由为 clean/flip/tie，主动校正标签方向与强度，提升 DPO 在噪声和模糊偏好下的鲁棒性
practical_value: '- 若业务中用 DPO/RLHF 对齐 LLM 排序器、广告文案生成或 Agent 行为，可引入基于 policy-reference
  margin 的在线路由：margin 接近 0 或反向时按 tie/flip 处理，而不是硬训，能降低点击/转化等隐式反馈中的误标和争议样本损伤。

  - 不必在数据清洗阶段一次性过滤可疑样本，而是在训练中动态估计并修正监督方向/强度；对搜索推荐中的点击 vs 未点击、或 LLM-as-judge 分歧样本，可构造
  robust DPO 损失，减少 false negative/positive 影响。

  - 对于电商多模态内容或 Agent 行为偏好冷启动，tie 路由提供更平滑监督，适合标注分歧较大的场景；可先做 human disagreement 分析，再设定
  flip/tie 阈值。

  - PLC-DPO 可直接作为 loss 层替换现有 DPO，无需改数据或模型结构，适合已部署 DPO/RLHF 的团队快速验证。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：DPO 假设每个偏好对都完全可靠，但真实数据中常存在反向、弱或模糊标签，直接优化会带来有害策略更新。

方法关键点：PLC-DPO 不再仅过滤可疑样本，而是根据校准后的 policy-reference margin 在线把每个训练对路由为 clean、flip 或 tie 三类。对 clean 保留原方向；对 flip 反转损失方向；对 tie 削弱或置平训练强度，从而主动修正监督方向和强度。这样把噪声偏好学习从被动过滤变为后验标签校正。

结果：在 57 个 dataset-model-benchmark 单元上，PLC-DPO 对 DPO 的平均 win rate 达到 60.5，下一名仅为 55.5；注入噪声、tie 压力测试、人类分歧分析和自我确认诊断均显示其路由稳定，并能区分翻转对与弱方向对。
