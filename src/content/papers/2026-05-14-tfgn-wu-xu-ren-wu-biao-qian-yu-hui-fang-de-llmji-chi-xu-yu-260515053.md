---
title: 'TFGN: Task-Free, Replay-Free Continual Pre-Training Without Catastrophic Forgetting
  at LLM Scale'
title_zh: TFGN：无需任务标签与回放的LLM级持续预训练架构
authors:
- Anurup Ganguli
affiliations:
- Independent Researcher
arxiv_id: '2605.15053'
url: https://arxiv.org/abs/2605.15053
pdf_url: https://arxiv.org/pdf/2605.15053
published: '2026-05-14'
collected: '2026-05-15'
category: Training
tags:
- Continual Learning
- Catastrophic Forgetting
- LLM
- Pre-training
- Gradient Orthogonality
- Backward Transfer
one_liner: 提出一种内部架构叠加层TFGN，在无回放、无任务ID的条件下，实现LLaMA 3.1 8B等多尺度的近零灾难性遗忘与>99.59%的梯度正交性
score: 10
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
灾难性遗忘是LLM在生产环境中持续学习的核心障碍。现有方法依赖数据回放、任务标识符或Fisher惩罚项，三者均无法满足隐私合规、任务标签未知、大规模无惩罚的部署需求。长上下文窗口不能替代持久权重内化，前沿模型在续训时仍面临显著的能力退化。

**方法关键点**
- **架构叠加层**：TFGN插入Transformer的逐块计算中，生成输入条件化的参数高效更新，不改变其余网络，保持前向传播全密集（无稀疏门控）。
- **读写解耦**：保护来自写入路径——不同域的梯度因结构设计自动落入近乎正交的子空间，无需正交性损失项；读取路径则保持共享，支持跨域正向迁移。
- **无任务依赖**：无需回放缓冲、任务ID、外部调度器或正则化惩罚，保护由架构本身保障。
- **双模式**：支持从头训练（FS）与预训练骨干改造（Retrofit），持续阶段的训练参数仅为全量的~1-14%。

**关键实验**
- **设置**：6个异构文本域（普通英语、Python、数学、生物医学、中文、JavaScript），每阶段10亿tokens，总分三步尺度（~398M、~739M、~9B）和FS/RF两种模式。
- **基线**：标准微调（Std-FT）和LoRA r=256。
- **核心结果**：
  - BWT（反向迁移）：LLaMA 3.1 8B改造模式下低至**-0.007**，~739M从零训练模式比Std-FT改善约14倍。
  - 梯度正交性：所有条件下跨域梯度的L2正交比例**≥99.59%**，平均余弦相似度<0.10。
  - 稳定性：HellaSwag精度跨阶段波动<0.01；定性展示中基线完全生成域外字符，TFGN保持域一致文本。
  - 正向迁移：JavaScript未训练时，Python训练后其PPL下降**26.8%**（8B改造）和**62.0%**（739M从零），证实读取路径的跨域协同。

**核心观点**
稳定性是写入问题，不是读取问题；TFGN通过构造性梯度解耦，使LLM在不牺牲可塑性的前提下关闭灾难性遗忘。
