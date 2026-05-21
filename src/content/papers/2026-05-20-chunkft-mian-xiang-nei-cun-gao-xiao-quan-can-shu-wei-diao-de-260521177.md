---
title: 'ChunkFT: Byte-Streamed Optimization for Memory-Efficient Full Fine-Tuning'
title_zh: ChunkFT：面向内存高效全参数微调的字节流优化框架
authors:
- Yongkang Liu
- Zijing Wang
- Mengjie Zhao
- Ercong Nie
- Mingyang Wang
- Qian Li
- Feiliang Ren
- Shi Feng
- Daling Wang
- Hinrich Schütze
affiliations:
- Northeastern University, China
- Shanghai Jiao Tong University, China
- CIS, LMU Munich, Germany
- MCML, Germany
- Shandong University, China
arxiv_id: '2605.21177'
url: https://arxiv.org/abs/2605.21177
pdf_url: https://arxiv.org/pdf/2605.21177
published: '2026-05-20'
collected: '2026-05-21'
category: Training
direction: 大模型全参数微调 · 字节流内存优化
tags:
- Memory-Efficient Fine-Tuning
- Chunk-wise Optimization
- Byte-balanced Partitioning
- Sparse Gradient
- Full-Parameter Training
- LLM
one_liner: 通过按字节预算划分模型参数为轮转块，仅激活当前块计算梯度，实现内存近似LoRA的全参数微调。
practical_value: '- 在电商/推荐场景微调大模型受限于GPU内存时，可借鉴ChunkFT的轮转块训练策略：将模型按实际字节成本分块（不止按层），每次只针对当前块计算梯度与优化器状态，显著降低内存峰值且支持梯度累积与动量，避免因内存不足而被迫使用低效的PEFT方法。

  - 块划分不依赖网络结构，适配Transformer各类算子（Embedding, Linear, LayerNorm），可直接嵌入现有HuggingFace/Torch训练流程，对业务代码侵入小。

  - 字节均衡分块避免了层间参数量差异导致的内存抖动，使训练过程更稳定，便于在单卡上规模化调优（例如用一张24GB卡微调7B模型）。

  - 轮转间隔T的选择对最终效果不敏感，可优先设置较大值加速收敛，减少工程调参负担；该设计也可迁移至推荐系统的稀疏参数更新（如Embedding表的轮转更新）。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
全参数微调（FFT）虽效果好，但内存开销巨大，限制了大模型在资源受限环境的应用。参数高效微调（LoRA等）存在复杂推理任务的性能差距，而现有内存高效方法（LOMO、BAdam、HiFT）或牺牲动量/二阶矩，或因层间参数大小差异导致内存剧烈波动，且反向传播时仍需计算完整梯度，造成计算浪费。  

**方法**  
ChunkFT将可训练参数按**字节级训练开销**（含参数、梯度、fp32主副本、AdamW状态）均衡划分为K个轮转块，每次只激活一块：
- 每个块维护CPU端fp32权重与优化器状态，激活时异步加载至GPU；
- 前向计算使用全模型，**反向仅对激活块内的参数切片生成梯度**（通过自定义算子实现，无需修改网络结构）；
- 同一块连续更新T步后切至下一块，支持梯度累积及AdamW完整动量和二阶矩；
- 理论分析表明该轮转优化等价于块坐标下降，收敛到一阶稳定点。  

**关键结果**  
- **内存**：Llama 2-7B，FP32，序列1024，batch=1仅需13.72 GB，而LoRA约18-20 GB；batch=8时26.71 GB，显著低于BAdam（58.90 GB）和HiFT（54.91 GB），且内存抖动率仅0.01（BAdam 0.44）。  
- **速度**：在BoolQ上，batch=8时耗时4855秒，快于BAdam（5690秒）和HiFT（6501秒），与LoRA接近（4154秒）。  
- **性能**：RoBERTa-large SuperGLUE平均77.6，超越Adam（74.9）；Llama 2-7B SuperGLUE平均84.9，超越所有基线；Llama 3-8B数学推理平均47.7，优于APOLLO（46.6）等；Llama 3-70B数学平均63.7，同样最优；MT-Bench上Llama 2-7B达5.6，Llama 3-8B达6.8，均超过全参数微调。  

> **一句话**：ChunkFT通过“轮转激活、按字节分块”将全参数微调的内存降至LoRA量级，同时保持甚至超越全参数微调的性能。
