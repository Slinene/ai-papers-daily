---
title: 'SpaceDG: Benchmarking Spatial Intelligence under Visual Degradation'
title_zh: 视觉退化下空间智能评测基准 SpaceDG
authors:
- Xiaolong Zhou
- Yifei Liu
- Ziyang Gong
- Jiarui Li
- Qiyue Zhao
- Muyao Niu
- Yuanyuan Gao
- Le Ma
- Xue Yang
- Hongjie Zhang
affiliations:
- Shanghai Jiao Tong University
- Shanghai Artificial Intelligence Laboratory
- University of Electronic Science and Technology of China
- Chongqing University
- The University of Tokyo
arxiv_id: '2605.22536'
url: https://arxiv.org/abs/2605.22536
pdf_url: https://arxiv.org/pdf/2605.22536
published: '2026-05-20'
collected: '2026-05-25'
category: Eval
direction: 多模态大模型空间推理鲁棒性评测
tags:
- Spatial Reasoning
- Visual Degradation
- MLLM Benchmark
- 3D Gaussian Splatting
- Robustness
one_liner: 首次大规模评测多模态模型在真实视觉退化下的空间推理鲁棒性，并证明退化感知训练可超越人类
practical_value: '- **退化数据增强提升 Agent 鲁棒性**：在训练电商搜索、虚拟试穿等多模态 Agent 时，可直接引入 SpaceDG
  的退化合成引擎（基于 3DGS）生成逼真的运动模糊、低光照、JPEG 压缩等图像，能显著提升模型对真实世界图像质量的鲁棒性，且不损害干净图像性能。

  - **空间推理任务的迁移**：SpaceDG-Bench 定义的三类空间任务（相机中心、相机-物体、物体中心）可改造为商品陈列合理性判断、家具摆放推荐等电商场景的评测，检验模型对空间关系（如“笔记本相对显示器在左边”）的理解。

  - **退化下的多模态 fallback 策略**：评测发现纯文本基线（GPT-5.4 无图像）在严重退化时准确度居然超过某些视觉模型，提示 Agent 设计时可在图像质量过低时自动切换至纯文本推理模式，避免错误空间决策。

  - **训练效率启示**：在 SpaceDG 退化数据上微调后，8B 模型即可超越人类退化条件下的表现，说明小模型通过针对性数据增强也能获得强鲁棒性，适合电商侧轻量部署。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有多模态大模型（MLLM）空间推理基准均假设视觉输入完美，忽略真实环境中普遍存在的运动模糊、低光照、雾、镜头畸变、压缩噪声等退化。这带来关键问题：模型在视觉退化下的空间智能是否鲁棒？

**方法关键点**：
1. 提出 SpaceDG，第一个大规模退化感知空间理解数据集。基于物理的退化合成引擎将退化形成过程嵌入 3D 高斯溅射（3DGS）渲染，模拟 9 种退化类型，生成约 1000 个室内场景、100 万 QA 对。
2. 构建 SpaceDG-Bench，包含 11 种推理类别、9 种退化类型，共 10K+ VQA 实例，经人工验证。
3. 评估 25 个开源/闭源 MLLM，涵盖从相机中心、相机-物体到物体中心的空间任务。

**关键结果**：
- 所有模型在视觉退化下空间推理准确率大幅下降（降幅可达 20.9%），暴露严重鲁棒性缺口。
- 在 SpaceDG 上微调后，模型退化鲁棒性显著提升，甚至超越人类退化条件下的表现（微调 8B 模型达 66.1%，人类退化 59.5%），且干净图像性能无损。
- 纯文本非图像基线在某些任务中竞争力强，说明空间推理并不完全依赖清晰视觉。
