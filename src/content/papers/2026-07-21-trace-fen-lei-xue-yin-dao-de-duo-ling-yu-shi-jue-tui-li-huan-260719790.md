---
title: 'Trace: A Taxonomy-Guided Environment for Multidomain Visual Reasoning'
title_zh: TRACE：分类学引导的多领域视觉推理环境
authors:
- Md Tanvirul Alam
affiliations:
- Rochester Institute of Technology
arxiv_id: '2607.19790'
url: https://arxiv.org/abs/2607.19790
pdf_url: https://arxiv.org/pdf/2607.19790
published: '2026-07-21'
collected: '2026-07-26'
category: Reasoning
direction: 可验证奖励的视觉推理合成训练
tags:
- RLVR
- Visual Reasoning
- Procedural Data
- VLM
- Synthetic Data
- Scene Grammar
one_liner: 基于场景语法与可执行任务程序构建可控、可验证的多域视觉推理数据，RL微调使VLM跨24基准平均提升3.5–4.1个百分点
practical_value: '- **合成商品图像训练数据**：借鉴场景语法（scene grammar）思想，按属性（背景、角度、材质）程序化生成大量商品图片，训练多模态模型精准理解商品属性，替代昂贵的人工拍摄。

  - **可自动验证的视觉问答构造**：利用可执行任务程序（task program）生成带精确答案的视觉问题，实现完全自动化的评测与奖励计算，可用于商品详情页问答、图像描述一致性校验等场景。

  - **RL微调提升多模态Agent决策**：将RLVR框架迁移至真实业务指标（点击率、转化率等可计算信号），微调多模态Agent在图像排序、商品匹配等任务中的推理能力，无需额外人工标注。

  - **分类学控制生成多样化训练样本**：采用taxonomy-guided variation机制，可扩展到搜索词、查询意图的组合生成，丰富长尾覆盖，增强模型在电商推荐中的泛化能力。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：RLVR在语言模型上显著提升推理能力，但在视觉-语言模型上的扩展受限于缺乏广覆盖、精确可验证且可复现的训练数据。现有方案要么混合多源数据带来异构性，要么局限于单一场景生成。

**方法关键点**：提出TRACE环境，通过场景语法和可执行任务程序将任务构造分解为视觉生成与答案计算两部分。共享的语义状态驱动图像渲染、问题提示、类型化答案、验证器及可回放轨迹。环境包含1000个任务、277个场景语法、11个视觉域，支持语义和视觉的受控变化。在生成的64000个实例上对Qwen2.5-VL进行RLVR微调，奖励来自精确的答案匹配。

**关键结果**：微调后，Qwen2.5-VL-3B在24个外部基准上的宏平均提升3.51个百分点，7B提升4.06个百分点，证明广义的程序化训练可迁移到任务分布之外。
