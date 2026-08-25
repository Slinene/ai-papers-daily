---
title: A Dual-Expert Strategy Integrating LLMs to Mitigate Negative Transfer in Cross-Domain
  Sequential Recommendation
title_zh: 缓解跨域序列推荐负迁移的双专家 LLM 策略
authors:
- Hyeongjun Yun
- Kihyuk Song
- Jaegul Choo
- Chung Park
affiliations:
- SK Telecom
- KAIST
arxiv_id: '2608.23131'
url: https://arxiv.org/abs/2608.23131
pdf_url: https://arxiv.org/pdf/2608.23131
published: '2026-08-24'
collected: '2026-08-25'
category: RecSys
direction: 跨域序列推荐 · 负迁移抑制
tags:
- Cross-Domain Sequential Recommendation
- LLMRec
- Negative Transfer
- Dual Experts
- Contrastive Learning
- Attention Mask
one_liner: 提出 DuELRec，用域门控双专家与双采样对比学习抑制 LLMRec 跨域负迁移
practical_value: '- 多域/多场景推荐若出现负迁移，可设计同域/跨域双专家结构，分别用同域因果 mask 和跨域因果 mask 建模，再通过逐 item
  门控融合；门控权重可视化能快速定位哪些域需要更强单域信号。

  - LLM 做序列推荐不要只做 token 级自回归，应在 LLM 输出后增加 item-aware attention transformation，把 subtoken
  聚合为 item 表示并在 item 级做 block causal mask，强制捕获协同信号，避免纯文本模式误导。

  - 负采样不要只用同域负样本，加入 30%-50% 跨域负样本（论文 p=0.4）可以增强跨域判别能力，改动小、收益稳定，适合电商跨品类召回或广告多场景排序。

  - ID-free 检索式 LLMRec 适合冷启动与新域扩展，但 warm item 通常弱于 IDRec；通过上述 item 级协同信号可同时提升 cold/warm，且无需为新
  item 重训。工程上可用冻结 LLM + LoRA + 两个浅层 transformer expert 控制延迟，线上预建 item embedding 索引做相似度检索。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
跨域序列推荐（CDSR）利用用户多域交互历史预测下一项。IDRec 冷启动差，LLMRec 可迁移但只建模 token 自回归，忽略 item 级协同信号，导致跨域负迁移——混合多域训练反而比单域训练更差；论文实验显示 LLMRec 的负迁移比 IDRec 更严重。

## 方法关键点
- **Domain-Gated Dual Experts**：在冻结 LLM backbone 上加两个 transformer experts。Item-aware attention transformation 将 subtoken 聚合为 item 表示，并用 block-level mask。Single-domain expert 只在同域 item 间做因果注意力；cross-domain expert 允许跨域因果注意力。Gating network 逐 item 加权融合两者，bias-variance 分解表明最优门控会偏向更可靠专家。
- **Dual-Sampling Token-to-Item Contrastive Learning**：token-to-item encoder 得到物品 embedding，用 pairwise ranking loss；负采样同时从同域和跨域 item pool 随机抽取（p=0.4），增强跨域判别。
- **辅助 instruction tuning**：用 LoRA 对 LLM 做推荐文本适配。
- **ID-free 检索式**：候选集相似度打分，避免生成式幻觉。

## 关键实验
在 Amazon 5 域和 Telco 5 域上对比 26 个 SOTA。Amazon HR@5 相对最佳 baseline 提升：Books +3.81%、Jewelry +20.6%、Outdoors +1.70%、Toys +10.8%；Telco 各域均有提升。负迁移分析显示其他 LLMRec 在多数域低于单域 SASRec，DuELRec 在所有域缓解负迁移，且在冷启动/warm item 均优于 IDRec。消融证明双专家与跨域负采样至关重要。线上部署于电信助手 App，14 域、约 5M 用户，CTR 从 0.90% 提升到 1.33%，相对提升 47.6%。训练比 SyNCRec 慢 1.67x，但无需新 item 重训，推理快于 RecFormer 3.19x。

## 最值得记住的一句话
用单域专家提供无偏信号、跨域专家提供迁移信号，通过逐 item 门控按 bias-variance 自适应抑制跨域噪声，是 LLMRec 缓解负迁移的有效范式。
