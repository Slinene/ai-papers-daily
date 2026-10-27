---
title: 'SLIDE: Search-to-List Item Distillation for Single-Rollout Generative Retrieval'
title_zh: SLIDE：搜索到列表蒸馏实现单次贪心生成式检索
authors:
- Tianyu Zhan
- Gui Ling
- Ran Tao
- Kunhai Lin
- Tong Xiong
- Wang Yang
- Kaixuan Zhang
- Zhihong Chen
- Yuliang Yan
- Dan Ou
affiliations:
- Zhejiang University
- Taobao & Tmall Group of Alibaba
arxiv_id: '2610.34764'
url: https://arxiv.org/abs/2610.34764
pdf_url: https://arxiv.org/pdf/2610.34764
published: '2026-10-26'
collected: '2026-10-27'
category: GenRec
direction: 生成式检索 · 列表蒸馏
tags:
- Generative Retrieval
- Knowledge Distillation
- Semantic ID
- List-wise Generation
- Single Greedy Decoding
one_liner: 将离线item级beam search结果按分数拼接为列表蒸馏目标，训练学生单次贪心生成Top-K，以低成本逼近或超越线上beam search检索
practical_value: '- 线上部署用单次贪心解码替代 item-level beam search：蒸馏后 0.5B 学生可逼近或超越同尺寸直接训练模型的
  beam search，服务质量不变但推理路径更简单、延迟更低；teacher 仅离线构造数据，可无限扩容量。

  - 蒸馏目标顺序不能乱：保留 teacher beam-score 降序对头部 HR 和 NDCG 至关重要；随机打乱会明显降低头部检索质量。如果自建列表蒸馏数据，不要做去重/有效性过滤再拼接，直接按固定长度
  SID 块拼接并保持顺序。

  - 目标长度与评价深度对齐：当 HR@K 为核心指标时，蒸馏目标取 K 个 teacher 候选即可，过长会显著增加离线 beam search 成本而不提升对应截断指标。

  - 列表级 RL 后续优化空间大：在 SLIDE 基础上做列表级 RL，相对 SFT 提升可达 3.46-7.67%，远高于 item 级 RL 的 0.59-1.17%；可继续叠加
  relevance reward 和 LLM-as-judge 自洽性奖励进一步提升相关性。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
生成式检索通常采用 point-wise 训练 + item-level beam search，线上多路径展开，无法建模跨商品依赖，也难以直接优化列表级目标。单次贪心列表生成虽自然，但同一模型下比 beam search 在 Taobao Search 上 HR@20 差 18.4%。原因有二：beam search 搜索空间更大；行为监督中正样本稀疏且后位监督不足。

**方法关键点**
- 三阶段框架：教师训练 → 离线蒸馏数据构造 → 学生列表生成蒸馏。
- 教师使用 PF-Fine-Ranking 列表（转化商品在前，点击其次，曝光未点击最后）做 list-wise 训练；随后冻结教师执行 item-level beam search 得到 Top-K SID。
- search-to-list 转换：按 beam-score 降序直接拼接 K 个固定长度 SID，末尾加 EOS，不插入分隔符，不做映射或过滤，形成单条长度为 K*L+1 的序列作为蒸馏硬目标。
- 学生从原始预训练初始化，仅用这些 hard target 做 token-level NLL，teacher forcing；线上学生一次贪心解码至 EOS，再切块、去无效和重复。

**关键实验**
- 数据集：FORGE 和 Taobao Search；学生均为 Qwen2.5-0.5B。
- 直接训练 greedy 在 FORGE 几乎不出候选；在 Taobao Search HR@10 为 0.3206，而 beam search 为 0.4498。
- SLIDE 用同尺寸 0.5B teacher 蒸馏，Taobao HR@10 提升至 0.4321；7B teacher 让学生 greedy 达 HR@10 0.4578，超过同尺寸直接训练 beam search；FORGE 上 7B teacher 相对 beam search HR@10 提升 20.49%。
- 顺序消融：随机打乱蒸馏目标顺序导致 HR@1 从 0.1470 降至 0.0602，NDCG@20 从 0.3010 降至 0.2271，说明顺序对头部检索关键。
- RL 后续：列表级 RL 相对提升 3.46-7.67%，item 级仅 0.59-1.17%。

**最值得记住**
离线搜索、在线列表生成：把 beam search 的探索能力蒸馏进一次贪心轨迹，才能真正摆脱多路径在线解码。
