---
title: 'From Topical Relevance to Answerability: Entailment Distillation for Conversational
  Retrieval'
title_zh: 从主题相关到可回答性：面向对话检索的蕴含蒸馏
authors:
- Shuai Qin
- Guojia An
- Weikang Guo
- Pei Ke
- Jiwei Wei
- Yang Yang
- Jie Zou
affiliations:
- University of Electronic Science and Technology of China
- Southwest University of Finance and Economics
arxiv_id: '2609.03482'
url: https://arxiv.org/abs/2609.03482
pdf_url: https://arxiv.org/pdf/2609.03482
published: '2026-09-03'
collected: '2026-09-05'
category: RAG
direction: 对话检索 · 可回答性 · 蕴含蒸馏
tags:
- Conversational Retrieval
- Entailment Distillation
- Answerability
- Cross-Encoder
- Abductive Recall
- LLM4IR
one_liner: 提出 CLEAR，用答案-段落蕴含蒸馏和段落中心溯因召回，缩小对话检索中主题相关与可回答性差距。
practical_value: '- 在电商客服/商品问答 RAG 中，不要只优化 query 与商品的 topical similarity：可以在 rerank
  阶段加入 answerability 头，训练时用 NLI 模型对「答案-商品/内容」算 entailment 再蒸馏到 cross-encoder，推理时只需
  context+passage，能有效把「能回答问题」的候选提上来。

  - 对低相似但可回答的商品详情页、评论区、文档，可离线用 LoRA fine-tune 的 LLM 为每个 item 反向生成多个可能 query，建成向量索引，在线做
  query-to-query ANN 匹配并 RRF 融合；这样能找回 dense retrieval 漏掉的候选，同时避免在线 LLM 延迟。

  - NLI teacher 信号偶尔会倒置（负例 entailment 高于正例），不要直接丢弃；借鉴其 adaptive calibration：正例按 passage
  相似度放大，负例按不相似度削弱，保留 hard negatives 排序，可稳定 reranker 训练。

  - 工程上把 LLM 生成和 entailment 计算全部放到离线，在线只留 ANN lookup + 固定 size cross-encoder，延迟可比
  autoregressive rewrite 方案低约 3-4 倍，适合低延迟线上检索链路。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
对话检索普遍把主题相关性当作可回答性的代理，但存在系统性 answerability gap：top-1 常与当前 query 主题相似却无法支撑答案。统计显示 TopiOCQA 上 semantic trap 比例从 vanilla Dense 的 18.38% 上升到强 CDR 基线 QRACDR 的 27.92%，说明检索越强，这类陷阱反而越明显。为此需要把监督从 topical matching 转向 answerability。

## 方法关键点
- CLEAR 由双通道召回和答案感知重排组成。
- 召回：保留 ANCE dense retrieval；新增 passage-centric abductive recall，用 LoRA fine-tune Llama 3.1 8B，从每个 passage 反向生成多条可能 query，形成离线 query pool；在线用同一个 query encoder 做 context-to-query ANN 匹配，再与 dense list 做 RRF 融合。
- 重排：RoBERTa cross-encoder 双头，contextual relevance head + answerability head。用 frozen DeBERTa-v3-large NLI teacher 对 (answer, passage) 计算 entailment probability，通过 KL 蒸馏到 answerability head，推理时只使用 context+passage，不需要 answer。
- Adaptive calibration：当 NLI teacher 对负例 entailment 分数高于正例时，用 passage similarity 放大正例、按不相似度削弱负例，保留负例间 dark knowledge 排序。
- 训练目标为 L = L_rel + γ·L_ans，推理分数为 β·σ(s_ctx) + (1-β)·s_ans。

## 关键实验
在 TopiOCQA、QReCC 和 zero-shot TREC CAsT 19-21 上评估。CLEAR 在 TopiOCQA 上 MRR 达 46.2，超过 QRACDR 的 38.7；QReCC 上 MRR 69.3，远高于 ConvSearch-R1 的 53.7。Ablation 显示相同 candidate pool 下，relevance-only CE 换成 answerability-aware A-CE 后 top 指标显著提升，且 calibration 去掉会掉点。Frozen NLI 用 answer oracle 重排 MRR 49.1，蒸馏后 CLEAR 46.2，接近 oracle 而无需 answer。在线延迟约 171.9 ms，比 DiSCo 和 ConvSearch-R1 低约 3-4 倍。

最值得记住：对话检索的瓶颈不是 query 改写或 dense 相似度不够，而是主题相似不等于可回答；训练时从答案-段落 entailment 蒸馏监督到 reranker，推理时无需答案即可显式建模 answerability。
