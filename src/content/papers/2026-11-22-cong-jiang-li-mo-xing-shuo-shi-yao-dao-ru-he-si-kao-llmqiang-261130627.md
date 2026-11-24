---
title: 'From Rewarding What Models Say to How They Think: Attention Process Reward
  Model for LLM Reinforcement Learning'
title_zh: 从奖励模型说什么到如何思考：LLM强化学习的注意力过程奖励模型
authors:
- Kairong Han
- Nuanqiao Shan
- Ziyu Zhao
- Xinpeng Dong
- Zijing Hu
- Dian Jin
- Leyan Deng
- Junjian Ye
- Lujia Pan
- Fei Wu
affiliations:
- Zhejiang University
- Noah's Ark Lab, Huawei Technologies
arxiv_id: '2611.30627'
url: https://arxiv.org/abs/2611.30627
pdf_url: https://arxiv.org/pdf/2611.30627
published: '2026-11-22'
collected: '2026-11-24'
category: Training
direction: LLM强化学习 · 过程奖励模型
tags:
- LLM
- Reinforcement Learning
- Process Reward Model
- Attention
- Counterfactual
one_liner: 提出基于隐状态与注意力图的APRM过程奖励模型，以细粒度内部信号提升LLM强化学习效果
practical_value: '- 在电商/搜索场景用 LLM 做多步推理生成（如推荐解释、Agent 工具选择）时，不要只奖励最终点击或转化，可引入中间隐状态/注意力模式的过程奖励，迫使模型走可靠推理路径而非碰答案。

  - 训练一个轻量过程奖励模型（46M 量级）作为插件，用排名 + 反事实样本训练，与 PPO/GRPO 等 RL 方法结合，并周期性更新以应对策略分布漂移；该范式可直接迁移到广告文案生成、query
  改写等 RLHF pipeline。

  - 警惕 text reward aliasing：文本表面不同但内部推理路径相同，或表面相同但推理不同。在用户反馈稀疏的推荐系统中，可结合隐状态相似度或注意力模式来判别生成内容质量，减少纯文本奖励噪声。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
现有 LLM 强化学习主要依赖最终输出或文本推理轨迹的奖励，粒度粗且易受表面文本干扰，忽略模型内部如何思考。作者指出 text reward aliasing 问题：不同文本可能对应相同推理路径，或相同文本对应不同推理，导致奖励噪声和不可靠的推理。  

**方法关键点**  
提出 Attention Process Reward Model (APRM)，用隐藏状态和注意力图作为输入，为每一步推理分配内部奖励，捕捉高质量推理模式。APRM 仅约 46M 参数，通过 ranking 和 counterfactual objectives 训练，作为判别器区分优劣推理路径。其输出奖励集成到 PPO/GRPO 等 RL 优化中，并通过周期性更新适应训练中的分布漂移。  

**关键结果**  
在多个代表性 RL 方法上集成 APRM 后，平均 pass@8 提升 2.88%，验证内部推理信号用于 LLM 强化学习的有效性。
