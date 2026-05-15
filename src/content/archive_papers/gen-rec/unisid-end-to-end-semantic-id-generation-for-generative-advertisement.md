---
title: 'UniSID: End-to-End Semantic ID Generation for Generative Advertisement Recommendation'
authors: Jie Jiang et al. (11 人)
affiliation: Tencent × 武汉大学
date: 2026-02
venue: arXiv
topic: gen-rec
topic_name: 生成式推荐
topic_icon: 🎯
idea: 把 Semantic ID 构造从 "先学 embedding 再 RQ 量化" 的两阶段范式改造成端到端联合优化：Embedding 与 SID 共同从原始广告数据训练，避免两阶段语义损失与
  RQ 的层间误差累积。配合多粒度对比学习 + summary-based 重建，Hit Rate 提升最高 4.62%、Recall 最高 45.46%。
paperUrl: https://arxiv.org/abs/2602.10445
tags:
- Semantic ID
- Generative Recommendation
- End-to-End
- Contrastive Learning
unverified: false
detail:
  contribution: 首次把 Semantic ID 生成做成端到端联合训练框架 UniSID，跳过 "embedding 学习 → RQ 量化" 的两阶段瀑布；并行预测各层
    SID 替代残差链式预测，从根本上避免 RQ 的层间误差累积；为生成式广告推荐贡献了一套可直接接入推荐主目标的 SID 构造范式。
  background: 生成式推荐近年成为主流方向：把 item 表示成离散 Semantic ID (SID) 序列，让 LLM 风格的生成模型来 "生成下一个
    item"。但 SID 怎么造一直被 RQ-VAE 路线主导——先训一个 item embedding，再用 Residual Quantization 多层离散化。两大痛点：(1)
    **目标错配**：embedding 训练目标（重建/对比）≠ 下游推荐目标，量化后语义打折扣；(2) **误差累积**：RQ 第 k 层预测的是前 k-1
    层的残差，前层错一点后层就指数发散。UniSID 的工程动机是腾讯广告系统真实落地，要求 SID 必须直接对 ad ranking / retrieval
    有效。
  method: '**(1) Ad-enhanced 输入 schema**：把异构广告信号（任务指令、图、文本、结构化属性）线性化拼成统一 token 序列，绕过
    pretrained embedding 瓶颈，让原始语义直接流入 SID 学习。**(2) 并行多层 SID 预测（替代 RQ 残差链）**：所有 SID
    层都从同一份完整广告上下文预测，不再依赖前层残差，从结构上切断误差累积链。**(3) 多粒度对比学习**：在不同 SID 粒度上构造 positive pair，强制粒度对齐——确保
    coarse SID 抓共性、fine SID 抓差异。**(4) Summary-based ad reconstruction**：用 SID 重建广告的
    high-level summary（而非原始字段），迫使 SID 编码高阶语义而不是表层 token。**(5) 三损失联合优化**：multi-granularity
    SID 对比损失 + embedding 对比损失 + summary 重建损失，端到端一起回传。'
  experiments: 在腾讯广告下游场景报告：next-ad prediction **Hit Rate +4.62%**、ad retrieval **Recall
    +45.46%**、next-item prediction **Recall +11.83%**，相对最强 RQ-VAE 类 baseline 一致领先。多个下游任务上做
    ablation 验证三个损失模块各自贡献。
  pros: 把生成式推荐里 "两阶段 SID" 的根本性目标错配问题正面解决，工程上证明 SID 与推荐目标可以共同优化；并行多层预测的设计简单优雅、直接解决
    RQ 误差累积；三损失协同设计与广告语义结构紧贴；腾讯实际广告系统落地经验，数字有说服力。
  cons: 端到端训练对算力 / 数据规模要求更高，小厂复现门槛上升；目前主要在广告域验证，跨场景（短视频 / 电商）泛化结论待补；并行多层预测虽避免误差累积，但层间一致性约束变弱，可能引入新的耦合问题；论文未开源代码。
  inspiration: 把 "先 embedding 再 SID" 的解耦观从根上重新审视——SID 应该是推荐目标导向的可学表示，而不是 embedding
    的事后产物；后续工作可探讨 (a) 端到端 SID 与生成式 ranker 的联合训练、(b) 多模态信号在 SID 层的细粒度对齐、(c) 跨域 SID
    的迁移与统一。
  takeaway: 腾讯把生成式推荐 SID 构造从两阶段范式推进到端到端的代表工作。
