---
title: 'SCoRD: Semantic-Assisted Continual Retriever-Reranker Distillation for LLM-Based
  Recommendation'
title_zh: SCoRD：语义辅助的 LLM 推荐检索-重排持续蒸馏
authors:
- Seunghyun Baek
- Gyuseok Lee
- Seunghan Lee
- Wonbin Kweon
- Dong Wang
- SeongKu Kang
affiliations:
- Korea University
- University of Illinois at Urbana-Champaign
- Sungkyunkwan University
arxiv_id: '2608.19998'
url: https://arxiv.org/abs/2608.19998
pdf_url: https://arxiv.org/pdf/2608.19998
published: '2026-08-20'
collected: '2026-08-21'
category: RecSys
direction: LLM 检索-重排持续协同蒸馏
tags:
- Continual Learning
- Knowledge Distillation
- LLM Reranker
- Sequential Recommendation
- Retrieval-Rerank
- Intent Memory
one_liner: 提出语义意图助手与三阶段持续蒸馏，让 LLM 重排与轻量检索器在非平稳流中低成本高效协同更新
practical_value: '- 在带 LLM 重排的检索-重排线上，不要对每个新数据块做全量蒸馏：用 retriever 序列内 item 对齐置信度筛选
  bottom 20% 的低置信序列做 LLM 蒸馏，能显著降低 LLM 调用和训练成本，同时把增益集中在困难样本上。

  - 把 LLM 的语义推理从 free-form generation 改成「动态意图记忆 + 多标签选择」，可复用为商品的 intent/兴趣标签系统；意图向量可以注入
  retriever 的序列表征，增强 ID 模型的语义判别力，且推理端几乎没有额外延迟。

  - 在 retriever 每日在线更新时，不重新调用 LLM，只聚合行为相似用户序列的意图分数作为 collaborative pseudo-label，能提供稳定语义监督；适合电商/信息流里每天冷启动或新增序列频繁的场景。

  - 用相邻周期意图直方图差分识别衰退意图，再从 retriever 候选集里按 intent 后验采样负例，替代随机负采样，可更有效地捕捉用户偏好漂移，适合替代现有召回/排序模型中的负采样策略。

  - 新用户无历史行为时，意图级语义先验能明显提升冷启动效果；可在用户冷启动阶段直接用 LLM 打好的 intent 标签作为特征或约束。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
LLM 作为 reranker 的推荐系统通常采用 ID retriever + LLM reranker 两段式流水线，以平衡效果与推理成本。但线上数据是持续到达的非平稳流，用户、物品不断新增，偏好会漂移。若每次新数据到来都更新 LLM reranker 并做蒸馏，训练成本是 retriever 的 3.5–9.4 倍、推理成本是 72.4–144.4 倍，工程上不可行；只频繁更新轻量 retriever 又缺少语义指导。现有 continual KD 方法 CCD 假定 ID 教师-学生能力差距不大，难以迁移到 LLM 与 ID 模型强不对称的场景。

## 方法关键点
- **语义推理助手**：将 LLM 的 free-form intent generation 改为 memory-based selection，构建动态意图记忆。LLM 先对序列推断意图，通过 hold-out 验证后存入记忆；助手用 query-key-value 多标签分类预测意图，并聚合相关意图向量注入 retriever 表征，得到 semantic-guided representation。
- **Stage 1 重排到检索蒸馏**：基于 retriever 序列置信度选择 bottom 20% 的 hard sequences，仅在该子集上执行 listwise ranking distillation，同时用 LLM 推断的 intents 更新记忆并训练助手。
- **Stage 2 检索器持续更新**：不调用 LLM。用 behaviorally similar 用户序列的意图分数构造 collaborative pseudo-intent label；通过相邻 block 意图直方图差分得到 drift prior，再用 Dirichlet-Multinomial 后验做 intent drift-aware negative sampling。
- **Stage 3 检索到重排蒸馏**：将 retriever 的 item embeddings 投影进 LLM prompt，并用 intent-drift negatives 提供辅助监督，使 reranker 对齐近期协同模式。

## 关键结果
在 Books、Yelp、Movies & TV 三个数据集上，SCoRD 的 reranker 和 retriever 在 N@5、H@5 等指标全面超过 CCD、PISA、LLMD4Rec、CoT-Rec。例如 Book 上 retriever N@5 从 CCD 的 0.3158 提升到 0.4787；Movies 上 reranker N@5 达到 0.6072，明显优于 CoT-Rec 的 0.5658。新用户与偏好漂移用户增益更大；意图生成时间约为 CoT-Rec 的 1/10（Book 上 1.4h vs 15.4h）。消融显示 semantic-guided representation 和 intent drift-aware negative sampling 贡献最大。

最值得记住的一点：LLM 的语义推理可以蒸馏为「意图记忆 + 多标签选择」，以极低成本在 retriever 不频繁调用 LLM 的周期内持续提供意图级指导。
