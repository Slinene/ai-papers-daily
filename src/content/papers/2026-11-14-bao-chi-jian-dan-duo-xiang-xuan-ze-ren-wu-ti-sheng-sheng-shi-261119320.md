---
title: Keep it Simple! A Multiple-Choice Task can Benefit Generative Recommendation
title_zh: 保持简单：多项选择任务提升生成式推荐
authors:
- Wei-Hsiang Huang
- Jyun-Yu Jiang
- Pu-Jen Cheng
affiliations:
- National Taiwan University
- Coupang
arxiv_id: '2611.19320'
url: https://arxiv.org/abs/2611.19320
pdf_url: https://arxiv.org/pdf/2611.19320
published: '2026-11-14'
collected: '2026-11-17'
category: GenRec
direction: 生成式推荐 · Semantic ID · 辅助任务
tags:
- Generative Recommendation
- Semantic ID
- Multiple-Choice
- Auxiliary Task
- Sequential Recommendation
one_liner: 给生成式推荐加一个多项选择辅助任务，显式构造正负候选集，NDCG@10 最高提升 79%
practical_value: '- 在现有 SID 生成式推荐（如 TIGER）上，可以直接加一个多项选择辅助任务：每个训练样本把 ground-truth item
  与 n_c-1 个均匀采样的负样本拼成候选集，再用 task token 区分主/辅任务；损失取 L_main + L_aux，工程成本极低，不需要预训练 LLM。

  - 候选集大小建议 n_c=2~10；n_c=10 在稀疏场景（Scientific/Yelp）提升最明显，稠密场景（MovieLens）提升较小。过大会引入
  false negative 并饱和。

  - 训练时主任务与辅助任务比例保持约 1:1 较稳，不要过度偏向主任务；负采样用 uniform 即可，long-tail/warm-set/dynamic 策略没有显著额外收益。

  - 辅助任务使 decoder 在后期 cross-attention 更关注候选 item，能缓解仅靠语义相似推荐的问题，有助于理解用户高层意图；在排序/召回模型显式加入对比信号是低成本涨点思路。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**

生成式推荐通常用 SID 自回归生成下一个 item，但训练只优化 ground-truth 的 NLL，缺少负样本和相对排序信号。这与 BPR 重视正负相对排名的思想不一致；同时，SID 训练分布稀疏，许多 item 组合没见过，OOD 组合泛化差。

**方法关键点**

- 在 TIGER 的 seq2seq 生成式推荐框架上，增加一个多项选择辅助任务：把正例 item 与 n_c-1 个均匀采样的负例构成候选集，随机打乱后拼在历史序列后方。
- 引入三个可学习 token：p1 表示主任务，p2 表示辅助任务，p3 分隔历史和候选集；类似 prefix tuning，不依赖预训练 LLM。
- 辅助任务仍生成正例 SID，训练目标为 L = L_main + L_aux；共享表示函数，减少目标冲突。
- 信息论角度：辅助任务隐式最大化 I(G; I+|C) 并抑制 I(G; I-|C)，使表示更鲁棒；候选集作为输入促进组合泛化。

**关键结果**

在 Scientific、Instruments、Yelp、MovieLens 1M 四个数据集上，以 TIGER 为基础，TIGER+nc=10 相比 TIGER 的 NDCG@10 分别提升 10.3%、10.2%、79.0%、4.9%，且 p<0.05。稀疏场景提升尤其明显。分析显示：模型在辅助任务中几乎 100% 能从候选集中选出正确项；decoder 在后期 cross-attention 更关注候选 item；不同负采样策略与动态调度相比 uniform 无显著额外收益。

**最值得记住的一句话**

生成式推荐不要只做 next-item NLL 生成，加一个显式对比正负样本的多项选择辅助任务，就能以极低成本显著提升效果，尤其在稀疏数据上。
