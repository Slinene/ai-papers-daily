---
title: 'PR-OPD: Privileged Representation On-policy Self-Distillation for Agentic
  Reinforcement Learning'
title_zh: 特权表征在线策略自蒸馏用于智能体强化学习
authors:
- Muyang Li
- Jie Yang
- Zhengyu Fang
- Junchao Zhu
- Zhengkun Xiao
- Ruining Deng
- Zhe Jiang
- Shigang Chen
affiliations:
- University of Florida
- University of Illinois at Chicago
- Case Western Reserve University
- Vanderbilt University
- Weill Cornell Medicine
arxiv_id: '2609.36642'
url: https://arxiv.org/abs/2609.36642
pdf_url: https://arxiv.org/pdf/2609.36642
published: '2026-09-28'
collected: '2026-10-14'
category: Agent
direction: Agent RL · 特权表示自蒸馏
tags:
- Agentic RL
- Privileged Self-Distillation
- Hidden State Alignment
- GRPO
- Hindsight Skill
- On-policy Distillation
one_liner: 提出 PR-OPD，用分层隐藏状态对齐替代 token 概率蒸馏，把智能体自生成技能的特权优势传给无技能策略，推理零额外开销
practical_value: '- 在电商导购/客服 Agent 的 RL 训练中，若手头有事后信息（用户真实意图、成交/退货、人工反馈），可让同一策略先跑 GRPO，再对每条轨迹生成
  hindsight skill，用无技能/有技能两次前向做 teacher；蒸馏目标用隐藏状态对齐，而不是输出 logits/KL。很多点击/转化信号是稀疏 episode
  reward，这样能把事后信息变为稠密监督。

  - 工程实现很轻：只增加一个每层轻量 MLP projector（512 维隐藏层），teacher 与 student 共享权重，推理时丢弃 projector；不引入外部
  teacher 模型、技能库或额外推理开销，适合线上部署。

  - 小模型直接对齐原始 hidden state 可能崩，务必保留 projector；并且要对齐所有层而非只 last layer，因为技能信息在中间层最强；先
  warm start 是关键，WebShop 上 N=120 优于 N=100，10-30 个监督步已经能拿到大部分收益。业务里可先纯 reward 训练到一定成功率，再开启表示蒸馏。

  - 有些改进不会体现在 top-1/token 概率上（如 action token 概率几乎不变但隐藏状态大幅变化），所以训练日志不能只看 loss 或 token
  accuracy；可以通过线性 probe 诊断隐藏状态是否携带可迁移信息，再决定用表示对齐。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**

RLVR 只给每个 episode 一个标量奖励，信号稀疏。特权自蒸馏让同一策略在额外技能上下文中作为 teacher，再用 token 概率指导学生。但论文发现两个现象：技能在上下文中把 WebShop 成功率从 42.2% 拉到 56.2%，却只改变不到四分之一的 token 概率，action token 上几乎不变；同时隐藏状态在超过 80% 的 response token 上发生改变，线性 probe 可以识别技能。也就是说技能带来的优势主要隐藏在表征里，token 概率蒸馏只能传递很薄一层信息。

**方法关键点**

- 两阶段训练：先 GRPO 预热 N 步，让策略学会基本任务与错误分析；第二阶段加入表征监督。
- 每条 rollout 完成后，同一 policy 作为 analyzer 为轨迹生成一条 hindsight skill：成功轨迹总结可复用 workflow，失败轨迹指出关键错误和修正方法。
- 同一 policy 再以 student（无技能）和 teacher（有技能）两次前向读取同一 response，teacher stop-gradient；student 每层 hidden state 经过轻量 MLP projector（512 隐藏层）后，按归一化 cosine 距离对齐到 teacher 对应层。
- 总目标为 GRPO + KL + entropy + λ·LPRA；共享全部权重，只有 projector 额外引入，推理零开销，无外部技能库、无单独 teacher。

**关键结果**

在 ALFWorld 和 WebShop 上，PR-OPD 在两个 backbone（Qwen2.5-3B、Qwen3-1.7B）的所有设定中整体最优：3B 上 ALFWorld 总体成功率 71.1% vs GRPO 66.4%（+4.7），WebShop accuracy 67.2% vs 55.5%（+11.7）；1.7B 上 WebShop accuracy 57.0% vs 43.0%（+14.0）。相同自生成技能下，token OPD 降到 57.8%，低于 GRPO 8.6 点；隐藏状态对齐达 72.7%，高出 6.3 点，二者相差 14.9 点。消融显示小模型必须加 projector（1.7B 无 projector 从 43.8 跌到 36.7，加 projector 到 46.9）；warm start 点很关键，WebShop 上 N=120 比 N=100 高 7.5 点 accuracy。线性 probe 表明技能信息在中间层最强，输出特征接近随机。

最值得记住的一句话：特权信息的优势更多留在隐藏表征里，而不在输出 token 概率里，因此要传递这种优势，应该对齐隐藏状态，而不是蒸馏概率。
