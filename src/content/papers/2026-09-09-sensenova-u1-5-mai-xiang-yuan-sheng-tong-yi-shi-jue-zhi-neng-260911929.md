---
title: 'SenseNova-U1.5: Towards Native Unified Visual Intelligence'
title_zh: SenseNova-U1.5：迈向原生统一视觉智能
authors:
- Haiwen Diao
- Jiahao Wang
- Chenjing Ding
- Hanming Deng
- Jiangnan Chen
- Ruixi Zhang
- Ruohui Wang
- Wenwen Tong
- Xiangyu Fan
- Yubo Wang
arxiv_id: '2609.11929'
url: https://arxiv.org/abs/2609.11929
pdf_url: https://arxiv.org/pdf/2609.11929
published: '2026-09-09'
collected: '2026-09-14'
category: Multimodal
direction: 原生统一多模态模型与图像生成
tags:
- Native Multimodal
- Image Generation
- Encoder-free
- On-policy Distillation
- MoE
- Text Rendering
one_liner: 发布8B-MoT原生统一多模态模型，在无Encoder/VAE架构下完成理解、推理与视觉生成，并借多专家on-policy蒸馏增强视觉能力
practical_value: '- 电商商品图生成与编辑：利用其多参考编辑、主体身份/几何保持与未修改区域保护能力，可自动完成商品换背景、多商品组合、局部保留等广告素材生成；双语文本渲染能力适合生成带价格、卖点、促销文案的营销图。

  - 多专家 on-policy distillation 可迁移到业务模型：针对不同任务（文案生成、视觉审美、图像编辑）分别优化专家，再用 on-policy
  蒸馏整合到统一模型，避免多模型部署的运维成本与延迟。

  - Encoder-free/VAE-free 架构减少图像 token 转换中的信息损耗，对生成式推荐中直接建模商品视觉特征（如生成商品图或场景图）有参考价值；支持
  4K 原生分辨率适合高细节素材生产。

  - 对长、复杂、结构化视觉指令的泛化能力，提示多模态理解可迁移到视觉规划与创作，可尝试用于 Agent 自动排版、生成商品详情页布局或广告创意版式。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有多模态统一模型通常依赖外部视觉 encoder 或 VAE，造成信息瓶颈与端到端训练困难；同时视觉生成质量、文本渲染与编辑能力仍有差距。

**方法关键点**：
- 推出 8B-MoT 原生统一多模态模型，采用 encoder-free、VAE-free 架构，可直接处理与生成视觉内容。
- 强化视觉接口：通过空间一致的 patch 重建，使视觉 token 与生成质量更稳定。
- 训练数据与任务优化：精心构建生成与编辑数据，改进任务 formulation，增强结构 prompt，支持高达 4K 原生分辨率。
- 后训练阶段：为视觉美学、双语文本渲染、信息图生成、图像编辑分别优化专家，再用 multi-expert on-policy distillation 将能力蒸馏回统一模型，实现能力整合。

**关键结果**：
- 在图像保真度、文本渲染、复杂构图、多参考编辑、交错生成等指标上大幅提升。
- 指令跟随能力增强，主体身份、几何结构、未修改区域保持更好。
- 尽管生成数据中结构化格式有限，模型仍能泛化到长、复杂、结构化视觉指令，证明多模态理解可迁移到视觉规划与创作。
- 开源训练代码，包括 SFT、RL 和 on-policy distillation。
