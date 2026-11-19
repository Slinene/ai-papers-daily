---
title: On-Policy Morphing into Hybrid Attention Models
title_zh: FlashMorph2：On-Policy 层选择构建混合注意力模型
authors:
- Disen Lan
- Xuanda Wang
- Jianbin Zheng
- Huafeng Kuang
- Wei Tang
- Yu Cheng
affiliations:
- Fudan University
- ByteDance Seed
- Nanyang Technological University
arxiv_id: '2611.24809'
url: https://arxiv.org/abs/2611.24809
pdf_url: https://arxiv.org/pdf/2611.24809
published: '2026-11-18'
collected: '2026-11-19'
category: Training
direction: 混合注意力模型层选择与恢复训练
tags:
- Hybrid Attention
- Layer Selection
- On-Policy
- LLM Efficiency
- Long Context
- FlashMorph2
one_liner: 用 on-policy 层选择与恢复目标下的联合优化，高效将预训练 Transformer 改造成混合注意力模型
practical_value: '- 业务中部署长上下文 LLM（如超长行为序列、多文档商品信息）时，混合注意力可大幅降低 KV cache 成本；FlashMorph2
  仅需 0.72–3.57 GPU 小时即可完成 0.6B–8B 模型改造，适合有预算限制的团队快速尝试。

  - 层选择必须 on-policy：不要用连续插值或 teacher-forced 隐藏状态评估，而应在实际离散混合架构上用自己的隐藏状态做 logits distillation；否则选择策略与部署架构不一致，恢复后效果明显变差。

  - 选层阶段冻结权重会忽略后续恢复训练的影响；将层选择分数和模型权重在恢复目标下联合优化（类似 NAS 的一阶/二阶优化）能显著提升长上下文检索/召回任务，对召回密集型业务尤其有用。

  - 对于 Agent 或 RAG 场景中的长上下文推理，可以只在少数关键层保留 full attention，其余层用线性注意力；FlashMorph2 在召回密集型任务上
  +0.76，说明这种方案在需要精确信息抽取的业务链路中风险较低。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

## 动机
混合注意力模型（部分层 full attention + 部分层 linear attention）能平衡长上下文建模能力与推理效率。把预训练 Transformer 改造成这种结构，核心是决定在预算下哪些层保留 full attention。现有 FlashMorph 采用 off-policy 层选择，存在两个不一致：① 连续分支插值和 teacher-forced 隐藏状态与离散混合计算的实际路径不符；② 选层时权重冻结，未考虑后续恢复训练中的参数适配。

## 方法关键点
FlashMorph2 提出 on-policy 层选择：每次迭代采样离散的 hybrid architecture，用该架构自己的隐藏状态进行端到端评估，而不是依赖教师模型的隐藏状态。具体使用 TopK(φ+g, K) 采样离散层选择，并用 logits distillation 作为层选择损失。同时，在恢复目标下联合优化层选择分数和模型权重，使选择结果能反映适配后的真实性能。

## 关键结果
在 Qwen3 0.6B–8B 多个规模和多种 linear attention 变体上，FlashMorph2 一致优于现有层选择方法：相比 FlashMorph，RULER 平均提升 +2.42 分，LongBench 提升 +1.08，召回密集型任务提升 +0.76。层选择过程仅需 0.72–3.57 GPU 小时，高效且可扩展。
