---
title: The State-Prediction Separation Hypothesis
title_zh: 状态-预测分离假说
authors:
- Giovanni Monea
- Nathan Godey
- Kianté Brantley
- Yoav Artzi
affiliations:
- Cornell University
- Harvard University
arxiv_id: '2607.01218'
url: https://arxiv.org/abs/2607.01218
pdf_url: https://arxiv.org/pdf/2607.01218
published: '2026-06-30'
collected: '2026-07-02'
category: Training
direction: Transformer 架构改进 · 预训练效率
tags:
- State-Prediction Separation
- Transformer Architecture
- Pretraining Efficiency
- Language Modeling
- Dual-Stream
one_liner: 分离 Transformer 中的状态存储和下一 token 预测功能，显著提升语言模型预训练效率和下游表现。
practical_value: '- 用户行为序列建模（如点击序列）可借鉴双流设计：显式分离长期兴趣状态的存储和短期行为预测，可能提升数据效率和下游任务表现。

  - 对于生成式推荐模型（用 LLM 生成 Semantic ID），分离持久状态与瞬时预测流可改善生成质量并加速收敛。

  - 在预训练大型序列模型时，可尝试引入状态-预测分离，以更少的计算和 token 预算获得更强的表征，再微调至搜索/推荐任务。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：标准 Transformer 每一层的隐藏状态既要预测当前 token，又要作为记忆供未来步骤使用，这种双重角色可能产生冲突，限制性能。该文提出**状态-预测分离假说**：将这两种功能解耦到不同的计算流中，能获得更好的语言建模效果。

**方法**：设计双流 Transformer 变体。一条**状态流**处理输入 token，形成跨时间步的持久状态；另一条**预测流**专门基于状态流生成下一 token 预测。两条流在注意力计算上隔离但共享部分参数，确保状态不受短期预测目标的干扰。

**结果**：在 300M~1.6B 参数规模的预训练实验中，分离架构始终优于同等算力的标准 Transformer，验证损失更低。在 1.6B 规模，仅用 18B 训练 token 即达到标准模型用 47B token 的验证损失（2.6× token 节省）。下游任务平均提升 2--3 个百分点。梯度分析证实分离设计引入了根本不同的优化信号，排除了混淆因素。
