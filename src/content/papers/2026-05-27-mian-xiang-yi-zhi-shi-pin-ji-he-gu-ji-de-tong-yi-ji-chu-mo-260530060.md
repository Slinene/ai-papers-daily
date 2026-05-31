---
title: Towards Consistent Video Geometry Estimation
title_zh: 面向一致视频几何估计的统一基础模型 ViGeo
authors:
- Zhu Yu
- Jingnan Gao
- Runmin Zhang
- Lingteng Qiu
- Zhengyi Zhao
- Rui Peng
- Yichao Yan
- Kejie Qiu
- Siyu Zhu
- Si-Yuan Cao
affiliations:
- Zhejiang University
- Tongyi Lab, Alibaba Group
- Shanghai Jiao Tong University
- Fudan University
arxiv_id: '2605.30060'
url: https://arxiv.org/abs/2605.30060
pdf_url: https://arxiv.org/pdf/2605.30060
published: '2026-05-27'
collected: '2026-05-31'
category: Other
direction: 视频几何估计 · 动态分块注意力
tags:
- Video Geometry Estimation
- Dynamic Chunking Attention
- Depth Completion
- Foundation Model
- Temporal Consistency
one_liner: 通过动态分块注意力实现流式与全序列视频几何估计的统一模型，并引入补全式数据精炼提升监督质量
practical_value: '- 动态分块注意力允许同一模型在训练后无缝切换双向/因果注意力模式，适合构建既能离线全量处理又能在线流式推理的序列模型（如用户行为序列建模），避免重复训练。

  - 补全式数据精炼框架利用教师模型从稀疏、有噪标注生成稠密且时序一致的真值，可迁移至推荐系统中含噪 implicit feedback 或稀疏行为序列的伪标签生成，提升训练数据质量。

  - 统一预测深度、法线、点图的多任务设计启示：在推荐模型中可对点击、转化、时长等多目标共享 backbone，以一致优化提升整体效果。

  - 时序一致性约束的思想可启发推荐中的兴趣演变建模，例如在长序列用户行为中引入连贯性正则，避免短期噪声冲击。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：视频几何估计需要同时保证空间稠密和时序一致，但现有方法大多针对离线全序列或在线流式单独设计，难以统一；同时缺乏高质量稠密标注，限制了模型训练。

**方法**：提出 ViGeo，一个基于 plain transformer 的前馈基础模型。核心是**动态分块注意力**——训练时随机混合双向和因果注意力模式，测试时无需重训即可自适应切换，从而支持流式、全序列及长视频推理。为提升监督质量，设计**补全式数据精炼框架**：先训练一个视频深度补全教师模型，该模型以稀疏/噪声标注为条件，利用多视图时序信息生成稠密、一致、可靠的伪真值，用于训练学生 ViGeo。模型同时预测深度、表面法线和点图。

**结果**：仅使用公开数据集训练，在在线、离线及长视频深度估计、法线估计、点图估计上全面超越先前 SOTA，深度估计相对误差降低 8.3%–31.2%。
