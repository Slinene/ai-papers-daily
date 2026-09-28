---
title: 'Stale-Document Poisoning: When Outdated Retrieval Overrides Correct Model
  Answers'
title_zh: 陈旧文档毒化：过期检索覆盖模型正确答案
authors:
- Md Shamim Ahmed
- Lukas Galke Poech
- Richard Röttger
affiliations:
- University of Southern Denmark
arxiv_id: '2609.31342'
url: https://arxiv.org/abs/2609.31342
pdf_url: https://arxiv.org/pdf/2609.31342
published: '2026-09-25'
collected: '2026-09-28'
category: RAG
direction: RAG 时间适用性 · 陈旧文档毒化
tags:
- RAG
- Temporal Applicability
- Knowledge Conflict
- Selective Trust
- Causal Intervention
one_liner: 发现RAG中过时文档可使模型在原本正确时被翻转，并定位为选择性信任失败
practical_value: '- 在电商/客服 Agent 的 RAG 知识库中，为文档增加生效/失效日期或 supersession 关系，检索后先判断文档是否仍在适用期，而不只是发布时间或相关性。可作为索引字段或后置过滤。

  - 提示词里避免全局“遵循检索文档”指令，改为要求模型结合文档的适用期限判断；必要时显式给出“该推荐自 X 日期起失效”，能显著提升大模型对过期内容的抵制。

  - 检索侧可加 recency-aware hybrid re-ranker，但必须确保时间元数据可靠；日期缺失或错误时收益消失甚至反转，因此需要元数据治理。

  - 评测 RAG 时增加“反向毒化”指标：只统计未检索时答对、检索后答错的样本，观察过期文档是否推翻已有正确知识；同时测试匹配的当前文档是否被遵循，以区分全面失败与选择性信任失败。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
RAG 常被用来解决模型知识过时，但检索到的文档本身也可能已经过期。与恶意构造不同，陈旧文档曾经真实有效，只因时间推移而不再适用；模型若盲目信任，会推翻自己原本正确的回答。论文将这一问题称为 stale-document poisoning。

## 方法关键点
- 构建源验证的 317 个知识反转基准，覆盖医学、法律、软件/API、平台政策；每项包含 timely answer、superseded answer，匹配当前/过期文档。
- 中毒率定义为：未检索时答对、加入过时文档后答错的样本比例；并设置匹配当前文档对照。
- 50 个时间适用性控制：同一历史文档，只改变评估日期，比较日期单独 vs 显式给出失效边界（文本或表）下的行为。
- 因果干预：在评估日期位置进行双向激活修补，分离 attention/MLP 贡献，并用发现-确认划分进行 head 定位。
- 检索侧防御：固定 recency-aware hybrid re-ranker，结合 semantic relevance、recency、supersession cues。

## 关键结果
- 12 模型在 settled 反转接近满分，近期反转准确率显著下降（如 Qwen-7B 0.61，GPT-4o 0.76）。
- 过时文档无指令翻转 30% Llama、37% Qwen 原本正确回答；显式 follow 指令升至 66% 和 75%；匹配当前文档遵循率 97–100%。
- 固定证据只改日期，模型变化很小；显式给出失效边界后，Qwen-72B 做出全部 50 次正确切换，Llama-70B 47/50（表格格式 50/50）。
- 因果修补显示评估日期状态可直接改变最终决策，早期主要由 attention 贡献；相同 head 也参与普通日期比较和非时间阈值任务。
- 日期准确时，hybrid re-ranker 降低中毒 4.6–10.0 个百分点；日期缺失/错误时收益消失或反转。

## 最值得记住的一句话
可靠 RAG 的核心不是检索到最相关的文档，而是判断检索到的文档是否仍然适用；显式有效性边界能让大模型做到这种选择性信任，但日期元数据本身不够。
