---
title: 'ZO-Act: Efficient Zeroth-Order Fine-Tuning via One-Shot Activation-Informed
  Low-Rank Subspaces'
title_zh: ZO-Act：基于单次激活信息低秩子空间的零阶微调
authors:
- Xun Dong
- Yibo Xu
- Naigang Wang
- Xin Li
- Penghang Yin
- Zi Yang
affiliations:
- University at Albany, SUNY
- IBM T. J. Watson Research Center
arxiv_id: '2607.01125'
url: https://arxiv.org/abs/2607.01125
pdf_url: https://arxiv.org/pdf/2607.01125
published: '2026-07-01'
collected: '2026-07-02'
category: LLM
direction: LLM 高效零阶微调 · 激活子空间
tags:
- Zeroth-order optimization
- activation subspace
- low-rank adaptation
- memory-efficient fine-tuning
- LLM fine-tuning
- quantized LLM
one_liner: 利用激活矩阵低秩基约束零阶优化扰动，大幅降低梯度估计方差，实现高效LLM微调
practical_value: '- 在无法使用反向传播或内存极度受限的场景（如移动端、隐私保护环境）下，可将该方法用于微调电商搜索/推荐系统中的LLM组件，仅需前向传播损失评估。

  - 低秩子空间构建方式与LoRA类似，但可结合零阶优化，直接适应量化LLM（如INT4），冻结量化权重优化低维系数，适合部署轻量级推荐模型。

  - 仅前向计算显著降低显存占用，显式系数矩阵兼容Adam优化器，能更快收敛，可借鉴到需要频繁冷启动或增量更新的推荐Agent微调流程。

  - 理论分析揭示的方差-偏差权衡可为选择扰动子空间维度提供指导：高激活秩层可分配更多秩，平衡近似误差与梯度估计质量，可扩展到推荐系统中多任务LLM的参数高效微调。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：零阶（ZO）优化可绕过反向传播微调LLM，但现有方法扰动全权重或随机低维子空间，导致高方差和性能受限。LLM激活和梯度具有低秩特性，这提供了更优的子空间约束可能。

**方法**：提出ZO-Act，针对每个线性层，初始化时对一批输入激活矩阵做SVD得到固定的低秩基矩阵 \(U\)，将权重更新约束在 \(U\) 的列空间内，仅优化轻量的系数矩阵 \(C\)。前向传播只需评估损失，通过对称扰动 \(C\) 估计梯度，显式可训练参数可直接使用Adam等动量优化器。因为基础权重冻结，天然支持量化模型微调。理论证明，扰动低维系数 \(C\) 能降低ZO估计的方差依赖收敛项和有限差分误差，而子空间近似偏差被激活低秩结构控制。

**结果**：在Llama-3-8B、OPT-13B及INT4量化Llama-3-8B上，覆盖语言理解、问答、常识推理任务，ZO-Act一致超越现有强ZO微调基线（如MeZO），在维持内存效率的同时提升下游任务精度。
