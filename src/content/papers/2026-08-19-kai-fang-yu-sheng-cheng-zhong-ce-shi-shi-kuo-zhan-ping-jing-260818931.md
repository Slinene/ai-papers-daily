---
title: 'Test-Time Scaling in the Wild: Why Exploitation, Not Exploration, Is the Bottleneck'
title_zh: 开放域生成中测试时扩展：瓶颈在利用而非探索
authors:
- Davide Romano
- Kanak Raj
- Jerrod Parker
- Daniele Giofrè
affiliations:
- Thomson Reuters
arxiv_id: '2608.18931'
url: https://arxiv.org/abs/2608.18931
pdf_url: https://arxiv.org/pdf/2608.18931
published: '2026-08-19'
collected: '2026-08-20'
category: Eval
direction: LLM 测试时扩展 · 开放域生成评估
tags:
- test-time scaling
- reward model
- open-ended generation
- headroom capture
- diversity collapse
- LLM-as-judge
one_liner: 五种TTS计算归一化对比：候选池不缺好答案，奖励模型相关性≈0.12，Fusion最佳仅捕获40% headroom
practical_value: '- 在电商/广告文案、商品标题、Agent 回复等开放域生成中，上线 Best-of-N + reward model 选优前，先在小样本测
  RM 分数与真实质量的 Spearman ρv；若低（如<0.2），额外采样基本是浪费，应直接放弃 RM 选择。

  - 优先把候选池做生成式合成（Fusion）而不是打分选优：同一候选池下，Fusion 的 headroom capture 约 40%，明显高于 BoN 的约
  15%，且不依赖外部 verifier，适合商品文案/卖点融合。

  - 不要把 PRM 引导的树搜索用于开放域文本生成；错误 PRM 会指数型剪掉好分支，导致多样性崩溃，并行采样更稳。

  - 迭代 refine 的收益要警惕长度偏置：写作/文案类 benchmark 的提升可能与“写得更长”混淆，迁移到广告或商品描述时用长度匹配评估，并监控 length-score
  相关。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
测试时扩展（TTS）在数学、代码上有效，但前提是答案可验证；开放域生成（医疗咨询、法律分析、金融、创意写作）没有单一正确答案，奖励模型是否可靠、TTS 哪一类策略有效，此前没有按计算量归一化的系统比较。

## 方法关键点
- 把固定 token 预算 T 拆成 exploration（生成候选）与 exploitation（选择/合成最终输出），定义 oracle quality Q*、realized quality Q、headroom capture h=(Q-μ)/(Q*-μ)。
- 对比五种 TTS 家族：Best-of-N + ORM、Beam Search、Particle Filter、Sequential Refinement、Fusion。
- 用 Qwen3.5-397B-A17B 做统一 judge，并在分层样本上与各 benchmark 原生 judge 做一致性校验。
- 提出偏差修正 oracle estimator，避免 judge 噪声下 max score 高估候选池质量。
- 理论推导 h_BoN≈ρv，即 BoN 的 headroom capture 等于外部 verifier 与真值的 Spearman 相关。

## 关键结果
- 在 HealthBench、PRBench、LEXam、WildBench、WritingBench 上，计算量提升 8×，Best-of-N 收益停滞；两个 ORM 的 ρv 平均仅 0.12，选择近似随机。
- 树搜索（Beam Search/Particle Filter）更差：PRM 引导导致多样性崩溃，Particle Filter 的 pair-wise cosine 距离只有 0.04-0.07，明显低于并行采样。
- Fusion 是唯一在 Qwen3.5 全 benchmark 上稳定提升的方法，但整体也仅捕获约 40% headroom；Sequential Refinement 只在 PRBench 真实增益，WritingBench 增益多由长度偏置解释。
- 候选池 oracle quality 随 compute 稳定上升，说明瓶颈不在候选生成，而在 exploitation。

最值得记住的一句话：候选池不是瓶颈——奖励模型相关性≈0.12，导致从好候选里挑/合成最终输出的利用环节塌掉。
