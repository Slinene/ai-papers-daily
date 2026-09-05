---
title: Tail-Likelihood Reinforcement Learning
title_zh: 尾部似然强化学习
authors:
- Shrinivas Ramasubramanian
- Daman Arora
- Fahim Tajwar
- Guanning Zeng
- Qingyang Wu
- Zhongzhu Zhou
- Chenfeng Xu
- Haiwen Feng
- Yuda Song
- Aarti Singh
affiliations:
- Carnegie Mellon University
- University of California, Berkeley
- Impossible, Inc.
- Together AI
- Aurora Innovation
arxiv_id: '2609.02987'
url: https://arxiv.org/abs/2609.02987
pdf_url: https://arxiv.org/pdf/2609.02987
published: '2026-09-02'
collected: '2026-09-05'
category: Training
direction: 生成式策略的尾部优化RL训练
tags:
- RL
- Tail Optimization
- Generative Policies
- Best-of-k
- Advantage
one_liner: 通过最大化超过随机奖励阈值的对数概率，保留生成式策略对稀有高奖励样本的覆盖，提升Best-of-k性能
practical_value: '- 在生成式推荐/搜索词/广告文案场景用 RL 优化连续奖励（点击率、转化价值）时，可借鉴 TailRL 将连续奖励按随机阈值二值化，转化为“超过阈值”的成功事件，让训练更关注高价值尾部样本，避免模型只学会平均平庸输出。

  - 推理阶段若使用 Best-of-N 采样/重排序，训练时需保留高奖励候选的覆盖。TailRL 的梯度可视为 Best-of-k 梯度混合，能防止尾部坍塌，直接提升线上多候选采样收益。

  - 工程实现成本低：只需修改 advantage 函数或奖励处理逻辑，兼容已有 RLHF/GRPO/PPO 流程，适合现有 LLM 推理微调管线快速验证。

  - 对回报分布长尾的业务（大促高转化、高客单、优质内容）尤其有效，可通过动态阈值模拟不同业务指标分位，平衡模型在不同难度目标间的泛化。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

动机：RL 通常优化平均奖励，但生成式策略的平均奖励无法区分对稀有高奖励样本的覆盖能力。两个策略均值相同，但高奖励尾部概率可能差异巨大；而训练和推理阶段采样增加时，收益依赖保留高奖励概率质量。标准 RL 训练可能逐渐丢失稀有高奖励样本覆盖，导致 Best-of-k 退化。

方法关键点：TailRL 不看期望奖励，而把连续奖励转化为一族二元成功事件——对每个阈值，问策略超过该阈值的概率。优化目标是最大化超过随机选取阈值的对数概率。其梯度对稀有高奖励 rollout 赋予更高权重，并可解释为 Best-of-k 梯度的混合。实现上只需修改 advantage 函数，与现有 RL pipeline（如 PPO/GRPO）兼容。

关键结果：在目标定位、迷宫导航、GUI grounding 和代码优化四个任务中，TailRL 利用稀有高奖励训练样本避免次优解，并使模型在推理时从额外采样中获得更大收益，验证了其对尾部覆盖和 Best-of-k 性能的提升。
