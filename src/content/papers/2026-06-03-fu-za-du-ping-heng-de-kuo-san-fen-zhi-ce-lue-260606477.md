---
title: Complexity-Balanced Diffusion Splitting
title_zh: 复杂度平衡的扩散分治策略
authors:
- Noam Issachar
- Dani Lischinski
- Raanan Fattal
affiliations:
- The Hebrew University of Jerusalem
arxiv_id: '2606.06477'
url: https://arxiv.org/abs/2606.06477
pdf_url: https://arxiv.org/pdf/2606.06477
published: '2026-06-03'
collected: '2026-06-05'
category: Training
direction: 扩散模型·时间维度分治与动态容量分配
tags:
- Diffusion Models
- Complexity-Balanced Splitting
- Temporal Partitioning
- Generative Models
- De Boor Equidistribution
one_liner: 基于等分布原理将扩散过程切分为等难度子任务并分配专用子网络，在不增加推理成本下显著提升生成质量。
practical_value: '- **动态算力分配思路可迁移至生成式推荐**：电商中的生成式推荐（如物品标题、理由生成）若采用扩散范式，可借鉴 CBS 按生成阶段难度分配模型容量，将困难阶段（如构建语义
  ID 的后期细粒度部分）用更大子网络处理，提升生成质量而不增加总推理成本。

  - **复杂度估计的轻量方案**：使用袖珍辅助模型预测不同时间步的近似难度（Dirichlet 能量或轨迹加速度），无需昂贵搜索。在推荐场景中，可对 embedding
  生成过程建立类似的复杂度度量，指导 MoE 专家网络的选择或自适应推理步数。

  - **分治思想用于多智能体协调**：Agent 系统中处理长链路任务时，可根据任务片段复杂度动态分配不同能力的 Agent，类似 CBS 按时间分片分配子网络，提高整体协作效率。

  - **训练时的阶段型容量分配**：在训练生成式推荐模型时，可参考 CBS 的等分布原则，让不同训练阶段（如从噪声到语义）使用不同容量的小模型，节省训练资源，适合大规模电商模型的高效训练部署。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：标准扩散模型用单一架构处理从纯噪声到精细化数据分布的全程，不同阶段难度差异巨大，统一分配算力导致效率低下。

**方法关键点**：基于函数逼近理论和 de Boor 等分布原理，提出 Complexity-Balanced Splitting（CBS）框架——将扩散时间线划分为若干“等近似负担”的区间，每个区间由专门的子网络负责，困难区间分配更大容量网络。为量化局部复杂度，引入两种可计算的监控函数：空间度量（生成流场 Dirichlet 能量）和几何度量（采样轨迹加速度），并通过一个轻量辅助模型快速估计这些剖面，避免昂贵的超参数搜索或启发式划分。

**关键结果**：在 SiT、JiT 和 UNet 等架构及多个数据集上，CBS 一致提升合成质量，不增加单步推理成本。特别地，在 SiT-XL 上配合 CFG 时，FID 相对朴素时间划分方案改善约 35%。
