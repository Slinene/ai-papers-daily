---
title: How Much Training-Inference Mismatch Can On-Policy Distillation Tolerate?
title_zh: 在线蒸馏能容忍多少训练-推理失配？
authors:
- Cong Yu
- Ziting Wang
- Songlin Jiang
- Sitong Zhang
- Chengliang Chai
- Youhe Jiang
- Eiko Yoneki
- Tuo Shi
affiliations:
- Aalto University
- Nanyang Technological University
- Beijing Institute of Technology
- University of Cambridge
- Shenzhen University of Advanced Technology
arxiv_id: '2611.11450'
url: https://arxiv.org/abs/2611.11450
pdf_url: https://arxiv.org/pdf/2611.11450
published: '2026-11-07'
collected: '2026-11-11'
category: Training
direction: LLM 在线蒸馏的训练-推理失配容忍度
tags:
- On-Policy Distillation
- Training-Inference Mismatch
- Quantization
- Asynchronous Rollouts
- FP8
- KV Cache
one_liner: OPD对训练-推理失配容忍度高，模型相关量化预算，FP8+异步rollout训练提效1.62倍
practical_value: '- 做生成式推荐/Agent 策略在线蒸馏时，可先标定 mismatch budget：量化、异步 rollout 造成的训练-推理失配在一定阈值内不会明显损失效果，不必追求完全一致的推理环境，省下的算力可投入更大
  KV cache 或更高异步度。

  - 采用 lightweight admission check：用少量校准样本评估候选配置（FP8/int8、staleness 步数）是否在预算内，避免全量训练试错，显著降低实验成本。

  - 模型特定 FP8 配方可提升 1.93 倍 KV-cache 容量，适合长序列用户行为建模（历史行为文本、会话推荐），同时保持训练质量；可探索逐层量化，敏感层保留
  BF16。

  - 注意权重噪声/异步造成的序列级前缀偏移，逐 token 校正不够；训练/部署时需监控序列级指标而非只看 token loss。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：On-policy distillation（OPD）需模型采样自身回复并由固定教师打分，推理成本高；常见用量化推理与异步 rollout 降本，但引入训练-推理失配，在 RL 中会破坏稳定性，对 OPD 的影响未知。

方法：将所有失配来源统一到一个尺度，三对师生模型上测量化，单对模型上测权重滞后与注入噪声；提出轻量 admission check，用校准预算筛选 rollout 配置，避免为每个候选跑完整训练；设计模型专属 FP8 配方。

结果：OPD 可容忍大量失配且训练质量无明显下降，更高水平时退化，形成经验失配预算；量化质量代价及量化引入的失配因模型而异，部分层对低精度敏感；在会使 RL 失稳的 rollout 配置下 OPD 仍稳定；权重噪声下失配改变生成前缀，引入逐 token 校正无法解决的错误；FP8 配方保持训练质量，KV-cache 容量至少为 BF16 的 1.93 倍，FP8+异步 rollout 达到同等质量速度快 1.62 倍。
