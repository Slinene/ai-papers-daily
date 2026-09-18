---
title: 'UniPolicy: Unified Objective-Specific Policies for Generative Search Advertising'
title_zh: UniPolicy：生成式搜索广告的统一目标专属策略
authors:
- Kun Yao
- Yuhang Zhou
- Yichi Zhang
- Zeliang Tong
- Shengri Xue
- Haitao Wang
- Siyu Lu
- Qianlong Xie
- Xingxing Wang
affiliations:
- Meituan
arxiv_id: '2609.20630'
url: https://arxiv.org/abs/2609.20630
pdf_url: https://arxiv.org/pdf/2609.20630
published: '2026-09-17'
collected: '2026-09-18'
category: GenRec
direction: 生成式广告检索 · 多目标RL对齐
tags:
- Generative Retrieval
- Multi-Objective RL
- MoE-LoRA
- Semantic ID
- Search Advertising
- GRPO
one_liner: 用目标前缀、MoE-LoRA路由和专属FFN解耦多目标生成式广告检索策略，在线提升CTR/RPS/收入
practical_value: '- 多目标生成式检索不要简单 reward fusion：用 objective prefix token + 稀疏 MoE-LoRA
  + objective-specific FFN，在同一个生成骨干上做层级参数隔离，显著缓解 eCPM/CTR/相关性之间的梯度竞争。

  - 利用多阶段行为日志构造 Click > Exposure > Miss 的 pairwise margin loss，把“曝光未点击”样本用起来，显式建模候选间相对偏好，能提升生成结果的
  NDCG 和点击候选排序。

  - 推理侧采用共享 KV cache 的并行多策略 beam search，业务可灵活分配各目标候选配额；固定候选预算下用 trim-and-backfill
  兜底，P99 延迟只增加 2.5%，适合工业检索在线部署。

  - 目标前缀 token 可控性强：单独输入 <eCPM>、<CTR>、<Relevance> 即可触发对应偏好，线上可以按活动或场景动态调整配额，复用到电商推荐/广告召回的多业务目标平衡。'
score: 10
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
生成式搜索广告检索通常对齐单一奖励（如 eCPM）或对多奖励做简单加权融合。单目标会牺牲用户体验和长期生态；朴素融合则把异质目标压缩到同一参数空间，梯度竞争导致某一目标主导、其他目标信号被淹没。此外，传统生成式检索只依赖点击正样本，难以利用曝光未点击等行为差异，推理时单目标 beam search 也无法按业务偏好灵活分配候选配额。

## 方法关键点
- **目标条件前缀 tokens**：为 eCPM、CTR、Relevance 分别设计 learnable prefix token，拼接到输入序列，既注入目标隐式 prompt，又引导后续参数路径。
- **稀疏 MoE-LoRA 参数解耦**：在 Transformer FFN 侧并联多个 LoRA branch，用轻量 router 动态选 top-3，不同目标激活不同低秩子空间；加入负载均衡 loss 和多样性 loss 防止专家坍塌。
- **目标专属残差 FFN**：在顶层输出层为每个目标保留独立 FFN，进一步在策略表达层解耦。
- **多阶段行为漏斗偏好**：利用 Click、Exposure、Miss 构造 Click > Exposure > Miss 序关系，设计带 margin 的 pairwise Funnel loss，补充点击-only 监督缺失的相对偏好。
- **训练与推理**：每个目标独立 rollout 和 GRPO 优化，禁用 KL；推理时共享 KV cache 并行 beam search，按业务配额合并候选，trim-and-backfill 保证固定候选预算。

## 关键实验
在美团搜索广告系统的大规模日志上训练和评估，对比 SFT、单目标 GRPO、Reward-Sum GRPO、Sequential GRPO、MOPD。UniPolicy 取得最高 NDCG@10（0.4218），归一化 eCPM@1=1.129、CTR@1=1.046、Rel@1=1.172，均超过对应单目标 GRPO 基线。7 天在线 A/B 显示：CTR +0.71%，RPS +1.58%，广告收入 +1.32%，P99 延迟仅 +2.5%。

**最值得记住的一句话**：多目标生成式检索的出路不是 reward fusion，而是 policy decoupling——用目标前缀+稀疏参数路由在共享骨干内保留多个可独立优化的策略空间。
