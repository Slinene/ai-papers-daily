---
title: Learning to Solve Hard Problems in RL for LLMs by Never Giving Up
title_zh: 在LLM强化学习中通过永不放弃采样解决难题
authors:
- Michael Noukhovitch
- Hamish Ivison
- Nathan Lambert
- Aaron Courville
affiliations:
- Mila, Université de Montréal
- Allen Institute for AI
- University of Washington
- Trillium Labs
arxiv_id: '2609.13443'
url: https://arxiv.org/abs/2609.13443
pdf_url: https://arxiv.org/pdf/2609.13443
published: '2026-09-10'
collected: '2026-09-16'
category: Training
direction: RL for LLMs 动态采样训练优化
tags:
- RL for LLMs
- GRPO
- dynamic sampling
- curriculum
- asynchronous RL
- Matthew Effect
one_liner: 揭示RL训练LLM的“马太效应”，提出NGU动态采样将计算从易题重分配到难题，显著提升困难任务pass@1
practical_value: '- 在 RLHF/GRPO 训练推荐、对话或 Agent 策略时，若 prompt/任务难度差异大，可借鉴 NGU：用异步 RL
  对简单 prompt 快速过滤，对困难 prompt 持续采样直到出现正样本；但需设置继续采样概率 p 并限制历史 completion 的 age，避免 off-policy
  噪声。

  - 对于需要同时满足多个约束的电商导购 Agent 或广告文案生成，标准 per-aspect reward 会导致模型只优化容易满足的约束。可先按模型初期 pass
  rate 重分难度，再对难样本动态加采样，提升所有约束全部通过率。

  - 工程上，NGU 的 anchor positives 比直接 downsampling 稳定：保留所有正样本，对负样本按比例 rescale advantage
  保持组内优势之和为零；推荐优先使用。

  - 离线评估要按难度分桶（如按用户分群、query 难度）分别报告提升，避免整体指标掩盖马太效应；同样适用于推荐系统的长尾 item/query 优化。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
RL post-training 在数学、代码、Agentic coding 等任务上呈现明显“马太效应”：初始模型已能解决的简单问题获得大幅提升，而困难问题提升甚微。对 Olmo 3.1 RL-Zero、DeepCoder、DeepSWE 的分析表明，RL 改善与初始 pass@1 成正比。标准 GRPO 对每个 prompt 固定采样 K 个 completion，导致计算大量浪费在易题上：K 过大时易题中仅一个错误样本就会让整个 group 进入训练，造成冗余；K 过小时难题难以采样到正样本。实验表明单纯增大 K 并不能解决难题，反而降低整体表现。

**方法关键点**
- NGU 基于异步 RL：每个 prompt 先采样 K=4 个 completion；若全对则快速过滤，若全错则以概率 p_NGU 继续采样 K 个，直到出现正确 completion 或放弃，形成几何分布的采样次数。
- 收集到的历史 completion 构成大的 GRPO group：只保留 age < T=4 的 rollout 用于更新；利用所有历史奖励计算 baseline，对保留的正样本 anchor，并将负样本 advantage 按 n+/n- 比例 rescale，保持组内优势之和为零。
- 设计选择：stale 过滤 T=4 最佳；anchor positives 优于 downsampling 和 no rescale。

**关键结果**
- GSM8k Platinum：固定总 batch size 下，K=4 优于 K=8/16/32；NGU 进一步在 extra hard 子集上提升，并且训练 batch 中难题占比接近 Pareto 最优。
- Deepscaler math（Qwen3 4B）：NGU 在 hard/easy 性能权衡上优于所有固定 K 配置，也优于基于初始难度的 curriculum learning。
- Manufactoria coding：标准 GRPO（per-test reward）停滞在 80% 左右测试通过率，无法让单个问题通过全部测试；NGU 持续提升 hard tests，最终学会通过所有测试，恢复效率与 all-tests reward 相当。

**最值得记住的一句话**：RL 训练 LLM 不应该对所有 prompt 固定分配采样预算，而应动态地将计算从易题转移到难题——快速过滤已解决项，持续尝试未解决项，同时控制 off-policy 陈旧度。
