---
title: 'FashionLens: Toward Versatile Fashion Image Retrieval via Task-Adaptive Learning'
title_zh: FashionLens：面向多功能时尚图像检索的任务自适应学习
authors:
- Haokun Wen
- Xuemeng Song
- Xinghao Xie
- Xiaolin Chen
- Xiangyu Zhao
- Weili Guan
affiliations:
- Harbin Institute of Technology (Shenzhen)
- City University of Hong Kong
- Southern University of Science and Technology
- Nanjing University
- National University of Singapore
arxiv_id: '2605.22552'
url: https://arxiv.org/abs/2605.22552
pdf_url: https://arxiv.org/pdf/2605.22552
published: '2026-05-21'
collected: '2026-05-22'
category: Multimodal
direction: 多模态时尚检索 · 任务自适应表示与采样
tags:
- Fashion Image Retrieval
- Multi-Task Learning
- Spherical Interpolation
- Gradient-Guided Sampling
- MLLM
- Benchmark
one_liner: 提出任务自适应学习框架，通过球面查询校准与梯度引导采样解决多任务检索中的特征干扰与优化失衡，性能全面领先。
practical_value: '- **梯度引导自适应采样 (GGAS)**：利用 `[RET]` token 的梯度范数目衡量任务实时难度，并用 EMA 平滑后结合数据集大小先验重新加权采样概率，可迁移至电商多任务模型（如同时优化点击率、转化率、互补推荐）以自动平衡高资源与高难度任务，避免小样本任务欠拟合。

  - **球面查询校准器 (PGSQC)**：通过信息瓶颈结构生成意图感知的适应提议，再使用自适应球面线性插值动态旋转查询表示，使同一模型能灵活适配相似、搭配、属性筛选等不同检索意图。可在生成式推荐的多场景召回中借鉴，用可学习的插值系数替代硬路由，减小特征冲突。

  - **统一多模态指令框架**：基于 MLLM 将图片、文本、视频、多图组合及修改文本等多样化查询输入纳入统一编码，并使用自然语言指令显式指定检索意图，为构建电商通用搜索或
  Agent 工具调用提供了清晰模板，便于扩展到视频摘要、对话式搜索等复杂交互。

  - **异构数据整合 Benchmark 构建**：U-FIRE 通过人工设计指令模板将 15 个碎片化数据集标准化，并加入两个未见过的组合任务评估 OOD 泛化，可直接用于电商领域多任务模型的全方位测试与上线前的鲁棒性验证。'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

**动机**：时尚电商中的用户搜索意图高度多样，包括以图搜图、文本寻物、跨域匹配、搭配推荐等，当前模型多针对单一任务设计，碎片化严重，且多任务联合训练时存在特征干扰（不同意图对匹配的定义不同）和优化失衡（数据规模与任务难度差异大），难以构建一个真正通用的统一检索框架。为此，论文旨在打造一个能处理多种查询格式和搜索意图的通用时尚图像检索系统。

**方法关键点**：
- **U-FIRE 基准**：整合 15 个数据集涵盖 9 类检索任务，新增两个未见过的组合任务（街拍+修改文本→商城图、多图+文本→搭配单品），并用自然语言指令模板统一样本格式，显式标注检索意图。
- **基于 MLLM 的统一编码**：使用 Qwen3-VL 作为骨干，通过可学习的 `[RET_q]` 和 `[RET_t]` 令牌分别聚合查询与候选图像表示。
- **提案引导的球面查询校准器 (PGSQC)**：为解决特征干扰，利用信息瓶颈结构（可学习低秩矩阵 A 和 B）生成意图适应提议，再通过自适应球面线性插值 (Slerp) 将初始查询表示旋转到任务对齐的度量空间，插值系数、低秩矩阵均由查询表示动态生成，并施加正交和范数正则化。
- **梯度引导自适应采样 (GGAS)**：用 `[RET]` 令牌的梯度幅值定义实时任务难度，经 EMA 平滑后，乘以数据集大小的平方根先验得到采样分数，按概率分布进行批次级采样，避免高难度任务因数据少而被忽视。

**关键实验**：
- 在 U-FIRE 的 11 个任务（含 2 个未见任务）上对比通用多模态检索器 (UniIR, VLM2Vec-V2, MM-Embed, GME)、时尚 VLP 模型 (Fame-ViL, FashionSAP, DA-Fashion) 及微调基线。
- FashionLens 在平均 mR@(1,5,10) 达到 52.21，显著优于最强通用模型 GME (35.40) 和最强时尚模型 DA-Fashion (35.40)；在 OOD 任务上优势更明显，如 Task 10 领先 40.24 点。
- 消融实验证实 GGAS 带来最大提升，PGSQC 优于直接使用提议或线性插值，且实例级参数化优于共享参数。

**一句话**：将检索意图解耦为可学习的球面旋转，并用梯度驱动动态平衡多任务训练，是构建工业级通用时尚搜索系统的高效范式。
