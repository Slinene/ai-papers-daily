---
title: 'Ask to Be Sure: Informative Interactions for Confident Multi-Turn LLM Recommendation'
title_zh: 以问求证：基于熵减奖励的多轮 LLM 对话推荐
authors:
- Cedar Site Bai
- Duanshun Li
- Zhenyu Liao
- Sheikh Sarwar
- Huiyuan Chen
- Yuan Chen
- Changhe Yuan
- Haiyang Zhang
- Qilin Qi
affiliations:
- Amazon
arxiv_id: '2608.15949'
url: https://arxiv.org/abs/2608.15949
pdf_url: https://arxiv.org/pdf/2608.15949
published: '2026-08-16'
collected: '2026-08-18'
category: GenRec
direction: 生成式对话推荐 · 熵减奖励
tags:
- Conversational Recommendation
- LLM
- Entropy Reduction
- DPO
- Uncertainty Estimation
- Multi-turn Dialogue
one_liner: 用推荐熵减作为多轮交互奖励，无需 ground truth 即可训练更高效的对话推荐 LLM
practical_value: '- 可以把“采样推荐列表的加权熵”作为在线 Agent 的不确定性信号：每次用户回复后采样 top-k 商品列表，计算熵减，作为无监督
  reward 或筛选样本，用于训练导购/客服 Agent，避免人工标注交互好坏。

  - DPO 偏好对可由熵减重打标签，替换 CollabLLM 里 LLM-judge 的 interactivity 分数；工程上只需在原有生成流程中加一个采样和熵计算模块，成本低，且更贴合推荐目标。

  - 加权熵公式中 rank j 权重为 1/log2(j+1)，可借鉴到推荐列表评估：强调 top 位置的一致性，避免长尾商品波动干扰不确定性估计。

  - 评估时除了 Hit@k，还应关注达到目标商品所需轮次；电商多轮导购中可把“轮次效率”作为核心指标，与转化率一起优化交互策略。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
LLM 进入对话推荐后，如何设计多轮交互以有效获取用户偏好仍是难点。已有方法要么训练分离的 RL agent，把交互限制在选择题或 Yes/No 格式；要么像 CollabLLM 用 LLM-judge 奖励 interactivity，但没有度量实际获得了多少推荐相关的信息。本文从推荐不确定性出发，将一次交互的有效性定义为推荐熵的降低，用来奖励 LLM 生成更有信息量的提问。

**方法关键点**
- 对同一对话状态重复采样 top-m 推荐列表，统计 item 经验分布，计算 Shannon 熵；并用权重 1/log2(j+1) 对第 j 位加权，突出靠前推荐的一致性。
- 定义 turn-level 熵减（assistant turn + user response 前后的熵差）和 conversation-level 熵减（从该 turn 展开到对话结束的总熵差），作为无需 ground-truth 的奖励。
- 将该奖励用于 SFT 样本筛选和 DPO 偏好对重打标签；数据由 Claude Sonnet 4 模拟用户基于 INSPIRED/ReDial 参考对话生成，模型用 Llama-3.2-1B-Instruct LoRA 微调。

**关键实验**
在 INSPIRED 和 ReDial 上，对比 Vanilla、SFT(Raw)、SFT/DPO(CollabLLM)。INSPIRED 上 DPO(Turn Entropy) 的 Hit@1/Hit@5/模拟对话命中分别为 3.32%/5.21%/27.94%，优于 CollabLLM 的 3.15%/5.09%/26.60%。ReDial 上 DPO(Conv Entropy) 模拟对话命中达 32.83%，且轮次最低 2.74。结果表明，熵减奖励在无 ground-truth 情况下比 CollabLLM 的 ground-truth hit + LLM-judge interactivity 奖励更有效，同时提升推荐质量和对话效率。

**最值得记住的一句话**
用“推荐熵减”作为多轮交互的信息增益信号，直接对齐推荐不确定性，比主观判断交互性更可落地且无需 ground-truth 推荐。
