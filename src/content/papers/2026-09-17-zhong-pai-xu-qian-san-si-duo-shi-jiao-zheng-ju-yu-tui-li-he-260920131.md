---
title: 'Think Thrice Before Reranking: Multi-perspective Evidence and Reasoning Integration
  for Text Reranking'
title_zh: 重排序前三思：多视角证据与推理融合的文本重排序
authors:
- Lijun Liu
- Zhengzong Chen
- Wenyan Li
- Yuanyuan Zhao
- Fei Huang
affiliations:
- Honor Device Co., Ltd
arxiv_id: '2609.20131'
url: https://arxiv.org/abs/2609.20131
pdf_url: https://arxiv.org/pdf/2609.20131
published: '2026-09-17'
collected: '2026-09-18'
category: RecSys
direction: LLM 文本重排序 · 多轨迹推理
tags:
- LLM Reranking
- Multi-perspective Reasoning
- GRPO
- Listwise Ranking
- Progressive Training
- Text Ranking
one_liner: 提出 MERIT-Rank，用语义、意图、证据三个互补推理轨迹联合重排序，并以渐进式 SFT+GRPO 训练，4B 模型超越多数 7B/32B
  重排器
practical_value: '- 将 query-doc 相关性拆成「语义对齐 / 意图满足 / 证据支撑」三个互补视角，在单模型内先分视角生成 reasoning
  + 排序，再合成最终排序；该结构能显著减少单链推理错误传播，适合搜索广告精排中的复杂 query 场景。

  - 渐进式 RL 可直接借鉴：SFT 先学格式与基础推理；GRPO 第一阶段用格式奖励 + 相对提升奖励（对比初始召回/BM25 的 NDCG、MRR、RBO），第二阶段再引入绝对
  MRR/NDCG，收敛更稳且持续提升排序质量。

  - 数据合成与验证方法可复用：用强 teacher 生成多轨迹，弱模型修格式，再双重过滤（合成排序 NDCG@10 必须优于任一单视角；相关文档必须置顶）；电商多目标/多信号训练数据合成可参考该验证逻辑。

  - 在长候选集滑动窗口重排场景，多视角联合模型用更少窗口（3 vs 9）即可达到同等精度，总 tokens 和延迟更低，对线上成本敏感的重排链路有借鉴价值。'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
现有 LLM 推理式重排虽强，但普遍只走单条推理链；推理错误会沿自回归生成传导到最终排序。真实 query-document 相关性是多面的（语义、意图、证据），单链只能覆盖部分信号，鲁棒性受限。

**方法关键点**
- 构建 Multi-Trajectory Reasoning Space：定义语义对齐、意图满足、证据支撑三个互补视角，每个视角生成独立 reasoning + ranking。
- 单模型联合重排：先逐视角生成中间排序，再生成 synthesis reasoning 聚合各视角证据得到最终排序，避免多模型 ensemble 开销。
- 数据合成与验证：用 DeepSeek-R1 生成多轨迹，GPT 修格式；双重过滤要求合成排序 NDCG@10 优于任一单视角，且相关文档置顶；最终 21,032 条，10k SFT + 11k RL。
- PRPO 渐进训练：先 SFT 学格式；GRPO stage1 用格式奖励 + 相对提升奖励（对比初始检索的 NDCG/MRR、RBO 对齐）；stage2 再引入绝对 MRR/NDCG。

**关键结果**
- BRIGHT：4B 平均 NDCG@10 36.6，超过 ReasonRank-7B 35.7、ERANK-4B 30.5；7B 37.1，32B 40.3。
- TREC/BEIR：7B TREC avg 74.1、BEIR avg 56.4，较 ReasonRank-7B 69.8/54.4 提升明显。
- 消融：去掉任一视角均掉点；去掉 synthesis reasoning 掉 1.84，去掉全部 reasoning 掉 4.95；去掉 SFT 掉 1.94，去掉 P-GRPO 掉 2.35。
- 效率：BRIGHT 子集上同精度下只需 3 个滑动窗口 vs ReasonRank 9 个，总 tokens 更少、延迟更低。

**最值得记住**：在单模型内用互补多视角推理轨迹替代单链推理，并配合从相对到绝对的渐进式 SFT+GRPO 优化，是小模型做高鲁棒重排的有效路径。
