---
title: 'R2QRec: Learning Recommendation Queries from Retrieval Feedback'
title_zh: R2QRec：从检索反馈中学习推荐查询
authors:
- Weixin Chen
- Shuchang Liu
- Hailan Yang
- Yuhan Zhao
- Li Kang
- Xuefeng Zhang
- Chenghao Zhang
- Xinyuan Wang
- Hanchen Yang
- Yinghao Wu
affiliations:
- 快手科技
- 香港浸会大学
arxiv_id: '2610.39984'
url: https://arxiv.org/abs/2610.39984
pdf_url: https://arxiv.org/pdf/2610.39984
published: '2026-10-29'
collected: '2026-10-30'
category: QueryRec
direction: 生成式推荐 · 检索反馈强化学习
tags:
- Query Generation
- Retrieval Feedback
- GRPO
- Reciprocal Rank Fusion
- LoRA
- LLM4Rec
one_liner: 用固定检索器构造可检索 query 监督，并以 RRF 融合排名反馈优化 query 生成器
practical_value: '- 可借鉴 **retrieval-verified SFT** 做 query/文案生成：在无法标注“正确 query”的场景，先用
  LLM 生成候选 query，再用固定 retriever 对 target item 的命中 rank 过滤，只保留能检索到 target 的表达作为 SFT
  数据；比直接拟合商品/内容标题更贴合线上检索行为。

  - 用固定检索器 + RRF 融合后 target rank 作为奖励，可在电商/广告搜索推荐中直接复用：让线上 ES/向量召回服务执行当前 policy 的
  query set，取 target item 在融合列表中的 rank，奖励设为 `-log(1+rank)`，再接 GRPO，无需单独训练 reward model。

  - 工程实现上只训练 LoRA，冻结 LLM backbone、retriever 和 item index；query generator 不枚举 item，推理成本主要在生成，检索可走预计算
  item embedding + 近似索引，适合大 catalog 冷启动和线上迭代。

  - 多 query + RRF 是轻量但有效的召回融合方式；query 数 K 可以推理期灵活调整而不改变 checkpoint。该方法还显示 query generator
  的跨域迁移能力，新域/冷启动时可直接用其他域训练好的 generator，比重新训练 ID 类模型更易复用。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
基于 query 的推荐把“表达用户需求”和“匹配 item”解耦，核心难点是交互日志只有 item 目标，没有对应 query 标注。已有的 title 监督方法直接让生成器模仿 target item 文本，容易偏离实际检索行为；而固定 retriever 的检索结果本身可以提供更强的监督和评估信号。

**方法关键点**
- 冻结 retriever 和 item index，只训练 query generator 的 LoRA 参数；从用户上下文生成 K 个自然语言 query，分别检索后用 Reciprocal Rank Fusion (RRF) 融合推荐。
- **Item-verified SFT**：对每个训练样本，用 base LLM 生成 M 个候选 query，只保留能把 target item 检索进 top-τ 的 query 作为 SFT target；这样 item label 只定义“可接受表达”，不固定措辞。
- **Fusion-aware refinement**：生成 G 组 query set，计算 target 在 RRF 融合列表中的 rank，reward 为 `-log(1 + rank)`；用 GRPO 的组内标准化 advantage 更新 policy，并以 SFT checkpoint 作为 KL reference 约束策略漂移，不需要 reward model。
- 目标分析：log-rank 可分解为带权 top-N miss risk，头部 cut-off 权重更高；单个 query 的 target rank 不能决定融合后的 rating，必须对 query 组合反馈优化。

**关键实验**
在 Yelp、MovieTV、Amazon Books 三个公开数据集上做 open-pool 推荐，全体 item 参与检索；对比 SASRec、BERT4Rec、LightGCN、UniSRec、TIGER、LETTER、BM25、BIGRec、GPT4Rec、QueRec、QueryAgent-R1 等。
R2QRec 在 24 个 dataset–metric 组合中 23 个最优；NDCG@10 相对最强 baseline 分别提升 Yelp +68.7%、MovieTV +3.5%、Books +42.1%。MovieTV 上 Recall@5/10 相对最强 baseline 提升 +11.9%/+17.3%。消融显示去掉 retrieval verification 后 MovieTV NDCG@10 从 5.07% 降至 4.03%；GRPO 较 SFT-only 提升 0.74 个百分点；KL 和 G>1 均有贡献。跨域迁移中，用 MovieTV 训练的 generator 在 Books 上 NDCG@10 达 8.09%，超过 Books in-domain 的 7.66%。候选排序场景中 MemRec 更强，但 R2QRec 的核心优势在 open-catalog 检索式推荐。

**最值得记住的一句话**
用固定 retriever 把 item 命中转成 query 监督信号，再对 RRF 融合后的 target rank 做 GRPO，是一条无需 reward model 的 query 学习闭环。
