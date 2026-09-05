---
title: 'Locked at the Entrance, Open Inside: Where RLVR Narrows the Solution Space'
title_zh: 入口锁定，内部开放：RLVR 收窄推理解空间的位置研究
authors:
- Qiancheng Zhou
- Ruizhe Li
affiliations:
- School of Future Technology, Shanghai University
- School of Computer Science, University of Birmingham
arxiv_id: '2608.29188'
url: https://arxiv.org/abs/2608.29188
pdf_url: https://arxiv.org/pdf/2608.29188
published: '2026-08-28'
collected: '2026-09-05'
category: Reasoning
direction: RLVR 推理多样性收缩与入口干预
tags:
- RLVR
- reasoning diversity
- entropy collapse
- test-time scaling
- parameter interpolation
- Countdown
one_liner: 定位 RLVR 训练后解空间收缩集中在首个算术操作前，提出晚期参数插值在保持 pass@1 下恢复 37% 覆盖。
practical_value: '- 电商/搜索/Agent 场景用 RLVR 或 RLHF 优化 LLM 后，要监控早步 token 熵：若首步熵快速塌缩，生成候选的多样性和长尾覆盖会下降，影响
  query 推荐、文案生成和探索型 Agent。

  - 想要恢复多样性但不想牺牲主指标，可尝试参数级干预：将晚期层参数与早期 checkpoint 插值，比 surface prompt 有效，类似推荐模型在 exploit/explore
  间做平滑 trade-off。

  - 训练管线建议优先 staged SFT–DPO–RLVR，而不是直接上 RLVR；这样能保留早步熵，避免削弱后续多次采样、self-consistency、树搜索等
  test-time scaling。

  - 若业务依赖 RLVR 后模型生成多个候选，不要指望 prompt 层“生成更多样方案”能救回来，需要从训练状态或解码策略入手。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：RLVR 大幅提升单样本准确率（pass@1），但收缩策略解空间，导致重复采样、自一致性等 test-time scaling 收益递减。需要定位多样性丢失发生在推理轨迹的哪个阶段。

**方法关键点**：以 Countdown 任务为对象，将解空间按“首个操作数与运算符”穷举为 discrete entrance families，对比 PPO（Qwen2.5-3B）和 GRPO（Qwen2.5-3B-Instruct）。分析各 family 覆盖率、首算之前/之后的逐 token likelihood shift，并通过仅提供未选 entrance prefix 区分“无法发起”与“无法执行”；随后尝试 surface prompting 与 late-layer 参数插值（与早期 checkpoint 插值）恢复多样性。

**关键结果**：两种训练下解覆盖率最多下降 67%，即使全程可解的问题也减半；收缩集中在入口：首算前逐 token likelihood shift 是下游推理的 11–16 倍。仅给未选 entrance prefix 可将低访问 family 完成率从 0.018 提升至 0.212（PPO），证明替代方案仍可执行但不再被发起。晚期参数插值在 pass@1 不降的前提下恢复 37% 解覆盖率；surface prompting 无效。在 6 个数学基准、7B/14B 模型上复现早步熵塌缩，但 SFT 基线保留 2 倍以上覆盖率，SFT–DPO–RLVR 分段管线可保留早步熵。
