---
title: Latent Residual Reasoning for Ranking in Generative Recommendation
title_zh: 生成式推荐排序中的隐式残差推理
authors:
- Haihan Shi
- Ruidong Han
- Wenjie Wang
- Shangyu Chen
- Sunhao Dai
- Yongqi Li
- Yangyang Li
- Fei Jiang
- Wei Lin
- Fuli Feng
affiliations:
- University of Science and Technology of China
- Meituan
- Renmin University of China
- The Hong Kong Polytechnic University
- Academy of Cyber
arxiv_id: '2610.36890'
url: https://arxiv.org/abs/2610.36890
pdf_url: https://arxiv.org/pdf/2610.36890
published: '2026-10-27'
collected: '2026-10-28'
category: GenRec
direction: 生成式推荐 · 隐式残差推理排序
tags:
- Generative Recommendation
- Latent Reasoning
- LoRA
- Ranking
- CTR Prediction
- Industrial Recommendation
one_liner: 提出 Refiner 框架，用残差分数修正、历史查询和 LoRA 适配，在不重训基座的前提下增强生成式排序
practical_value: '- 工程架构：对已部署排序模型做推理增强，不需要全量重训。冻结 base model，只加 LoRA 到 Transformer
  和一个独立 reasoning prediction head；日级更新时加载最新 base checkpoint，同时继承上一日 Refiner 参数，只更新新增参数，适合渐进上线。

  - 输入与 mask 设计：每个候选分配独立 reasoning token，autoregressive 地从上一轮 hidden state 提取；history
  queries 从用户行为序列尾部取 2-4 个位置作为全局上下文。候选 mask 必须保持候选间隔离，只允许访问自己的前序 reasoning token。

  - 训练目标：残差修正 + MSE 监督累计分数，比每步用 BCE 重新预测完整分数更有效；推理步数 1-2 步性价比最高，更多步边际收益快速衰减。

  - 业务收益：工业 A/B 在 PV-CTR +0.75%、GMV +0.46%，且对长历史用户、冷启动/低频 item 增益更明显；有类似困难样本的业务可优先尝试。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
生成式推荐排序模型通常一次前向直接产出候选分数，效率高但缺少面向细粒度排序的多步细化能力。LLM 的显式 CoT 不适用于广泛部署的非文本 ID 推荐模型；隐式推理在连续隐空间中有潜力，但如何与 ranking objective 对齐、如何同时处理多个候选、以及如何不重训已部署模型，仍缺少成熟方案。

## 方法关键点
- **残差推理机制**：每一步不重新预测完整分数，而是预测 additive correction；累计分数 = base score + 每步残差，并用 MSE 监督累计分数与真实标签。
- **输入构造**：为每个候选分配独立 reasoning token，从上一步 hidden state 的候选位置 autoregressive 提取；引入 history queries 从用户行为序列尾部提取压缩表示，提供全局用户上下文。
- **mask 设计**：保持候选间隔离，reasoning token 只能访问自身候选、同候选前序 reasoning token、以及所有用户侧信息，防止信息泄漏。
- **参数高效微调**：冻结预训练 base model，仅增加 LoRA 模块和独立 reasoning prediction layer；推理前先用 freeze 的 base model 得到 S0 和 hidden states。

## 关键结果
- 公开数据集 Steam 和 MovieLens10M 上，MTGR+Refiner 相比 MTGR：Steam AUC 0.7872 vs 0.7698（+2.3%），GAUC 0.7594 vs 0.7397（+2.7%）；MovieLens AUC 0.7864 vs 0.7674（+2.5%），GAUC 0.7043 vs 0.6755（+4.3%）。
- 工业离线数据：CTR GAUC +1.6‰，CTR AUC +1.8‰；CTCVR AUC +2.5‰，CTCVR GAUC +2.1‰，且统计显著。
- 在线 A/B：PV-CTR +0.75%，UV-CTCVR +0.21%，GMV +0.46%。
- 消融和超参分析：移除 history queries 或残差监督都会掉点，End-to-End 全量微调最差；N_HQ=2/4 最优；推理步数 1-2 步足够，后续残差幅度快速衰减。

## 最值得记住的一句话
用残差分数修正而不是每步重新预测，配合候选隔离的 latent reasoning token、少量 history queries 和冻结 backbone 的 LoRA 适配，是低成本把推理能力叠加到工业排序模型上的有效方式。
