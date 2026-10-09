---
title: 'OneSearch-VL: Unified Multimodal Deep Research Agent for Image and Video'
title_zh: OneSearch-VL：统一图像/视频的多模态深度研究 Agent
authors:
- Hongyu Li
- Manyuan Zhang
- Kaituo Feng
- Shu Chen
- Dian Zheng
- Hao Li
- Hao Yu
- Zhangquan Chen
- Zoey Guo
- Ray Zhang
affiliations:
- BUAA
- CUHK
- NTU
- THU
- HFUT
arxiv_id: '2610.12419'
url: https://arxiv.org/abs/2610.12419
pdf_url: https://arxiv.org/pdf/2610.12419
published: '2026-10-07'
collected: '2026-10-09'
category: Agent
direction: 多模态深度研究 Agent 统一训练
tags:
- Multimodal Agent
- Deep Research
- Visual Grounding
- Evidence Graph
- RL
- Video Understanding
one_liner: 以视觉证据图 VGEG 与证据/定位双层奖励 EVGR 为核心，统一训练单图、多图、视频深度研究 Agent
practical_value: '- **用显式证据图统一数据构造、SFT 轨迹过滤与 RL 过程奖励**：在电商商品图像/视频理解中，可构建「视觉 anchor
  → 商品实体 → 来源化属性事实 → 答案操作」的 VGEG 结构，使商品问答/导购 Agent 的证据链路可追溯，便于生成训练数据和做细粒度评测。

  - **把过程奖励拆成 evidence traceability + visual grounding 两个维度**：最终答案正确之外，分别检验检索事实是否被工具观察支持，以及模型是否真的定位到正确商品区域/视频帧。消融显示两者同时使用比只用答案+query
  奖励平均高 3.8 个点，适合迁移到电商多模态 Agent 的 RL 训练，降低幻觉和“不看图就答”。

  - **评测按 research operation 分层，而不是只报总体准确率**：单 anchor lookup、multi-hop、多 anchor join/comparison/arithmetic、knowledge-conditioned
  counting 等操作化分层，能定位 Agent 具体弱项；电商场景同样可以按“属性抽取、跨商品比较、规格计算、多图统计”拆 benchmark，避免平均分掩盖能力短板。

  - **单图/多图/视频联合 SFT 有跨输入迁移收益**：共用同一套 action-observation 工具 schema 和动作空间，联合训练达到 55.8
  平均分，优于单类型训练；电商场景中商品主图、多角图、商品视频共用一套策略，可以减少多套系统维护成本并提升一致体验。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
单图、多图、视频深度研究都需要视觉定位、外部检索和事实合成，但具体视觉操作不同；现有方法缺少一个统一结构来保留从局部视觉 anchor、实体关系、来源支持事实到最终答案操作之间的完整依赖，导致数据构造、过程监督和评测难以对齐。

## 方法关键点
- 提出 **VGEG（Visually Grounded Evidence Graph）** 作为任务级参考图，连接视觉 anchor、真实实体、多跳关系与来源化事实、答案产生操作。
- 数据引擎：从 2.5M YouTube 视频筛选到 70k；生成 dense caption tree（视频 → event → key frame → object bbox）；通过 image search / OCR / text search 构建 Web evidence graph；基于 VGEG 做 QA 生成、证据验证、实体 fuzzing 改写为视觉指代，并合成 expert trajectory。
- 数据集：SFT 110K（图像 36k、多图 37k、视频 35k，平均 10.1 个工具轮次）+ RL 10K。
- 统一策略：基于 Qwen3-VL-8B，共享 action-observation schema 和工具集，包含 crop、OCR、超分、锐化、透视校正、image/text search、视频时间段选择和帧提取。
- RL 引入 **EVGR**：从 VGEG 派生 evidence ledger；两个 judge 分别打 **evidence traceability**（事实是否被工具观察支持且推理遵循观察）和 **visual grounding**（正确实体/区域/帧是否被识别并驱动检索），与答案正确、query 质量组成奖励，用 GRPO 优化。

## 关键实验
- 7 个单图 benchmark 平均 58.3，超过 Qwen3-VL-8B Agent 16.3 点、OpenSearch-VL-8B 1.7 点，其中 6 个最优。
- OneSearch-MI-Bench 提升 20.2 点，OneSearch-Video-Bench 提升 17.6 点，VideoDR 提升 27.0 点。
- 数据混合消融：单/多图/视频联合 SFT 六榜平均 55.8，优于单类型训练 51.7–55.1。
- 奖励消融：acc-only 56.3，acc+query 57.3，单独加 trace / ground 分别 59.0 / 59.3，同时加入 full EVGR 达 61.1，显示两个过程维度互补。

**最值得记住**：不要只给最终答案打奖励；用同一个 VGEG 结构把数据构造、轨迹过滤、RL 过程奖励和 operation 级评测串起来，分别监督“证据可追溯”和“视觉 grounding”。
