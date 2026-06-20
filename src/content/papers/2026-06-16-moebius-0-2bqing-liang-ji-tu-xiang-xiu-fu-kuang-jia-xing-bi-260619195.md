---
title: 'Moebius: 0.2B Lightweight Image Inpainting Framework with 10B-Level Performance'
title_zh: Moebius：0.2B轻量级图像修复框架，性能比肩10B模型
authors:
- Kangsheng Duan
- Ziyang Xu
- Wenyu Liu
- Xiaohu Ruan
- Xiaoxin Chen
- Xinggang Wang
affiliations:
- Huazhong University of Science and Technology
- VIVO AI Lab
arxiv_id: '2606.19195'
url: https://arxiv.org/abs/2606.19195
pdf_url: https://arxiv.org/pdf/2606.19195
published: '2026-06-16'
collected: '2026-06-20'
category: Other
direction: 图像修复轻量化 · 知识蒸馏
tags:
- Lightweight Architecture
- Image Inpainting
- Knowledge Distillation
- Latent Diffusion
- Model Compression
- Efficient Inference
one_liner: 通过新型骨干块与自适应多粒度蒸馏，用2%参数实现超10倍推理加速，修复质量媲美10B级工业模型
practical_value: '- 骨干块中的 Local-λ 和 Interactive-λ 模块将空间与语义信息压缩为固定线性矩阵，大幅减少参数，这种“张量分解”式的特征交互压缩思路可直接用于推荐模型中的
  MLP 层或 Attention 层压缩，降低推理成本。

  - 自适应多粒度蒸馏策略在潜在空间动态平衡像素、语义等多层级损失，无需解码回像素空间，该方法可迁移到排序模型的知识蒸馏中：在 embedding 或 logits
  层直接进行多目标蒸馏，避免昂贵的全图输出，提升效率。

  - 将 10B 通用大模型的专业能力蒸馏到 0.2B 任务专用模型，在推荐场景可借鉴为：用大规模通用推荐模型（如 LLM4Rec）蒸馏出针对特定业务（如服饰 Occlusion
  预测、商品图补全）的高效小模型，降低延迟。

  - 整体框架强调“极致压缩 + 针对性蒸馏”，启发我们在 Agent 工具调用或搜索结果补全等实时性要求高的任务中，构造一个能快速执行的轻量 specialist，而非依赖厚重通用模型。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机：** 10B 级工业基础模型在图像修复上表现优异，但计算成本过高，难以部署。构建高度优化的任务专用小模型是可行路径，但极端结构压缩会导致严重的表征瓶颈。

**方法：** 提出 Moebius，一个高效轻量修复框架。核心是重构扩散骨干的 Local-λ Mix Interaction (LλMI) 块，包含 Local-λ 和 Interactive-λ 模块，将空间上下文和全局语义先验优雅地总结为固定尺寸的线性矩阵，保留复杂隐空间交互的同时大幅削减参数。为充分释放紧凑架构的能力，配合自适应多粒度蒸馏策略：仅在潜在空间操作，动态平衡多种基于梯度的损失（如像素对齐、语义对齐、感知相似度等），避免像素空间解码的高昂开销，实现高保真对齐。

**结果：** 在自然图像和人像修复基准上，Moebius 生成质量媲美甚至超越 10B 级工业通用模型 FLUX.1-Fill-Dev。参数量仅后者 2% 以下（0.22B vs 11.9B），总推理时间加速 >15 倍，为高保真修复树立了新的效率标准。
