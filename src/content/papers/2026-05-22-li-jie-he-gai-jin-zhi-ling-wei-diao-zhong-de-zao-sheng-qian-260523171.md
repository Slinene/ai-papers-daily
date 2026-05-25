---
title: Understanding and Improving Noisy Embedding Techniques in Instruction Finetuning
title_zh: 理解和改进指令微调中的噪声嵌入技术
authors:
- Abhay Yadav
affiliations:
- Johns Hopkins University
arxiv_id: '2605.23171'
url: https://arxiv.org/abs/2605.23171
pdf_url: https://arxiv.org/pdf/2605.23171
published: '2026-05-22'
collected: '2026-05-25'
category: Training
direction: 指令微调 · 嵌入噪声注入
tags:
- Noisy Embeddings
- Instruction Finetuning
- SymNoise
- NEFTune
- Curvature Regularization
- LLaMA
one_liner: 理论揭示均匀与高斯噪声等价性，提出对称伯努利噪声 SymNoise，显著超越 NEFTune
practical_value: '- 在指令微调中改用对称伯努利噪声（±1 对）替代均匀噪声，实现简单、即插即用，成本极低，可直接提升对话/推荐解释的生成质量。

  - 噪声缩放定律：不同噪声分布通过规范二阶矩可校准，例如高斯噪声需除以 √3 才能达到与均匀噪声相似的扰动幅度，避免噪声过量导致性能退化。

  - 双端点扰动（正负同时训练）的曲率正则化设计可迁移至多模态对齐、语义ID 生成等任务，增强局部光滑性，抑制过拟合。

  - 在电商场景的少量标注指令数据（如商品描述生成、客服多轮对话）上，SymNoise 有助于稳定微调，提升回答多样性和长度质量，且不牺牲标准任务能力。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
指令微调（instruction finetuning）中，NEFTune 通过向嵌入注入均匀噪声大幅提高模型指令跟随能力，但其为何优于常用的高斯噪声一直缺乏解释。此工作旨在揭示噪声类型的等价性条件，并提出更优的噪声策略，从而更高效地利用有限指令数据、防止过拟合。

### 方法关键点
- **理论分析**：推导均匀、高斯、伯努利噪声的期望 L2 范数，证明在相同范数缩放（如高斯除以 √3、伯努利除以 √3）下，不同噪声在微调中表现可比，解释了 NEFTune 中均匀噪声的合理性。
- **SymNoise 方法**：向嵌入同时添加对称的伯努利噪声（ε ∈ {-1, 1} 等概率），分别得到正扰动嵌入 X + ε/√3 和负扰动嵌入 X - ε/√3，拼接后输入模型。这隐含地强制模型在嵌入邻域满足 f(x+ε) ≈ f(x-ε)，实现更严格的曲率正则化，而无需直接计算 Hessian。
- **算法实现**：沿用 NEFTune 的噪声缩放因子 α/√(Ld)，仅在嵌入层改动前向，训练开销几乎无增加。

### 关键结果
- 在 LLaMA-2-7B + Alpaca 数据集上，SymNoise 使 AlpacaEval 胜率从 29.79% 跃升至 69.04%，相较 NEFTune 的 64.69% 提升 6.7%。
- 在 Evol-Instruct、ShareGPT、OpenPlatypus 四个数据集上平均胜率 75.33%，高于 NEFTune 的 72.80%。
- 在 OPT-6.7B、LLaMA-1-7B、LLaMA-2-7B 等多个模型上均一致优于 NEFTune。
- OpenLLM Leaderboard（ARC, HellaSwag, MMLU）任务得分保持或轻微提升，说明生成质量提升不牺牲常识推理能力。
- 消融实验：高斯噪声若未适当缩放（除以 √3）则性能退化；单纯伯努利噪声不加对称分量效果不如 SymNoise。生成回复更长但非简单重复，2-gram 重复率相近。

**最值得记住的一句话**：对称伯努利噪声通过双端点扰动实现更强曲率正则化，是替换均匀噪声的简单高效微调策略，可在多个指令数据集和模型上稳定提升生成质量。
