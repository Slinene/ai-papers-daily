---
title: 'Generative News Recommendation Reproduces Popularity: A Memorization-Based
  Analysis'
title_zh: 生成式新闻推荐复现流行度：基于记忆的分析
authors:
- Shotaro Ishihara
affiliations:
- Nikkei Inc.
arxiv_id: '2611.25606'
url: https://arxiv.org/abs/2611.25606
pdf_url: https://arxiv.org/pdf/2611.25606
published: '2026-11-19'
collected: '2026-11-20'
category: GenRec
direction: 生成式新闻推荐 · 记忆与流行度偏差
tags:
- generative recommendation
- popularity bias
- memorization
- news recommendation
- LoRA
- diversity
one_liner: 在2000万新闻会话上训练Llama 3 8B生成式推荐器，证明高频目标被更强记忆并导致输出高度集中
practical_value: '- 若你的生成式推荐直接输出商品标题/广告文案，可用论文中的 verbatim/approximate memorization
  和 Gini concentration 离线审计输出分布；当 distinct titles 远少于训练集高频数、GS score 偏高时，说明模型可能在做“安全默认输出”而非个性化。

  - 不建议盲目用 target-level dedup 来缓解，论文中 dedup 后 exact-match 准确率从 2,461 骤降到 81；可改为 frequency-aware
  loss reweighting + recency decay，让近期商品/广告权重更高，避免历史爆款主导。

  - 推理侧采用 candidate-grounded / constrained decoding（trie 或 retrieval-augmented）强制生成映射到当前有效候选集，能防止标题后缀腐败和“一个
  prompt 坍缩到同一头部 item”。

  - 评估需同时报告 lexical diversity 和 semantic diversity：论文中 dedup 后 entropy 提升但 GS score
  反升，说明词面多样化不代表语义多样化；在电商/广告中同样要关注类目/品牌覆盖度。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：

生成式推荐能直接生成物品标题，不再局限于排序候选集。但在新闻场景中，模型可能反复暴露已经热门的文章，压缩用户接触的信息多样性，这与新闻的社会责任相冲突。已有工作大多只测量输出偏差，很少解释“为什么生成模型会集中输出”。该研究从训练数据记忆（memorization）切入，检验行为日志中的高频字符串如何被模型记住并在生成时复现。

方法关键点：
- 数据：日本经济新闻服务约2000万浏览会话（2023年1月），每个会话至少3篇文章；将会话组织为 `a1 [ARTICLE_SEP] a2 ...` 文本序列。
- 模型：对 Meta-Llama-3-8B-Instruct 做 LoRA 持续训练，rank=16，2 epochs，max_len 512，lr=1e-4，8×A100。
- 评估：每个会话第一个标题作为 prompt，第二个作为后继；取该 prompt 最频繁后继作为 reference；用 greedy decoding 生成下一个标题，最多50 tokens。
- 度量：用 Gini-based concentration、Shannon entropy、GS score、distinct title count 衡量分布集中度；用最长共同前缀字符数（verbatim memorization）和归一化 Levenshtein 相似度（approximate memorization）衡量记忆强度。

关键结果：
- 生成输出比真实后继分布更集中：concentration 0.9072 vs 0.9003，entropy 7.169 vs 9.147，GS score 0.3364 vs 0.1911，distinct titles 20,689 vs 101,026（约为1/5）。
- 参考频率越高，记忆越强：log reference frequency 与 verbatim memorization r=0.3042，与 approximate memorization r=0.3344。
- 记忆越强，生成频次越高：log generation frequency 与 verbatim memorization r=0.1965，与 approximate memorization r=0.3084；出现多个不相关 prompt 被映射到同一生成标题，某生成标题出现25,840次。
- 探索性 target-level dedup 后，verbatim memorization 从0.1356降至0.0164，distinct titles 从20,689增至39,479，但 exact-match 准确率从2,461降至81，且 GS score 反升至0.4658（语义多样性未改善）。

最值得记住的一句话：生成式推荐中的流行度偏差不仅来自用户偏好或排序目标，更可能源于模型对高频字符串的优先记忆，形成“行为频率→重复训练文本→记忆→集中输出”的传导链；缓解需在损失重加权、受限解码和多样性重排等层面系统设计。
