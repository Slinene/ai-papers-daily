---
title: 'SwapRec: Warming Up Cold Items Through Training-Time Swaps'
title_zh: SwapRec：通过训练时交换提升序列推荐冷启动鲁棒性
authors:
- Marta Moscati
- Jan Malte Lichtenberg
- Davide Abbattista
- Antonio De Candia
- Laura Boggia
- Matteo Ruffini
affiliations:
- Albatross AI
- Johannes Kepler University Linz
arxiv_id: '2609.00913'
url: https://arxiv.org/abs/2609.00913
pdf_url: https://arxiv.org/pdf/2609.00913
published: '2026-09-01'
collected: '2026-09-03'
category: RecSys
direction: 序列推荐 · 冷启动 · 训练时替换
tags:
- cold-start
- sequential recommendation
- training-time augmentation
- SASRec
- BERT4Rec
one_liner: 把冷物品按内容相似度替换为温邻居的训练增强用于序列推荐，显著提升推理时冷替换鲁棒性和冷品曝光
practical_value: '- 如果线上已经用“冷品→最相似温品”的 inference 替换，直接把同一条 NN 映射放到训练里，按概率 p_swap 对输入序列和
  target 同时替换；加入 M_swap 限制每序列替换数，能低成本提升 ID 模型对冷启动点击的鲁棒性，不用改架构或加额外组件。

  - p_swap 与 M_swap 控制增强强度，M_swap 会让替换更容易落在序列前部，从而给冷品 ID 更多梯度更新；对电商/音乐等有内容 embedding
  的目录，直接用 title/description/image embedding 计算 cosine NN map 即可。

  - 评估冷启动时不要只看全量 HR，应细分 n_train≤threshold、严格冷启动(n_train=0)、以及 swap/init/drop 三种处理；论文中
  baseline 在严格冷启动时 swap 常常不如 drop/init，而 SwapRec 让 swap 成为最佳策略。

  - 在 Amazon 数据上，SwapRec 同时提升冷品暴露比例和 catalog coverage（30.7%→31.8%，coverage 0.578→0.632），适合需要平衡新商品/新广告主曝光与精排效果的场景。'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

**动机**
ID-based 序列推荐在用户点击冷品时，实时个性化容易受损：保留冷品会导致不准确的 embedding，丢弃冷品又阻断实时更新。工业界常用 inference 时将冷品 swap 成最相似温品，但论文表明 SASRec/BERT4Rec 对这种 swap 并不鲁棒，甚至会严重掉点。

**方法关键点**
- 用物品 side information（音频、标题/描述、电影剧情等 embedding）的 cosine similarity 构建最近邻映射 φ(i)。
- 训练时对序列每个位置独立以概率 p_swap 替换为 φ(s_k)，**同时作用于输入序列和训练 target**；每序列最多替换 M_swap 个 item。
- 冷品训练频次低，替换会使冷品 ID 获得更多梯度更新；M_swap 限制替换数量，会促使替换集中在序列前部，进一步增加冷品更新。
- 推理时仅对输入序列中的冷品执行同一 swap，不替换 target；无需改模型架构，也不需要额外训练组件。

**关键实验**
在 Music4All-Onion、Amazon All_Beauty、ML-20M 三个数据集上，以 SASRec 和 BERT4Rec 为 backbone，对比 MultVAE、Item-kNN、ALS。

最值得关注的数字：
- 全量序列 inference swap 下，SASRec 在 Onion 的 HR@10 从 0.0422 提升到 0.2404（SwapRec 后）；ML-20M 从 0.0524 提升到 0.1102；Amazon 从 0.0126 提升到 0.0494。
- 严格冷启动（n_train=0）的 swap/init/drop 对比中，SwapRec 让 swap 策略明显成为最优；如 Onion SASRec swap 从 0.0423 提升到 0.2405。
- RQ3 显示 Amazon top-10 冷品占比从 30.7% 提升到 31.8%，catalog coverage 从 0.5779 提升到 0.6322。

**一句话**：把 serving 阶段的冷品替换提前到训练，是改动最小、收益稳定的冷启动方案。
