---
title: Discrete Diffusion Inference-Time Control with Nested Sequential Monte Carlo
title_zh: 离散扩散推理时控制的嵌套序贯蒙特卡洛方法
authors:
- Lohithsai Yadala Chanchu
- Hany Abdulsamad
- Christian A. Naesseth
affiliations:
- University of Amsterdam
arxiv_id: '2608.20123'
url: https://arxiv.org/abs/2608.20123
pdf_url: https://arxiv.org/pdf/2608.20123
published: '2026-08-20'
collected: '2026-08-23'
category: LLM
direction: 离散扩散文本生成推理时控制
tags:
- Discrete Diffusion
- Sequential Monte Carlo
- Inference-Time Control
- Text Generation
- NSMC
- Alignment
one_liner: 提出 NSMC 与 FA-NSMC 用于离散扩散文本生成推理时奖励引导，修正偏差并优于 best-of-n 与 bootstrap SMC
practical_value: '- 若在电商/广告文案、搜索词生成中采用离散扩散语言模型（DDLM），可替换 best-of-n 为 NSMC：best-of-n
  易高估 reward，bootstrap SMC 有权重退化，NSMC 能更稳定地按序列级 reward（如点击率、合规性、品牌语调）做推理时引导，无需额外训练。

  - FA-NSMC 通过 fully adapted proposal 融入 reward 信息，能提高采样效率；在生成式推荐场景中，若 reward 模型计算昂贵（如
  LLM judge 打分），可优先考虑 FA-NSMC 减少粒子数。

  - 论文修正了 Feynman-Kac 控制中嵌套 SMC 的 bias 问题：实际工程中若自己实现 SMC 控制，需注意 final estimate 的无偏/有偏处理，避免离线评估指标系统性偏乐观。

  - 该方法适用于任意序列级可微/不可微 reward，可作为生成式排序、push 文案、query 推荐的在线后处理层，但需权衡每 token 的 SMC 递归开销。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：离散扩散语言模型（DDLM）生成文本可双向建模，但不天然对齐安全或奖励目标；推理时控制可避免重训练。现有粒子方法 best-of-n 有 overoptimism，bootstrap SMC 有 weight degeneracy。

**方法关键点**：提出嵌套序贯蒙特卡洛（NSMC）和 fully-adapted NSMC（FA-NSMC），用于 Feynman-Kac 控制下的 DDLM 采样。NSMC 通过嵌套粒子系统估计 conditional expectation，缓解权重退化；FA-NSMC 进一步把 reward 信息引入 proposal 分布，提高效率。论文修正了先前 NSMC 公式中的错误，避免最终估计偏差。

**关键结果**：在 toxicity 控制和 fluency 控制任务上，NSMC 与 FA-NSMC 一致优于 best-of-n 和 bootstrap SMC，能用更少采样获得更好的 reward-quality trade-off。
