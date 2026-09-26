---
title: Multimodal Thinking with Renderable Programs
title_zh: 基于SVG原语的多模态推理框架 SVGLM
authors:
- Sunli Chen
- Ding Zhong
- Ziqiao Ma
- Jiaxin Liu
- Zeyuan Yang
- Hao Zhang
- Lie Lu
- Joyce Chai
- Chuang Gan
affiliations:
- University of Massachusetts Amherst
- University of Michigan
- University of Illinois Urbana-Champaign
- Dolby Laboratories
arxiv_id: '2609.30130'
url: https://arxiv.org/abs/2609.30130
pdf_url: https://arxiv.org/pdf/2609.30130
published: '2026-09-24'
collected: '2026-09-26'
category: Multimodal
direction: 多模态推理 · SVG 程序生成
tags:
- SVG
- Vision-Language Model
- Multimodal Reasoning
- Program Synthesis
- Image Editing
- Mathematical Reasoning
one_liner: 利用SVG作为文本与图像中间表示，让VLM在推理过程中生成可解释的图像程序
practical_value: '- 将图像编辑/生成任务转为 SVG 程序输出，可精细控制元素坐标、颜色、几何关系，适合电商商品图、广告模板自动化生成与多轮修改。

  - 利用 SVG 的双重性（既是图像描述又是文本指令），可设计 “think-with-image” 链：先生成 SVG 示意图辅助推理，再输出最终答案，提升图表解析、几何布局类任务的稳定性。

  - 微调范式可复用：收集领域内“文本指令-图像编辑对”，用开源 VLM 训练生成 SVG 代码，并与自然语言推理任务混合训练，避免外部扩散模型不可控。

  - 在需要精确理解图像结构（如优惠券布局、信息图审核）的场景，可以要求模型输出 SVG 表示进行可验证解析，而不是依赖像素级预测。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：当前 VLM 擅长视觉内容理解与文本推理，但难以在推理链中生成并利用图像；全模态模型虽统一生成，但输出为栅格或潜表示，缺乏可解释性和可控性。  
**方法关键点**：SVGLM 使用可缩放矢量图形（SVG）原语作为文本与图像之间的中间表示，利用 SVG 既可作为图像描述又可直接作为文本指令的双重性，使通用 VLM 在推理过程中生成可渲染、可编辑的图像程序。提供大规模 SVG 图像编辑数据集，并给出开源 VLM 的微调范式，将图像编辑任务形式化为 SVG 程序生成，在数学推理基准上训练模型进行“思维可视化”。  
**关键结果**：实验表明 SVGLM 在数学推理任务上获得强大的 SVG 生成能力与 think-with-image 智能，证明 SVG 是构建数字领域 agent 的合适介质，桥接文本推理与像素图像。
