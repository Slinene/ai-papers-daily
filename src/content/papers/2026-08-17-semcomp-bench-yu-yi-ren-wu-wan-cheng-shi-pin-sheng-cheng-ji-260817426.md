---
title: 'SemComp-Bench: Benchmarking Semantic Task Completion in Video Generation'
title_zh: SemComp-Bench：语义任务完成视频生成基准
authors:
- Keyu Tu
- Zhuowei Chen
- Mengqi Huang
- Yuxin Wang
- Jiahao Zhu
- Zhendong Mao
- Yongdong Zhang
affiliations:
- University of Science and Technology of China
- FrameX.AI
- Sun Yat-sen University
arxiv_id: '2608.17426'
url: https://arxiv.org/abs/2608.17426
pdf_url: https://arxiv.org/pdf/2608.17426
published: '2026-08-17'
collected: '2026-08-22'
category: Eval
direction: 视频生成评估 · 语义任务完成
tags:
- Benchmark
- Video Generation
- Semantic Grounding
- VLM Evaluation
- Outcome-Oriented
one_liner: 提出 SemComp-Bench 基准，用 VLM 评估视频生成在结果达成与语义 grounding 上的表现
practical_value: '- 评估思路可迁移：在商品短视频/广告创意生成中，聚焦最终结果是否达成与任务相关语义是否保持，不必苛求逐帧一致，降低审核成本。

  - 采用 VLM 回答结构化二值问题输出 OA/GR 两个分数，可在生成式推荐中分离“目标达成”和“语义相关性”做自动化质量评测，定位失败环节。

  - 四阶段数据 curation pipeline 可参考：从原始视频自动提取参考图、指令和结果片段，规模化构建业务生成评估集，加速模型迭代。

  - Semantic grounding 定义允许无关属性变化，可迁移到电商商品属性控制：只绑定关键属性（材质、形状、功能），其他外观可多样化，适配创意生成。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：视频生成模型在视觉保真和时序连贯上进展显著，但能否在达成指令结果的同时保持与参考图的高层语义 grounding 仍未充分评估。为此定义语义任务完成视频生成：要求结果达成预期且与参考图在任务相关高层语义上对应，不要求完整中间步骤或外观一致。

**方法关键点**：构建 SemComp-Data，覆盖六个域；每个实例包含参考图、详细指令、简要指令和 outcome-centric 视频片段；用可扩展四阶段 curation pipeline 将原始视频转为标准化实例。提出 SemComp-Bench 评测协议，用 VLM 回答结构化二值问题，分别输出 OA Score（结果达成）和 GR Score（生成可靠性）。

**关键结果**：在代表性视频生成模型上评测，结果表明在达成预期结果的同时保持任务相关语义 grounding 仍具显著挑战（摘要未给出具体分数）。
