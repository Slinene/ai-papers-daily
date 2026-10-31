---
title: 'There Is No Free Lunch in RLVR: Every pass@1 Gain Has a pass@k Price'
title_zh: RLVR 无免费午餐：pass@1 提升必付 pass@k 代价
authors:
- Yinuo Liu
arxiv_id: '2610.39295'
url: https://arxiv.org/abs/2610.39295
pdf_url: https://arxiv.org/pdf/2610.39295
published: '2026-10-29'
collected: '2026-10-31'
category: Training
direction: RLVR 训练中 pass@1 与 pass@k 权衡
tags:
- RLVR
- pass@k
- reasoning models
- exponential tilt
- entropy collapse
- inference compute
one_liner: 用定理证明 RLVR 中 pass@1 增益必然伴随 pass@k 下降，并给出精确权衡边界与诊断方法
practical_value: '- 在电商/搜索/推荐中用 RLVR 微调 LLM 生成式召回、query 推荐或 Agent 策略时，不能只看 top-1 命中或
  pass@1：pass@1 显著提升可能以牺牲 pass@k 覆盖率、多样性和长尾生成为代价，必须同时监控 pass@k 或候选多样性指标。

  - 论文提供的诊断方法（从 eval log 读 pass@1-pass@k 前沿、order-preserving test、price）可直接迁移到线上 AB：评估生成式推荐/搜索改写模型的
  exploration-exploitation 权衡，避免只优化单点指标。

  - 熵崩溃结论提醒：RL 微调后生成多样性会塌缩，电商文案、push 消息、搜索 query 生成需要加熵正则或约束，防止生成同质化候选影响后续排序与多样性。

  - 多 prompt/多任务联合优化时注意“独家专业化”现象：提升某些 query 模板或类目的生成成功率可能损害另一些，需按 prompt/类目分层监控并设置约束。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：RLVR 训练后模型 pass@1 提升，但采样预算 k 增大时基模型会反超，引发争论：是 RL 未能增加推理能力，还是训练不足的暂时现象？

**方法关键点**：将 RLVR 建模为对基础策略在跨 prompt 共享策略上的指数倾斜。在“独占专业化”假设下，用 Stiemke 对偶等证明：任何提升 pass@1 的更新必然降低某些 prompt 的成功率；正 prompt 价格是精确条件，而“只是某 prompt 上最优策略”并不足够。进一步，loss 触及最难 prompt 时强制出现 pass@k 交叉，交叉数量由逐 prompt 成功率的符号变化（全正性上界）限定，且该界紧，可恢复已知单交叉结果。同一倾斜恒等式还导出熵崩塌与熵-性能律，统一两股文献。

**关键结果**：RLVR 无法拓宽推理前沿，只能沿前沿移动；受约束更新可描绘精确的 pass@1-pass@k 前沿，彻底移除交叉会损失全部 pass@1 增益。论文给出可从任意评估日志读取 bound、order-preserving test 和 price 的诊断方法。结论是：没有免费午餐，只有可度量的价格。
