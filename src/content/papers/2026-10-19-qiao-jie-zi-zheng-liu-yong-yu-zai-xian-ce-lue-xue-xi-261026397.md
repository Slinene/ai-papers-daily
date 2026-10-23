---
title: Bridged Self-Distillation for On-Policy Learning
title_zh: 桥接自蒸馏用于在线策略学习
authors:
- Runsheng Chen
- Yihong Liu
- Raoyuan Zhao
- Michael A. Hedderich
- Hinrich Schütze
- Matthias Grabmair
affiliations:
- Technical University of Munich
- LMU Munich
- Munich Center for Machine Learning (MCML)
arxiv_id: '2610.26397'
url: https://arxiv.org/abs/2610.26397
pdf_url: https://arxiv.org/pdf/2610.26397
published: '2026-10-19'
collected: '2026-10-23'
category: Training
direction: 蒸馏训练 · On-Policy 推理蒸馏
tags:
- self-distillation
- on-policy distillation
- reasoning traces
- cross-tokenizer
- closed API teacher
one_liner: 提出 Bridged Self-Distillation 统一框架，用教师推理轨迹作特权上下文，通过自教师与 verifier 实现在线策略蒸馏，适用于任意教师场景
practical_value: '- 蒸馏大模型用于业务中的 query 生成、推荐解释、Agent 规划时，若教师是开 API 或分词器不同，可直接采用 BSD：教师只输出推理文本作为上下文，学生自我蒸馏，省去
  logits 对齐和词汇映射。

  - 用业务 verifier（点击率、转化率、规则满足等）作为结果信号，结合在线策略样本只对失败 rollout 施加 token 级修正，可训练出更贴合业务目标的小模型。

  - 特权上下文技巧可迁移：训练时给模型额外的推理线索或高质量解释，推理时不暴露，类似推荐中训练时使用详细的用户行为解释，部署时只用原始特征，可有效提升小模型能力。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
从强教师模型蒸馏到小模型面临两个不匹配：教师的解可能难以模仿，且 token 级概率不兼容甚至不可用。不同教师场景（共享 tokenizer、跨 tokenizer、闭源 API）通常需要各自定制监督方式。

**方法关键点**  
提出 Bridged Self-Distillation (BSD)。外部教师只负责离线生成推理轨迹作为特权上下文；学生模型在无该上下文的情况下生成 rollout；学生的一个副本以该上下文为条件，作为“自教师”在学生自身的 token 空间中对相同 rollout 打分。然后利用得到的 token 级指导来调整不成功 rollout 上的更新，由 verifier 提供结果信号。由于外部教师仅被查询来生成文本，同一训练流程可直接迁移到共享 tokenizer、跨 tokenizer 和闭源 API 三类教师场景。

**关键结果**  
在三类教师场景中，BSD 均相较基础模型取得提升，并超过为各场景专门设计的基线方法，展示了统一的蒸馏路径。
