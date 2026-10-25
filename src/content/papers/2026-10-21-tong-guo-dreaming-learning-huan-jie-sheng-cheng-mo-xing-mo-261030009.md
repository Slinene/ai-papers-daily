---
title: Mitigating Model Collapse through Dreaming Learning
title_zh: 通过 Dreaming Learning 缓解生成模型模型崩溃
authors:
- Matteo Benati
- Alessandro Londei
- Denise Lanzieri
- Raffaello Mastromarino
- Vittorio Loreto
affiliations:
- Sapienza University of Rome
- Sony CSL Rome, CREF
- University of Copenhagen
- Complexity Science Hub Vienna
arxiv_id: '2610.30009'
url: https://arxiv.org/abs/2610.30009
pdf_url: https://arxiv.org/pdf/2610.30009
published: '2026-10-21'
collected: '2026-10-25'
category: Training
direction: 生成模型训练 · 模型崩溃缓解
tags:
- model collapse
- synthetic data
- temperature
- spectral analysis
- generative models
- Dreaming Learning
one_liner: 用高温自采样样本作正则，阻止合成数据训练中的谱隙变窄与多样性塌缩
practical_value: '- 在电商/广告场景用 LLM 批量合成 Query、商品标题或推荐理由时，若后续模型继续在这些合成数据上训练，容易出现多样性下降。可以借鉴
  Dreaming Learning：训练时额外对一个高温度 Td>1 下模型自身采样结果加正则 loss，低成本抑制分布塌缩。

  - 数据积累不一定能阻止模型崩溃，尤其采样温度 Ts<1 时。如果合成数据链路里为了可控性使用了低温度采样，要主动引入高温度样本或正则，而不是只增加数据量。

  - 该工作用 transition operator 的次主导特征值和谱隙监控多样性，适合做离线监控指标：在训练生成式推荐/Query 模型时，可以周期性观察谱隙是否收窄，提前发现模型多样性退化。

  - 方法实现简单，只增加一个 loss 项，不改变模型结构，容易嵌入现有 LLM/SLM 训练流程；对 124M GPT-2 级别模型也验证有效，中小规模业务模型可参考。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

动机：生成模型在合成数据上反复训练会损失多样性、性能下降，即模型崩溃。现有缓解主要靠保留真实数据累积，但该工作发现仅靠累积在低采样温度下不足以阻止崩溃，需要从训练正则角度解决。

方法关键点：作者在受控 Markov 设定下用 transition operator 的特征值谱研究崩溃。次主导特征值控制链的 mixing 速度，也决定探索范围。低采样温度 Ts<1 相当于反复 sharpening，使次主导特征值趋近单位圆、谱隙变窄，模型逐步退化到近乎确定系统。Dreaming Learning 作为正则器，在常规训练的同时，对模型在升高温度 Td>1 下生成的自身样本增加 loss。高温采样会 flatten 预测分布，训练这些样本可以防止 learned operator 的转移概率过小，从而保持特征值远离单位圆、谱隙稳定。

关键结果：在 5000 代实验中，谱测量与上述机制一致；该方法在 LSTM 语言模型和 124M 参数的 GPT-2 上仍能保持缓解效果。
