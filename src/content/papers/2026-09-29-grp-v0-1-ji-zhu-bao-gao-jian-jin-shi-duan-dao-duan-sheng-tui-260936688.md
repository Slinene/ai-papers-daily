---
title: GRP v0.1 Technical Report
title_zh: GRP v0.1 技术报告：渐进式端到端生成推荐
authors:
- Wenfeng Zhuo
- Vincent Xue
- Charles Wei
- Cong Ni
- Ruiming Lu
- Jiwen Ren
- Mo Li
- Peng Yang
- Xufei Wang
- Dongheng Li
affiliations:
- Snap Inc.
arxiv_id: '2609.36688'
url: https://arxiv.org/abs/2609.36688
pdf_url: https://arxiv.org/pdf/2609.36688
published: '2026-09-29'
collected: '2026-09-30'
category: GenRec
direction: 生成式推荐 · Semantic ID 与统一排序
tags:
- Semantic ID
- Generative Recommendation
- GRPO
- Multi-Head Prediction
- Progressive Deployment
- Serving Optimization
one_liner: 单编码器-解码器统一生成式召回与排序，冻结排序头作奖励并用带 margin 的 GRPO 保护召回，按渐进路径在线替换级联
practical_value: '- 渐进式迁移：不要一次性替换多阶段级联。先把生成模型作为一个召回源上线，按 source rate / ranking pass
  rate / engagement profile 与现有源逐一对比，退役被压制源并把 quota 转给模型，再逐步 bypass ranker。这套协议适合把
  LLM 生成式召回引入电商/信息流。

  - 统一生成与排序的模块设计：用 stop-gradient 的 MHP 作为 ranking head，避免排序 loss 干扰生成表征；候选必须通过 residual
  path 直接进 DCN-V2，否则 cross-attention 可能学会忽略候选，退化到只学用户先验。业务上可复用到统一召回+精排模型。

  - 强化学习要保护 logged target recall：mGRPO 的 one-sided reference-anchored margin 能防止 policy
  为 reward 漂移而丢失真实目标；在电商推荐有用户真实行为时，可以把 SFT 后的生成式召回用 RL 微调，并结合 margin 维持召回。

  - 工程/新鲜度：item-level fusion 将一个历史 item 压缩为单 token、encoder:decoder 1:2 更省时；Semantic
  ID 到 item 的映射异步刷新，配合持续增量训练应对 catalog 快速变化；KV cache + CUDA graph + C++ 预处理可把生成检索延迟降约
  70%。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

动机：直接用一个生成模型替换多阶段级联推荐会得到负向线上结果；级联内含大量新鲜度、资格过滤、校准、多样性规则，生成模型没有；且 frozen 模型在快速变化目录上 exact-item recall 几天内崩塌。因此采用渐进式部署：先作为 retrieval source 进入漏斗，逐源对比，淘汰弱源，最后 bypass ranker。

方法关键点：
- 架构：T5 风格 encoder-decoder；Qwen3-VL Semantic ID 做分层 code，加 co-engagement contrastive 提升 codebook 利用率；item-level fusion 将每个历史 item 压成 1 个 token，扩展历史 4×；偏 decoder 的 1:2 层配比；block-wise 独立解码候选 item。
- 排序与奖励：共享 trunk 的 MHP 模块通过 stop-gradient 输入，生成候选经 residual path 直连 DCN-V2，防止 cross-attention 忽略候选；冻结该模块作为 RL reward。
- 后训练：只训练 decoder，用 mGRPO，在 GRPO 之上加 one-sided reference-anchored margin，保护 logged target 的 log-prob 竞争优势。
- Serving：异步 SID→item catalog，configurable bypass early ranker；KV cache + CUDA graph 等将检索阶段延迟降 69%。

关键结果：
- 离线：Qwen3-VL SID 较 MM-SID Recall@20 +11.9%；MHP 重设计使 Complete AUROC +20.9%、Share AUPRC +114.6%；mGRPO Reward Recall@10 +1.6%（1节点）/ +3.1%（2节点）且 Recall 不降。
- 在线：作为 retrieval source，RL view time +0.45% vs SFT；RL+4× decode budget view time +0.39%（p=.031）；早期 bypass 后，post-trained source rank 升至第4且中性；替换弱源后 view time +0.82%、shares +2.56%。

最值得记住的一句话：**不要用“一晚替换级联”来评测生成式推荐；把模型作为新召回源逐源对比、复用自身排序头做奖励并以 margin 保护召回，才是可落地的端到端路径。**
