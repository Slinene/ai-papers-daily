---
title: Reference-Based Bias Detection in LLMs via Relative Representations of Hidden
  States
title_zh: 基于隐藏状态相对表示的参考式 LLM 偏见检测
authors:
- Marek Jeliński
- Jan Dubiński
- Maciej Chrabaszcz
- Sebastian Cygert
affiliations:
- NASK - National Research Institute, Poland
- Warsaw University of Technology, Poland
- Gdańsk University of Technology, Poland
arxiv_id: '2609.10060'
url: https://arxiv.org/abs/2609.10060
pdf_url: https://arxiv.org/pdf/2609.10060
published: '2026-09-08'
collected: '2026-09-13'
category: Eval
direction: LLM 偏见审计·相对表示
tags:
- bias detection
- relative representations
- hidden states
- fine-tuning
- audit
- LLM
one_liner: 用隐藏状态与锚点句的相似度构建相对表示，在共享空间中度量微调前后偏见偏移 ΔB
practical_value: '- 可用于业务模型上线前/微调后的低成本偏见回归监控：不依赖输出级标注或裁判模型，直接对 checkpoint 隐藏状态做 ΔB
  检测，约 3 分钟完成，适合 CI 流程。

  - 在电商推荐/广告文案生成等场景，可借鉴相对表示方法，用固定锚点句集合编码不同群体/属性，快速审计模型对性别、地域、品牌等的隐含关联漂移。

  - 对 LoRA/PEFT 微调尤其注意：结果更依赖模型，建议结合输出级评估使用，不要单独作为放行标准。

  - 若业务中已有针对敏感群体的句子模板，可将 ΔB 作为模型迭代时的内部指标，与输出 A/B 测试互补，提前拦截高风险检查点。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有 LLM 偏见审计大多依赖模型输出，需要昂贵基准或裁判模型，且可能漏掉从未出现在生成文本中的内部表征偏移。

**方法关键点**：提出基于参考的隐藏状态审计方法。针对同一模型家族的不同变体（如微调前后），由于微调会改变表征几何，绝对隐藏状态不可直接比较。因此用每个句子与一组固定锚点句的相似度编码，得到相对表示，进入共享比较空间。在该空间中度量目标群体与正/负属性关联的偏移，定义为 Representational Bias Shift ΔB。

**关键结果**：在 3 个模型家族和 WildGuardMix、DecodingTrust、ToxiGen 上，ΔB 与输出级偏见变化在 18 个测试设置中 15 个显著相关，全微调下最高 |r|=0.84 (p<0.001)，参数高效适应下更依赖模型。阈值化 ΔB 检测偏见增大的 checkpoint，ROC AUC 介于 0.65-0.99；在 WildGuardMix 和 DecodingTrust 上比 SEAT 基线分离效果更好。ΔB 对锚点集、属性集、目标模板变化稳定。方法无需任务特定评估数据，约 3 分钟审计一个模型，计算开销为输出级基准的 1/50 到 1/3。定位为输出级审计的补充，而非替代。
