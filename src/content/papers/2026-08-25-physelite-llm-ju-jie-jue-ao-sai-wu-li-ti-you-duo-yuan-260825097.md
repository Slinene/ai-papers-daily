---
title: 'PhysElite: How Far Are LLMs from Solving Olympiad-Level Physics Problems?'
title_zh: PhysElite：LLM 距解决奥赛物理题有多远
authors:
- Ruoran Xu
- Wending Gao
- Liyunfeng Chen
- Aixin Shi
- Haoyu Cheng
- Zixiang Fang
- Yiqiang Zou
- Qiufeng Wang
affiliations:
- Xi'an Jiaotong-Liverpool University
arxiv_id: '2608.25097'
url: https://arxiv.org/abs/2608.25097
pdf_url: https://arxiv.org/pdf/2608.25097
published: '2026-08-25'
collected: '2026-08-30'
category: Eval
direction: 多模态 LLM 物理推理基准与过程评估
tags:
- Multimodal LLM
- Physics Reasoning
- Benchmark
- Process Evaluation
- Olympiad
- Bilingual
one_liner: 构建大规模双语多模态物理奥赛基准 PhysElite，含 11586 题；最强多模态模型答案准确率仅 33.7%，并提供步骤级过程评估。
practical_value: '- 步骤级过程评估可迁移到电商推荐 Agent 的诊断：在 query 改写→召回→排序→解释等多步推理链中，对中间步骤单独打分，定位失败子环节，而不是只看最终推荐命中率。

  - 构建垂类专家级评测集的思路可借鉴：覆盖知识点、视觉形式和解题过程，用于电商商品知识问答、促销规则计算等多模态场景，衡量 LLM 的业务推理能力。

  - 复杂物理题中 MLLM 准确率仅 33.7%，提示业务中的数值计算、多步推理不能完全依赖 LLM，应结合计算器、规则引擎等外部工具，如价格、库存、优惠叠加逻辑。

  - 双语对齐和分步解答标注可用于微调生成式推荐理由、购物决策解释，让模型输出可核验的推理过程。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

动机：现有物理基准难度偏低，对视觉形式、知识点和逐步解题过程的覆盖不足，无法真实反映多模态大模型在专家级物理推理上的能力。  
方法：构建 PhysElite，包含 11586 个奥赛级物理问题，每题配备视觉图、中英双语分步解答和最终答案；评测 18 个开源与闭源 MLLM，除最终答案准确率外，还引入步骤级过程评估来定位推理链中的失败位置。  
结果：最强模型答案准确率仅 33.7%，过程评估显示模型在不同步骤的失分模式差异明显；数据已在 HuggingFace 公开。
