---
title: 'FIRM-Video: Check Before You Score for Reliable Text-to-Video Reward Modeling'
title_zh: FIRM-Video：先检查再评分实现可靠文本到视频奖励建模
authors:
- Peiyuan Zhang
- Xiangyu Zhao
- Hongbo Liu
- Xiaoxing Hu
- Mingxin Liu
- Shuran Ma
- Yunhang Shen
- Jian Hu
- Haihan Gao
- Haoyu Cao
affiliations:
- Shanghai Jiao Tong University
- Tencent Youtu Lab
- Tongji University
arxiv_id: '2608.21839'
url: https://arxiv.org/abs/2608.21839
pdf_url: https://arxiv.org/pdf/2608.21839
published: '2026-08-21'
collected: '2026-08-29'
category: Eval
direction: 文本到视频奖励模型 · 评估基准
tags:
- Text-to-Video
- Reward Model
- Checklist
- Evaluation
- Multimodal
one_liner: 提出 check-before-score 清单驱动框架，构建 90K 训练数据和基准，8B 奖励模型在 VBench 上 Best-of-8
  采样达最优
practical_value: '- 在电商视频/广告创意评估中，可将整体评分拆为「指令遵循、世界一致性、感知质量」等维度，并为每个维度构建 checklist；先逐项验证视频证据再聚合分数，避免
  LLM 整体打分时的漏检和归因混淆。

  - 对商品视频生成或文案+视频的联合评估，可借鉴「prompt 分解为加权原子要求」：把用户/运营指令转化为可独立验证的细粒度要求（如颜色、质地、动作、文字），每项单独打分后加权求和，提升判断的稳定性和可解释性。

  - 感知质量维度采用通用视觉缺陷分类（如模糊、闪烁、压缩伪影等），可作为广告素材机审/质量分系统的先验检查表，结合 LLM 做可解释的缺陷定位。

  - 将 checklist 验证结果转化为自然语言分析再训练端到端 reward model 的做法，可复用于构建创意内容优选模型：先用结构化检查生成监督信号，再蒸馏到小模型，用于线上
  Best-of-N 采样或创意排序。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有文本到视频评价方法多采用固定 rubric 的整体打分或开放式推理，存在检查不完整、理由不可信、维度归因纠缠等问题，影响奖励模型的可靠性与效率。

**方法关键点**：提出 FIRM-Video，基于 check-before-score 原则的统一 checklist 驱动数据构建框架。针对指令遵循（IF），把 prompt 分解为带权重的原子要求；针对世界一致性（WC），构建基于可见实体和动作的 prompt 校准目标特定检查；针对感知质量（PQ），使用通用视觉缺陷分类。每个准则先对照时序视觉证据验证，只聚合已验证的决策，并将验证结果与分数转为自然语言分析用于端到端奖励建模。构建 FIRM-Video-90K（29,348 个视频，88,044 个维度特定实例）和 FIRM-Video-Bench（250 视频，750 人标注点）。

**关键结果**：基于 Qwen3-VL 的 FIRM-Video-8B 在 FIRM-Video-Bench 上取得最佳总体 MAE，并在三个视频生成器的 Best-of-8 采样中，一致取得 VBench 的 Total、Quality、Semantic 最高分。
