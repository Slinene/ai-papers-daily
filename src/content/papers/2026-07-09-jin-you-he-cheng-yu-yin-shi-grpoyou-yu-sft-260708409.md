---
title: 'When Synthetic Speech Is All You Have: Better Call GRPO'
title_zh: 仅有合成语音时，GRPO优于SFT
authors:
- Shashi Kumar
- Yanis Labrak
- Hasindri Watawana
- Sergio Burdisso
- Esaú Villatoro-Tello
- Kadri Hacioğlu
- Petr Motlicek
- Andreas Stolcke
affiliations:
- Idiap Research Institute
- EPFL
- Uniphore
- Brno University of Technology
arxiv_id: '2607.08409'
url: https://arxiv.org/abs/2607.08409
pdf_url: https://arxiv.org/pdf/2607.08409
published: '2026-07-09'
collected: '2026-07-11'
category: Training
direction: RL微调在合成数据域适应中优于SFT
tags:
- GRPO
- Synthetic Speech
- Domain Adaptation
- ASR
- Reinforcement Learning
- Low-Resource
one_liner: 在合成语音ASR域适应中，GRPO强化学习比监督微调大幅降低WER 40-45%
practical_value: '- 当真实用户反馈昂贵或受限时（如冷启动、隐私保护），可使用合成数据 + GRPO 做策略优化，GRPO 无需 critic 网络，工程实现简单，适合在线
  RL 或模拟环境下的 Agent 策略训练。

  - GRPO 的组内相对奖励机制可类比推荐场景中的 listwise 优化：从一组多样化输出中选出低错误（高奖励）假设，抑制劣质输出，可借鉴用于生成式推荐/query
  推荐的偏好对齐。

  - 分析表明 GRPO 的增益来自行为校准（停止判据、注意力对齐）而非表示层变化，提示在 RL 微调推荐对话 Agent 时，可重点监控和优化行为指标（如终止时机、幻觉率），而非只关注隐层表示。

  - 论文结论“当合成数据是主要资源时，RL 应优先于 SFT”可迁移到使用 LLM 生成训练数据的场景：用 SFT 预热后接 GRPO 可进一步榨取合成数据的上限。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：在银行等受监管领域，真实语音因隐私合规难以大规模收集，合成 TTS 语音成为替代，但其声学分布与真实录音存在 mismatch。此前工作仅用监督微调（SFT）缓解该 gap，效果有限。本文探索强化学习是否更能挖掘合成语音的价值。

**方法**：将 LLM 基 ASR 的域适应视为 RL 问题，采用 **GRPO**（Group Relative Policy Optimization）——一种无 critic 的 PPO 变体，以 WER 为奖励信号，对同一语音输入采样一组候选文本，组内相对奖励驱动策略更新。实验分纯 GRPO 和 SFT→GRPO 组合两种方式。

**结果**：纯合成数据适应下，GRPO 相比 SFT 相对 WER 下降 **40%**（36.71% → 22.09%），SFT→GRPO 组合进一步降至 **45%**。分析表明，GRPO 主要减少插入错误，通过改善停止校准和语音-文本注意力对齐实现，而早期编码器表示无显著变化，即 RL 通过**行为**而非表示提升性能。结论：当合成语音是主要适配资源时，RL 应优先于 SFT。
