---
title: 'VideoCoCo: Code-as-CoT for Physically-Consistent Video Generation via an Agentic
  Dual-Engine System'
title_zh: VideoCoCo：基于双引擎与可执行代码思维链的物理一致视频生成
authors:
- Haodong Li
- Tianfei Ren
- Xiaoxiao Ma
- Chunmei Qing
- Zhen Fang
- Sipeng He
- Ziyu Guo
- Haoyu Wu
- Juanxi Tian
- Yihang Zou
affiliations:
- CUHK
- USTC
- SCUT
- HKU
- NTU
arxiv_id: '2607.27380'
url: https://arxiv.org/abs/2607.27380
pdf_url: https://arxiv.org/pdf/2607.27380
published: '2026-07-28'
collected: '2026-08-03'
category: Other
direction: 视频生成 · 可执行代码思维链
tags:
- Video Generation
- Code-as-CoT
- Agentic System
- Physical Consistency
- Dual-Engine
- Blender Simulation
one_liner: 用可执行 Blender 代码作为过程级思维链，将物理推理与视觉生成解耦，显著提升视频物理一致性
practical_value: '- 双引擎“过程推理 + 精细生成”的架构可启发在推荐系统中分离策略规划（如用户意图理解、多步交互设计）与内容生成，提升复杂流程的可控性。

  - 用可执行代码作为中间表示，确保了确定性、可解释和可审计，类似思想可用于推荐场景中需要严格逻辑保证的环节（如营销规则引擎、动态定价逻辑）。

  - 为适应模拟草稿域差异而专门构建配对数据集的方法，可迁移到推荐系统的域适配数据增强，例如合成用户行为轨迹与真实轨迹的对齐训练。

  - 整体工作偏向视频生成，直接用于搜推系统的业务点有限，更多是架构与表示层面的理念参考。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有文本到视频模型难以生成物理一致的动态，因为时空演化必须从高度压缩的文本中隐式推断，缺乏显式的过程控制。已有思维链方法引入的中间表示（计划、视觉状态）要么不可执行，要么时序稀疏，无法精细约束完整物理过程。

**方法**：提出 VideoCoCo，一个双引擎 Agent 框架。给定文本提示，编码 Agent 生成可执行的 Blender 程序，显式定义场景几何、材质及逐帧运动；模拟引擎运行该程序输出确定性的时空草稿（draft）；随后生成视频引擎基于草稿进行条件化编辑，将其转换为逼真视频。这一解耦将物理推理与高保真视觉实现分离。为弥合模拟草稿与真实视频的域差异，作者构建了 VideoCoCo-3K 数据集，包含草稿-指令-目标三元组用于微调视频编辑器。

**关键结果**：在物理一致性基准 PhyGenBench 上，VideoCoCo 将基线 OmniWeaving 的得分从 0.475 提升至 0.558；在综合质量基准 VBench-2.0 上，从 52.18 提升至 77.88，均取得最优平均分，验证了可执行代码作为中间表示的有效性。
