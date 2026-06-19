---
title: 'EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts'
title_zh: 面向强化学习Rollout的系统感知自推测解码
authors:
- Minseo Kim
- Minjae Lee
- Seunghyuk Oh
- Kevin Galim
- Donghoon Kim
- Coleman Hooper
- Harman Singh
- Amir Gholami
- Hyung Il Koo
- Wonjun Kang
affiliations:
- FuriosaAI
- University of California, Berkeley
arxiv_id: '2606.18967'
url: https://arxiv.org/abs/2606.18967
pdf_url: https://arxiv.org/pdf/2606.18967
published: '2026-06-16'
collected: '2026-06-19'
category: Training
direction: LLM训练加速 · 自推测解码
tags:
- speculative decoding
- reinforcement learning
- self-speculative decoding
- system-aware
- rollout acceleration
one_liner: 系统感知自推测解码框架，自适应切换推测解码与草稿长度，将RL rollout延迟降低19.6%且不损失模型质量。
practical_value: '- 在RL微调LLM（如GRPO/PPO）时，rollout生成是瓶颈，可直接采用自推测解码（self-speculative
  decoding）：从目标模型量化出轻量draft模型，无需额外训练，保持与进化策略分布对齐，降低工程维护成本。

  - 系统感知的SD切换策略（toggle policy）根据批次大小和计算状态动态开启/关闭推测解码：只在内存密集、并行验证能利用闲置算力时启用，避免计算密集阶段引入额外开销。此动态调度思想可迁移到生产环境的在线推理加速中。

  - 接受率感知的草稿长度自适应（acceptance-aware draft-length adaptation）：根据近期接受率动态调节每次推测的token数量，匹配draft质量变化，避免无效生成。类似机制可用于自适应调整推理时的speculative长度，降低延迟抖动。

  - 整体框架强调系统级的协同设计，而不只是算法优化。做推荐/Agent类LLM应用时，若涉及线上更新或频繁微调，可考虑将系统负载感知纳入推测解码的调度策略，提升资源利用率。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：强化学习（RL）已成为LLM后训练提升推理与Agent能力的核心范式，但rollout生成是延迟瓶颈：自回归解码顺序生成，且少数长尾响应决定批次完成时间。推测解码（SD）虽能加速固定模型推理，但在RL rollouts中面临两个关键挑战：（1）训练中目标策略持续进化，固定draft模型分布失配导致接受率下降；（2）rollout过程中活跃批次大小逐渐收缩，解码从计算密集转向内存密集，传统SD在计算密集段反而增加开销。

**方法**：提出**EfficientRollout**，一个系统感知的自推测解码（self-SD）框架。核心包括：
- **自推测解码**：从目标模型自身通过量化（如4-bit）诱导出draft模型，与进化策略天然耦合，无需单独预训练或在线微调draft模型。
- **系统感知SD切换策略**：监控批次大小与硬件计算/内存状态，仅在内存密集且并行验证能利用闲置算力时启用推测解码，避免在计算密集段引入额外负担。
- **接受率感知的自适应草稿长度**：根据近期token接受率动态调整每次推测的token数，使预算与draft质量匹配，减少无效草稿步。

**结果**：在RL rollout上，相比加速后的AR基线，EfficientRollout将rollout延迟降低最高19.6%，端到端训练延迟降低12.7%，且最终模型质量无损。
