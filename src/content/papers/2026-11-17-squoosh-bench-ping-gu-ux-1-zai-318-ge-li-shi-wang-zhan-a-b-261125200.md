---
title: 'Squoosh Bench: Evaluating UX-1 on 318 Historical Website A/B Tests'
title_zh: Squoosh Bench：评估 UX-1 在 318 个历史网站 A/B 测试上的表现
authors:
- Rohith Pasula
- Johari Dramiga
- Viraj Shah
- Suzan Halim
- Tyler Dooskin
affiliations:
- Squoosh AI
arxiv_id: '2611.25200'
url: https://arxiv.org/abs/2611.25200
pdf_url: https://arxiv.org/pdf/2611.25200
published: '2026-11-17'
collected: '2026-11-22'
category: Eval
direction: 模拟购物者 A/B 测试结果评估
tags:
- A-B Testing
- Simulated Users
- LLM Evaluation
- E-commerce
- Behavior Modeling
one_liner: 模拟购物者模型 UX-1 在 318 个历史 A/B 测试中预测结果准确率 84%，远超通用 LLM，可辅助实验优先级决策
practical_value: '- 在电商/推荐业务中，可训练用户行为模拟模型（如基于浏览序列 fine-tune 的 UX-1）对 UI 变更、排序调整等 A/B
  测试候选进行离线预筛，优先测试预测胜率高的变体，节省真实流量成本。

  - 论文显示 UX-1 预测为 variant win 的 126 个实验中 93.7% 实际获胜，说明高置信预测可大幅缩小测试候选集（从 318 缩至 126）同时覆盖
  86.1% 的赢家；但仍有 19 个赢家被漏掉，因此对预测 inconclusive 或低置信的候选不应直接丢弃，可保留小流量验证。

  - 评估方法上，页面角色掩码和结果屏蔽有效避免信息泄漏，类似离线评估推荐系统时应严格隔离用户行为与测试结果，防止未来信息泄漏。

  - UX-1 基于人类浏览数据 fine-tune 而非仅依赖通用 LLM，表明用户行为序列建模对预测真实用户反应至关重要，业务中可考虑把用户行为 embedding
  与 LLM 结合提升模拟保真度。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：实验团队必须决定哪些网站变更值得用真实流量测试。测试弱变体会浪费流量，而丢弃潜在好变体会错失收益。为此评估是否能用模拟购物者的预测来辅助决策。

**方法**：构建 Squoosh Bench，筛选 412 个历史网站 A/B 测试，排除运行≤21天的 94 个，保留 318 个。每个系统需预测 original win / variant win / inconclusive。页面角色被掩码，真实结果在推理时隐藏。Squoosh UX-1 是在人类浏览数据上微调的模型，为每个实验臂模拟 1000 个购物者并预测结果；同时对比了 Qwen3 Next 80B 等通用模型配置。

**结果**：UX-1 正确分类 267/318（84.0%，95% Wilson 区间 79.5-87.6%），显著高于 Qwen3 Next 80B 的 196/318（61.6%）。UX-1 在 126 个实验中偏向 variant，其中 118 个实际获胜（93.7%），4 个失败，4 个无结论；剩余 192 个实验中有 19 个额外 variant win。UX-1 的短名单覆盖了 137 个真实赢家中的 118 个（86.1%），但漏掉的 19 个赢家表明不能仅凭预测淘汰候选。
