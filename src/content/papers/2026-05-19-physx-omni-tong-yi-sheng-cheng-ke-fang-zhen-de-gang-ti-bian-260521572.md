---
title: 'PhysX-Omni: Unified Simulation-Ready Physical 3D Generation for Rigid, Deformable,
  and Articulated Objects'
title_zh: PhysX-Omni：统一生成可仿真的刚体/变形体/关节体3D资产
authors:
- Ziang Cao
- Yinghao Liu
- Haitian Li
- Runmao Yao
- Fangzhou Hong
- Zhaoxi Chen
- Liang Pan
- Ziwei Liu
affiliations:
- S-Lab, Nanyang Technological University
- ACE Robotics
arxiv_id: '2605.21572'
url: https://arxiv.org/abs/2605.21572
pdf_url: https://arxiv.org/pdf/2605.21572
published: '2026-05-19'
collected: '2026-05-23'
category: Multimodal
direction: 3D生成 · 物理仿真 · 多模态学习
tags:
- 3D Generation
- Simulation-Ready
- VLM
- Dataset
- Benchmark
- Physical Assets
one_liner: 提出统一框架与数据集，实现跨类别仿真就绪3D生成，并构建含六维度评估的基准
practical_value: '- **几何表示trick**：论文提出的高分辨率几何直接编码方法，避免压缩损失，可借鉴到电商3D商品重建中，提升细节保真度（如服饰纹理、家具结构）。

  - **数据集构建思路**：PhysXVerse覆盖多种物理属性，电商可类似构建带材质、可变形参数的商品3D数据集，支撑VR试穿、物理交互模拟。

  - **评估维度扩展**：PhysX-Bench引入尺度、材质、可供性等六维度评估，生成式商品3D模型也可引入类似benchmark，避免只看几何相似度。

  - **多类别统一框架**：统一处理刚体、变形体、关节体的生成流水线，可启发我们将不同商品类型（硬质电子、软体衣物、可动家具）纳入同一生成系统，降低维护成本。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有3D生成方法普遍忽略物理属性，或仅支持单一资产类型（刚体、变形体或关节体），难以用于需要真实物理交互的仿真与具身智能任务。

**方法**：
- 提出PhysX-Omni统一框架，核心是一种面向VLM的高效几何表示法：直接编码高分辨率3D结构，无需网格压缩，显著提升生成质量。
- 构建首个通用仿真就绪3D数据集PhysXVerse，涵盖室内外多种类别，带有材质、密度、运动学等物理标注。
- 设计PhysX-Bench评估基准，从几何、绝对尺度、材质、可供性、运动学、功能性描述六个维度全面评测生成与理解能力。

**关键结果**：
- 在传统指标和PhysX-Bench上，PhysX-Omni均表现强劲，较之前方法在物理属性一致性和细节保真度上显著提高。
- 额外实验展示了其在仿真场景生成和机器人策略学习中的直接应用潜力，生成资产可直接用于物理模拟。
