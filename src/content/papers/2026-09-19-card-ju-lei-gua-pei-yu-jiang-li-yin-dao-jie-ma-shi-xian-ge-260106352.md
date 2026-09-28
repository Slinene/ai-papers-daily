---
title: 'CARD: Cluster-level Adaptation with Reward-guided Decoding for Personalized
  Text Generation'
title_zh: CARD：聚类适配与奖励引导解码实现个性化文本生成
authors:
- Yutong Song
- Jiang Wu
- Weijia Zhang
- Chengze Shen
- Shaofan Yuan
- Weitao Lu
- Jian Wang
- Yu Wang
- Nikil Dutt
- Amir M. Rahmani
affiliations:
- University of California, Irvine
- University of Amsterdam
- TikTok
arxiv_id: '2601.06352'
url: https://arxiv.org/abs/2601.06352
pdf_url: https://arxiv.org/pdf/2601.06352
published: '2026-09-19'
collected: '2026-09-28'
category: LLM
direction: LLM 个性化文本生成 · 聚类 LoRA 与解码注入
tags:
- Personalization
- LoRA
- Reward-guided Decoding
- Clustering
- Text Generation
- PEFT
one_liner: 提出分层个性化框架 CARD：用户聚类学习组级 LoRA，簇内对比隐式学习个体偏好，推理仅解码注入实现高效个性化生成
practical_value: '- 电商/广告文案生成可借鉴“先用户聚类 + 组级 LoRA”的两级适配：用行为或风格特征对用户分簇，每簇训练一个 LoRA，避免
  per-user 全量微调，兼顾个性化与规模化部署。

  - 簇内个体差异无需人工标注：用用户历史真实文本（如历史点击商品标题、评价、搜索词）作为正样本，簇级通用生成文本作为负样本，做对比学习得到轻量 user preference
  vector，可直接迁移到个性化 push 文案、商品描述生成。

  - 推理时个性化只注入 decoding：base model 冻结，仅加载 lightweight user preference vectors 和 low-rank
  logit corrections；工程上线上可按用户簇切换对应 LoRA 和向量，存储与推理开销低，适合需要高频 A/B 和千人千面文案的推荐场景。

  - 冷启动用户可先归入簇使用组级 LoRA + 默认偏好向量，后续积累数据再学习个体向量，平滑过渡成本低，可复用到新客或低活用户个性化激活。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：LLM 个性化文本生成需在细粒度个性化与可扩展部署间平衡。RAG 方法面临历史文本拼接带来的上下文成本与噪声，PEFT 方法若按用户全量微调则难以规模化，且个体差异常缺乏显式标注。

方法关键点：CARD 采用分层渐进式个性化。先按用户共享风格模式聚类，为每个簇学习 group-specific LoRA adapter，提供稳健泛化与低资源表现。为捕获簇内个体差异，提出隐式偏好学习机制：对比用户自己撰写的文本与簇级生成文本，无需人工标注即可推断用户风格偏好。推理阶段个性化仅注入 decoding：使用轻量 user preference vectors 与 low-rank logit corrections 修改输出分布，base model 保持冻结。这种设计把个性化与模型主体解耦，降低部署与更新成本。

关键结果：在 LaMP 与 LongLaMP 个性化文本生成基准上，CARD 的生成质量优于对比基线，同时显著提升效率与可扩展性，适合实际个性化文本生成场景。
