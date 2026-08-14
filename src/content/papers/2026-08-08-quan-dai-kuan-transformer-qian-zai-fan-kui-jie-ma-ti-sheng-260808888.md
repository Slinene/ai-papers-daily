---
title: Full-bandwidth transformer
title_zh: 全带宽Transformer：潜在反馈解码提升预训练效率
authors:
- Xi Wang
- Ziyang Cai
- Zheng Zhan
- Harry Dong
- Ying Fan
- Gustavo de Rosa
- Tim Pearce
- John Langford
affiliations:
- Johns Hopkins University
- Princeton University
- Microsoft
arxiv_id: '2608.08888'
url: https://arxiv.org/abs/2608.08888
pdf_url: https://arxiv.org/pdf/2608.08888
published: '2026-08-08'
collected: '2026-08-14'
category: Training
direction: LLM 预训练 · 潜在反馈多遍并行
tags:
- latent feedback
- transformers
- data-efficient pretraining
- multi-pass training
- LLM decoding
- recurrence
one_liner: 顶层隐藏状态与token嵌入融合反馈，以近零解码开销换来约1.5–2倍数据效率与更强推理
practical_value: '- 若在电商/搜索的 LLM Reasoner（选品解释、query理解、Agent 规划）中部署生成模型，可将 latent
  feedback decoding 作为推理期增强：只需把上一步顶层 hidden state 经 GLU 与当前 token embedding 融合后输入，KV
  cache 和 serving 栈基本不动，每 token 仅多两次 D×D 矩阵乘法；配合少量多遍训练后，在数学/编码/指令任务上稳定提升。

  - 把 prompt 预填充作为重点优化对象：对用户画像、历史行为、候选商品的 prompt 先跑 1–2 遍 fused prefill，再进入生成，收益前置于第一个反馈步，验证损失和
  5-shot acc 都有明显提升，适合高价值、可接受额外 prefill 成本的推荐 Agent 调用。

  - 数据稀缺的领域微调可以参考训练调度：多数步用标准单遍 NTP，后期混入少量两遍/三遍 batch；只需 3% 三遍 batch 即可让反馈映射从发散变收缩，大幅提升长程稳定性；同时用
  prefix mixin 对齐训练与推理的 prompt-then-generate 分布。

  - 融合设计要强制使用 hidden state：用 GLU 让 hidden state 走 value 通路、token 只作 gate，避免 additive
  shortcut 让模型退化回普通 token 输入；再加上 RMSNorm、输入输出 embedding 绑定、jitter noise，可在不牺牲标准 decoding
  的前提下获得表示质量提升。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
自回归 Transformer 的水平方向有稠密注意力，但垂直方向反馈很窄：解码时只有采样 token 回到栈底，顶层隐藏状态被丢弃。在高质量数据越来越稀缺的情况下，这促使通过更多计算从每个 token 榨取更多信号，而不是只堆更多数据。

**方法关键点**
- 提出 latent feedback decoding：把上一位置顶层隐藏状态 h^L_{t-1} 与当前 token embedding e_t 通过 GLU 融合，状态走 value 通路，token 作 gate：e_t⊗h_{t-1}=W_U h_{t-1}⊙σ(W_G e_t)。不修改 attention/KV cache，只增加两次 D×D 矩阵乘法。
- 训练用多遍并行近似：第 1 遍为标准前向；第 2 遍把上一遍隐藏状态右移一位、与 token embedding 融合后重跑全栈；对每遍输出都算 NTP loss。
- 调度上大部分训练保持单遍，后期引入两遍、少量三遍 batch；3% 三遍 batch 能把反馈映射从发散转为收缩固定点，支持长程推理。
- prefix mixin 随机让序列前缀保持普通 token embedding、后缀才融合，匹配推理的 prompt-then-generate 结构；稳定技巧包括 RMSNorm、输入输出权重绑定、深度缩放和 jitter noise。
- 推理分 STANDARD/SOFT/FUSED 三种，SOFT 仅改变生成输入，FUSED 额外对 prompt 做一次融合 prefill。

**关键结果**
1B 模型训练到 400B tokens，Phi-4 数据、8K 上下文。融合 prefill 在验证 loss 与 5-shot LM Eval 上都有提升；100B full-bandwidth + 2 遍 prefill 达到 200B 标准 baseline，200B 达到 400B，约 2× 数据效率。SOFT 在 GSM8K、Math500、HumanEval、MBPP 上全面超过同权重 STANDARD；200B 模型在 Math500 从 0.27 升至 0.37，超过 1T 标准 baseline；指令调优后 GSM8K 64.5→67.9、HumanEval 42.5→45.9。Base 模型生成答案明显更短且准确率不降；状态追踪实验中，浅层线性 probe 准确率从接近随机升至 99.6–100%。

**最值得记住的一句话**
Token 是 transformer 唯一的跨步反馈通道；把顶层隐藏状态作为连续反馈送回栈底，可以在不改 attention/KV cache 的情况下，以近零解码开销把数据效率提升约一倍。
