---
title: RL Can Only Reinforce What It Sees Succeed
title_zh: RL 只能强化其见到成功的动作
authors:
- Ruben Sanchez-Corcuera
- Unai Zulaika
- Aritz Bilbao-Jayo
- Miguel Fernandez-de-Retana
affiliations:
- University of Deusto
arxiv_id: '2611.26084'
url: https://arxiv.org/abs/2611.26084
pdf_url: https://arxiv.org/pdf/2611.26084
published: '2026-11-19'
collected: '2026-11-21'
category: Training
direction: RL 改变预训练先验与观察的权衡
tags:
- RL
- GRPO
- pretraining prior
- rare actions
- training dynamics
- language models
one_liner: RL 只能强化训练中出现的成功动作，罕见正确动作能否学会可由期望成功组数预测
practical_value: '- RL 训练中正确动作的“成功组数”需大于约 35 组才有 50% 学会概率；业务里想用 RL 教会策略处理罕见事件（长尾商品转化、异常
  query 改写、规则变更后的新行为），先统计该事件在 rollout 中的期望成功组数，低于阈值先做 SFT/数据增强/重放，不要直接上 RL。

  - 学习率、优化器、GRPO 变体、模型规模（1.3M-85M）只移动阈值，不改变需要计数的量；调参收益有限，瓶颈是 rollout 中成功样本是否足够成“组”。

  - 预训练 hedge 倾向在 RL 后会变成二极决策；若罕见正确动作被当噪声，训练会出现全有或全无，上线后策略可能突然翻转。建议监控 rollout 中成功动作组数，作为训练是否可能起飞的前置指标。

  - 电商 Agent 在用户兴趣漂移或规则变化下，如果新行为在探索中极少成功，直接 RL 很难切换；可先用专家演示/老策略构造成功轨迹，确保新行为达到组数阈值后再放给
  RL。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：当熟悉规则失效，agent 必须在预训练先验与当前观察之间权衡。现有 outcome-reward RL 如何改变这种权衡、尤其在正确答案罕见时，不够清楚。

方法：在贝叶斯玩家生成的游戏上从零训练 1.3M-85M 参数的小语言模型，使先验与正确答案精确可知。比较 base 模型的 hedging 行为与 RL 训练后的决策行为；核心度量是训练前可计算的“期望成功组数”——即各尝试组中动作获胜的组数期望。

结果：Base 模型像语料一样 hedging，RL 将其推向决策，方向由奖励决定。但当正确动作罕见时，单次 run 二极化：要么全局学会，要么完全不会。起飞与否可由期望成功组数预测，约 35 组对应 50% 成功几率。该关系对 4-256 组大小、新旧问题、学习率/优化器/GRPO 变体/模型规模稳健；这些因素只移动阈值，不改变被计数的量。
