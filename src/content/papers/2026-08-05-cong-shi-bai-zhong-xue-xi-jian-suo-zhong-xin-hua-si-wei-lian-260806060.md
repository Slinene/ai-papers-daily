---
title: 'Learning from Failures: Retrieval-Centric CoT via Hard Negatives for Unified
  Multimodal Retrieval'
title_zh: 从失败中学习：检索中心化思维链与难负样本驱动的统一多模态检索
authors:
- Zelong Sun
- Jun Wang
- Kaicheng Yang
- Tiancheng Gu
- Ziyong Feng
- Zhiwu Lu
affiliations:
- Glint Lab
arxiv_id: '2608.06060'
url: https://arxiv.org/abs/2608.06060
pdf_url: https://arxiv.org/pdf/2608.06060
published: '2026-08-05'
collected: '2026-08-07'
category: RecSys
direction: 多模态检索 · 检索中心化思维链
tags:
- Multimodal Retrieval
- Chain-of-Thought
- Hard Negative Mining
- Dual-Mode Embedder
- Reinforcement Learning
- LVLM
one_liner: 提出UniME-R1，基于检索反馈生成思维链纠正嵌入器混淆，借助难负样本与强化学习提升检索
practical_value: '- **检索反馈驱动的思维链**：在推荐重排序阶段，可对初始召回结果生成解释性推理文本，放大易混淆 item 的细微差异，用于
  query 改写或特征增强。

  - **难负样本挖掘策略**：有效模拟线上召回失败 case，尤其适用于构建对抗训练集，提升模型对相似商品/视频的判别力。

  - **双模式嵌入器设计**：直接检索与 CoT 增强检索双路并行，可在精排场景中作为混合表示，或用于多阶段漏斗中粗精排衔接。

  - **检索导向强化学习**：将对齐奖励直接定义在检索指标上，可迁移至推荐场景中，优化生成式推荐模型的最终曝光收益而非中间 token 似然。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：统一多模态检索常因忽略细粒度判别线索而导致语义相似候选混淆。现有 CoT 方法仅从查询侧生成解释，未诊断检索器自身的误解。论文主张有效检索推理应基于检索反馈。

**方法**：提出 UniME-R1，由嵌入器和顾问组成。顾问以初始检索结果为条件，逐候选项分析被嵌入器混淆的鉴别线索，生成检索中心化思维链 (RC-CoT)。若目标在 top-k 内，直接重排；否则用 RC-CoT 精炼检索方向，由双模式嵌入器在全库重检。训练时，挖掘难负样本模拟真实失败，联合优化直接检索与 RC-CoT 增强检索，并采用监督学习和检索导向强化学习对齐顾问输出与检索结果。

**结果**：在 MMEB-V2 及多个通用多模态检索基准上，UniME-R1 一致提升检索性能，超越多个强基线。
