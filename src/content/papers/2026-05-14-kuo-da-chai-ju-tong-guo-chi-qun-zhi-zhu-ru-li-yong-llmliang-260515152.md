---
title: 'Widening the Gap: Exploiting LLM Quantization via Outlier Injection'
title_zh: 扩大差距：通过离群值注入利用LLM量化
authors:
- Xiaohua Zhan
- Kazuki Egashira
- Robin Staab
- Mark Vero
- Martin Vechev
affiliations:
- ETH Zurich
arxiv_id: '2605.15152'
url: https://arxiv.org/abs/2605.15152
pdf_url: https://arxiv.org/pdf/2605.15152
published: '2026-05-14'
collected: '2026-05-16'
category: LLM
tags:
- LLM
- Quantization
- Security
- Outlier
- AWQ
- GPTQ
one_liner: 首次通过注入离群值让LLM在量化后触发恶意行为，成功攻破GPTQ、AWQ等优化型量化
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
LLM量化已成为高效部署的标准手段，但现有量化条件攻击局限于简单的零量化方法（如LLM.int8()、NF4），对GPTQ、AWQ等优化型方法无效。而实际部署中，优化型量化因其更好的性能保留而被广泛采用，这为攻击者留下了可利用的真空地带。本文首次揭示了通过注入离群值可以广泛攻击多种量化方法，显著扩大了量化安全威胁的范围。

**方法关键点**
- **攻击思路**：利用量化算法对离群值敏感的特性——当一个量化组内存在极大离群值时，其余权重会被迫归零，导致量化后矩阵极度稀疏。攻击者通过设计双目标训练，在全精度下抑制恶意行为，在量化后激活攻击。
- **四步攻击流程**：(1) 零初始化：选取某一层FFN块，用近零噪声重新初始化，利用残差连接保持前向传播。(2) 启动双目标微调：训练模型使切换块外学习恶意行为，切换块内学习抑制；引入KL正则保持原始效用。(3) 注入离群值：在选定的权重矩阵中，按每组32个权重注入一个极大离群值，迫使量化后其余权重归零。(4) 精调用量化代理：构建仅保留离群值的代理模型，精调强化量化后恶意行为；对Mistral模型额外添加激活噪声以弥补代理与真实量化器的差异。
- **可攻击的量化方法**：覆盖零量化（LLM.int8()、NF4、FP4、GGUF 0-quant）、数据无关优化型（GGUF k-quant、HQQ、SINQ）和数据依赖优化型（GPTQ、AWQ、AutoRound、GGUF i-quant）。

**关键实验**
- **设定**：三种攻击场景（Jailbreak、Over Refusal、Content Injection），三个模型（Qwen2.5-7B、Llama3.1-8B、Mistral-7B），多种量化方法。
- **攻击成功率**：量化后ASR普遍>90%，而全精度版本ASR被压制到5%以下。首次成功攻破GPTQ 4-bit（ASR 89.7%–95.7%）、AWQ（87.3%–95.0%）等优化型量化。
- **效用保留**：平均基准得分相对原始模型保留90%以上（Llama3.1与Qwen2.5）或80%以上（Mistral）。
- **防御有效性**：高斯噪声防御无效；层内权重分布异常可被KS检验检测；但直接剔除或缩放离群值的防御在攻击尺度较大时失效。

**最值得记住的一句话**
首次表明LLM量化的安全风险不局限于简单方案，而是广泛存在于当前主流、复杂的量化方法中。
