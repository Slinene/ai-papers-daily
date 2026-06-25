---
title: RoPE-Aware Bit Allocation for KV-Cache Quantization
title_zh: RoPE感知的KV缓存比特分配量化方法
authors:
- Fengfeng Liang
- Yuechen Zhang
- Jiaya Jia
affiliations:
- Hong Kong University of Science and Technology
- The Chinese University of Hong Kong
- Xiaomi Corporation
arxiv_id: '2606.24033'
url: https://arxiv.org/abs/2606.24033
pdf_url: https://arxiv.org/pdf/2606.24033
published: '2026-06-22'
collected: '2026-06-25'
category: LLM
direction: LLM 推理 · KV cache 量化 · RoPE 感知比特分配
tags:
- KV-cache quantization
- RoPE
- bit allocation
- long-context inference
- efficient serving
- attention logit error
one_liner: 将RoPE注意力下的KV缓存量化建模为按频率块分配比特的优化问题，用能量分数贪心分配显著减少查询-键logit误差并提升长文本性能
practical_value: '- 部署长上下文LLM（如客服、历史行为分析）时，可借鉴RoPE分块的能量分布实现差异化比特分配，在相同压缩率下大幅减少关键信号失真，避免统一量化在低比特下的质量崩塌。

  - 使用无标签的激活统计量（Q/K向量的2-范数）计算分块重要性，无需下游任务反馈，适合线上快速校准（仅需少量无标注前缀）。

  - 工程实现参考：采用packed cache布局和融合attention核，直接解压缩到临时寄存器，避免物料化fp16 KV缓存，可有效降低显存带宽压力，使长上下文解码速度超过fp16基线。

  - 方法的核心思路（按结构单元动态分配精度）可迁移至其他位置编码或特征交互场景，例如推荐模型中的特征域重要性差分量化。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
Long-context推理中KV缓存占据显存主要部分，低比特量化是必要的。现有方法将每个键视为平坦向量均匀量化，但RoPE注意力下查询-键logit按2维频率块分解，不同块对量化误差的敏感度差异极大。均匀分配比特会过度保护低影响块而欠保护高影响块，导致logit失真和下游性能崩溃。因此需要面向RoPE结构的块级比特分配。

## 方法
- **块能量分数**：基于预RoPE坐标的Q/K激活统计，计算每个频率块的能量得分 \( s_i = \frac{1}{2} E[||q^{(i)}||^2_2 + ||k^{(i)}||^2_2] \)，该分数无标签，从短校准前缀取得。
- **贪心比特分配**：在给定平均比特预算下，将比特分配给能使 \( \sum_i s_i 4^{-b_i} \) 最小的块，利用边际增益（每次分配四分误差）贪心分配，理论上最优。
- **编码实现**：同比特宽的块分组后使用TurboQuant-MSE局部量化，值（V）保持均匀量化。
- **打包缓存服务**：设计packed cache布局，融合attention核直接从压缩码流解量化为临时张量，避免物料化fp16 KV缓存，显著降低HBM带宽。

## 关键实验结果
- **RoPE-logit fidelity**：在10个模型（涵盖Qwen、Llama、DeepSeek、Mistral、GLM等架构）上，2和3比特预算下，每层RoPE-logit MAE相对均匀TQ-MSE降低32–80%，全部367层对比均获胜。
- **长文本检索与理解**：Llama-3.1-8B-Instruct上K2V2预算时，NIAH六任务平均从70.6升至97.4（接近fp16的99.6），LongBench-EN八任务平均从36.87升至53.31。
- **推理任务**：在AIME 2024/2025上，DeepSeek-R1-Distill-Qwen-7B无近期token缓冲区，K3V2时获得51.7/37.5（fp16为54.2/37.9），而TQ-MSE为0.0。
- **系统加速**：Qwen2.5-3B-Instruct上K3V3实现3.24×压缩，128K上下文时解码延迟1.34×快于fp16 FlashAttention2，峰值显存从56.31GB降至19.85GB，256K/512K长度fp16 OOM时可继续运行。

> **一句话点睛**：按照RoPE频率块的能量高低动态分配量化比特，能用极低的额外开销，将原本在2–3比特崩溃的KV缓存质量拉回接近fp16的水平，让长上下文LLM真正可部署。
