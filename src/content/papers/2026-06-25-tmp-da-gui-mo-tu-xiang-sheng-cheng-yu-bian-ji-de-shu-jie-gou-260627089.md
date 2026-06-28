---
title: 'TMP: Tree-structured Mixed-policy Pruning for Large-scale Image Generation
  and Editing'
title_zh: TMP：大规模图像生成与编辑的树结构混合剪枝框架
authors:
- Peizhen Zhang
- Yang Li
- Xunsong Li
- Songtao Liu
- Zewen Liu
- Qiangqiang Hu
- Guotong Guo
- Jupeng Ding
- Yifu Sun
- coopersli
affiliations:
- Multimodal Model Department, Tencent
arxiv_id: '2606.27089'
url: https://arxiv.org/abs/2606.27089
pdf_url: https://arxiv.org/pdf/2606.27089
published: '2026-06-25'
collected: '2026-06-28'
category: Other
direction: 大规模图像生成模型的结构化剪枝与优化
tags:
- structured pruning
- MoE
- DiT
- image generation
- model compression
- efficient inference
one_liner: 首个树结构混合策略剪枝框架，统一 MoE 和 DiT 架构，将 80B 混元图像压缩至 20B（75%），质量损失有限，实现单卡推理
practical_value: '- 剪枝策略的混合设计思想可迁移至大规模推荐模型（如多专家用户点击率模型）的压缩：针对不同模块（专家层、注意力层）采用差异化剪枝策略，而非一刀切

  - 工程上实现 80B→20B 后单卡（24GB）推理的优化经验（如 KV cache 裁剪、内存调度）对部署巨型推荐模型有直接参考价值

  - 树结构搜索最优剪枝率的方法论可借鉴：在推荐系统召回 / 排序模型的剪枝中，自动搜索各层的压缩比，平衡精度与效率

  - MoE 架构的剪枝方案（如专家丢弃、路由剪枝）为电商搜索广告中的多专家模型（如多目标专家网络）压缩提供新思路'
score: 7
source: arxiv-cs.CV
depth: abstract
---

**动机**
现代图像生成模型参数规模剧增，如混元图像 3.0 达 80B 参数，需 3 张 80GB GPU 推理，极大限制实用部署。现有结构化剪枝方法多针对 DiT 架构定制，无法适应 MoE 基模型。

**方法关键点**
提出 TMP 框架，采用树结构搜索各层的混合剪枝策略：对 MoE 和 DiT 层分别设计专家级、注意力头、FFN 维度的剪枝方案，并引入 step-distilled 模型在最后阶段协同修剪。通过树搜索自动确定全局最优剪枝率分配，避免手工调参。

**关键结果**
- 压缩混元图像 3.0 从 80B 至 20B（75% 参数削减），生成质量下降有限。
- 优化后 20B 模型可在单张 24GB 4090 GPU 上推理，原 80B 模型需 3×80GB。
- 在高效模型 Z-Image turbo 上压缩 6B 至 4B（33% 削减），退化可忽略。
- 代码与权重已集成至开源社区。
