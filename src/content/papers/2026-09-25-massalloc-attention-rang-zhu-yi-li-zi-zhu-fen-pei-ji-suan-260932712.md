---
title: 'MassAlloc Attention: Let Attention Allocate Its Own Compute'
title_zh: MassAlloc Attention：让注意力自主分配计算
authors:
- Jingze Shi
- Zhangyang Peng
- Xianduo Li
- Yanlin Qi
- Xiaotian Lin
- Haoxian Chen
- Liangdong Wang
- Guang Liu
- Yuyu Luo
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Beijing Academy of Artificial Intelligence
- Université Paris Cité
arxiv_id: '2609.32712'
url: https://arxiv.org/abs/2609.32712
pdf_url: https://arxiv.org/pdf/2609.32712
published: '2026-09-25'
collected: '2026-09-29'
category: Training
direction: 高效注意力 · 自适应计算分配
tags:
- Sparse Attention
- Long Context
- FlashAttention
- Compute Allocation
- Training Efficiency
- Inference Acceleration
one_liner: 提出MALA，保留完整QK打分，按归一化注意力贡献度跳过低价值后处理，显著降低长上下文训练/推理计算且保持精度
practical_value: '- 在长用户行为序列建模或长上下文推荐中，可借鉴 MALA 思路：保留完整 QK 打分以捕获任意长程兴趣依赖，但用归一化贡献阈值跳过低贡献
  tile 的 V 加载和 PV 累积，从而降低线上推理延迟和离线训练 FLOPs，且精度损失极小。

  - 统一阈值 τ/L_q 的设计省去逐层/逐头/逐输入单独标定，适合电商场景中用户序列长度动态变化（从几十到几千）的部署；可根据线上延迟要求全局调整 τ，无需重新训练。

  - 反向传播复用前向保存的 finalized normalizer，仅用标准 attention 状态推导嵌套支持，不额外存 mask 或索引，内存开销与 FullAttn
  持平，对显存受限的推荐模型训练尤其有吸引力。

  - 与 MoBA、DSA 等提前丢弃 QK 的稀疏方法不同，MALA 保留完整 QK 打分，适合需要精确长程关联检索的任务（如跨会话用户兴趣召回、长文档中的商品关联），可作为底层注意力替换方案集成到现有长上下文
  LLM 推荐或 Agent 系统中。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长上下文注意力中，Full softmax attention（FullAttn）的归一化质量高度集中，大量低贡献交互仍执行完整后处理（softmax、V加载、PV累积及反向计算）。现有稀疏方法往往在QK前丢弃交互，可能损失任意长程关联。本文希望保留完整因果QK打分，但让注意力根据自身归一化贡献动态分配post-score计算，降低长上下文训练/推理成本。

### 方法关键点
- 提出 **MALA**，融合注意力原语，分离QK分数发现与post-score执行；每个合法因果tile先计算QK，若贡献低于阈值则跳过后续softmax、V加载、PV累积等。
- 使用统一阈值 **τ/L_q**：L_q为查询可见键数量，τ为共享无量纲容差，避免逐层/逐头标定，实现跨上下文自适应。
- **前向在线分配**：利用演化online-softmax normalizer Z^(t)，测试候选tile最大贡献比值，跳过低于阈值的tile；保证首个合法tile必保留，支持因果访问。
- **反向离线分配**：复用前向保存的finalized normalizer Z_R，与相同阈值判断，推导出嵌套于前向支持内的保留集，无需存储mask或索引，仅使用标准attention状态。
- 支持训练前向/反向、推理prefill/decoding，同一容差；保留完整QK二次复杂度，节省来自低贡献post-score路径。

### 关键实验与结果
- **匹配工作研究**：8K上下文、平均约1024 post-score slots/query下，MALA在线决策的省略质量均值0.0188% vs 参考oracle 0.0182%，静态分配大幅更差。
- **操作保真度**：1K–32K上下文，平均省略质量≤0.0062%，输出误差≤0.021%，梯度误差≤0.38%。
- **关联召回**：8K、d_model=512时MALA准确率89.67% vs FullAttn 89.97%，远超MoBA 47.25%、DSA 52.61%。
- **算子性能**：128K序列、8 H100 TP下，训练前向/反向延迟降低2.2×/3.0×，解码降低1.6×，peak memory与FullAttn持平。
- **缩放定律**：0.6B–14B模型，14B在32K长上下文训练总FLOPs降低23.1%，perplexity差距<0.001。
- **模型级评估**：14B和32B在知识、推理、RULER 32K/128K检索与FullAttn相当。

**最值得记住的一句话**：MALA证明可以在完整保留QK分数发现的前提下，用统一的归一化贡献阈值动态分配post-score计算，实现近FullAttn质量下的大幅训练/推理加速。
