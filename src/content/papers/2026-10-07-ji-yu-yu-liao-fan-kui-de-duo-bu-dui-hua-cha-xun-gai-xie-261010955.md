---
title: Learning Multi-Step Query Rewriting via Corpus Feedback for Conversational
  Search
title_zh: 基于语料反馈的多步对话查询改写
authors:
- João Coelho
- Hong Wang
- Jie Yuan
- Zhuoer Wang
- Samson Koelle
- Wei Niu
affiliations:
- INESC-ID
- Carnegie Mellon University
- Amazon
arxiv_id: '2610.10955'
url: https://arxiv.org/abs/2610.10955
pdf_url: https://arxiv.org/pdf/2610.10955
published: '2026-10-07'
collected: '2026-10-09'
category: QueryRec
direction: 对话查询改写 · 检索反馈
tags:
- Conversational Search
- Query Rewriting
- Reinforcement Learning
- Pseudo-Relevance Feedback
- LLM Agent
- GRPO
one_liner: 将对话查询改写重构为多步检索过程，Agent 通过检索反馈依次执行意图消解、词汇改写和伪文档生成，仅用检索奖励训练即超过单步改写基线
practical_value: '- 把 query 改写/扩写从单步改为多步，动作类型化为 intent、rephrase、HyDE、stop，并让后续动作显式看到前一步
  top-k 结果。可直接套在电商搜索的 query 改写、广告选词、push 文案生成，尤其适合需要反复试探语料分布的召回场景。

  - 不需要人工 rewrite 标注，仅用检索指标（如 rank-based reward、nDCG）做强化学习，就能让策略自动学会“先消歧、再词汇对齐、最后做伪文档匹配”的步骤顺序；可以降低标注成本，并更容易与已有召回器对齐。

  - 伪文档动作不是简单复制检索结果，而是吸收已检索 passage 的词表；8-gram 复制检测和 unigram Jaccard 可用于线上安全/去重审计。推理成本要按场景估算，设置
  max steps 和早停可控制 token 开销。

  - 在 BM25 上训练的改写策略可零样本迁移到 dense retriever（尤其强的 embedding model），意味着可以用廉价稀疏检索离线训练、线上换更强的向量召回，或反向验证鲁棒性。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
对话式搜索中，用户的当前 query 往往依赖历史轮次中的实体和话题，例如“它什么时候发布的”。主流对话查询改写（CQR）方法通常只做单步改写，且不观察检索结果，导致改写无法根据目标语料的词汇、实体分布进行修正。本文将其重构为序列检索问题：Agent 可以多次改写、检索，并基于返回的 passage 决定下一步动作。

## 方法关键点
- **动作空间类型化**：Agent 每步可选择 intent（消解指代和省略）、rephrase（词汇重述）、hyde（合成伪文档，便于文档-文档匹配）或 stop（终止）。每步检索 top-5 passage 追加到上下文，作为下一步反馈。
- **训练两阶段**：先用 32B 模型蒸馏动作格式到 4B 模型进行 SFT，再用 GRPO 强化学习优化检索奖励；奖励采用 RIRS（rank-incentive reward shaping），依赖最终排名，不使用任何人工 rewrite 标注。
- **无监督涌现策略**：RL 后策略自然形成一致动作顺序——先 intent 消解，再可选 rephrase，最后生成基于已检索 passage 的 HyDE。8-gram 检测显示伪文档并非简单复制（中位数为 0），但 unigram Jaccard 显示其吸收了检索结果的词表（0.137 vs 无关 passage 的 0.014）。

## 关键实验
在 TopiOCQA 和 QReCC 上使用 BM25 检索，对比 ConvSearch-R1、RETPO、ADACQR 等基线。多步 multi-action Agent 取得：TopiOCQA MRR 41.4、nDCG@3 40.6（ConvSearch-R1 Qwen2.5 为 35.2/33.5）；QReCC MRR 57.2、nDCG@3 55.8。受控实验显示：仅单步 typed action 反而下降，增益来自“迭代 + 类型化动作 + RL”。零样本迁移到 TREC CAsT 上超过 ConvSearch-R1 的 NDCG@3；BM25 上训练的策略迁移到 dense retriever 仍有效，其中 TopiOCQA 上 Qwen3-Embedding 达到 MRR 51.0。

## 最值得记住的一句话
检索反馈不应只看作训练信号，而应成为 Agent 每步可见的状态；让改写策略在每一步观察并利用已检索结果，能在无人工改写标注下学会更优的查询消歧和词汇对齐。
