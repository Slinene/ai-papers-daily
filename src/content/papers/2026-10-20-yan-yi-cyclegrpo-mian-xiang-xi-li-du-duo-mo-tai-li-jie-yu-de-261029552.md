---
title: Generalized CycleGRPO for Fine-Grained Multimodal Understanding and Grounding
title_zh: 广义 CycleGRPO：面向细粒度多模态理解与定位的统一强化学习框架
authors:
- Xin Zhang
- Haochen Wang
- Beibei Lin
- Zhaoxiang Zhang
- Robby T. Tan
- Jason Li
- Dacheng Tao
affiliations:
- NUS
- UCAS
- NTU
arxiv_id: '2610.29552'
url: https://arxiv.org/abs/2610.29552
pdf_url: https://arxiv.org/pdf/2610.29552
published: '2026-10-20'
collected: '2026-10-26'
category: Multimodal
direction: 多模态强化学习 · 区域-文本循环一致性
tags:
- CycleGRPO
- Multimodal Grounding
- GRPO
- Reinforcement Learning
- MLLM
- Temporal Grounding
one_liner: 以区域-文本循环一致性作为可验证奖励，统一图像/视频细粒度理解与定位的RL框架
practical_value: '- 在电商多模态商品理解中，可将「图像区域 → 文本描述 → 再定位回区域」作为无人工标注、无外部 LLM judge 的循环一致性奖励，用
  gIoU/mask overlap 做可验证信号，低成本训练区域级属性识别（如商品局部卖点、材质、Logo）。

  - 视频广告/直播切片场景可借鉴 temporal cycle 与 DOVE 的对比评估思路：训练模型对目标片段生成能区分相似重复片段的描述，提升“哪个时刻出现什么卖点”的定位与文案生成一致性。

  - 工程实现上，统一 spatial/temporal/spatio-temporal region-space 表示，使同一套 GRPO 奖励逻辑适配框、mask、时间区间和时空证据，适合多模态搜索/推荐团队整合多种区域标注；无需外部
  judge、奖励可验证，降低 RLHF 成本。

  - 业务可借鉴有限：该方法面向视觉 grounding 任务，不直接改变推荐排序或用户建模；但可作为商品视觉理解底座，为后续生成式推荐、多模态检索提供更细粒度的对齐特征。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：细粒度多模态智能要求模型既能理解指定区域，又能从语言找回区域；现有方法将两个方向拆开，依赖任务特定标注。

方法关键点：Generalized CycleGRPO 用统一强化学习将区域描述与再定位形成闭环。输入区域后，MLLM 生成候选描述，再对每句描述做定位以重建区域；输入与重建区域的 overlap 作为可验证奖励，无需参考 caption 或外部 LLM judge。区域用统一空间 + overlap 度量表示，使同一学习原则从图像 mask/box 扩展到视频时间区间和时空证据。视频场景下还奖励能区分相似重复事件的描述，并引入 DOVE 对比基准。

关键结果数字：图像上 SAMTok 在 GroundingSuite 整体 gIoU 从 57.5% 升至 68.2%，GRES 平均 gIoU 从 71.2% 升至 78.7%；时间任务 Charades tIoU 达 51.9%，DOVE TEC 达 33.3%，高于 Qwen3-VL 初始化的 45.6% 和 14.8%；时空任务 V-STaR mAM 34.6%→36.2%，mLGM 47.2%→49.8%。
