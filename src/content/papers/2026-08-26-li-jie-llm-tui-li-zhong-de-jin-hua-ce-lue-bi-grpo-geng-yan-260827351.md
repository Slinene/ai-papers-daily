---
title: 'Understanding Evolution Strategies for LLM Reasoning: Broader Reasoning Coverage
  than GRPO'
title_zh: 理解 LLM 推理中的进化策略：比 GRPO 更广的推理覆盖
authors:
- Yunpeng Ba
- Zhi Zheng
- Yue Xie
- Jiaqing Li
- Xialiang Tong
- Tao Zhong
- Mingxuan Yuan
- Zhichao Lu
- Xuyang Wu
- Zhenkun Wang
affiliations:
- Southern University of Science and Technology
- National University of Singapore
- Huawei Noah's Ark Lab
- City University of Hong Kong
- Harbin Institute of Technology, Weihai
arxiv_id: '2608.27351'
url: https://arxiv.org/abs/2608.27351
pdf_url: https://arxiv.org/pdf/2608.27351
published: '2026-08-26'
collected: '2026-08-28'
category: Training
direction: LLM 推理后训练 · 进化策略
tags:
- Evolution Strategies
- GRPO
- LLM Reasoning
- Pass@K
- Entropy Collapse
- Post-training
one_liner: 系统分析 ES 与 GRPO 的推理后训练行为，发现 ES 保持更广推理覆盖、提升 Pass@K，大参数漂移不必然导致灾难性遗忘
practical_value: '- 作为显存受限或长轨迹 Agent 微调的备选方案：ES 无需 backprop，只做前向 rollout，适合电商 Agent
  长对话、多步工具调用。实现时务必对 population rewards 做 z-score 归一化，并使用 one-point estimator（两 point
  在 regenerated reasoning rewards 上无增益），可节省一半前向成本。

  - 若业务目标需要候选多样性（搜索推荐中的 query 建议、生成式推荐的多个 item 候选、push 文案多版本），考虑 ES 或 ES→GRPO 顺序训练：ES
  保持探索，避免 entropy collapse，提升 Pass@K/覆盖率；再用 GRPO 强化单点准确率。已证明顺序混合可在 Pass@1 和 Pass@K
  之间扩展 Pareto 前沿。

  - 超参数 scaling：大模型（1.5B/3B）ES 用 N=16 即可接近 N=64 的效果，0.5B 需 N=32，说明模型越大所需扰动方向越少。业务上可先用小规模扫描
  population size，以降低评估成本。

  - 参数 drift 大不等于遗忘：ES 更新幅度远大于 GRPO（40 倍以上），但 held-out 性能保持甚至更好，主要更新集中在 LayerNorm
  和 attention。持续学习场景下，可监控 held-out 任务，不必过度担心 drift。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
Evolution Strategies (ES) 作为 memory-efficient 后训练方法，能微调 LLM 推理能力，但其优化行为、灾难性遗忘风险、有效超参数设置均未系统理解。主流 GRPO 虽提升 Pass@1，但存在 entropy collapse，导致大 K 重复采样成功率（Pass@K）下降。需要明确 ES 是否只是低效的 GRPO 替代，还是具有独立优势。

**方法关键点**  
- 理论：定义 verifier-projected Jensen-Shannon diversity，证明参数扰动诱导的群体多样性可提升正确答案发现概率，且在奖励加权与中心更新条件满足时（Proposition 1），ES 更新后的模型可保持 Pass@K 优势。  
- 实验：在两个后训练设置——Easy（Qwen2.5-1.5B/3B/7B 在 GSM8K）和 Hard（DeepSeek-R1-Distill-Qwen-1.5B 在 DeepScaleR）——对比 Base、GRPO、ES，以及顺序组合 ES→GRPO、GRPO→ES（同总更新预算）。  
- 分析：测量 ES 与 GRPO 的参数 drift（相对 L2）、更新幅度分布稀疏性、held-out 任务表现；消融 reward normalization、perturbation scale、population size、one-point vs two-point estimator。

**关键结果数字**  
- Easy Setting 中，GRPO 在 18 个 Pass@16/32 对比中有 15 个低于 base；ES 的 Pass@1/16/32 均高于 base，且 Pass@16/32 高于 GRPO。例：Qwen2.5-1.5B 上 GRPO Pass@1 +7.8pp 但 Pass@32 -1.1pp，ES Pass@1 +2.9pp 且 Pass@32 +0.2pp。  
- Hard Setting 平均 Pass@32：ES 78.9 > GRPO 78.0 > Base 77.4；ES→GRPO 达 79.2，在 Pareto 前沿上提供非支配点。  
- 参数 drift：Full ES 相对 L2 是 GRPO 的 40.7–44.1 倍，但 77.6–93.0% 更新幅度小于 1.5e-3；保留大更新可维持性能。ES 大更新集中在 LayerNorm/attention，GRPO 集中在 embedding/head。  
- held-out 平均 Pass@32 变化：Easy Setting 中 ES 为正，GRPO 为负。  
- 超参数：z-score 归一化关键；大模型 population size 可减半（1.5B/3B 用 N=16 接近 N=64，0.5B 需 N=32）；two-point 无优势。

**最值得记住的一句话**  
在 reasoning 后训练中，ES 以更少显存换取更广的 Pass@K 覆盖，并可与 GRPO 顺序混合平衡单点精度与多样性，适合需要候选覆盖的场景。
