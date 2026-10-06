---
title: 'Towards Looped Models Done Right, Part II: Rethinking at Fixed Points'
title_zh: 循环模型的不动点重思考：训练与推理高效捷径
authors:
- Benhao Huang
- Chufan Shi
- Junlin Chen
- Shicheng Wen
- Zhengzhong Liu
- Eric Xing
- Xuezhe Ma
affiliations:
- Institute of Foundation Models
- USC
- CMU
arxiv_id: '2610.06833'
url: https://arxiv.org/abs/2610.06833
pdf_url: https://arxiv.org/pdf/2610.06833
published: '2026-10-04'
collected: '2026-10-06'
category: Training
direction: 循环 Transformer 固定点训练/推理加速
tags:
- looped LLM
- fixed point
- KV cache
- depth prior
- orthogonal injection
- RL
one_liner: 从不动点视角重构循环 LLM，以学习深度先验和正交注入支撑终端 KV 共享、蒸馏预填充与 RL 状态复用
practical_value: '- 若使用循环/looped 模型做 latent reasoning 或深度重排，解码时采用 terminal KV sharing，只保留终点
  KV；前提是训练深度先验必须覆盖深层并让状态接近不动点，固定深度训练会在共享后大幅掉点（论文中 GSM8K 从 50.6 掉到 21.2）。可作为 KV cache
  降本 3× 的工程方案。

  - 把固定深度/固定 PLN 先验换成可学习 categorical depth prior：以 inverse perplexity 为 reward，用 PopArt
  归一化 advantage，并用 entropy 系数平衡深度多样性、用 mean penalty 控制平均计算预算；可直接用于 query 改写/Agent
  自修正动态分配迭代步数。

  - 输入注入时采用 OrthoInj：将 carryover 状态先投影到输入向量的正交补，再加输入；可避免状态沿输入分量抵消注入，提升训练稳定性和 PPL，代码上只是一行投影。

  - RL 后训练（如 GRPO）对循环策略打分时，复用 rollout 保存的终点状态，在单次 forward 记录的计算图上循环 backward 计算 Neumann
  梯度，scoring+backward 时间约减半，避免 trajectory 重放。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：循环语言模型每一轮 recurrence 都会增加训练激活、解码 KV、预填充计算和 RL 重放成本。论文从不动点出发：当循环状态接近 z⋆=F(z⋆;x)，终点可替代完整轨迹，从而把各项成本与深度解耦。但现有训练对不动点塑造不够：固定深度训练破坏终端 KV 共享，Huginn 固定深度先验监督被稀释；输入注入存在 carryover 沿输入分量放大/抵消问题。

方法关键点：
- 训练用截断 BPTT，仅反传最后 b 步，避免均衡梯度 warm-up，同时塑造可共享的不动点。
- 推理用终端 KV 共享，只保留每 token 最后一步 KV；静态缓存约 3× 减少。
- 预填充蒸馏：学生直接预测深度 R 的隐藏状态，再补一次 teacher recurrence 生成 KV。
- RL 复用 rollout 终点状态，在单次记录的图上用 Neumann-(b−1) 循环 backward，避免 trajectory 重放。
- 学习深度先验：categorical 分布 + inverse perplexity reward + PopArt advantage + entropy 正则 + 均值预算惩罚。
- OrthoInj：把 carryover 投影到输入向量的正交补后再注入，保证每次输入强度一致。

关键结果：100M/400M/1.6B 规模训练。Learned prior 在终端 KV 共享下验证 PPL 比固定 PLN-5 降低 0.7–1.8%；1.6B 时 3× 更小 KV cache 达到 fixed-depth full-cache 下游平均，并接近 Untied 12（AVG 差 1.5 点）。OrthoInj 相比 Parcae 验证 PPL 降低 0.3–1.4%，下游平均各尺度最高。8K 预填充蒸馏最快 1.79×，下游 gap 1.0–4.5 点；RL 复用使 scoring+backward 时间约 2× 降低，GSM8K pass@1 差距不超 1.6 点。

最值得记住：接近不动点时，终点的价值远大于轨迹本身；但前提是训练必须通过深度先验和输入注入主动塑造容忍终端共享、可复用的不动点。
