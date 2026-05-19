---
title: 'SNLP: Layer-Parallel Inference via Structured Newton Corrections'
title_zh: 结构化牛顿层并行：用廉价代理雅可比实现Transformer层间并行推理
authors:
- Ligong Han
- Kai Xu
- Hao Wang
- Akash Srivastava
affiliations:
- Red Hat AI Innovation
- MIT-IBM Watson AI Lab
- Core AI, IBM
arxiv_id: '2605.17842'
url: https://arxiv.org/abs/2605.17842
pdf_url: https://arxiv.org/pdf/2605.17842
published: '2026-05-17'
collected: '2026-05-19'
category: Training
direction: 层并行推理 · 结构化牛顿校正
tags:
- Layer Parallelism
- Newton's Method
- SNLP
- IDN
- HCN
- Training Regularization
one_liner: 将层间隐藏状态视为非线性残差方程，用结构化代理雅可比替换精确雅可比，结合训练正则化，实现层并行加速。
practical_value: '- IDN 正则化让残差块的雅可比逼近 I，可移植到生成式推荐的 Transformer 编码器/解码器训练中，降低层间依赖，为后续并行化创造空间。

  - 推理时使用 IDN（即 hl+1 = f_l(hl-1) + (h_l - h_l-1)）做轻量校正，可实现层间并行评估，结合算子融合与 chunk 划分，在0.5B模型上获得2.3×加速，此模式可试用于电商搜索/推荐模型的实时推理加速，特别是当模型深度较大时。

  - HCN 利用架构内残差混合矩阵（如mHC）作为代理雅可比，避免任何雅可比估计开销；若系统已有流式记忆或路由结构，可直接复用其权重作为并行校正算子。

  - SNLP 训练正则（让有限步牛顿迭代解逼近序列解）同时改善序列PPL（降低4.7%~23.4%），可作为通用的训练正则项提升模型质量，即使不启用并行推理也值得尝试。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：自回归语言模型按层顺序执行，深度依赖成为延迟瓶颈，而现有张量/流水线并行未解此问题。若将层间隐藏状态轨迹视为非线性残差方程的解，可用牛顿类方法并行求解，但精确雅可比计算代价过高，朴素的固定点迭代不稳定。

**方法关键点**：
- 提出 SNLP 框架，用廉价结构化代理雅可比替代精确层雅可比，在残差 Transformer 中退化为**身份牛顿(IDN)**，即 hl+1 = f_l(hl-1) + (h_l - h_l-1)；在mHC 类架构中使用残差混合矩阵作为**HCN**代理。
- 非线形层评估可并行，而 Newton 校正变为轻量的结构化递归（前缀和形式的传播），分离了昂贵并行计算与廉价顺序校正。
- **SNLP 感知正则**：训练时让有限步（K=1）SNLP 求解结果与顺序轨迹匹配，促使层动态适应所选代理，同时降低分支雅可比范数（如 IDN 正则将层雅可比谱估计降低约12×）。
- 推理时采用**层融合**（多并行层合并为宽矩阵乘）和**chunk 策略**（分组校正），实现硬件友好执行。

**关键实验**：
- 在 Nanochat 0.5B/3B 从头训练模型上评估，使用 ClimbMix 数据集，PPL 为主要指标，并在 H100 测速。
- IDN 正则化后序列 PPL 降低 4.7%~23.4%。
- 0.5B 模型上 SNLP 推理可达到 2.3× 加速（如12xF2-h0），同时 PPL 较基线降低 32.1%（如16xF1-h0 配置）。
- 3B 模型虽提升 PPL 但未获加速，因块宽度已饱和 H100。
- 对角线牛顿（DiagN）多数仅恢复至序列 PPL，身份牛顿更利于质量提升。

**核心 insight**：SNLP 并非精确恢复序列计算，而是引入一种**求解器诱导的推理偏置**，当训练使得代理校正足够准确时，这种偏置可在保持或提升质量的同时暴露层并行性。
