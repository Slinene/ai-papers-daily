---
title: Towards Efficient Whole Page Ranking with One-Pass Inference
title_zh: 高效整页排序：前缀感知单遍推理多物品打分
authors:
- Qi Xu
- Zhigang Hua
- Zijie Lei
- Yan Xie
- Jizhe Zhang
- Lynn Lu
- Delun Du
- Sha Hua
- Ren Mao
- Ke Pan
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2611.05542'
url: https://arxiv.org/abs/2611.05542
pdf_url: https://arxiv.org/pdf/2611.05542
published: '2026-11-03'
collected: '2026-11-05'
category: RecSys
direction: 整页排序 · 前缀感知NAR scoring
tags:
- whole-page ranking
- one-pass inference
- prefix-aware scoring
- constrained beam search
- RQ-VAE
- ads-organic
one_liner: 前缀感知NAR打分MIS：一次请求级编码+活跃前缀条件打分，质量接近AR，解码快4.07×/3.54×
practical_value: '- 混排/整页重排（含 LLM/生成式重排）：把全局候选编码与顺序评分解耦，预计算 candidate/slot 表示，只在活跃
  beam 上做轻量前缀条件打分；不要每一步重新编码整个候选池。

  - 约束 beam search：只物化 B×C 活跃打分行，配合 mask 与 min-heap top-B；在广告位/间隔/类目约束下可加大 beam width，不必增加全模型前向。

  - 长历史/大 catalog：用 RQ-VAE 将 item 历史向量存成共享 codebook + 残差码，当前候选保持全精度；质量损失很小，历史存储可从
  187.81 MiB 降至 2.207 MiB。

  - 线上验证：离线 scorer lift 只能说明优化空间，需做 hash 分层随机实验；关注真实 CPU 成本——本方案 ranking-service CPU
  -9.73%，但 prediction-service CPU +1.39%，不能只看单侧。'
score: 9
source: arxiv-stat.ML
depth: full_pdf
---

**动机**：整页混排要同时优化广告与自然内容，受广告位、间距等强约束。纯 NAR 按 item-position 独立打分，无法建模已选前缀对后续 item 的影响；AR 能捕获顺序依赖，但每个 continuation 都要重跑序列模型，线上 CPU 开销大。需要兼顾顺序依赖与单次请求编码。

**方法关键点**
- MIS 将候选集/位置编码与顺序打分解耦：全局 self-attention 建模候选间交互，不注入输入顺序 embedding；position tower 建模槽位上下文；前缀处理只更新已选序列状态。
- 打分 = base item-position score + prefix-conditioned residual；PA-1 直接用 predecessor 状态，PA-N 用 causal Transformer 编码已选前缀，当前候选项 query 获得顺序上下文。
- 长历史用 RQ-VAE 压缩历史 item 向量为共享 codebook + 残差码；beam search 只物化 B×C 活跃行，不建高阶前缀张量。
- 训练用 observed slate 的多任务多标签损失，线上用固定权重组合各任务打分并做约束 beam search。

**关键结果**
- KuaiRand-1K：MIS-PA-N 质量接近 CGA，AUC 0.6423 vs 0.6424，NE 0.9554 vs 0.9553，生成 lift 18.284% vs 18.279%；RL4RS 三项点估计均优于 CGA。
- 解码延迟比 CGA 快 4.07×/3.54×，FLOPs 约为 CGA 的 1/5。
- RQ-VAE 历史 catalog 从 187.81 MiB 降至 2.207 MiB，AUC 仅降 0.0005，lift 降 0.164pp。
- 工业随机实验：realization +0.104%，总 watch time +0.058%，ranking-service CPU -9.73%，但 prediction-service CPU +1.39%。

**最值得记住**：把昂贵的候选集/槽位编码压缩为一次共享前向，顺序依赖只留在轻量前缀条件头上，不必在 AR 与 NAR 之间二选一。
