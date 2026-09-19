---
title: 'dQwen3.5: Hybrid-Attention Diffusion Language Models'
title_zh: dQwen3.5：混合注意力扩散语言模型
authors:
- Anton Xue
- Litu Rout
- Aditya Akella
- Adam Klivans
- Sujay Sanghavi
- Sanjay Shakkottai
affiliations:
- University of Texas at Austin
arxiv_id: '2609.20751'
url: https://arxiv.org/abs/2609.20751
pdf_url: https://arxiv.org/pdf/2609.20751
published: '2026-09-17'
collected: '2026-09-19'
category: Training
direction: 扩散语言模型适配 · 混合架构
tags:
- Diffusion LM
- AR-to-DLM
- Hybrid Attention
- Parallel Decoding
- Training Efficiency
one_liner: 将因果 RNN 骨干保留、仅双向化注意力层，实现 AR 到扩散语言模型的高效适配，训练 token 减半且保持并行/任意顺序解码
practical_value: '- 若业务已有 hybrid AR 生成模型（如 query 生成、商品文案、搜索词生成），可直接做 AR→DLM 适配：只把
  attention 层的因果 mask 关掉，保留 RNN 因果，再按论文做 token shifting 和复用未用 token id 作为 mask/pad/BOS，无需新
  embedding 或改架构，即可继承权重并得到并行/任意顺序解码能力。

  - 训练预算上，扩散适配 50B tokens 通常够用，尤其大模型不要盲目拉到 100B；把下游指标（而非训练 loss）作为停止/选 checkpoint
  依据，同时学习率按原始能力保留来选，防止灾难性遗忘。

  - 线上低延迟生成可借鉴 block decoding（块大小 32）做半自回归：块内任意顺序并行，块间左到右，适合搜索建议、push 文案等需要部分结构化的场景；confidence
  threshold 在 2–16× NFE 加速下仍维持较好的 HumanEval 表现，可直接探索。

  - 微调数据配比：初始 71% 领域代码不如 50% code + 35% general 混合，加入通用语料后 19/20 指标提升；对推荐/搜索生成模型的领域微调有同样启示——保留通用数据，且对代码/执行类数据可做可执行性验证过滤。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
AR-to-DLM 适配比从零训练便宜，但主流 AR 模型已转向混合注意力架构（如 Qwen3.5 用 Gated DeltaNet RNN 与 attention 交错），其中 RNN 天然因果且难以双向化，现有适配几乎都基于 full-attention。论文验证保留因果 RNN 主体、仅双向化少数注意力层，是否能得到高效且保持并行/任意顺序解码能力的 DLM。

### 方法关键点
- 在 Qwen3.5 0.8/2/4/9B 上，每 3 个 Gated DeltaNet 层后接 1 个 attention 层；仅去掉 attention 的因果 mask，GDN 保持因果；另适配 full-attention Qwen3-1.7B 作控制。
- Token shifting：在序列前加 BOS，隐藏状态位置 k 预测 token k+1，保持原 AR readout 对齐；复用未用 token id 作 mask/pad/BOS，不 resize embedding。
- 训练数据：50% code + 35% general + 15% math，来自 Nemotron 14 个子集；代码子集经执行验证仅保留 53.4% 通过样例。
- 用 time-reweighted masked diffusion 目标，50B 和 100B 两种预算；解码评估 any-order 指标（local/global AR-ness）与并行 speedup。

### 关键结果
- 相比 trunk 匹配的 full-attention 控制，hybrid 达到同样训练损失只需约一半 tokens（median 2.21×）。
- dQwen3.5-2B 50B 在 6/7 基准上超过 CoDA（200B）；dQwen3.5-9B 50B 在 MMLU、GSM8K、MATH500、HumanEval+ 等 4/7 指标上领先 Dream-7B（580B）、Dream-Coder-7B（322B）与 LLaDA-8B（2.3T）。
- 50B 已够：延长到 100B 对 9B 仅 1/7 指标提升；dQwen3.5-9B 的 local AR-ness 为 0.636，与 full-attention DLM 相当，且 HumanEval 并行解码在所有 >1× speedup 领先可比模型。

### 一句话
保留因果 RNN 主体、仅双向化少数注意力层，是更高效的 AR-to-DLM 适配起点。
