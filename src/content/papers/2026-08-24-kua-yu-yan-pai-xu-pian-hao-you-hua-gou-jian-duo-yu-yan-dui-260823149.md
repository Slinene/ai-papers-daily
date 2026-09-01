---
title: 'Language Chain in Alignment: Cross-lingual Ranking Preference Optimization'
title_zh: 跨语言排序偏好优化：构建多语言对齐的层级 ranking 框架
authors:
- Seungyoon Lee
- Minhyuk Kim
- Jungseob Lee
- Heuiseok Lim
affiliations:
- Korea University
arxiv_id: '2608.23149'
url: https://arxiv.org/abs/2608.23149
pdf_url: https://arxiv.org/pdf/2608.23149
published: '2026-08-24'
collected: '2026-09-01'
category: Training
direction: 跨语言 LLM 偏好对齐 · Learning-to-Rank
tags:
- Cross-lingual Alignment
- Preference Optimization
- Learning-to-Rank
- LambdaLoss
- Multilingual LLM
- DPO
one_liner: 将 Learning-to-Rank 引入跨语言偏好对齐，利用英语偏好知识提升目标语言一致性与质量
practical_value: '- 在多语言推荐/Agent 回复场景，可用英语高质量偏好数据构建跨语言排序对，通过层级偏好（目标语言正确语言 > 英语正确内容
  > 目标语言错误语言）同时约束语言一致性和内容质量，减少语言混淆。

  - 将 DPO 的 pairwise 比较升级为 listwise ranking，利用 LambdaLoss 权重（如 nDCG2）对多个候选响应进行全局排序，能更精细地优化目标，例如在生成式推荐中同时对相关性、多样性、语言等维度排序。

  - 在偏好优化损失中加入 NLL 项（如 α=0.2）可防止模型只增大 reward margin 而抑制被拒样本概率，避免生成退化，对业务中 LLM 微调有价值。

  - 低资源语言/场景下，跨语言 ranking 比单纯 binary 对比更稳健，可借鉴到冷启动物品推荐或小语种文案生成，利用高资源语言偏好知识迁移。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
LLM 对齐高度依赖英语偏好数据，导致其他语言响应出现语言不一致、质量低下等问题。现有方法要么依赖昂贵人工标注，要么简单混合多语言数据，无法充分利用模型内部的英语偏好知识，难以实现有效的跨语言对齐。

## 方法关键点
- **层级偏好构建**：为每个 prompt 构造四元组（目标语言 chosen/rejected、英语 chosen/rejected），定义偏好层级：目标语言 chosen > 英语 chosen > 目标语言 rejected > 英语 rejected，将语言一致性与质量统一到一个排序结构中。
- **LambdaLoss 排序目标**：将 DPO 的二元比较扩展为 listwise ranking，对所有 pairwise 的组合优化隐含奖励差距，采用 nDCG 权重惩罚排序错误，使模型能够同时学习跨语言和语言内偏好。
- **联合 NLL 损失**：在 ranking loss 之外加入目标语言 chosen 响应的 NLL 项（α=0.2），防止模型只增大 margin 而抑制 rejected 概率，保持生成流畅性。
- **多种权重方案**：支持 LambdaRank、nDCG2、nDCG2++，验证框架的鲁棒性。

## 关键结果
- 在 Llama-2-7B、Llama-3-8B、Mistral-7B 上，5 种语言（中、印尼、韩、斯瓦希里、孟加拉）的 AlpacaEval 均超越 SFT+DPO 和 CLO；低资源语言如斯瓦希里语 Llama-3 WR 达 62.17。
- 知识任务 MMMLU 和 Belebele 也获得提升，印尼语 MMMLU 提升 4 分以上，韩语 Belebele 达 68.66。
- 内部奖励与 log-likelihood 分析显示，CRPO 同时增大 chosen 概率与 reward margin，而其他方法主要靠抑制 rejected。
- 外部奖励模型评估显示 CRPO 生成质量更高，如 Mistral 印尼语从 -0.037 提升到 0.805。

**最值得记住的一句话**：用英语偏好作为逻辑锚点，把跨语言对齐转化为 listwise ranking，同时优化语言一致性与生成质量。