---

把 Semantic ID 构造从 "先学 embedding 再 RQ 量化" 的两阶段范式改造成端到端联合优化：Embedding 与 SID 共同从原始广告数据训练，避免两阶段语义损失与 RQ 的层间误差累积。配合多粒度对比学习 + summary-based 重建，Hit Rate 提升最高 4.62%、Recall 最高 45.46%。

## 核心贡献

首次把 Semantic ID 生成做成端到端联合训练框架 UniSID，跳过 "embedding 学习 → RQ 量化" 的两阶段瀑布；并行预测各层 SID 替代残差链式预测，从根本上避免 RQ 的层间误差累积；为生成式广告推荐贡献了一套可直接接入推荐主目标的 SID 构造范式。

## 背景

生成式推荐近年成为主流方向：把 item 表示成离散 Semantic ID (SID) 序列，让 LLM 风格的生成模型来 "生成下一个 item"。但 SID 怎么造一直被 RQ-VAE 路线主导——先训一个 item embedding，再用 Residual Quantization 多层离散化。两大痛点：(1) **目标错配**：embedding 训练目标（重建/对比）≠ 下游推荐目标，量化后语义打折扣；(2) **误差累积**：RQ 第 k 层预测的是前 k-1 层的残差，前层错一点后层就指数发散。UniSID 的工程动机是腾讯广告系统真实落地，要求 SID 必须直接对 ad ranking / retrieval 有效。

## 方法

**(1) Ad-enhanced 输入 schema**：把异构广告信号（任务指令、图、文本、结构化属性）线性化拼成统一 token 序列，绕过 pretrained embedding 瓶颈，让原始语义直接流入 SID 学习。**(2) 并行多层 SID 预测（替代 RQ 残差链）**：所有 SID 层都从同一份完整广告上下文预测，不再依赖前层残差，从结构上切断误差累积链。**(3) 多粒度对比学习**：在不同 SID 粒度上构造 positive pair，强制粒度对齐——确保 coarse SID 抓共性、fine SID 抓差异。**(4) Summary-based ad reconstruction**：用 SID 重建广告的 high-level summary（而非原始字段），迫使 SID 编码高阶语义而不是表层 token。**(5) 三损失联合优化**：multi-granularity SID 对比损失 + embedding 对比损失 + summary 重建损失，端到端一起回传。

## 实验结果

在腾讯广告下游场景报告：next-ad prediction **Hit Rate +4.62%**、ad retrieval **Recall +45.46%**、next-item prediction **Recall +11.83%**，相对最强 RQ-VAE 类 baseline 一致领先。多个下游任务上做 ablation 验证三个损失模块各自贡献。

## 优点

把生成式推荐里 "两阶段 SID" 的根本性目标错配问题正面解决，工程上证明 SID 与推荐目标可以共同优化；并行多层预测的设计简单优雅、直接解决 RQ 误差累积；三损失协同设计与广告语义结构紧贴；腾讯实际广告系统落地经验，数字有说服力。

## 局限

端到端训练对算力 / 数据规模要求更高，小厂复现门槛上升；目前主要在广告域验证，跨场景（短视频 / 电商）泛化结论待补；并行多层预测虽避免误差累积，但层间一致性约束变弱，可能引入新的耦合问题；论文未开源代码。

## 对后续工作的启发

把 "先 embedding 再 SID" 的解耦观从根上重新审视——SID 应该是推荐目标导向的可学表示，而不是 embedding 的事后产物；后续工作可探讨 (a) 端到端 SID 与生成式 ranker 的联合训练、(b) 多模态信号在 SID 层的细粒度对齐、(c) 跨域 SID 的迁移与统一。

## 一句话总结

腾讯把生成式推荐 SID 构造从两阶段范式推进到端到端的代表工作。
