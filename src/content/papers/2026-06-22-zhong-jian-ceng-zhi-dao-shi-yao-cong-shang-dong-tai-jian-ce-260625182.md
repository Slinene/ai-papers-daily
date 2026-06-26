---
title: 'What Intermediate Layers Know: Detecting Jailbreaks from Entropy Dynamics'
title_zh: 中间层知道什么：从熵动态检测越狱攻击
authors:
- Sofiia Nikolenko
- Michele Papucci
- Mina Rezaei
- Shireen Kudukkil Manchingal
affiliations:
- LMU Munich
- University of Pisa
- CNR-ILC
- Oxford Brookes University
- Munich Center for Machine Learning
arxiv_id: '2606.25182'
url: https://arxiv.org/abs/2606.25182
pdf_url: https://arxiv.org/pdf/2606.25182
published: '2026-06-22'
collected: '2026-06-26'
category: LLM
direction: LLM安全 · 中间层熵动态
tags:
- Jailbreak Detection
- Entropy Dynamics
- Intermediate Layer
- Logit Lens
- LLM Safety
- Adversarial Robustness
one_liner: 利用LLM中间层token预测熵的单调趋势特征，无需训练即可跨模型检测越狱攻击
practical_value: '- 在电商推荐Agent或对话系统中，可实时监测恶意prompt：提取用户输入token级预测熵的**单调秩趋势得分**，无需微调模型，适合低延迟在线检测。

  - 直接使用**中间层logits**而非最终输出层计算熵，可捕捉更明显的越狱信号，架构一致性允许跨不同LLM（如Llama、Qwen系列）复用。

  - 特征工程聚焦于**熵值随token位置的演化轨迹**（如单调性），而非简单的均值/方差，这种动态特征对于对抗性输入的微小扰动更鲁棒。

  - 该检测方法完全基于冻结模型，不依赖额外安全分类器训练，可快速嵌入已有Agent pipeline，作为安全兜底层。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：越狱攻击通过精心设计的提示词绕过LLM安全对齐，现有防御多针对输入/输出文本，但对模型内部有害意图的表征机制了解不足。

**方法**：使用logit lens分析冻结LLM在各层对输入token的**预测熵**。发现**静态统计量**（如熵的均值、方差）区分越狱与正常提示的能力很弱，而**捕捉熵值跨token位置演化趋势的特征**（如单调秩趋势得分）能提供强判别信号。该信号在**中间层**最显著，靠近模型输出层反而衰减，表明越狱相关结构集中在中层表征。

**结果**：在Llama、Qwen、Gemma等多个模型和对抗基准上，基于熵动态的特征无需额外训练即可实现架构一致的越狱检测分离，验证了中间层不确定性动态能稳定编码有害意图。
