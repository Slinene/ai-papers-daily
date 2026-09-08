---
title: 'PRICE: A Systematic Study of LLM Adaptation Choices for Bitcoin Price Forecasting'
title_zh: PRICE：比特币价格预测中 LLM 适配选择的系统研究
authors:
- Maryam Fakhari
- Mehran Safayani
affiliations:
- Isfahan University of Technology
arxiv_id: '2609.05235'
url: https://arxiv.org/abs/2609.05235
pdf_url: https://arxiv.org/pdf/2609.05235
published: '2026-09-04'
collected: '2026-09-08'
category: LLM
direction: LLM 时间序列预测 · 适配策略
tags:
- LLM
- Time Series Forecasting
- LoRA
- Bitcoin
- Decoding
- Prompting
one_liner: 系统验证 LoRA、递归推理、整数表示、CTF 提示与零温度解码如何提升 LLM 比特币价格预测精度与稳健性
practical_value: '- 低资源数值预测可直接复用：4-bit 量化 LLM + LoRA 在有限硬件上可重训，适合电商销量/GMV/出价等频繁更新的数值预测，不必上大参数全量微调。

  - 连续值取整是一种简单有效的表示 trick：用整数代表价格、销量、金额等，可降低回归误差和 token 空间，业务上可先做分箱/取整再训练。

  - 多步预测用递归推理而非一次性输出，配合 temperature=0 解码，能显著提升多步预测稳定性和误差；广告消耗、库存曲线预测可借鉴。

  - CTF 提示固定 Context/Task/Format 结构优于 CoT/few-shot，且微调后仍有效；在构建 LLM 预测/排序任务 prompt
  时优先设计统一结构，而不是依赖复杂推理提示。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：加密货币市场强波动和非平稳性使传统时序预测困难；LLM 在时序预测有潜力，但金融场景下各适配选择如何联合作用缺乏系统研究。

方法：基于 4-bit 量化 LLaMA-3 8B，提出 PRICE 框架，集成 LoRA 参数高效微调、递归多步推理、整数取整数值表示、Context-Task-Format（CTF）提示、精确零温度解码。通过消融逐一考察各选择。

结果：每个组件均贡献精度/可靠性；LoRA 降低训练门槛，递归推理提升精度，整数表示一致降低误差；CTF 优于 CoT、iCoT 和 few-shot，零温度解码提升递归稳定性。与 8 个 transformer/时序基础模型对比，验证集和测试集均取得最低预测误差，且不同评估期稳健性更强。
