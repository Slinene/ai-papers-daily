---
title: 'VABench: Measuring Embodied Spatial Intelligence through Visual Demonstrations,
  Active Perception, and Metric Control'
title_zh: VA-Bench：通过视觉演示、主动感知与度量控制评测具身空间智能
authors:
- Zhongbo Zhang
- Jiayi Jin
- Yifan Wang
- Zaibin Zhang
- Haiwen Diao
- Lijun Wang
- Huchuan Lu
affiliations:
- Dalian University of Technology
- Nanyang Technological University
arxiv_id: '2609.19554'
url: https://arxiv.org/abs/2609.19554
pdf_url: https://arxiv.org/pdf/2609.19554
published: '2026-09-16'
collected: '2026-09-19'
category: Eval
direction: Embodied 空间智能评测基准
tags:
- embodied AI
- spatial intelligence
- MLLM benchmark
- active perception
- metric control
one_liner: 提出 VA-Bench 基准，评估通用 MLLM 在 RGB 演示、主动视角选择与度量命令下的完整观察-推理-执行闭环能力
practical_value: '- 评测设计：构建 held-out 几何/布局变体与长程组合任务，可类比电商推荐中不同页面布局、用户意图与多步转化场景下的泛化评测，避免只测单一分布

  - 主动感知闭环：模型主动选择相机视角而非被动接收多视图，对应交互式推荐中逐轮选择信息源，利用执行反馈修正策略，可提升长程任务成功率

  - 高层决策与低层执行解耦：固定模型无关控制器只执行模型指定的度量式目标，业务上可将 LLM 意图输出与具体执行引擎分离，降低耦合并便于快速迭代

  - 行为诊断体系：除最终成功率外，报告轨迹级行为诊断与子任务进度，推荐系统评估可借鉴，不只盯点击率，还要诊断用户路径、探索行为等中间指标'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有空间智能基准多止于语言描述物体位置，未覆盖不完整观测下识别并获取缺失证据、统一空间坐标、执行动作并基于反馈修正的完整闭环。

**方法关键点**：VA-Bench 让通用 MLLM 仅从 RGB 演示学习过程语义，主动选择相机视角，输出度量式笛卡尔目标命令，由固定模型无关控制器执行；模型不获取物体位姿、轨迹真值或动作头。基准包含 14 个基础任务家族（11 单臂 + 3 双臂）、7 个 held-out 几何/布局变体和 1 个五物体长程组合赛道。评估 12 个模型条件、每任务 20 个物理验证种子、3 次独立运行，报告最终成功率、九种轨迹级行为诊断和子任务进度。

**关键结果数字**：最佳模型在标注运行中目标定位 100.0%、空间关系 78.9%，但三跑宏平均任务成功仅 53.93±3.17%；主动相机控制显著优于被动多视角，配对比较中成功率从 27.86% 提升至 57.50%；held-out 几何迁移可令任务成功下降超 30 个百分点；无模型完成严格长程任务，尽管有显著部分进度。
