---
title: 'LooseControlVideo: Directorial Video Control using Spatial Blocking'
title_zh: LooseControlVideo：基于空间阻塞的导演式视频生成控制
authors:
- Shariq Farooq Bhat
- Niloy J. Mitra
- Kalyan Sunkavalli
affiliations:
- Adobe Research
arxiv_id: '2606.19495'
url: https://arxiv.org/abs/2606.19495
pdf_url: https://arxiv.org/pdf/2606.19495
published: '2026-06-16'
collected: '2026-06-21'
category: Multimodal
direction: 文本到视频生成 · 3D布局控制
tags:
- text-to-video
- 3D control
- DNOCS
- spatial blocking
- video generation
- layout conditioning
one_liner: 用有向3D稀疏框实现文本到视频的精确空间编排，显著提升轨迹、遮挡与运动一致性
practical_value: '- 在电商广告视频创作中，可直接用稀疏3D框定义商品运动路径与遮挡关系，替代密集深度图人工制作，降低动态多对象场景的成本。

  - 系统采用的 **DNOCS 编码** 将 3D 尺寸、方向和深度顺序解耦，可借鉴到多模态商品展示生成中，为推荐场景的虚拟主播或交互式货品演示提供显式遮挡先验。

  - 局部精调能力允许在不破坏全局上下文的情况下，单独调整某个商品的轨迹或添加交互，适合实时协同创意编辑。

  - 稀疏控制范式对 Agent 动作推演可视化有启发：用少量关键 3D 框约束复杂物理交互，可能迁移到虚拟环境下的多智体行为规划。'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有文本到视频模型难以精确控制3D空间编排，尤其多物体场景中语义布局与动态纠缠。密集深度图引导虽能保持结构保真度，但为形变体动态事件创作逐帧精确信号极其繁重。

### 方法
提出 **LooseControlVideo**，用**稀疏有向3D框**作为“阻塞”代理：用户只需放置带朝向的3D包围盒定义高层布局与运动轨迹，模型自动生成合理的遮挡、交互和动态。核心引入 **DNOCS** 编码，统一表达3D尺寸、方向与深度排序的遮挡关系。在 **Wan 2.2** 预训练文生视频模型上微调，使用融合 DNOCS 标注的视频数据集。还支持局部精调，如调整跳跃轨迹或增加交互，而对全局场景干扰最小。

### 关键结果
在 nuScenes、HO-3D、BEHAVE 三个多对象动态基准上显著超越基于 2D 框和光流的基线：轨迹误差降低 **1.2-3 倍**，刚性运动一致性提升 **2 倍**，遮挡准确度提升 **1.5-2 倍**。
