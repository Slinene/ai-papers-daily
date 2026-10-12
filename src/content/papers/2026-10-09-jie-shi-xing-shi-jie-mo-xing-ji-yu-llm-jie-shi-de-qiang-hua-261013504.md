---
title: 'Beyond Temporal Proximity: Explanatory World Models for Credit Assignment
  in Reinforcement Learning'
title_zh: 解释性世界模型：基于 LLM 解释的强化学习长时延信用分配
authors:
- Oriol Corcoll
- Qiyao Wei
- Ciarán Mark Gilligan-Lee
affiliations:
- Spotify
- University of Cambridge
arxiv_id: '2610.13504'
url: https://arxiv.org/abs/2610.13504
pdf_url: https://arxiv.org/pdf/2610.13504
published: '2026-10-09'
collected: '2026-10-12'
category: GenRec
direction: 生成式推荐 · 长时延奖励归因
tags:
- RL credit assignment
- LLM explanations
- reward redistribution
- generative recommender
- delayed rewards
- conservative hierarchical operator
one_liner: 用 LLM 对轨迹结果做解释并按事件相关性重分配奖励，显著改善长时延信用分配，在游戏与推荐基准上超过 PPO/LaRe
practical_value: '- **用 LLM 做用户长期行为归因，替代纯时间折扣**：对留存/转化等延迟数十甚至数百步的奖励，提示 LLM 从历史推荐中挑出真正贡献的
  item，并按重要性权重重新分配奖励到这些步骤，保持 episode 总奖励不变。可以直接复用到现有 RLHF/RL 推荐训练，且无需改变 policy 架构。

  - **CHO 层级重分配要程序化、缓存解释图**：一次 LLM 调用生成轨迹解释图，之后递归分摊奖励无需额外模型调用；同一解释图可对不同 reward function、不同深度复用。工程上把解释图缓存起来，离线训练只调用一次
  LLM，避免成本爆炸。

  - **蒸馏解释规则为 action mask/gating 规则**：在线策略无需每步调用 LLM，把 LLM 发现的用户流失规则（如 KuaiRand 中
  5 步内 tag 重叠导致 disengagement）固化为动作掩码，既能提升 session length 和累计 return，又不引入推理延迟。

  - **解释变体与指标强相关，选型要匹配业务目标**：Lombrozo breadth 在 AUC/log loss 上最优，但 ranking metrics
  变化小；Halpern counterfactual 对排序偏好改变更明显。若业务关注 candidate 排名，应优先 HP；若关注整体判别能力，选 LB。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
生成式推荐系统用 RL 优化时，奖励往往在数百甚至数千次交互后才出现。标准 RL 通过折扣回报按时间邻近分配信用，使得远处但关键的动作信号极弱，导致样本效率低下。生产环境交互昂贵、无法大规模试错，需要更强先验来识别哪些历史动作真正促成了长期结果。  

**方法关键点**  
- 提出 Explanatory World Models (EWM)：给定轨迹与某个结果事件，用 frontier LLM（Claude Sonnet 4.5）生成加权解释图，指出哪些前序事件与该结果相关。  
- 保守层级重分配算子 CHO：从 rewarded phenomenon 出发，递归把奖励按解释权重分配给被引用事件，保持 undiscounted return 不变；一次 LLM 调用产出的解释图可缓存、可对多种 reward function 复用。  
- 解释与奖励函数解耦：改变奖励函数不会改变解释关系，增加迁移性。  
- 六种解释 prompt 变体：基于 Halpern 实际因果（HP）、Deutsch 不易变解释（D）、Lombrozo 广度（LB）与简洁性（LS）等。  

**关键实验与结果**  
- Crafter：EWM 在所有 episode 长度下超过 PPO/LaRe，且延迟越长优势越大，L=1000 时约为 LaRe 的 2 倍，PPO 接近随机。  
- WordCraft 3-mix 难任务：EWM-LLM 几乎达到 oracle 解释器效果，而 PPO/LaRe 几乎不学习。  
- KuaiRand offline：LB 变体 AUC +1.99pp、log loss -5.01e-3，改善判别；排名指标上 LaRe 变化最大。  
- KuaiRand online A2C：EWM 发现的 5 步 tag 重叠流失规则作为 action gate，使累计 return 从 3.77 提升到 6.74，unbounded 版本达 13.25，接近 oracle 15.65。  
- 工业级生成式推荐 offline replay：Recall 3.75×、converted 3.86×、broad reach 4.0×，显示能提升下游行为代理指标。  

**最值得记住的一句话**  
解释关系可以作为奖励函数无关、可复用的信用先验，把稀疏长时延奖励重新锚定到真正有贡献的历史动作上。
