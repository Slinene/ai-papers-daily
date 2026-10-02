---
title: Sharpening Tax in Post-Training
title_zh: 后训练中的锐化税：基座与后训练LLM智能体的覆盖率权衡
authors:
- Changdae Oh
- Qi Zeng
- Qi Qi
- Andrey Zhmoginov
- Deren Lei
- Yun He
- Hoang Phan
- Hangoo Kang
- Azalia Mirhoseini
- Sharon Li
affiliations:
- Meta Superintelligence Labs
- University of Wisconsin–Madison
- NYU
- Stanford University
arxiv_id: '2610.01509'
url: https://arxiv.org/abs/2610.01509
pdf_url: https://arxiv.org/pdf/2610.01509
published: '2026-09-30'
collected: '2026-10-02'
category: Agent
direction: LLM Agent RL后训练 · 测试时扩展诊断
tags:
- Sharpening Tax
- pass@K
- RL post-training
- PTGS
- agentic evaluation
- test-time scaling
one_liner: 提出Sharpening Tax度量后训练对测试时覆盖率的损失，并给出PTGS自适应温度采样以同时提升pass@1与pass@K
practical_value: '- 评估Agent或对话式购物策略时，除了pass@1，应监控pass@K与Sharpening Tax；若业务需要高覆盖/多样性（如商品候选生成、长尾query召回），后训练模型可能过度牺牲覆盖，可保留base模型+轻量harness做多次采样。

  - 在用PPO/GRPO训练推荐Agent或生成式推荐策略时，可引入PTGS：为每个prompt维护Beta成功统计，按难度自适应采样温度，硬任务升温、易任务降温；无需改RL算法，可降低熵崩塌，兼顾单次准确率与长尾覆盖。

  - 仅用8个rollout即可低成本估计Sharpening Tax，相关性ρ=0.85预测更大预算下的tax；可用于上线前诊断或做模型路由：后训练模型处理高置信任务，base模型处理需要探索/候选多样性的任务。

  - RL对齐后的双峰化会使中间难度任务消失，需评估是否把可救回的长尾任务推向永久失败；对电商/广告中的个性化Agent，应关注always fail比例，PTGS可缓解该问题。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：现有关于RL后训练是否只是“锐化”已有行为而非扩展能力边界的讨论，主要集中在数学和代码任务；Agent任务需要多轮工具调用、长程交互和环境反馈，原本预期后训练可能引入新能力。论文系统检验了这一假设。

方法关键点：
- 在BFCL v4 multi-turn、WebShop、ACEBench三个Agent benchmark上，评估14组base/post-trained LLM对（Gemma-4、Ministral-3、Qwen2.5、Qwen3.5），base模型配轻量harness（system prompt + 放宽工具解析）。
- 提出Sharpening Tax：原始可扩展性A(K)=Σ_{k=1}^{K-1}(pass@K−pass@k)，校准版S(K)=A(K)/((K−1)(1−pass@1))；tax为base−post的差值。
- 提出PTGS：RL训练时用Beta-Binomial后验在线估计每个prompt的成功率，按难度设置采样温度T_x=τh(ˆp_x)，硬prompt升温、易prompt降温，可即插即用于PPO/GRPO。
- 理论解释：A(K)为预算内首次成功前的期望失败次数；后训练将任务双峰化导致覆盖损失；PTGS提高包含成功或混合成功/失败的rollout组概率。

关键实验：
- base模型配harness后，随rollout预算K增大能追上甚至超过post-trained模型；例如WebShop上gemma-4-31B base pass@128约85%，而RL模型约56%。
- 后训练模型pass@1更高，但pass@K增长更慢；crossover预算随模型规模增大而提前（Gemma-4 4B到31B，WebShop k*从>128降到≈3）。
- 后训练将per-task成功率双峰化，WebShop中间难度任务占比从87.6%降至30.0%。
- Sharpening Tax在42个模型-benchmark组合中多数为正（Tax_S(128)>0 36/42），且Tax_S(8)可预测Tax_S(32)（ρ=0.85）。
- PTGS在Sokoban/FrozenLake上，PPO/GRPO均同时提高pass@1与pass@128并降低tax；例如PPO Sokoban pass@1 46.5→61.1，pass@128 55.0→69.7，Tax_S 0.094→0.081。

最值得记住的一句话：后训练主要改变模型解决任务的可靠性，而不是扩展可解决任务的范围；可靠性与覆盖面应当一起增长。
