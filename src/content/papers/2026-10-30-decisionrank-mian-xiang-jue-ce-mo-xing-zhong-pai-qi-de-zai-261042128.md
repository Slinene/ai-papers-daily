---
title: 'DecisionRank: On-Policy Distillation for Decision-Model Rerankers'
title_zh: DecisionRank：面向决策模型重排器的在线策略蒸馏
authors:
- Yanran Wu
- Dian Yu
- Chongyang Bai
- Jieyi Zhang
- Rui Liu
- Tianyi Chen
- Shike Mei
- Hang Cui
- Frank Shyu
- Sandeep Pandey
affiliations:
- Meta
- Purdue University
arxiv_id: '2610.42128'
url: https://arxiv.org/abs/2610.42128
pdf_url: https://arxiv.org/pdf/2610.42128
published: '2026-10-30'
collected: '2026-11-02'
category: RecSys
direction: 决策重排模型蒸馏 · 单 token 排序
tags:
- decision model
- on-policy distillation
- reranking
- first-token ranking
- RankNet
- LLM distillation
one_liner: 用 item-space on-policy distillation 把生成式 LLM 排序偏好蒸馏到单 token 决策重排器，8B 超
  27B 教师且快 24.5 倍
practical_value: '- 如果线上重排为了低延迟采用单 token doc-id score，可以不必再靠离线静态 RankNet 蒸馏；把学生当前排序的
  top-K 作为 teacher-forced 前缀，在 item space 用 reverse KL 对齐 teacher 的条件 next-item 分布，训练与推理完全一致，且
  teacher 无需和学生共享词表或架构，适合接闭源/跨家族 LLM 教师。

  - 工程实现：每步用学生 first-token logits 排序取 top-20，一次性 teacher-forced forward pass 拿到 step
  2–19 的条件分布，再对剩余候选做 Plackett-Luce 归一化和 reverse KL；不需要自回归 rollout，稳定且省算力。联合离线 RankNet，λ=0.1，16k
  查询即可在多种 teacher/student 尺寸上稳定增益。

  - 对推荐/广告重排的负向结论也有用：AR SFT/AR OPD/Listwise GRPO 在单 token 打分器上不稳定，尤其会伤 general retrieval；因此如果目标是
  first-token 推理，不要套用生成式策略优化，应直接用 item-space conditional feedback。

  - 附带收益：该方法蒸馏出的 first-token scorer 在 TREC DL/BRIGHT 上 ECE 低于生成式教师，且无需标定专用目标；这对需要阈值截断/出价置信度校准的广告或推荐场景是可直接复用的性质。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
生成式 LLM 的 listwise 重排（如 RankGPT）效果好但自回归解码太慢；单 token 决策模型延迟低，但更难把教师的“顺序偏好”蒸馏进 first-token score。静态离线排序监督（offline RankNet）不能根据学生当前预测动态纠错，而标准 token-level on-policy distillation 依赖自回归 rollout，和 first-token 推理结构不一致。

## 方法关键点
- 学生用 query + 100 篇候选作为输入，取每篇文档对应单 token ID 的 first-token logit 作为分数，排序即最终排名。
- **Item-space On-Policy Distillation**：按学生当前分数排序得 top-K 排名，将该顺序作为 teacher-forced answer 前缀；teacher 一次前向给出每个 step 对剩余候选的条件选择分布；学生用同一组分数在剩余候选上做 Plackett-Luce 归一化，用 reverse KL 对齐 teacher。
- teacher 与学生通过候选 item ID 对齐，不要求共享词表或模型族；训练更新的是学生 first-token scores，与推理路径完全一致。
- 联合离线 RankNet：教师用 sliding window 生成全序，pairwise weighted RankNet 提供全局顺序；on-policy 项负责局部条件反馈。超参 K=20，监督 step 2–19，λ=0.1。

## 关键实验
- 数据：10k MS MARCO + 6k ReasonEmbed 查询；在 TREC DL、BEIR、BRIGHT、R2MED 上评估。
- 学生 Qwen3 1.7B/4B/8B，教师 Qwen3.8-27B；对比 pointwise/listwise 重排器。
- DecisionRank-8B 平均 nDCG@10 达 50.68，超过 DirectRank-8B 的 49.77；在 TREC DL 上 1.7B 学生（63.89）已超过 27B 生成式教师（62.97）。
- 8B 学生比 listwise DirectRank 快 24.5×（TREC DL）和 16.7×（BRIGHT），同时效果更好；并且跨 Gemma、Qwen、ReasonRank 三类教师均一致提升。
- 消融显示 item-space OPD 是唯一在四个 benchmark 上都稳定超过 RankNet 的目标；离线 + on-policy 互补。

## 值得记住的一句话
用学生当前排序作为 teacher-forced 前缀，在 item space 用 reverse KL 对齐条件 next-item 分布，让单 token score 直接吃生成式教师的顺序偏好，训练与推理完全一致。
