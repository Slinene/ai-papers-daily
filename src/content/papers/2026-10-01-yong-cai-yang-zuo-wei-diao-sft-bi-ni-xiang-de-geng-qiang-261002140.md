---
title: 'Finetuning with Sampling: SFT Learns Better Than You Think'
title_zh: 用采样做微调：SFT 比你想的更强
authors:
- Aayush Karan
- Sitan Chen
- Yilun Du
affiliations:
- Harvard University
arxiv_id: '2610.02140'
url: https://arxiv.org/abs/2610.02140
pdf_url: https://arxiv.org/pdf/2610.02140
published: '2026-10-01'
collected: '2026-10-02'
category: Training
direction: LLM 后训练 · MCMC 数据分布塑造
tags:
- SFT
- MCMC
- on-policy
- off-policy
- catastrophic forgetting
- posttraining
one_liner: 用投影采样把离策略专家轨迹逐步变为接近基座模型分布的数据，使 SFT 在科学、数学、医学任务上超越 RL 与自蒸馏
practical_value: '- 在电商/导购 Agent 里做 LLM 后训练时，如果手里有 GPT-4/GPT-5 生成的专家轨迹（如 query 改写、商品文案、购物建议），不要直接
  SFT。可以先跑一遍投影采样，把专家轨迹改写到基座模型自己的分布附近，再做 SFT，能明显减少通用能力遗忘。

  - 对难以写出 reward 的开放任务（如导购对话、医学/法规咨询生成），可以先采样出 on-policy 版本的高质量轨迹，再 SFT；这比直接上 GRPO/RL
  更稳，工程上只需要离线数据加工，不改变现有 SFT 训练管线。

  - 采样成本是一次性的，适合电商场景里「预先生成训练数据 → 日常微调」：建议 B=32、N_MCMC=10 起步，后续用 MCMC 步数作为数据质量与 token
  成本的旋钮；图 5 表明加采样步数能单调降低数据 KL、提高下游精度。

  - 如果要继续上 RL，采样 SFT 的 checkpoint 是很好的 RL 初始化，数学任务里 Sampling SFT + RL 拿到了更强结果；在商品推荐
  Agent 的 RL 训练前可用同方案做 warm-start。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

动机：后训练要在引入新能力的同时不丢已有能力。通常认为 RL 泛化好但依赖模型自己采到成功轨迹；SFT 能利用离策略专家数据，但容易弱泛化和灾难性遗忘。核心问题是如何保留离策略专家信息，同时让训练数据更接近基座模型分布。

方法关键点：
- 目标分布定义为信息投影 p_C(x)∝p(x)·1[x∈C]，即在保持与专家轨迹语义等价的前提下，与基座模型 KL 最近的分布。
- 用 Metropolis-Hastings 从专家轨迹初始化，分块续写：随机截断后缀，让基座模型在「问题 + 专家解 + 部分轨迹」的提示下完成续写，再按基座模型似然比接受/拒绝候选。
- 采样只发生在训练前，一次性成本；实验设置 B=32、N_MCMC=10、最大长度 T=1856。增加 MCMC 步数会单调降低生成数据与基座模型的 KL。

关键实验：在 Chemistry、MATH(3,4,5)、Medical 三个任务上评测。Chemistry 任务 Qwen2.5-7B-Instruct 从 base 34.3% 提升到 66.0%，超过 OPSD 的 61.8%，且遗忘最少；SFT 平均旧能力从 59.7% 掉到 52.0%，而 Sampling SFT 仅降到 58.6%。Math 任务 Qwen2.5-3B 在 MATH(3,4,5) 上从 31.5% 提升到 49.5%，超过 GRPO 45.7% 和 UFT 47.0%；MATH500 从 24.5% 提升到 58.2%。医学开放域任务中，Sampling SFT 保留旧能力最好。

最值得记住的一句话：不是改 loss 去迁就离策略数据，而是改数据分布去迁就 learner；采样可以作为后训练栈里的模型原生算子，把专家数据变成更容易被 SFT 吸收的 on-policy 数据。
