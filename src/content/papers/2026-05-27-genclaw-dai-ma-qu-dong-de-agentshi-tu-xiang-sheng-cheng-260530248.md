---
title: 'GenClaw: Code-Driven Agentic Image Generation'
title_zh: GenClaw：代码驱动的Agent式图像生成
authors:
- Junyan Ye
- Jun He
- Zilong Huang
- Dongzhi Jiang
- Xuan Yang
- Rui Chen
- Weijia Li
affiliations:
- Tencent Hunyuan
- Sun Yat-sen University
- Tsinghua University
- The Chinese University of Hong Kong
arxiv_id: '2605.30248'
url: https://arxiv.org/abs/2605.30248
pdf_url: https://arxiv.org/pdf/2605.30248
published: '2026-05-27'
collected: '2026-05-31'
category: Agent
direction: Agent · 代码中介的可控图像生成
tags:
- Code-Driven Generation
- Agentic Workflow
- SVG
- Controllable Image Synthesis
- Layer-wise Editing
- Visual Reasoning
one_liner: 提出代码驱动的Agent式图像生成范式，通过构思→草图→上色三层解耦，用可执行代码作为中间画布，大幅提升空间可控性与可解释性。
practical_value: '- **代码驱动布局可迁移至商品图模板生成**：电商场景中需要精确控制多个商品的位置、数量、文字信息（如促销标签），借鉴GenClaw用SVG/HTML构建结构化草图再渲染的思路，可将布局规划与纹理生成解耦，减少对象计数错误与属性绑定失败。

  - **分层编辑机制降低局部修改对非目标区域的破坏**：当需要修改主图中某一元素（如替换商品、移动logo）时，利用SAM分割后组织为JSONL图层，仅对目标层做编辑，可显著提升编辑一致性（文中PSNR从20以下提升到27.87），这对电商主图的迭代优化很有价值。

  - **搜索增强认知层可弥补模型知识滞后**：在生成含有最新赛事、节气、明星同款等时效性信息的商品图时，Agent主动搜索并结构化事实再写入代码画布，避免直接让生成模型凭空想象，提升文案准确性和知识可信度。

  - **代码中介的物理/几何推理可用于商品场景模拟**：当需要生成商品在特定环境下的摆放效果（如光照反射、堆叠结构）时，先通过Three.js等构建物理/几何草图作为约束，再交给渲染模型，能提升复杂空间关系的生成稳定性。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
现有图像生成Agent仅能通过重写提示词间接影响生成结果，本质上仍是黑盒“彩票式”采样，缺乏对画布的直接操控能力，导致复杂布局、精确计数、文本渲染等任务表现不稳。而人类艺术家创作是构思→草图→上色的透明过程。为此，论文提出代码驱动的Agent式生成范式GenClaw，让LLM以编程方式构建可执行草图，再由图像生成模型完成纹理填充，实现可控、可追溯的图像生成。

## 方法关键点
- **三层解耦架构**：认知结构化层负责意图理解、知识搜索与推理；可执行画布层根据任务选用SVG、HTML/CSS、Three.js等编写代码，生成包含对象位置、数量、文本、图层关系的结构草图；视觉生成与审阅层调用图像模型（如Gemini Flash Image）在草图基础上补充纹理与真实感，并通过VLM审阅。
- **代码扮演数字画笔**：代码天然适合表达空间坐标、绝对数量、图层遮挡等结构信息，弥补自然语言在空间描述上的模糊性。Agent无需模拟GUI操作，直接通过CLI/代码构建画布。
- **分层编辑方案**：通过VLM理解画面、SAM分割对象、图像模型补全遮挡，将图像分解为JSONL组织的图层，编辑时仅修改目标层，大幅提升局部编辑时非目标区域的像素一致性。
- **搜索增强与物理推理**：Agent调用搜索工具补全实时知识，或通过Python/Three.js构建物理/几何预览，将隐式规则转为显式视觉约束后再渲染。

## 关键实验
在GenEval++上，GenClaw整体得分0.878，显著优于重写型Agent（Mind-Brush 0.782），尤其在计数和空间关系任务上优势明显；在LongText-Bench中文长文本渲染达0.989，英文0.988；在ImgEdit上，非编辑区域PSNR达27.87（GPT-Image-1.5仅16.36），SSIM 0.718，显示分层编辑对一致性的保护；在Mind-Bench知识/推理驱动生成任务上达0.57，优于同期Agent方法。

## 核心观点
将图像生成从“让模型一次猜出整张图”转变为“让Agent像人类一样先用代码搭建结构骨架，再交由生成模型上色”，实现了可控性、可解释性与编辑性的同步提升。
