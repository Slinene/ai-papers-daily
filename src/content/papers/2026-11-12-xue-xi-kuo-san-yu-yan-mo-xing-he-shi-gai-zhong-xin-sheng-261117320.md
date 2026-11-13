---
title: Learning When Diffusion Language Models Should Regenerate
title_zh: 学习扩散语言模型何时该重新生成
authors:
- Minhae Oh
- Jeonghye Kim
- Jinwoo Koo
- Yeongoon Kim
- Jimin Seo
- Minsik Seol
- Jungwoo Lee
affiliations:
- Seoul National University
- KAIST
arxiv_id: '2611.17320'
url: https://arxiv.org/abs/2611.17320
pdf_url: https://arxiv.org/pdf/2611.17320
published: '2026-11-12'
collected: '2026-11-13'
category: Reasoning
direction: 扩散语言模型解码 · 验证器引导重生成
tags:
- Diffusion Language Models
- Verifier
- Decoding Strategy
- Self-Correction
- Inference-time
one_liner: 提出验证器 DiVR，预测部分生成序列能否最终正确，决定何时块级重生成及保留哪个候选，显著提升扩散 LM 推理准确率
practical_value: '- 在生成式推荐或语义 ID 生成中，若使用扩散/迭代式生成器，可训练一个验证器预测中间结果最终是否成功，替代仅靠 token
  confidence 或 likelihood 的简单修正策略；尤其适合需要早停或块级重生成的在线推理场景。

  - 训练验证器只需模型自身生成轨迹的最终正确性标签，无需额外人工标注；可离线收集正负轨迹，作为生成器的轻量级 reranker 或 gate，成本低且生成器无需改动。

  - 块级重生成比逐 token 修错更稳定，能避免孤立错误在固定上下文中被重复生成的问题；在搜索 query 生成、文案生成等对延迟敏感的业务中，可先按语义块划分再决定是否重新生成。

  - DiVR 与 SFT、RL 后训练兼容，可直接叠加在现有 diffusion/LLM 生成器上，适合作为推理时增强组件快速验证收益。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
扩散语言模型（MDLM）通过反复填充 mask 生成文本，理论上能重新生成并修正早期错误；但标准 decoding 不会回改已提交 token，常见 remasking 策略依赖调度、token confidence 或似然决定改哪里，没有学习预测最终答案是否正确。作者在 Sudoku 上诊断发现两个缺口：隐藏状态中含有错误信息但 token confidence 不可靠；孤立错误在周围上下文固定时 remask 往往会复现原错误。

### 方法
提出 DiVR，一个验证器（verifier），输入部分生成序列，预测其最终是否能到达正确答案。它用模型自身轨迹的最终正确性训练，生成器参数保持不变。推理时 DiVR 决定何时重新生成一个 block，以及在该 block 的两个候选中保留哪一个；相比逐 token 修错，块级重生成更稳定且成本可控。

### 结果
在 LLaDA-8B-Base 上，五个推理基准中，微调生成器的平均准确率从 35.3% 提升到 43.4%；额外成本仅为 greedy decoding 的 1.9–3.5×，优于使用 3.8–7.4× 成本的搜索基线。DiVR 还能与 SFT、RL 后训练叠加，并泛化到 Dream 等其他生成器。
