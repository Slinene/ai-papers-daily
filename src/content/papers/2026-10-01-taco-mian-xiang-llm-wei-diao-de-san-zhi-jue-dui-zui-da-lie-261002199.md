---
title: 'TACO: Ternary Absolute-max Column-wise One-sparse Optimizer for LLM Fine-Tuning'
title_zh: TACO：面向 LLM 微调的三值绝对最大列单稀疏优化器
authors:
- Jichao Jiang
- Cristian McGee
- El Houcine Bergou
- Hanqin Cai
- Aritra Dutta
affiliations:
- University of Central Florida
- Mohammed VI Polytechnic University
arxiv_id: '2610.02199'
url: https://arxiv.org/abs/2610.02199
pdf_url: https://arxiv.org/pdf/2610.02199
published: '2026-10-01'
collected: '2026-10-03'
category: Training
direction: LLM 全参微调内存优化器
tags:
- LLM fine-tuning
- memory-efficient training
- optimizer state compression
- TACO
- Muon
one_liner: 用每列最大梯度符号的稀疏更新替代 AdamW 状态，优化器状态降 174 倍，单卡 H100 可全参微调 30-32B 模型
practical_value: '- 在需要全参微调 LLM 的业务（生成式推荐、Agent 策略模型、query/文案生成）中，可用 TACO 替代 AdamW/AdamW8bit，显著降低优化器状态和峰值显存；据论文
  OPT-13B 上优化器状态 27.7GB→0.16GB，峰值显存 80.6GB→27.5GB。

  - 适合继续微调已用 AdamW 预训练或 SFT 过的模型：TACO 保留一阶梯度更新几何，可减少切换优化器带来的掉点，而 Muon 在 AdamW-pretrained
  模型上可能退化。

  - 工程落地可按层拆分：对二维权重矩阵使用 TACO，对 embedding/head 等使用 AdamW 或低内存方案；只存储每列绝对值最大梯度的符号及少量低精度分量，避免动量和二阶矩。

  - 单卡 80GB H100 能全参微调 30-32B 模型，降低硬件门槛，适合资源受限团队在推荐搜索场景中训练 LLM。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：全参数微调 LLM 时 AdamW 的优化器状态内存开销大，限制可训练模型规模。Muon 通过矩阵值更新减少优化器内存，但其更新几何与 AdamW 不同，微调 AdamW 预训练模型可能掉点。

**方法关键点**：TACO 沿用 Muon 的算子范数最速下降思路，在维度归一化的 1→1 算子范数下计算精确最速下降方向：对二维权重矩阵的每列，只选择绝对值最大梯度的符号，形成三值单稀疏方向。这样保留一阶梯度信息，同时优化器状态几乎为零。实际实现只为每列保存少量低精度梯度分量。

**关键结果**：OPT-13B 上相对 AdamW8bit，持久优化器状态从 27.7GB 降至 0.16GB，降低 174 倍；峰值训练内存从 80.6GB 降至 27.5GB，降低 2.9 倍；准确率和运行时间可比。TACO 进一步支持在单张 80GB H100 GPU 上全参微调 30-32B 参数模型，覆盖多个模型族和任务。
