---
title: Token-Level Advertising
title_zh: Token 级广告：生成式原生广告的潜在广告主混合拍卖机制
authors:
- Hanbing Liu
- Bowei Zhang
- Changyuan Yu
- Yinyu Ye
- Qi Qi
affiliations:
- Renmin University of China
- Baidu Inc.
- Stanford University
arxiv_id: '2608.27382'
url: https://arxiv.org/abs/2608.27382
pdf_url: https://arxiv.org/pdf/2608.27382
published: '2026-08-27'
collected: '2026-08-28'
category: Other
direction: 生成式广告 · token级拍卖机制
tags:
- mechanism design
- token-level advertising
- LLM auction
- DSIC
- KL-regularized welfare
- generation-native advertising
one_liner: 提出 LAMA 将广告主影响直接嵌入 token 级生成过程，满足 Markov DSIC/IR 且近最优 KL 正则化福利
practical_value: '- 把广告分配从固定 slot 迁移到 token 级生成轨迹：每次生成一个 token 都更新广告主后验，最终按后验采样赢家，适合对话式推荐、AI
  搜索摘要中的品牌植入；可用温度 β 显式控制商业化侵入度，与用户自然性平衡。

  - 报告由平台代理的工程方案很实用：共享 advertiser-conditioned LoRA 模型输出 advertiser-specific policy，一个
  value head 锚定 root value，通过 Bradley-Terry 目标学习 local advantages；部署时只对检索后的小候选集做常数额外
  forward，可降低多广告主生成式推荐的服务成本。

  - 支付设计中的 Bellman consistency 消息空间可在线上验证报告一致性，随机 settlement 只对赢家收费，实现 outcome IR
  和期望弱预算平衡，减少广告主对“参与即收费”的障碍，适合生成式广告冷启动。

  - 评估指标同时覆盖 welfare/revenue/value/quality 四个维度，尤其将 GEM-Bench 用户质量独立于 KL 惩罚，对生成式广告上线监控有直接参考价值。'
score: 10
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
生成式 AI 让内容由模型动态生成，传统预定义 slot 的广告分配抽象失效：广告机会在生成过程中才浮现，早期 token 选择影响后续品牌植入是否自然。机制设计需要把广告主影响直接嵌入生成过程，同时保证激励相容、平台收益与用户体验平衡。

## 方法关键点
- **LAMA 机制**：广告主在每个 prefix 提交局部 continuation value 报告，诱导 advertiser-specific next-token policy；平台通过 latent mixture 先采样 latent advertiser，再按该广告主策略采样 token，并用贝叶斯后验更新 allocation posterior。
- **支付与约束**：支付包含 entry fee 和沿路径的 posterior-weighted continuation value 变化；消息空间要求 Bellman consistency，在线只需存储标量并校验 soft Bellman 递归。证明满足 Markov DSIC 和 IR，KL-regularized welfare gap ≤ β log|N|，β→0 时趋近最优。
- **实践实现**：广告主无需自己计算报告，平台用共享 advertiser-conditioned LoRA 模型学习 local soft advantages 和 root value，通过 Bradley-Terry 目标从 pairwise 偏好中恢复 soft advantage，root value 由残差平均锚定；部署时仅增加常数 LM forward passes，支持小候选集实时服务。

## 关键结果
在 Webis Generated Native Ads 2024 的三个真实商业搜索 query 垂直（Workout/Vacation/Car）上，对比 allocate-before/after generation、response-level aggregation (MOSAIC) 等 baseline。LAMA 取得平均平台 welfare 0.5205、revenue 0.8305、advertiser value 0.8568、GEM-Bench user quality 66.5239，全面超过 baseline，尤其 revenue 比 allocate-after policy 高约 0.08，同时用户质量持平。

## 最值得记住的一句话
广告机会不是 slot，而是 token 级生成轨迹的一部分；机制设计可以同时塑造内容和分配广告。
