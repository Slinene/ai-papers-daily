---
title: 'AutoCompress: Automated Hardware-Guided Model Compression'
title_zh: AutoCompress：硬件引导的自动化大模型压缩
authors:
- Sheldon Liang
- Ali Taghibakhshi
- Saurav Muralidharan
- Sharath Turuvekere Sreenivas
- Ashwath Aithal
- Pavlo Molchanov
- Nima Tajbakhsh
affiliations:
- NVIDIA
arxiv_id: '2611.08290'
url: https://arxiv.org/abs/2611.08290
pdf_url: https://arxiv.org/pdf/2611.08290
published: '2026-11-05'
collected: '2026-11-06'
category: Training
direction: LLM 硬件感知压缩 · 可微 NAS
tags:
- LLM Pruning
- Hardware-Aware NAS
- Knowledge Distillation
- MoE
- Serving Cost Model
one_liner: 用可微架构搜索在硬件约束下自动压缩LLM，联合优化全局与逐层结构，精度超Minitron++且搜索成本降2-3.3×
practical_value: '- 模型部署/选型不要只看参数规模；应在目标 GPU + serving engine 上按层 profile prefill/decode
  时间和显存，建立 cost table。传统 weights+KV cache 的显存估算会漏掉 31-43%，实际 OOM 常来自 prefill workspace、runtime
  buffers、CUDA graph/context，建议用实测残差校准。

  - MoE 专家裁剪时，mask 不要放在 top-k routing score 前，而要放在 expert output 后；否则被小容量候选保留的专家吃不到梯度，最终蒸馏损失可差
  23%。router 输出层零初始化并取消 warmup，也能避免初始架构偏置。

  - 可复用到推荐/搜索 Agent 的 LLM 压缩：把 P99 延迟、batch throughput QPS 作为预算惩罚项，采用 Gumbel-softmax
  可微搜索 + logits 蒸馏，可自动找到异构层宽/专家数，替代人工枚举 uniform 结构，并节省约 2-3× 搜索 token。

  - 对消费级 GPU 部署（如 RTX 5070/5080）或单卡长上下文服务，可借鉴其“全局 hidden size + 逐层专家数/FFN width”联合搜索，能在严格延迟/显存约束下尽量保留质量。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**  
LLM 部署约束取决于硬件、workload 和 serving engine，参数规模不能预测延迟/吞吐/显存；Minitron 等剪枝方法仍需人工把部署需求翻译为参数预算，且强制 uniform 结构，排除了异构架构。AutoCompress 面向三类真实场景：本地 coding、datacenter serving、on-device 游戏 NPC，自动搜索满足目标的压缩模型。

**方法关键点**  
- 搜索空间：同时优化全局 hidden size、Mamba head 数，以及逐层 MoE routed experts 数、routed/shared FFN width；宽度 0 可表示删层。  
- 权重共享：按 activation importance 排序并重排权重，候选架构共享 prefix；用 Gumbel-softmax 软 mask 实现可微架构选择。  
- 成本模型：在 vLLM 中用 Nsight 按层测 prefill/decode 时间，构建 latency table；显存 = weights + KV/SSM cache + prefill workspace + runtime buffers + 残差项，修正传统公式漏掉的 31-43% 内存。  
- 训练目标：logit distillation + 资源 penalty，逐步锐化采样分布；router output 零初始化且无 warmup，MoE 采用 output masking 保持梯度稳定。  
- 恢复：从 parent 直接切片初始化，仅用 logits distillation，不依赖训练后的 supernet 权重。

**关键结果**  
- 在 RTX 5070 / RTX 5080 / H100 上，同样部署预算下相比 Minitron++，Avg8 分别高 6.57 / 2.35 / 0.57 个百分点；搜索 token 少约 2.0× / 3.0× / 3.3×。  
- 所有学生满足真实硬件约束：RTX 5070 学生压到 3.6B，实测 739.7ms / 3.93GiB，原模型 1147ms / 8.76GiB。  
- 120B Nemotron 3.5 Super 压到 74B，在单 B200 上以 BF16 支持 128K context、batch 16，内存 178GB，平均分 57.58→54.74。

**一句话记忆**  
可部署的模型压缩必须把 serving engine 的实测成本模型放进架构搜索，而不是拿参数 count 当目标。
