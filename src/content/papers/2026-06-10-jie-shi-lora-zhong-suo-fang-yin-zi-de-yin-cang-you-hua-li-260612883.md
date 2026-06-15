---
title: The Hidden Power of Scaling Factor in LoRA Optimization
title_zh: 揭示 LoRA 中缩放因子的隐藏优化力量
authors:
- Zicheng Zhang
- Haoran Li
- Jiaxing Wang
- Guoqiang Gong
- Anqi Li
- Yudong Hu
- Ting Xiong
- Yurong Gao
- Junxing Hu
- Zhida Jiang
affiliations:
- JD
- UCAS
- NKU
arxiv_id: '2606.12883'
url: https://arxiv.org/abs/2606.12883
pdf_url: https://arxiv.org/pdf/2606.12883
published: '2026-06-10'
collected: '2026-06-15'
category: Training
direction: LoRA 缩放因子优化
tags:
- LoRA
- Fine-tuning
- Scaling Factor
- Hyperparameter Optimization
- PEFT
one_liner: 发现 LoRA 缩放因子 α 主导优化，与学习率作用不同，提出平方根法则及 LoRA-α 框架
practical_value: '- 微调 LLM（如用于推荐解释生成、Agent 工具调用）时，放弃秩绑定的 α=2r 传统，采用平方根律 α = c√r（c
  可由少量实验确定，如 c≈4~8），用标准小学习率即可高效收敛，简化调参。

  - 若微调效果受限于收敛速度，优先放大 α 而非学习率：α 放大任务信号却不增加参数漂移（drift ratio），可避免过拟合与遗忘，特别适合在线持续微调场景。

  - LoRA-α 的发现直接支持在电商多任务微调中固定 α，使用统一的小学习率（如 1e-4），无需为不同任务反复调整学习率，降低超参搜索成本。

  - 频谱抑制平滑优化地形的洞察可用于诊断微调困难：若训练初期梯度方向杂乱，可增大 α 或降低秩以强化主成分信号，加速收敛。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LoRA 中缩放因子 α 常被视为学习率的补充，但其独立优化作用未被厘清，导致实践中使用启发式 α=2r 可能限制性能。

**方法关键点**：
- 通过大量实验与理论 **Signal-Drift 框架**，揭示 α 与学习率的不同机制：LoRA 的低秩结构产生**频谱抑制**，平滑优化地形，但标准超参过于保守，形成优化缺口。
- 证明 **α 是优化主驱动**：α 放大了任务相关信号成分，且不增加参数漂移占比（drift ratio），而增大学习率会同时放大噪声与漂移。
- 发现最优 α 与秩 r 呈**次线性平方根关系** α* = c√r，c 为较大常数（如实验中约 6~8），远超传统 α=2r，解释了现有启发式的不足。
- 提出 **LoRA-α**：将 α 设置为与秩无关的固定大值（如 c√r），配合标准小学习率（如 1e-4），无需精细调优即可达到高性能。

**关键结果**：在多个 NLP、VL 任务上，LoRA-α 一致超越标准 LoRA，提升幅度可达 2~5 个点，且超参搜索大幅简化。
