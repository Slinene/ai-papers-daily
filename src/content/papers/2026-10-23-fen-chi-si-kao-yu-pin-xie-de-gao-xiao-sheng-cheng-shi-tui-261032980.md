---
title: Separating Thinking from Spelling for Efficient Generative Recommendation
title_zh: 分离思考与拼写的高效生成式推荐
authors:
- Danil Gusak
- Anna Volodkevich
- Ivan Oseledets
- Evgeny Frolov
arxiv_id: '2610.32980'
url: https://arxiv.org/abs/2610.32980
pdf_url: https://arxiv.org/pdf/2610.32980
published: '2026-10-23'
collected: '2026-10-26'
category: GenRec
direction: 生成式推荐 · Semantic ID 推理优化
tags:
- Generative Recommendation
- Semantic ID
- Inference Efficiency
- Knowledge Distillation
- Beam Search
- Copy Mechanism
one_liner: 将生成式推荐中 backbone 的历史建模与 SID 逐码生成解耦，由轻量 decoder 完成 beam search，实现 3-8 倍吞吐提升且精度不降
practical_value: "- **架构选择：重 encoder + 轻 decoder 分离 serving**  \n  在生成式推荐（Semantic\
  \ ID）线上推理中，让大 backbone 只跑一次 prefill 输出固定大小的 next-item concept（如 1KiB），beam search\
  \ 全部下沉到 2 层 256 宽的轻量 decoder。concept 可作为 per-user state 预计算并缓存，在线只有轻 decoder 参与\
  \ decode，避免大模型反复处理 O(BK) 个 decode token。\n- **输入侧融合 item SID tokens 降低 prefill**\
  \  \n  用 MLP 把每个 item 的 K 个 code embedding 融合成单个 token，历史长度从 TK 降到 T；训练时通过 block-causal\
  \ mask 为每个位置提供下一 item 的 gold prefix targets，实现 dense training，一次前向即可监督所有 transitions。\n\
  - **轻 decoder 训练用教师分布做 label smoothing**  \n  将 full-backbone teacher 在 gold prefix\
  \ 上的 next-code 分布与 one-hot 混合（α 为 KD 权重），作为 decoder 的 CE 目标。在小数据集上可带来 16-23% NDCG@10\
  \ 提升，且 teacher 仅训练时使用，不增加 serving 成本。\n- **复购/重复消费场景加 history pointer**  \n  对音乐、视频、电商复购等\
  \ repeat-heavy 领域，基于 backbone last state 对历史 item 的 attention 构造 pointer，与生成分布混合（gate\
  \ 由 last state 学习）。在 Yambda 数据集上，pointer 将 Deco NDCG@10 从 0.079 提升到 0.171，几乎追平 FlatGR。"
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
生成式推荐通过逐 code 写出 Semantic ID 来检索物品，但标准 autoregressive 方法在 beam search 阶段需要在 backbone 上处理 O(BK) 个 decode token，其中 B 为 beam width、K 为 SID 深度。即使将历史输入从 TK tokens 融合为 T tokens（FusedGR），beam search 仍占生成时间的 91%（BPC-23 batch 128 下 14.9ms）。问题核心是：用户偏好建模（thinking）和 SID 拼写（spelling）被耦合在同一个大模型里。

## 方法关键点
- **Fused history**：用 MLP 将每个 item 的 K 个 code embedding 融合成单个 token，prefill 长度从 TK 降到 T。
- **Deco 解耦**：backbone 读历史一次，输出固定大小 next-item concept z（默认 M=2 个向量）；轻量 causal decoder 以 z 和已生成 prefix 为条件，在 trie 约束下完成 beam search。decoder 不接触历史，无需 backbone KV cache。
- **训练**：联合训练 backbone、fuser 和 decoder；dense training 对每个位置预测下一 item 的 codes。可用纯 cross-entropy（Deco-CE），也可用 full-backbone teacher 做知识蒸馏，将教师分布与 one-hot 混合作为 label smoothing。
- **Copy pointer**：针对 repeat-heavy 领域，用 backbone last state 对历史 item 的 attention 构造 pointer，与生成分布按 gate 混合，处理重复消费。

## 关键实验
在 7 个数据集（Amazon Beauty/Sports/Toys、BPC-23、Books-23、MovieLens、Yambda）上，Deco 匹配或超过 FusedGR/FlatGR teacher 的 NDCG/Recall。效率方面：50ms p95 延迟预算下，Deco 比 FusedGR 多服务 3.2-7.1× 用户（较 FlatGR 6.5-8.6×）；BPC-23 上 beam search 时间从 14.9ms 降至 2.1ms。扩展到 Qwen2.5 3B 时，Deco 较 FusedGR 达 16× 加速；1.5B Deco 与 69M FusedGR 吞吐相当且 NDCG@10 高 11%。候选池扩展上，Deco 在 k=1000 时比 FusedGR k=100 更快，Recall 提升 3×（0.267 vs 0.088）。

**最值得记住的一句话**：将 thinking（用户偏好建模）与 spelling（SID 逐码生成）解耦，是生成式推荐低成本 serving 的关键。
