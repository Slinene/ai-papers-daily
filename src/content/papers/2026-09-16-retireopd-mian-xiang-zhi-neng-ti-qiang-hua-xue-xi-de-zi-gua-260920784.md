---
title: 'RetireOPD: Self-Retiring On-Policy Distillation for Agentic Reinforcement
  Learning'
title_zh: RetireOPD：面向智能体强化学习的自适应退休在线策略蒸馏
authors:
- Yan Yu
- Zhengxi Lu
- Yizhou Liu
- Yichen Pan
- Aozhe Wang
- Qipeng Chen
- Hua Yang
- Wenqi Zhang
- Weiming Lu
- Qianglong Chen
affiliations:
- Zhejiang University
- Alibaba Group
arxiv_id: '2609.20784'
url: https://arxiv.org/abs/2609.20784
pdf_url: https://arxiv.org/pdf/2609.20784
published: '2026-09-16'
collected: '2026-09-18'
category: Training
direction: Agentic RL 训练 · 自适应退出蒸馏
tags:
- On-Policy Distillation
- Adaptive Teacher Retirement
- RLVR
- GRPO
- Agentic RL
- Teacher Construction
one_liner: 先奖励训练特权教师，再做在线策略蒸馏，并根据教师-学生分歧与相对成功率自适应退出教师监督
practical_value: '- **RLVR 训练 agent 时，别把「prompt 里塞特权信息」当成可靠 teacher**：电商/搜索 agent
  常想在训练期用用户画像、SKU 知识、检索结果等 offline-only 信息做 dense 监督。该工作表明，同容量模型仅靠输入特权上下文并不一定比无特权学生强，应先用环境奖励对
  skill-conditioned teacher 做一轮 RL，再冻结当教师。

  - **用在线信号决定何时退出蒸馏，比固定 annealing 或两阶段切点更稳**：可以监控教师-学生 token-level logprob gap 的相对变化
  ρ，以及学生的 relative competence η。当 gap 停止缩小且学生成功率超过教师一定比例（如 0.9）时退出 OPD，只保留 GRPO/RL。此逻辑适合跨品类、多模型尺度训练，不用逐任务调退火步数。

  - **稀疏奖励 + 特权 teacher 的组合能显著加速多轮 agent 前期学习**：业务里做购物 agent、搜索交互 agent、客服多轮决策时，可以先
  OPD 加速起步，再在冲突点后转纯 RL，避免教师天花板。退出后还能省掉 teacher forward pass，降低训练与后续微调成本。

  - **如果离线有技能库、查询改写规则、投放策略等仅训练期可用信息，可参考其 SkillBank + keyword retrieval 方式**：将特权技能作为
  teacher 输入，学生部署时不依赖这些信息，适合线上 latency 敏感但训练期可用的场景。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
多轮 agent 的 RLVR 只给轨迹级标量奖励，中间决策长期无监督。OPD 用带特权上下文的 teacher 提供 token 级 dense 监督，是常见补强方案。但两个假设常不成立：

- 特权 teacher 不代表可靠：同模型共享参数下，skill-conditioned 分支未必强于被监督学生，甚至 7B 模型仅靠 prompt 技能只拿 23.4% 成功率。
- 教师监督收益分阶段：早期 OPD 加速 GRPO，后期教师与学生分歧先降后升，继续匹配会卡在教师水平附近。

因此需要一个能在线判断「何时不再需要 teacher」的机制，而不是预定义蒸馏权重衰减或两阶段步数。

## 方法关键点
1. **Teacher Construction**：teacher 与学生同架构、同初始化，但 teacher 可见特权技能上下文 c+。先用环境奖励做 GRPO 优化 teacher，冻结后得到 skilled teacher πT，仅用于提供 dense 监督。
2. **Joint GRPO-OPD**：skill-free 学生采样轨迹，GRPO 提供组内相对 advantage；OPD 用 reverse KL 近似，token 级差距为 Δt = log πT(yt|x,c+,y<t) − log πθ(yt|x,y<t)。学生 loss 为 L_GRPO + λ L_OPD，λ=0.01。
3. **Adaptive Retirement**：每 W=5 步评估窗口平均 gap，计算相对变化 ρ；同时算 student 相对 competence η = 学生近期成功率 / 教师成功率。当 ρ ≥ δ 且 η ≥ γ 时退出 OPD，后续只跑 GRPO。默认 δ=0、γ=0.9。

## 关键结果
在 ALFWorld 和 WebShop 上，Qwen2.5-1.5B/3B/7B 三个规模：

- ALFWorld 成功率比 GRPO 提升 14.1–18.8 个百分点，如 3B 从 75.0% 到 93.8%。
- WebShop 准确率比 GRPO 提升 11.8–19.0 个百分点，如 1.5B 从 56.8% 到 75.8%。
- 每个 setting 都超过其自身的 skill-conditioned teacher。
- 消融中，持续 GRPO+OPD 只有 82.8%，RetireOPD 达到 92.2%；自适应退出比 linear annealing 更稳健，exit step 对 γ、δ 在较大范围内仅约 ±5 步波动。

最值得记住的一句话：**当教师-学生 logprob gap 停止下降且学生相对能力达标时，教师监督就从脚手架变成了天花板，应该让学生自己退休老师。**
