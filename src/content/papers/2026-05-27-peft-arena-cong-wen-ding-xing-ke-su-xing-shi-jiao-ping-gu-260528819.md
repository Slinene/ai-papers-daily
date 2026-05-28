---
title: 'PEFT-Arena: Understanding Parameter-Efficient Finetuning from a Stability-Plasticity
  Perspective'
title_zh: PEFT-Arena：从稳定性-可塑性视角评估参数高效微调
authors:
- Yangyi Huang
- Ruotian Peng
- Zeju Qiu
- Jiale Kang
- Yandong Wen
- Bernhard Schölkopf
- Weiyang Liu
affiliations:
- The Chinese University of Hong Kong
- Westlake University
- MPI for Intelligent Systems
arxiv_id: '2605.28819'
url: https://arxiv.org/abs/2605.28819
pdf_url: https://arxiv.org/pdf/2605.28819
published: '2026-05-27'
collected: '2026-05-28'
category: Training
direction: 参数高效微调的稳定性-可塑性权衡与几何分析
tags:
- PEFT
- Stability-Plasticity
- Orthogonal Finetuning
- Representation Geometry
- Benchmark
- Forgetting
one_liner: 提出 PEFT-Arena 基准，揭示 PEFT 方法的稳定性-可塑性权衡，正交微调 (OFT) 展现最佳前沿。
practical_value: '- **评估 LLM 微调时需同时监控通用能力遗忘**：业务中仅看下游指标会高估微调收益，建议加入指令遵循、知识问答等通用 benchmark
  作为稳定性指标，避免模型被破坏。

  - **优先选择结构化参数化方式**：在同等参数量下，正交微调 (OFT) 比 LoRA 变体更有利于保留预训练能力。若需要做领域适配（如电商商品知识、客服话术），可考虑
  OFT 或 Cayley 参数化，其谱保持性质能减少对通用能力表示几何的扭曲。

  - **用插值路径诊断过冲并后验修正**：SFT 末期常出现过冲，最佳权衡点早于最终 checkpoint。可用沿更新路径（加法方法缩放 ΔW，OFT 缩放 Cayley
  生成元）插值，找到更优的稳定性-塑性点；也可对 OFT 按层重缩放生成元，校正层间更新不平衡，在不额外训练的情况下恢复部分遗忘的通用能力。

  - **用激活空间几何指标监控遗忘**：Procrustes 残差、线性 CKA 等可用于检测微调对通用数据表示结构的扭曲程度，可作为离线评估的一部分，指导早停或超参选择。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
现有 PEFT 评估过度关注下游任务精度，忽略了对预训练基础能力的保留。模型在数学推理上提升 10 个点却可能悄悄丢掉 12 个点的指令遵循能力，单一指标会误导方法选择。论文将稳定性-可塑性困境引入 PEFT 评价，构建基准 PEFT-Arena，同时衡量目标域性能（plasticity）与通用能力保留（stability）。

**方法关键点**
- **双维度基准**：在数学与医学两个推理域，收集 SFT 和 RLVR 两种范式，联合评估目标任务准确率与通用能力（IFEval / NQ / BBH）平均分。
- **方法覆盖**：比较 Full FT、LoRA 系列（LoRA / PiSSA / MiLoRA / DoRA / AdaLoRA / VeRA / KeepLoRA）、乘法式 OFT（Cayley 正交参数化）、激活缩放 IA³，控制相近可训参数量。
- **几何分析**：在权重空间，通过奇异谱保留剖面与更新能量剖面刻画各方法对预训练谱结构的扰动；在激活空间，用 Procrustes 残差、Gram 失真、线性 CKA 量化通用数据表示的非等距扭曲，建立遗忘与表示几何损伤的联系。
- **路径诊断与后验修正**：沿参数化自然路径插值（加法式缩放 ΔW，OFT 缩放 Cayley 生成元）暴露 SFT 过冲现象，证明最终 checkpoint 非最优；提出对 OFT 的逐层生成元重缩放（SafeScale / MinScale），以无额外训练的方式恢复遗忘。

**关键结果**
- 在 Qwen2.5-7B 和 Llama3.2-3B-Instruct 上，Full FT 带来最大目标增益（Math +15.33，Med +7.27）但也造成最严重一般能力下降（-12.74，-12.56）。
- 约 20M 参数预算下，OFT-b32 在数学 SFT 上目标 +11.63 而一般能力仅 -2.60，优于 LoRA-r8（+7.17 / -7.75）及 PiSSA（+9.23 / -22.19）。OFT 在多个预算切片形成最前沿。
- RLVR 比 SFT 更稳定：OFT 在数学 GRPO 中目标 +12.60，一般能力反而 +1.93。
- 激活空间分析：OFT 产生的表示结构最稳定，Procrustes 残差 0.1279，CKA 0.934；PiSSA 则残差 0.4376，CKA 0.4402，与严重遗忘高度相关。
- 路径插值证实 SFT 过冲，OFT 使用 Cayley 路径插值 α=0.3 可达 45.77 目标分 + 48.64 一般分，优于稠密权重插值；逐层重缩放可将一般能力从 44.37 提升至 46.86 同时目标分仅微降至 47.83。

**一句话**
“PEFT 应追求在保留预训练几何结构的前提下获取新能力，而非简单追求下游精度。”
