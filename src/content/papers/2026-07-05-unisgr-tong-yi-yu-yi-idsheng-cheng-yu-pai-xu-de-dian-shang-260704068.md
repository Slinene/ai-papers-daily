---
title: 'UniSGR: Unified Framework for Semantic ID Generation and Ranking'
title_zh: UniSGR：统一语义ID生成与排序的电商生成式推荐框架
authors:
- Jiawei Sun
- Jun Yang
- Ziyue Guo
- Dongyue Xu
- Jianan Yan
- Lifang Deng
- Xiaoyi Zeng
affiliations:
- Alibaba International Digital Commerce Group
arxiv_id: '2607.04068'
url: https://arxiv.org/abs/2607.04068
pdf_url: https://arxiv.org/pdf/2607.04068
published: '2026-07-05'
collected: '2026-07-07'
category: GenRec
direction: 生成式推荐 · Semantic ID 多目标排序
tags:
- Semantic ID
- Generative Retrieval
- Multi-Objective Ranking
- VA-PMTP
- Task-Aware Tokens
- STARK
one_liner: 将多目标排序与语义ID生成联合训练，通过价值感知并行预测和任务感知Token缓解级联系统的目标错位
practical_value: '- **生成 + 排序共享表示**：在生成式推荐解码器上直接附加多目标排序模块（PLE），排序损失反向传播优化生成器表示，解决级联架构的目标错位问题，可复用到自家生成式召回系统。

  - **价值感知的并行多Token预测（VA-PMTP）**：为同一会话中的点击/加购/购买行为分别生成语义ID，并用业务价值权重（购买 > 加购 > 点击）加权的损失函数，使生成器天然偏向高价值候选，适用于多目标场景的召回优化。

  - **任务感知Token（TAT）**：在解码器输入前拼接可学习的点击/加购/购买任务Token，并通过漏斗感知对比学习（FACL）引导Token与对应行为物品表示对齐，几乎不增加推理成本就能注入目标偏好，适合需要多业务目标解耦的推荐系统。

  - **STARK树状注意力推理加速**：将束搜索的批次维度扩展改为序列维度扩展，利用预定义树注意力掩码消除前缀重复计算，用于语义ID生成推理可获得200%吞吐提升，在检索阶段可直接应用以降低延迟。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
电商推荐系统通常采用级联架构，上游检索与下游排序优化目标不一致，导致高价值但被检索遗漏的 item 无法被重排。生成式检索虽然能端到端生成候选，但缺乏细粒度的多目标排序能力。为此，论文提出 UniSGR，将语义 ID 生成与多目标排序统一在一个框架内训练，从根本上缓解目标错位。

## 方法关键点
- **二阶段训练范式**：先在多业务场景混合数据上做生成式预训练（Next Token Prediction），再进行场景特定的对齐微调，同时优化生成与排序任务。
- **价值感知并行多Token预测（VA-PMTP）**：为同一会话内的点击、加购、购买 item 分别生成语义 ID，并通过业务价值权重加权损失，使生成器倾向于输出高价值候选。
- **统一多目标排序模块**：复用了生成阶段的语义 ID、编码器表示及解码器隐藏状态，通过 Target Attention + PLE 结构预测多目标分，排序损失直接优化共享的表示。
- **任务感知Token（TAT）与漏斗对比学习**：在解码器前插入点击、加购、购买三个可学习 Token，通过对比学习让各 Token 对齐对应行为的 item 表示，使生成过程天然携带目标偏好信号。
- **STARK 推理加速**：用序列维度的树状注意力替代束搜索中的批次维度扩展，避免 KV cache 重复复制，在工业场景下提升 200% 吞吐。
- **Tokenization**：基于 Qwen3-VL 提取多模态 embedding，通过 RQ-VAE 3 层 codebook（8192 大小）平衡碰撞率与容量。

## 关键结果
- **离线测试**：在 Lazada 首页“Guess You Like”场景，UniSGR 的 HR@100 达 0.2195，显著优于 TIGER、OneRec 等基线；两阶段训练相比单一阶段训练在点击/加购/购买 HR 上均有明显提升。
- **消融实验**：MoE 结构对提升容量至关重要（移除后 HR@100 从 0.2195 降至 0.1725）；8192 codebook 是碰撞率与收益的最佳平衡点；模型规模从 0.2B 扩展到 2.0B 时呈现稳定但逐渐递减的收益。
- **在线 A/B 测试**：相比生产级联系统，IPV 提升 3.36%，交易笔数提升 2.17%，GMV 提升 5.68%。

## 最值得记住的一句话
联合生成与排序并共享解码器表示，用价值权重引导生成过程，能同时提升召回命中率和多目标业务指标。
