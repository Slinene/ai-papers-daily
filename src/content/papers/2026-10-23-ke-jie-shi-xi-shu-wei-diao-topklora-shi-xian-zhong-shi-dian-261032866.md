---
title: Interpretable sparse fine-tuning with TopKLoRA enables faithful circuit discovery
title_zh: 可解释稀疏微调 TopKLoRA 实现忠实电路发现
authors:
- Marek Masiak
- Andrzej Szablewski
- Nicola Cancedda
- Constantin Venhoff
affiliations:
- University of Oxford
- University of Cambridge
- Neuralk-AI
arxiv_id: '2610.32866'
url: https://arxiv.org/abs/2610.32866
pdf_url: https://arxiv.org/pdf/2610.32866
published: '2026-10-23'
collected: '2026-10-26'
category: Training
direction: 稀疏 LoRA 微调与电路可解释性
tags:
- TopKLoRA
- Sparse Fine-tuning
- Circuit Discovery
- Backdoor
- Interpretability
- LoRA
one_liner: 提出 TopKLoRA 稀疏 LoRA 变体，仅激活 k 个最大 latents，用于定位并精准移除后门电路
practical_value: '- 在业务 LLM 微调中引入 TopKLoRA 稀疏激活，可大幅减少 adapter 参数量和推理开销，同时保留性能，适合部署多个轻量适配器进行
  A/B 测试或个性化微调。

  - 利用 TopKLoRA 的稀疏电路发现能力，对电商/广告场景中涉及内容生成、推荐解释的模型进行行为审计：定位哪些 latent 维度对应特定输出（如生成违规文案、偏见推荐），实现精准裁剪而不影响整体指令遵循。

  - 当模型可能在开放数据或用户反馈上微调时，可借鉴该方法构建“模型 organism”并搜索后门电路，建立安全检测流程，防止恶意数据投毒导致推荐或对话策略被操纵。

  - 对于 Agent 与 LLM 结合的多模块系统，可将 TopKLoRA 用于各子模型的适配器部分，通过梯度路由构造局部化电路，便于诊断单点故障或恶意行为在链路中的传播。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：微调数据来源不可控，少量中毒样本即可植入后门。传统 PEFT 虽能捕获参数变化但缺乏可解释性，导致后门难以定位和清除。

**方法关键点**：
- 提出 TopKLoRA，一种可解释设计的 LoRA 变体：每个 token 仅激活 adapter 中 k 个最大的 latent，形成稀疏激活模式。
- 与 SAE 不同，TopKLoRA 仅在下游损失上训练，优化压力促使模型学习具有功能因果性的 latent。
- 在 gemma-2-2b、Qwen2.5-1.5B、Qwen2.5-7B 上构建 sleeper-agent 后门模型，利用 TopKLoRA 识别并消融实现后门的必要且充分电路。
- 提出利用 TopKLoRA latents 和梯度路由构造局部化电路的方法，验证电路搜索算法的可靠性。

**关键结果**：TopKLoRA 产生的稀疏电路比 dense LoRA 基线小一个数量级，可实现外科手术式消融恶意能力，同时不损失指令遵循性能。代码已开源。
