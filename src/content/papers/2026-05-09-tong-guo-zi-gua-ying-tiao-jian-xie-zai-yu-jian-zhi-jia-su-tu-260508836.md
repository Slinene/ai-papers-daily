---
title: Accelerating Multi-Condition T2I Generation via Adaptive Condition Offloading
  and Pruning
title_zh: 通过自适应条件卸载与剪枝加速多条件文生图生成
authors:
- Yuxin Kong
- Peng Yang
- Chongbin Yi
- Fan Wu
- Feng Lyu
affiliations:
- Huazhong University of Science and Technology
- Central South University
arxiv_id: '2605.08836'
url: https://arxiv.org/abs/2605.08836
pdf_url: https://arxiv.org/pdf/2605.08836
published: '2026-05-09'
collected: '2026-05-17'
category: Multimodal
direction: 多模态生成 · 端边协同推理优化
tags:
- text-to-image
- edge-computing
- multi-condition
- diffusion-models
- condition-pruning
- adaptive-offloading
one_liner: 端边协同系统通过启发式卸载和特征驱动条件剪枝大幅降低多条件T2I延迟，同时提升生成质量
practical_value: '- **条件重要性剪枝可迁移至推荐特征选择**：Conditioning Scale Estimator 通过特征激活强度和重叠度评估条件贡献，该思路可直接用于电商推荐系统中的多模态特征筛选，动态剪枝低贡献特征以降低推理成本。

  - **端边协同推理适用于大模型部署**：Subtask Manager 联合优化卸载策略与带宽分配，平衡本地与边缘延迟，可参考用于 Agent 推理场景中模型分片或模块的动态放置，降低整体响应时间。

  - **启发式延迟优化可复用**：针对异构任务的计算/通信成本差异，采用启发式算法快速求解近似最优卸载方案，适合需要实时决策的推荐推理流水线，例如决定特征是在
  CPU 还是 GPU 侧预处理。

  - **特征激活强度分析辅助模型加速**：通过量化中间特征的激活强度与重叠，可以指导模型压缩或动态网络宽度调整，在电商图片生成或虚拟试穿等多条件生成场景中直接降低推理开销。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：多条件文生图（T2I）可让用户精细控制生成结果，但多种条件输入带来大量预处理计算与额外通信开销，导致生成延迟难以容忍。现有系统缺乏对条件异构性的利用和冗余条件的识别。

**方法**：提出端–边协同系统，包含两个核心模块：
1. **Subtask Manager**：依据离线剖析得到的各条件计算与通信成本差异，设计启发式算法联合优化条件推理的卸载决策和带宽分配，平衡本地与边缘执行延迟，最小化预处理总耗时。
2. **Conditioning Scale Estimator**：轻量特征驱动模块，通过分析每个条件的特征激活强度及与其他条件的重叠程度，评估其实际贡献，据此自适应选择条件尺度并剪除不重要条件，加速去噪过程。

**结果**：在多种多条件 T2I 基准上，系统端到端延迟降低近 25%，生成质量（FID等指标）平均提升 6%，显著优于传统本地或纯边缘方案。
