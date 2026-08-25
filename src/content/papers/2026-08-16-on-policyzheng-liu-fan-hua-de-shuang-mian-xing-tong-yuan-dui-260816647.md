---
title: 'Every Coin Has Two Sides: On the Dual Nature of Generalization in On-Policy
  Distillation of Large Language Models'
title_zh: On-Policy蒸馏泛化的双面性：同源对齐与多教师跷跷板效应
authors:
- Zhaoyi Li
- Deyang Kong
- Yuan Wei
- Evan Yang
- Ranran Shen
- Mahardika Krisna Ihsani
- Ming Yang
- Wei Zhang
- Chuan Hao
- Jian Yang
affiliations:
- University of Science and Technology of China
- Peking University
- IQuest Research
- MBZUAI
- Zhejiang University
arxiv_id: '2608.16647'
url: https://arxiv.org/abs/2608.16647
pdf_url: https://arxiv.org/pdf/2608.16647
published: '2026-08-16'
collected: '2026-08-25'
category: Training
direction: On-policy蒸馏泛化与多教师集成
tags:
- On-Policy Distillation
- Multi-Teacher Distillation
- Generalization
- LLM Post-training
- Policy Alignment
one_liner: 控制实验发现OPD迁移教师推理行为而非答案，同源教师跨域泛化强但使多教师路由出现跷跷板效应
practical_value: '- 教师选型：做 LLM 蒸馏/对齐时，优先选同 base model 的 same-origin 教师，而不是只看 benchmark
  更强的跨架构/异源教师；尤其在需要跨域、跨语言或长程推理迁移时，同源教师能带来更稳定的全局策略对齐。

  - 训练数据筛选：不要按 teacher 是否解出问题过滤样本，teacher 端 pass-rate=0 的难题同样有价值；对 student 已稳定解决的
  prompt 可以动态丢弃，能带来小幅一致性提升并节省算力。

  - 多教师/多域路由：在多任务业务（搜索、推荐、广告文案等多域 LLM）里，不能把 prompt 路由当作能力隔离墙；教师影响会跨域拉扯，调整某一教师数据比例会产生跷跷板效应，必须全局监控所有域指标，且同源教师拉动力更强。

  - 诊断方法：除了训练 loss，监控 teacher-student 的 top-K token overlap 等策略对齐指标，可判断蒸馏是真正对齐整体策略还是仅拟合训练分布；在
  Agent 策略蒸馏中可用来控制跨能力迁移。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
On-policy distillation (OPD) 已被广泛用于 LLM post-training，但多数评估只在单一训练域、接近训练分布上进行，无法区分模型是学到了本地拟合还是发生了更广泛的策略迁移。这直接影响教师选择与 multi-teacher OPD (MOPD) 的设计。

**方法关键点**
- 采用 PG-style OPD：学生自采样轨迹，用 teacher 与 student 的 token 概率差作为逐 token 信号，等价于 reverse KL 的 k1 采样近似。
- 区分 same-origin（teacher 与 student 共享 base model）与 cross-origin（不同 base model）设置；教师包括 Qwen3-32B、Polaris-7B/4B、Light-R1-14B、JustRL-1.5B、Nemotron-1.5B 等，学生包括 DS-distill-1.5B/7B、Qwen3-8B-SFT 等。
- 控制变量实验：训练问题难度、语言/推理 horizon 迁移、跨域迁移（math↔code/science/IF）、MOPD teacher mixture ratio。

**关键实验与数字**
- 训练问题难度几乎不影响：BigMath 的 easy/hard/random 子集收敛到几乎相同精度；即使训练数据只用极简单或极难样本，仍恢复超过 80% 的默认 OPD 增益。
- 动态丢弃学生已解决样本带来小但稳定的提升：DS-distill-1.5B 均值从 41.4% 到 42.0%，DS-distill-7B 从 52.4% 到 52.8%。
- 仅用英文短 horizon 数学训练，同源 OPD 能让学生接近教师的中文与长程数学水平；更强的异源教师反而收益更小。
- 同源教师即使只提供数学 prompt，也能提升学生 code/science；反向同样成立；异源教师则主要表现为训练分布拟合，跨域 gap 明显。
- MOPD 中改变 JustRL/Nemotron prompt 比例，各域分数向更大份额教师基线移动：Setting 1 中 GPQA 早期下降约 5 pp；反转案例中，增加异源数学专家数据份额反而降低数学，因为同源非数学专家免费迁移了数学能力。
- Top-K overlap 显示同源 OPD 使 teacher-student 策略整体对齐，异源 OPD 对齐有限甚至下降。

**最值得记住的一句话**
OPD 迁移的是教师的推理行为而非具体答案；同源教师是实现跨域泛化的关键，但也使多教师路由无法隔离教师影响，最终表现为混合比例驱动的能力跷跷板。
