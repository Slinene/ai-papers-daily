---
title: How to Speculate about Uncertainty in Agentic Coding? A Draft-Model Gate Method
title_zh: 用草稿模型门控预测编程智能体失败的不确定性
authors:
- Konstantin Grotov
- Valentin Malykh
affiliations:
- Tel Aviv University
- IITU
arxiv_id: '2609.05274'
url: https://arxiv.org/abs/2609.05274
pdf_url: https://arxiv.org/pdf/2609.05274
published: '2026-09-04'
collected: '2026-09-07'
category: Agent
direction: LLM Agent 执行前失败预测门控
tags:
- Speculative Decoding
- Uncertainty Quantification
- Agentic Coding
- Draft Model
- Execution Gate
- Black-box LLM
one_liner: 用小型草稿模型对智能体轨迹做投机打分，在动作执行前门控拦截，降低错误率与成本
practical_value: '- 对调用黑盒 LLM API 的 Agent 工具链（如 SQL 查询、搜索 API、广告投放 API），可以在不加 logits
  的情况下做执行前拦截：用一个小型开源草稿模型对已生成的思维-动作轨迹做 teacher-forced 前向，提取 surprisal / gap / entropy，再接线性
  calibrator 预测下一步工具调用是否会成功。

  - 特征工程上务必把 reasoning span 和 action/tool-call span 分开统计。论文显示二者熵分布相反，混在一起会抵消失败信号，phase-aware
  特征带来 +5–6 AUROC。电商 Agent 里常见的“先分析再调接口”结构可以直接复用。

  - 用 veto gate 替换 execute-fail-retry 循环：失败概率高时不执行、注入 replan hint 重新生成，能减少 14–19%
  token 成本、6–8pp 执行错误率，适合对成本敏感、工具调用昂贵的场景；但要注意 false veto 可能轻微拉低端到端成功率。

  - 草稿模型在一个开源 Agent 轨迹上蒸馏后，可迁移到闭源 Agent（如 Claude），因此多模型/多供应商共存的推荐或电商 Agent 平台，可以训练一个通用不确定性打分器。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

动机：生产环境中的 LLM Agent（例如写代码、查库、调工具）常“自信地犯错”，失败只能在环境拒绝后暴露，此时已经付出执行、上下文填充和重试成本。现有不确定性估计通常需要模型 logits/权重或多次采样，无法直接用于闭源 API，且 agent 轨迹长、成本高。

方法关键点：
- 反转 speculative decoding：不用小模型加速生成，而是用一个小型开源 draft model 对 agent 已生成 token 做 teacher-forced 前向，得到 speculative surprisal、gap、entropy 三类信号；无需 agent logits。
- 利用 agent 轨迹的 phase 结构，把 reasoning span 和 action span 分开提取特征；每 phase × 每信号计算 mean、variance、max、min、skew、trend、首尾 10% 均值等 8 个统计量，再加两个 span 长度，共 50 维特征；只看最近 k=3 步窗口。
- 用 L1-regularized logistic regression 把 50 维特征映射为下一步动作成功的概率；下游接 pre-execution veto gate，阈值低于 τ 时阻止执行并触发更便宜的 replan。

关键结果：
- Agent 为 Qwen3-Coder-480B，draft 为 Qwen3-4B；在 SWE-rebench 训练，迁移评估 SWE-Bench Verified 与 DA-Code。
- 失败预测能力：SWE-Bench Verified 上 SU 达到 AUROC .77–.78，优于 verbalized confidence .57、Last-TP .70，接近白盒 HTC 的 .82；去掉 phase separation 后 AUROC 降至 .71。
- 部署收益：SWE-Bench Verified 每步执行错误率从 21% 降到 15%，DA-Code 从 14% 降到 6%；token 成本分别下降 14% 和 19%。
- 跨智能体迁移：Qwen 蒸馏的 draft 在闭源 Claude 3.5 Sonnet 上达到 .69 AUROC，远高于未训练的 .60。

最值得记住的一句话：用小型草稿模型“读”智能体已生成的轨迹，而不是获取智能体内部 logits，就能在动作执行前预测失败并低成本拦截。
