---
title: 'Context-Matched Distillation: Teacher Causality for Autoregressive Video Distillation'
title_zh: 上下文匹配蒸馏：面向自回归视频蒸馏的教师因果性
authors:
- Hmrishav Bandyopadhyay
- Xuanchi Ren
- Zijian Huang
- Jay Zhangjie Wu
- Tianshi Cao
- Ruilong Li
- Bryan Chu
- Sanja Fidler
- Yi-Zhe Song
- Zian Wang
affiliations:
- NVIDIA
- University of Surrey
arxiv_id: '2608.13391'
url: https://arxiv.org/abs/2608.13391
pdf_url: https://arxiv.org/pdf/2608.13391
published: '2026-08-12'
collected: '2026-08-16'
category: Training
direction: 视频生成蒸馏 · 因果对齐
tags:
- Causal Distillation
- Autoregressive Video Generation
- DMD
- Few-step Distillation
- Teacher-Student
one_liner: 提出因果蒸馏框架 CMD，对齐教师评分与学生生成时的因果信息集，提升自回归视频生成控制精度
practical_value: '- 因果对齐的蒸馏思想可迁移到序列生成模型（如自回归推荐、对话式 Agent）：教师评分时应只使用学生生成该 token 时已见到的历史与上下文，避免未来信息泄露造成训练-推理不一致。

  - Prefix Scoring 用学生实际生成的前缀（而非真实前缀）让教师评估当前 token，这类似于 NLP 中的 on-policy 蒸馏，可借鉴到基于
  LLM 的序列推荐或搜索 query 生成中，以缓解 exposure bias。

  - Prefix Corruption 通过对早期不可靠前缀加扰动来稳定训练，可应用于 RLHF 或蒸馏框架中处理训练初期策略不稳定问题，尤其在实时交互式生成场景（如直播电商文案、动态广告素材生成）有价值。

  - 论文主要面向视频生成，与电商/推荐直接业务关联有限，但其中的低延迟自回归生成 + 在线控制思想，对需要实时响应的交互式推荐系统（如对话推荐、动态出价策略）有架构参考意义。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：交互式自回归视频生成要求低延迟 rollout 和精确在线控制。少步蒸馏可加速生成，但现有视频 distribution matching distillation (DMD) 使用双向教师对完整片段评分，导致教师对当前目标的评分依赖未来帧和控制信号，与学生生成时的因果信息集不匹配，损害蒸馏效果。

**方法关键点**：
- 提出 Context-Matched Distillation (CMD)，用因果教师替代双向全片段评分，教师评估每个目标时不访问未来帧或控制。
- 同一因果教师初始化少步学生，保证教师训练、学生蒸馏与推理阶段因果结构一致。
- Prefix Scoring：用学生已生成的缓存前缀评估目标，使教师监督匹配学生实际 rollout 上下文，避免使用真实前缀带来的 distribution mismatch。
- Prefix Corruption：在训练早期对学生生成的不稳定前缀施加扰动，以稳定训练过程。
- CMD 自然扩展到帧级和块级自回归生成、长视频蒸馏以及相机条件控制蒸馏。

**关键结果**：在短视频和长视频基准上取得自回归方法中的最优综合性能，同时显著提升对时变相机控制的遵循度。
