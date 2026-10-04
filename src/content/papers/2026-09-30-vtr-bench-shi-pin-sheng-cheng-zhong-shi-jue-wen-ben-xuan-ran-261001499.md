---
title: 'VTR-Bench: A Systematic Benchmark for Evaluating Visual Text Rendering in
  Video Generation'
title_zh: VTR-Bench：视频生成中视觉文本渲染的系统性评测基准
authors:
- Yu Huang
- Jungang Li
- Zhiyuan Wang
- Yonghua Hei
- Song Dai
- Jiayu Yang
- Deyuan Liu
- Xiang Zheng
- Xiaoshuang Shi
- Hao Cheng
affiliations:
- City University of Hong Kong
- The Hong Kong University of Science and Technology (Guangzhou)
- The Hong Kong Institute of AI for Science, City University of Hong Kong
- Westlake University
- University of Electronic Science and Technology of China
arxiv_id: '2610.01499'
url: https://arxiv.org/abs/2610.01499
pdf_url: https://arxiv.org/pdf/2610.01499
published: '2026-09-30'
collected: '2026-10-04'
category: Eval
direction: 视频生成评测 · 文本渲染
tags:
- Video Generation
- Text Rendering
- Benchmark
- Agentic Framework
- OCR
- WER
one_liner: 系统评估视频生成模型的场景文本渲染能力，并提出关键帧引导的Agentic改进框架
practical_value: '- 广告/商品视频生成：引入 WER/字符级 OCR 校验，把品牌名、价格、卖点文案作为硬性 text fidelity 指标，纳入
  AIGC 创意 pipeline 的自动验收，避免错误文案上线。

  - 关键帧先验与迭代：在生成视频前先用图像模型生成并校验关键帧文字，通过视觉反馈做 candidate selection / refinement；这比直接烧视频生成更省成本，适合筛选电商展示素材。

  - Agentic Director 架构可迁移：Director 协调图像/视频生成与视觉评估，把“生成-检查-修正”闭环用于多模态广告 Agent，结合 prompt-specific
  chain-of-query 同时检查场景/运动约束。

  - 评测分离 fidelity 与 semantic/motion：自动评测时用 carrier-specific transcription 和 chain
  of query，避免单一 VLM 打分；对多模态 Agent 输出的结构化和可归因评估有参考价值。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：视频生成模型画质接近电影级，但场景文字渲染常出错，而现有评测关注画质、美学、物理合理性，忽视文字信息维度。

**方法**：构建 VTR-Bench，包含 300 条提示，覆盖广告、科学视频等 5 类场景；自动评测管线与人工对齐，文字保真度用 carrier-specific transcription，场景与运动要求用 prompt-specific chain-of-query。提出 Keyframe-Guided Agentic Framework：Director agent 协调图像与视频生成、视觉评估，通过视觉反馈进行迭代优化和候选选择。

**结果**：在 11 个 SOTA 视频生成模型上，最好模型整体 WER 仍达 0.250，普遍存在文字渲染失败；失败分析刻画当前模型在字形、布局、时序稳定性等方面的挑战。
