---
title: A Zeroth-Order Paradigm for LLM Preference Alignment
title_zh: 基于比较预言机的 LLM 偏好对齐零阶优化范式
authors:
- Peter Chen
- Xi Chen
- Wotao Yin
- Tianyi Lin
affiliations:
- UC Berkeley
- New York University
- Alibaba DAMO Academy
- Columbia University
arxiv_id: '2609.19144'
url: https://arxiv.org/abs/2609.19144
pdf_url: https://arxiv.org/pdf/2609.19144
published: '2026-09-15'
collected: '2026-09-17'
category: Training
direction: LLM 偏好对齐 · Zeroth-order 优化
tags:
- LLM Alignment
- Direct Preference Optimization
- Zeroth-Order Optimization
- Comparison Oracles
- Likelihood Displacement
- KL Regularization
one_liner: 提出 ComPO，用比较预言机从低 margin/noisy 偏好对中提取方向信号，缓解 likelihood displacement
practical_value: '- 在 LLM 排序、Agent 策略或生成式推荐的 preference tuning 中，不要直接丢弃低 margin 偏好对：按参考策略
  logπ 差异切分 clean/noisy，对 noisy 对改用比较信号更新，能保留数据并减少 likelihood displacement。

  - 工程上可采用冻结主干、只对 lm_head 输出层做稀疏扰动更新；阈值为保留约 1%-6% 的非零条目，显存可压到 16-30GB 级（A40），适合在已有线上
  checkpoint 上做轻量任务适配。

  - 在线正则化可参考：用当前 policy 对无标注 prompt 采样，计算 length-normalized log ratio 作为 reverse-KL
  代理，soft damping 调步长；配合 successful-batch replay buffer 可进一步稳定 LC win rate。

  - 训练诊断不要只看 benchmark：观察 comparison oracle 负输出计数分布、pairwise log-likelihood 变化方向，可作为
  likelihood displacement 的早期 sanity check。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：DPO 等直接偏好对齐方法虽省显存，但存在 likelihood displacement：训练只提升 preferred 相对 dispreferred 的 margin，却可能降低 preferred 的绝对概率，甚至把概率质量转移到不安全回答；低 margin/noisy 偏好对是重要诱因。简单过滤这些对会丢失有用比较信息。

**方法关键点**：
- ComPO 将 noisy 偏好对视为 comparison oracle：对当前参数加随机扰动，判断该扰动是否同时提高 preferred 对数似然、降低 dispreferred 对数似然，聚合 1-bit 信号估计方向。
- 实用实现只扰动输出层权重，冻结主干；用归一化扰动求和 + 逐项阈值化，保留约 1%-6% 的大幅值坐标。
- 先用 DPO/SimPO 在 clean 对上训练，再用 ComPO 在 noisy 对上做轻量更新。
- 在线扩展用当前策略对无标注 prompt 采样，计算 length-normalized reverse-KL 代理做 soft damping，并用成功 batch replay。

**关键结果**：在 Mistral/Llama/Gemma-2/Qwen3/Gemma-3 上，DPO+ComPO 普遍提升 AlpacaEval 2 LC 和 MT-Bench，如 Mistral-7B-Instruct LC 从 24.14 到 26.17，Llama-3-8B-Instruct 从 32.59 到 35.79；SimPO+ComPO 也一致提升。在线 damping+replay 进一步改善，如 Gemma-3-4B-it LC 从 40.00 到 42.55。Ablation 显示更多扰动数、3 层扰动、适当 λg 和更多 noisy pairs 有利。

最值得记住的一句话：低 margin 的偏好对不该被直接过滤，也不该硬拟合 margin loss；用比较信号做 zeroth-order 更新，可以在不显著增加显存的情况下从 noisy pairs 中稳定提取对齐方向。
