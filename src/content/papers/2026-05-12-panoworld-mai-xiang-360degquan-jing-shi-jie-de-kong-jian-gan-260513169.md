---
title: 'PanoWorld: Towards Spatial Supersensing in 360^circ Panorama World'
title_zh: PanoWorld：迈向360°全景世界的空间超感知
authors:
- Changpeng Wang
- Xin Lin
- Junhan Liu
- Yuheng Liu
- Zhen Wang
- Donglian Qi
- Yunfeng Yan
- Xi Chen
arxiv_id: '2605.13169'
url: https://arxiv.org/abs/2605.13169
pdf_url: https://arxiv.org/pdf/2605.13169
published: '2026-05-12'
collected: '2026-05-17'
category: Multimodal
direction: 全景空间推理 · 多模态大模型
tags:
- 360 Panorama
- Spatial Understanding
- MLLM
- Spherical Cross-Attention
- Pano-native
- Equirectangular Projection
one_liner: 提出全景原生多模态大模型PanoWorld，以球形空间交叉注意力注入几何先验，在全景空间推理上大幅超越现有方法
practical_value: '- 对于需要处理全景图像的多模态系统（如电商虚拟展厅或室内导航Agent），可借鉴PanoWorld的球形空间交叉注意力设计，避免简单投影分解带来的球形结构丢失，直接建模物体之间的连续空间关系。

  - 论文提出的几何感知元数据构造流水线（语义锚定、球形定位、参考系变换、深度感知推理）能生成高质量空间指令数据，可用于微调面向电商场景的视觉语言模型，提升商品3D空间问答准确性。

  - 在构建空间推理基准时，采用能力对齐的评估维度（如PanoSpace-Bench），能更细粒度诊断模型的空间理解短板，从业者可借鉴此类分项评测设计，针对Agent的空间感知模块进行定向优化。

  - 对于需要全局感知的任务（如仓库机器人货架扫描、店铺全景巡检），全景原生理解模式相比多视图拼接在推理效率和空间一致性上更具优势，可直接应用于实时智能体决策。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**  
当前多模态大模型（MLLM）在透视图像范式下视野狭窄，难以进行全局空间理解。360°全景感知提供了一种“超感知”能力，但现有方法多将全景图拆分为多个透视视角，丢失了等距矩形投影（ERP）的球形连续结构。为此，论文研究**全景原生理解**，要求模型直接在观测者为中心的球形空间上进行推理。  
**方法**  
1. **能力定义**：明确全景原生理解所需的关键能力——语义锚定、球形定位、参考系变换、深度感知的三维空间推理。  
2. **数据构造**：构建大规模几何感知元数据流水线，将混合来源的ERP全景图转化为具有语言对齐与深度信息的监督信号，并实例化为能力对齐的指令微调数据。  
3. **模型设计**：提出**PanoWorld**，引入**球形空间交叉注意力**，将球形几何信息注入视觉流，使模型能直接利用ERP固有的球面结构。  
4. **基准评测**：构建**PanoSpace-Bench**诊断基准，评估ERP原生空间推理能力。  
**结果**  
在PanoSpace-Bench、H* Bench和R2R-CE Val-Unseen等基准上，PanoWorld大幅优于所有专有和开源基线，证明专用全景原生监督与几何适配的必要性。
