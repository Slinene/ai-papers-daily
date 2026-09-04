---
title: Editable Visual Design
title_zh: 可编辑视觉设计：编码 Agent 驱动的分层设计生成
authors:
- Junyan Ye
- Wei Liu
- Dongzhi Jiang
- Zichen Wen
- HaoDong Li
- Zhutao Lv
- Jiaxin Lin
- Jinhua Yu
- Jun He
- Zilong Huang
affiliations:
- Tencent Hunyuan
- Sun Yat-sen University
- Tsinghua University
- The Chinese University of Hong Kong
- Shanghai Jiao Tong University
arxiv_id: '2609.04034'
url: https://arxiv.org/abs/2609.04034
pdf_url: https://arxiv.org/pdf/2609.04034
published: '2026-09-02'
collected: '2026-09-04'
category: Agent
direction: Agent 驱动的可编辑视觉设计
tags:
- Coding Agent
- Visual Design
- Image Generation
- HTML-CSS
- Editable Delivery
- Render-and-Reflect
one_liner: 让 VLM 先调用图像模型做美学参考，再写原生 HTML/CSS 交付可分层编辑的设计
practical_value: '- 广告/活动页创意生成：把“先出参考图再写 HTML/CSS”流程用于 banner/海报/商品主图。不要直接用扩散出 PNG，而是让图像模型只提供构图与色彩参考，由
  Coding Agent 写原生 DOM，文案层、素材层、背景层分离，运营可拖拽改字换图，适配多渠道尺寸和文案合规修改。

  - 素材资产层单独生成 + 绿幕/alpha 抠图，避免从参考图裁切导致的像素污染与图层纠缠；在电商商品图、活动背景、icon 等素材库可复用，提升素材可维护性。

  - 渲染自修复闭环：将 headless 浏览器确定性检查（元素溢出、资源加载失败、DOM 畸形）与 VLM 截图审美评审结合，适合广告创意平台做自动质检和改稿，减少人工巡检；一轮/两轮局部
  patch 即可收敛。

  - Agent Design Replay / 过程可视化可作为创意平台的可追溯能力：记录 prompt→参考图→素材→代码→修改轨迹，让运营/设计师理解 AI
  决策并介入，比黑盒出图更利于团队协作审核。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：纯扩散生成（GPT-Image-2、Nano-Banana）视觉表现强，但输出位图，文字易错、图层纠缠，难以二次编辑；纯 LLM/Coding Agent 生成 HTML/CSS 结构干净、文本可编辑，但缺乏全局审美直觉，只能做模板化色块/渐变，复杂素材易变成半成品。需要一个既能保留工程可编辑性、又能借用图像模型美学先验的设计生成范式。

**方法关键点**：
- 双引擎分工：VLM（GPT-5.6 Sol/Codex）作为“创意大脑”负责需求理解、规划、编码与判断；图像模型（GPT Image 2）作为“视觉世界模拟器”按需生成参考图与独立素材。
- “imagine first, then act”闭环：先让图像模型生成“想象效果图”，建立构图、色彩、风格先验，再写原生 HTML/CSS。
- 素材解耦：独立生成背景、主体、图标等资产，优先带 alpha 通道；否则绿幕抠图，避免从参考图像素裁切造成纠缠。
- 结构化编码：固定画布像素尺寸，DOM 元素作为可拖拽 layer，布局不依赖 viewport。
- 验证与自修复：headless 浏览器运行确定性规则检查（溢出、资源失败、DOM 畸形），再截图交给 VLM reviewer 做视觉反思，发现问题局部 patch。
- Agent Design Replay 记录需求→想象→素材→代码→修复轨迹，提升透明可追溯。

**关键结果**：论文主要给案例而非量化分数。与纯扩散、纯代码生成对比：扩散图出现中文乱码、不可分图层；纯代码布局大片空白/混乱；本流程字体干净、图层可分离。覆盖活动海报、信息图、长文本排版等场景；信息密集的红熊猫百科信息图交付 120 个可编辑图层/13 组，旅行海报 6 层/1 组，review 环节能捕捉并修复真实布局缺陷。局限：美学无 ground truth，质量难以量化，多页一致性未验证。

**一句话记忆**：把图像生成当前置“视觉模拟器”，让 Coding Agent 先看后写、以 HTML/CSS 交付可编辑分层设计，是平衡美学与工程可维护性的务实路线。
