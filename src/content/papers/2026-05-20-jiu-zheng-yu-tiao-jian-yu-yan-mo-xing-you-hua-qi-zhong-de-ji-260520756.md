---
title: Correcting Stochastic Update Bias in Preconditioned Language Model Optimizers
title_zh: 纠正预条件语言模型优化器中的随机更新偏差
authors:
- Nikhil Nayak
- Julia White
- Urchade Zaratiana
- Kelton Zhang
- Henrijs Princis
- Dhruv Atreja
- Henry Fawcett
- Matthew Thomas
- George Hurn-Maloney
- Ash Lewis
affiliations:
- Fastino Labs
arxiv_id: '2605.20756'
url: https://arxiv.org/abs/2605.20756
pdf_url: https://arxiv.org/pdf/2605.20756
published: '2026-05-20'
collected: '2026-05-21'
category: Training
direction: 预条件优化器偏差校正
tags:
- Bias Correction
- Preconditioned Optimizer
- AdamW
- Sophia
- Shampoo
- Language Model Pretraining
one_liner: 通过微批次交叉拟合与Delta方法逆修正，消除梯度-预条件子耦合和逆预条件有限样本偏差，提升AdamW、Sophia、Shampoo预训练效果
practical_value: '- **可用于生成式推荐/大模型训练中的优化器改进**：当使用AdamW、Sophia、Shampoo等自适应优化器时，将批次拆分为独立子批，分别估计梯度和预条件子，可移除耦合偏差；同时利用子批方差对逆预条件子做泰勒/Jackknife校正，降低逆运算的非线性偏差。代码级实现只需对现有优化器做包装（Algorithm
  1），无需改动模型。

  - **在噪声较大、预条件子估计不稳定的场景（如小批量、低EMA系数）效果更明显**：电商推荐模型中若使用对角二阶矩（AdamW）或曲率估计（Sophia），可借鉴本文的Delta方法逆校正，公式为
  \(\tilde{T}(\bar{p}_k) = 1/(\bar{p}_k + \lambda) - \widehat{\text{Var}}(\bar{p}_k)/(\bar{p}_k
  + \lambda)^3\)，仅需维护子批方差，计算开销极小。

  - **矩阵预条件子（如Shampoo）的校正可在特征基下进行**：对于推荐系统中可能的矩阵预条件（如K-FAC），可利用平均预条件子的特征分解，将每个子批投影到该基下，对特征值逐元素校正。避免反复特征分解，工程上可行。

  - **在Agent多智体训练中，若每个Agent的本地更新可视为微批次，可利用方差校正来提升全局聚合的稳定性**：将各Agent本地计算的预条件子统计量视为独立子批，使用Jackknife或方差校正再聚合，降低系统估计偏差，可能提升收敛速度和最终策略质量。

  - **注意拆分方式要保留原优化器的分母规模**：实验显示两折拆分（各用一半数据）会因分母样本减半而增大方差，推荐使用留一法（LOO）构造分母，保持分母接近全批量规模，从而在移除耦合的同时不显著增加噪声。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

**动机**  
自适应优化器（AdamW、Sophia、Shampoo）在语言模型训练中普遍使用，但其更新方向通常被视为“预条件子逆 × 随机梯度”的直接估计。实际上，由于在同一批数据上估计梯度和预条件子，二者存在统计耦合；同时，即使预条件子估计是无偏的，其逆（或逆根）因非线性变换也会有偏。这两个有限样本偏差在噪声大、预条件子不稳定时尤为显著，但现有优化器未显式处理。  

**方法关键点**  
- **偏差分解**：将更新偏差拆分为“梯度-预条件子耦合偏差”与“逆预条件偏差”，并给出统计表达式。  
- **交叉拟合去耦**：将当前批量划分为独立子批，用子批A计算梯度，子批B计算预条件子，再相乘，消除耦合项。  
- **方差校正逆**：利用子批间的变异性，对逆映射做Delta方法展开，减去二阶项：\( \tilde{T}(\bar{p}_k) = 1/(\bar{p}_k+\lambda) - \widehat{\text{Var}}(\bar{p}_k)/(\bar{p}_k+\lambda)^3 \)，可减少逆偏差至\(O(m^{-3/2})\)；矩阵预条件子则在平均预条件子的特征基下对特征值逐元素校正。  
- **适用三种优化器**：给出AdamW（对角二阶矩）、Sophia（对角曲率）、Shampoo（矩阵预条件）的具体校正公式，并可作为现有优化器的包装层（Algorithm 1）。  

**关键实验**  
在Qwen2.5-0.5B的预训练（FineWeb-Edu 256K序列）和指令微调上测试。预训练场景下校正效果显著：AdamW采用留一法交叉拟合+Jensen逆校正，评估损失从4.836降至4.687（-0.149 nats）；Sophia满校正从6.665降至6.595（-0.070 nats）；Shampoo满校正从5.792降至5.681（-0.110 nats）。在混合噪声数据（20% span替换）预训练中，AdamW校正后干净评估损失仍略有改善。指令微调从强预训练起点出发，校正效果中性偏正，但幅度微小。  

**核心结论**  
该框架说明有限样本下优化器的随机更新存在可修正的统计偏差，通过简单的子批拆分与方差校正就能降低偏差，改善预训练收敛质量，且实现成本低，可作为一个通用优化器增强组件。
