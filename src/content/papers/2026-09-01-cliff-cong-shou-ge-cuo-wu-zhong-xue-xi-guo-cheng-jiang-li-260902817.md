---
title: 'Cliff: Learning Process Rewards from the First Mistake'
title_zh: Cliff：从首个错误中学习过程奖励
authors:
- Peixuan Han
- Runhui Wang
- Ketan Ramaneti
- Jie Hao
- Gerald Friedland
- Chris Kong
affiliations:
- Amazon Web Services
- University of Illinois Urbana-Champaign
arxiv_id: '2609.02817'
url: https://arxiv.org/abs/2609.02817
pdf_url: https://arxiv.org/pdf/2609.02817
published: '2026-09-01'
collected: '2026-09-03'
category: Training
direction: LLM 强化学习 · 过程奖励塑形
tags:
- RLVR
- GRPO
- Process Reward
- Reward Shaping
- LLM Reasoning
- First Mistake Identification
one_liner: 提出 Cliff 奖励塑形，利用 LLM 教师定位学生 rollout 中第一个错误，将正确前缀与错误后缀赋予不同优势，平均比 GRPO 提升
  7%
practical_value: '- 在 Agent 多步决策或搜索推荐的多轮交互中，可以用 teacher LLM 定位用户不满意或决策错误的起始步骤，只对错误后缀给负反馈，正确前缀保持中性/轻微正反馈，这比全轨迹统一奖励更细粒度且易于实现。

  - 引入“首个错误”信号可避免训练需要精确步级奖励，降低标注成本；实测中等能力 LLM 即可胜任判断任务，且判断比生成更 robust，可借鉴用于电商场景中由中等规模模型判断对话/推荐轨迹质量。

  - λ=0 的关键设计：对正确前缀不要给额外正奖励，只将负奖励集中在错误后缀，能防止模型为了延长正确前缀而长度 hacking。在推荐/文案生成中同样可防止模型输出冗余内容。

  - 当 teacher 自己的参考解不可靠时，可先用可验证结果（如成交、点击）过滤 teacher 参考，只有 teacher 正确时才使用过程监督，否则回退到原始
  outcome reward，这一策略可迁移到有业务指标的推荐系统中。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
RLVR 的 outcome reward 粗粒度，无法区分推理过程质量；PRM 需要训练额外 reward model，OPD 假设 teacher 与 student 同分布，限制多。观察到一旦推理过程首次出错，后续评估信息有限（类似逻辑中的空真蕴含），所以只需定位首次错误，无需精确评估每一步。

**方法关键点**
- teacher 独立生成参考解并用 verifier 验证，未通过则回退 GRPO；
- teacher 判断学生 rollout，定位 Pitfall Step（首个错误步骤），将 rollout 分为正确前缀和错误后缀；
- token-level advantage 分配：正确 rollout 保持 Acor-b，错误 rollout 前缀给 λAcor-b（λ=0），后缀给 Ainc-b；偏移 b 保证均值为零；
- λ=0 避免长度 hacking；对超长 rollout 设 p(a)=0 强制惩罚。

**关键实验**
在 DAPO-math、Deepcoder 等 12 个场景，2 个学生模型（Qwen3-4B, Phi-4-mini）和 3 个 teacher（SOTA、Qwen3-32B、Gemma3-27B）上，Cliff 平均比 GRPO 提升 7%，比 OPD 提升 15%；teacher 判断准确率 >90%，平均 pitfall 位置偏差约 3 句；λ=0 时长度合理，λ=1 导致长度暴涨。

**最值得记住的一句话**
过程监督不需要精确评估每一步，只需定位“从哪一步开始错”，将正确前缀和错误后缀分开给优势，即可显著提升 RLVR。
