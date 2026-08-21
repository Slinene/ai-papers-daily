---
title: 'Learning how to Forget: Fine-tuning for Long-Context Sparse Attention'
title_zh: 学会遗忘：长上下文稀疏注意力的微调方法
authors:
- Matthias Seeger
- Zeyu Zhang
- Vihang Patil
- Konstantinos Benidis
- Sebastian Schelter
affiliations:
- Amazon Web Services
- University of Amsterdam
- Amazon
- Technical University Berlin
arxiv_id: '2608.19920'
url: https://arxiv.org/abs/2608.19920
pdf_url: https://arxiv.org/pdf/2608.19920
published: '2026-08-20'
collected: '2026-08-21'
category: Training
direction: 长上下文稀疏注意力微调
tags:
- long-context
- sparse attention
- KV cache
- fine-tuning
- H2O
- LoRA
one_liner: 提出在任意 KV cache 策略下微调 LLM 的方法，使模型与稀疏注意力协同适应，在中等 GPU 上超越序列并行训练
practical_value: '- **训练/推理一致性**：若线上推理启用 H2O、SnapKV 等稀疏 KV cache 策略，微调时务必使用同一策略做前向，否则模型在稀疏推理下会出现输出过长、乱码；论文中
  SP 训练模型在多个 Helmet 任务上严重退化。

  - **低成本长上下文微调**：单卡 40GB 可用 LoRA + 嵌套激活检查点 + CPU offload + delta encoding 处理 KV cache，将
  autograd 显存降至与推理相当，适合多轮对话、长工具输出、长行为序列等场景。

  - **缓存策略 trick**：H2O 归一化累积注意力分数、batch 维度独立淘汰、保留少量 attention sink 前 β 个 token，能提升长上下文稳定性；避免全局统一淘汰。

  - **工程落地**：可复用 KeysAndValues 库快速对比策略；推动 SDPA kernel 支持返回 summed attention weights
  和隐式 causal mask，降低稀疏注意力延迟。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
长上下文 LLM 在工具调用、CoT、多轮对话中需求增长，但 exact attention 显存随上下文线性增长。稀疏注意力用固定大小 KV cache 缓解推理显存，但现有微调大多用 sequence/context parallelism 做 exact attention，与推理时稀疏策略不一致，导致模型在推理时表现差。核心问题是：如何用中等硬件对稀疏注意力模型进行微调，使模型与 KV cache 策略协同适应。

**方法关键点**
- 支持任意 KV cache 策略（lastrec、smart lastrec、H2O 及归一化变体等），前向记录 replay log，反向 replay cache 避免对不可微策略求导。
- 将序列切分为 chunk，使用嵌套激活检查点：外层按层，内层按 cell，KV cache 检查点存 CPU，GPU 显存降到与推理相当。
- 利用 KV cache buffer 相邻 chunk 只差 S 个 token 的线性 recurrence，通过 scatter/gather + delta encoding，并借助 PyTorch autograd saved tensors hooks 以 (index, delta_key/delta_value) 替代完整 KV buffer，将 autograd 显存降低 k 倍。
- H2O 实现改进：Triton 代码输出 summed attention weights，配合 FlashInfer SDPA；支持归一化累积分数、batch 维度独立淘汰；开源 KeysAndValues 库。

**关键实验与结果**
在 Qwen3-4B-Instruct-2507 上 LoRA 微调（rank=16），用 Helmet 基准 64k/128k 上下文。缓存长度 32768，chunk 1024/2048，单 A100 40GB 可训，4 卡 DDP 提高 batch。对比 SP 训练模型在同样稀疏推理下的表现：Table 1 四个数据集互有胜负，但 Table 2 六个数据集上本文方法显著优于 SP 和 no-finetune，例如 trec coarse 96.0 vs 30.0/28.2，nlu 90.0 vs 28.6/24.8，json kv 49-50 vs 0-1。失败模式分析显示 SP 训练模型在稀疏推理下输出过长且多为乱码，本文方法学会正确停止输出。

**最值得记住的一句话**
推理时用什么 KV cache 策略，微调时就要让模型在同一策略下前向训练，否则训练与推理不一致会导致模型在长上下文任务中严重退化。
