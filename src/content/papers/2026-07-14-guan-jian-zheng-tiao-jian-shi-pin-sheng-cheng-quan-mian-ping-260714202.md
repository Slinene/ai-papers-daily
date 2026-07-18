---
title: 'KeyFrame-Compass: Towards Comprehensive Evaluation of Keyframe-Conditioned
  Video Generation'
title_zh: 关键帧条件视频生成全面评估基准
authors:
- Yuqi Tang
- Tengfei Liu
- Yizheng Lai
- Yuran Wang
- Yang Shi
- Wanshun Su
- Zhuoran Zhang
- Qixun Wang
- Xiaohan Zhang
- Xinlei Yu
affiliations:
- HKUST(GZ)
- Kling Team
- PKU
- RUC
- NWPU
arxiv_id: '2607.14202'
url: https://arxiv.org/abs/2607.14202
pdf_url: https://arxiv.org/pdf/2607.14202
published: '2026-07-14'
collected: '2026-07-18'
category: Eval
direction: 关键帧视频生成评估基准
tags:
- Keyframe-Conditioned Video Generation
- Evaluation Benchmark
- Multi-Modal
- Video Quality
- Keyframe Execution
one_liner: 首个系统性关键帧视频生成评估基准，分解六项执行度指标并揭示模型在忠实度与自然度间的权衡
practical_value: '- 若涉及商品展示视频生成（如电商详情页短视频），可借鉴六维关键帧执行度指标（存在性、保真度、时序、定位、持久性、唯一性）构建自动化质量校验流水线。

  - 自动化评估框架中“证据支撑的MLLM判断+专业感知模型”的组合，可用于离线评测生成视频对给定商品图片序列的还原程度，减少人工评审成本。

  - 实验揭示的“关键帧密度增加导致性能退化”结论，提示在设置关键帧数量时需平衡约束与自然度，对产品化参数调优有参考价值。

  - 开源模型无法正确解释故事板网格输入的时间顺序，提醒若采用此类输入格式需谨慎，或需设计前处理模块注入时序信息。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：关键帧条件视频生成工作流日益普及，但缺乏全面基准来评估模型是否忠实再现指定关键帧序列并保持整体视频质量。

**方法**：提出 KeyFrame-Compass，首个系统评估基准，包含 386 个精心策划样本，覆盖三个应用领域（生活记录、产品展示、电影叙事）、两种视频结构、两种提示粒度、两种条件格式、四种关键帧密度，实现可控分析。自动评估框架将关键帧执行分解为六个互补指标：存在性、保真度、时序一致性、时间定位、持久性和唯一性；整体视频质量通过证据支撑的 MLLM 判断结合专用感知模型评估。

**结果**：在九种代表性系统上实验发现三个根本局限：(1) 关键帧忠实执行与自然视频合成之间存在明确权衡；(2) 随关键帧密度增大，模型性能进一步下降；(3) 多数开源模型无法将故事板网格输入正确解释为时序关键帧序列。
