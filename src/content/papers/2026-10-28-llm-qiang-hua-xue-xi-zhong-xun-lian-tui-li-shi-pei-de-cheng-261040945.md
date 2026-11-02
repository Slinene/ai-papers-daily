---
title: On the Origin and Evolution of Training-Inference Mismatch in LLM Reinforcement
  Learning
title_zh: LLM 强化学习中训练-推理失配的成因与修正
authors:
- Yu Li
- Yufa Zhou
- Tian Lan
affiliations:
- George Washington University
- Duke University
arxiv_id: '2610.40945'
url: https://arxiv.org/abs/2610.40945
pdf_url: https://arxiv.org/pdf/2610.40945
published: '2026-10-28'
collected: '2026-11-02'
category: Training
direction: LLM 在线强化学习训练稳定性
tags:
- RLHF
- policy gradient
- importance sampling
- KL divergence
- training-inference mismatch
- asynchronous sampling
one_liner: 拆分数值偏差与策略滞后，提出 DLC 校正，稳定异步采样下 LLM 在线策略训练
practical_value: '- 在线 RL 训练 LLM 推荐文案/对话 Agent 时，若推理引擎与 trainer 分离，先对每个 prefix 的 score
  做 centering 再计算 advantage，可去除推理引擎数值差异带来的近固定偏差；类似 advantage normalization，但要按 prefix
  而不是全局批量做。

  - 对异步采样引入的 policy lag，不要只做 per-token importance weighting；持续监控重要性权重的 ESS，低于 0.5
  时强制同步 sampler 权重。该阈值在 Qwen3-1.7B 上被验证为崩溃临界点，可作工程默认触发条件。

  - 别只监控 sampler 端前缀上的 KL，它检测不到由滞后反馈导致的塌缩；建议增加与 on-policy baseline 的 KL 对比或 trainer
  侧 KL 监控，并配置自动 resync。'
score: 7
source: huggingface-daily
depth: abstract
---

## 动机
在线策略 RL 假设训练响应来自当前策略，但实际推理引擎采样与 trainer 分开，数值差异和异步采样的旧权重使数据 off-policy，单一校正难以同时稳定。

## 方法关键点
在 sampler 权重上评估 trainer，将每个采样 token 误差分解为数值偏差和策略滞后。数值偏差近似恒定，对每个前缀做 score centering 可移除主偏差；策略滞后由 trainer 自身更新形成反馈环路，importance weighting 仅在滞后比率集中时有效，Qwen3-1.7B 上 ESS 低于 0.5 时失效。DLC 结合三件事：centering 数值偏差、对滞后比率按 sampler 权重做 clipping、ESS 低于 0.5 时 resync sampler。

## 结果
在 Qwen3-0.6B 与 Qwen3-1.7B 上，stale sampler 下 DLC 使与 on-policy 训练的 KL 保持在两次独立 on-policy 训练 KL 的两倍以内；resync 避免 per-token 校正遗留的 collapse，而这种 collapse 在 sampler 前缀上测 KL 无法发现。
