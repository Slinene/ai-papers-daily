---
title: Text-Vision Co-Instructed Image Editing
title_zh: 文本-视觉协同指令的图像编辑
authors:
- Chenxi Xie
- Yuhui Wu
- Qiaosi Yi
- Lei Zhang
affiliations:
- The Hong Kong Polytechnic University
- OPPO Research Institute
arxiv_id: '2606.16767'
url: https://arxiv.org/abs/2606.16767
pdf_url: https://arxiv.org/pdf/2606.16767
published: '2026-06-14'
collected: '2026-06-18'
category: Multimodal
direction: 文本视觉协同的图像编辑
tags:
- Image Editing
- Multimodal Instruction
- Drag Editing
- Diffusion Models
- Dataset Construction
one_liner: 融合文本语义与拖拽/点击等视觉指令，实现空间可控且语义保真的图像编辑
practical_value: '- 文本与视觉提示协同的思路可借鉴到多模态商品检索，如允许用户上传图片并辅以文字说明区域编辑意图，提升交互精准度

  - 利用视频帧间差异自动构建编辑指令对的数据构造方法，可迁移到商品视频生成任务中，用于获得带空间标注的训练数据

  - TV-Edit-Bench 的多维度评估（语义忠实度、空间对齐、视觉一致性）可启发电商图像编辑场景的离线评估指标设计

  - 将稀疏视觉指令提升为语义感知控制表示的模块化设计，可启发多模态推荐中融合细粒度空间意图的架构'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有图像编辑方法中，纯文本指令语义表达强但空间控制粗粒度，纯视觉指令（拖拽、点击）空间精准但语义模糊。为结合两者优势，提出文本-视觉协同编辑。

**方法关键点**：
1. 从动态视频自动构建规模>23K 的文本-视觉指令配对数据集（TV-Edit-Dataset），为跨模态对齐提供监督。
2. 提出 TV-Edit 统一编辑框架：将拖拽/点击等稀疏视觉指令与图像-文本语义共同编入上下文，通过语义感知编码器提升为控制表示，注入预训练扩散编辑骨干。
3. 建立 TV-Edit-Bench 基准，以语义忠实度、空间对齐度和视觉一致性三维度评估，并设计控制文本-视觉变化以消除混淆因素。

**关键结果**：在多个编辑骨干（如 InstructPix2Pix、MagicBrush）上，TV-Edit 在语义保真、空间精度和结构一致性上均显著优于现有纯文本或纯拖拽基线方法，编辑结果更符合复合指令的意图。
