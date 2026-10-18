---
title: 'EMO: A Closed-Loop Test-Time Computation Framework via Alternating Context
  Optimization and Logits Steering'
title_zh: EMO：交替上下文优化与 logits 引导的闭环测试时计算框架
authors:
- Wei Xia
- Yehui Tang
- Zhi-Hong Deng
affiliations:
- Peking University
- Samsung Research Beijing
arxiv_id: '2610.22160'
url: https://arxiv.org/abs/2610.22160
pdf_url: https://arxiv.org/pdf/2610.22160
published: '2026-10-15'
collected: '2026-10-18'
category: LLM
direction: 测试时计算 · 上下文优化与 logits 引导
tags:
- test-time computation
- context optimization
- logits steering
- training-free
- LLM reasoning
one_liner: 训练免费的测试时框架 EMO 交替进行上下文估计与 logits 引导，平均提升 9.1 个百分点。
practical_value: '- 在电商文案/搜索 query 生成等场景，可复用 EMO 的闭环测试时优化：用在线反馈或 LLM 评判器生成文本梯度，仅更新任务上下文提示而不微调模型，快速适配热点词、活动规则或用户意图变化。

  - M-step 的 logits 对比修正思路可借鉴为轻量级生成控制：在同一 prefix 下对比“优化后上下文”与“旧上下文”的 next-token 分布，得到方向向量后对输出
  logits 加权，类似 contrastive decoding / classifier-free guidance，无需额外训练，适合控制推荐理由或广告标题的风格/关键词偏向。

  - 结果提示测试时算力分配：候选生成 + 验证/选择优于单纯增加 best-of-N 采样数量；成本敏感的生产环境可优先用更少候选 + 更强验证器，而不是堆采样数，尤其对
  Llama 等模型效果更明显。

  - 对 Agent 类系统有借鉴：外部评判器的文本反馈可作为上下文更新信号，让 agent 在多次交互中自我修正，无需访问 ground truth；但需额外日志与延迟预算，适合离线批处理或准实时场景。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：测试时上下文优化虽能适应冻结 LLM，但普通条件生成无法独立控制对上下文更新引起的分布偏移的强化程度，导致适应不稳定。

**方法**：EMO 训练免费框架，受 EM 启发交替执行 E-step 与 M-step。E-step 利用外部评判器的文本梯度更新问题相关系统上下文，无需金标答案。M-step 在同一前缀下对比修订前后上下文的下一 token 分布，构建置信度约束的 logit 修正向量，实现对分布偏移的可控强化；引导后响应的反馈再用于驱动下一轮上下文更新，形成闭环。理论上将参数优化与上下文优化统一到共享目标 KL 与加性 logit 表示，并在假设下证明小强度引导可单调降低目标 KL。

**结果**：在 8 个模型、6 个基准上，贪婪解码下 40 个聚合设置中 39 个提升，平均 +9.10 pp；相比仅上下文优化 TextGrad 平均再 +1.53 pp；与 best-of-N 对比，在匹配生成预算下 Llama 优势最强，且多数对比中 oracle 覆盖率更高，提示测试时算力应联合分配给候选生成和验证。
