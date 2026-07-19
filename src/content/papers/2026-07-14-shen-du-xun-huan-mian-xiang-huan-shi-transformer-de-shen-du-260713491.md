---
title: 'DeepLoop: Depth Scaling for Looped Transformers'
title_zh: 深度循环：面向环式 Transformer 的深度缩放方法
authors:
- Shuzhen Li
- Yifan Zhang
- Jiacheng Guo
- Quanquan Gu
- Mengdi Wang
affiliations:
- Princeton University
- University of California, Los Angeles
arxiv_id: '2607.13491'
url: https://arxiv.org/abs/2607.13491
pdf_url: https://arxiv.org/pdf/2607.13491
published: '2026-07-14'
collected: '2026-07-19'
category: Training
direction: 环式 Transformer 深度缩放
tags:
- Looped Transformer
- DeepNorm
- Training Stability
- Residual Scaling
- Depth Scaling
one_liner: 针对环式 Transformer 参数共享提出新的残差缩放规则，将 DeepNorm 指数从 1/4 提升到 1/2 以保证稳定训练
practical_value: '- 在推荐模型的深度序列编码器（如使用共享层堆叠的 SASRec 变体）中，若采用多轮循环以扩展感受野而不增加参数，可直接套用
  DeepLoop 的 α、β 缩放公式，避免因参数重复访问导致的训练不稳定。

  - 对于生成式推荐中基于环式 Transformer 的序列生成解码器，该缩放规则保证长循环深度下的梯度更新平衡，使更深的推理计算（test-time compute）成为可行，从而提升生成质量。

  - 在资源受限设备上部署大容量推荐模型时，可利用环式结构压缩参数存储，同时通过深度循环实现深度计算扩展，DeepLoop 提供了训练稳定性保障。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：环式 Transformer 通过重复使用固定数量的物理块来增加展开深度，从而在不增加参数量的前提下提升模型容量。然而，参数共享导致同一个模块在前后向传播中被多次访问，其残差分支接收并施加的是累积梯度，这与标准 DeepNorm 的假设（每层独立更新）冲突，直接沿用原有的缩放规则会导致训练不稳定。

**方法**：作者将这种“深度绑定”效应形式化为一个一阶扰动边界，该边界由访问对齐系数 κ_R 控制。当各次访问高度相关时，需要将残差缩放指数从标准的 1/4 提高到 1/2，才能使扰动界保持有界。基于此，提出 DeepLoop：保留 Post-LN DeepNorm 架构，并将缩放因子设为 α=(2N)^{1/2}，β=(8N)^{-1/2}，其中 N 为展开后的总深度（物理深度 × 循环轮数）。该设置在没有循环（即一轮遍历）时退化为标准 DeepNorm。

**结果**：在 GPT-2 Small 和 Medium 规模的环式语言模型上，DeepLoop 在物理块不被重复使用时与基线相当，而一旦激活循环深度，验证损失和下游任务准确率均有明显改善，证明了面向参数访问次数的残差缩放规则是实现稳定循环深度的关键。
