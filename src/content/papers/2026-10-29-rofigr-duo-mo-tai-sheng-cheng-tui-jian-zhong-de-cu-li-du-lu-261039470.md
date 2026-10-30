---
title: 'RoFiGR: Coarse Routing, Fine Refinement via Level-Adaptive Distillation in
  Multimodal Generative Recommendation'
title_zh: RoFiGR：多模态生成推荐中的粗粒度路由与分层自适应蒸馏
authors:
- Ji Dai
- Zhipeng Wei
- Zhuang Zhuang
- Rongfeng Guo
- Jie Chen
- Quan Fang
- Fei Pan
affiliations:
- Beijing University of Posts and Telecommunications
- Kuaishou Technology
arxiv_id: '2610.39470'
url: https://arxiv.org/abs/2610.39470
pdf_url: https://arxiv.org/pdf/2610.39470
published: '2026-10-29'
collected: '2026-10-30'
category: GenRec
direction: 生成式推荐 · Semantic ID 协同路由
tags:
- Generative Recommendation
- Semantic ID
- Multimodal
- Knowledge Distillation
- Coarse Routing
- Collaborative Filtering
one_liner: 融合协同信号对齐粗粒度 SID 与分层自适应蒸馏，提升多模态生成推荐的粗路由命中与排序
practical_value: '- 在 SID 构建阶段，把 cumulative L1-L2 code vector 与 frozen CF item embedding
  做对比对齐，可以将行为相似商品聚到同一粗前缀，同时保持 L1 分支活跃；电商场景可直接复用现有双塔/协同过滤模型，无需在线增加 teacher。

  - 序列编码时对 flatten 后的 SID 显式加入 item-distance 与 source-level bias（只加第一层 self-attention），能区分
  item 边界和层级来源，参数量仅 498 个标量，适合低延迟线上服务。

  - 蒸馏不要 uniform 分配层级权重：L1-L2 保持固定 anchor，L3-L4 用 teacher-student demand 的 bounded
  adaptive residual 动态分配；demand 只在 teacher 同时超过 student 和 catalog prior 时为正，可自动把监督集中到信息量大的粗路由层。

  - 推理中使用多 stream 独立 trie-constrained beam 后 stream-local normalization 再等权融合，能提升候选覆盖；通过
  beam slot 预算或 candidate cap 做精度-延迟权衡，线上不调用 teacher。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：生成式推荐逐码解码 Semantic ID，早期 L1/L2 属于粗路由，路由错误会提前排除大量相关 item。多模态推荐中，粗路由必须同时反映协同偏好与商品语义，但 uniform 训练目标未区分层级角色，扁平化历史也丢失 item 边界和 source level 信息。

**方法关键点**：
- **协同分层 SID 学习**：保留 MACRec 双树多模态残差量化；将 L1-L2 累计 code vector 与 frozen MISSRec item embedding 做对比对齐，加入 in-batch contrastive loss；碰撞 repair 仅限 L3-L4，保证行为相似 item 共享粗前缀。
- **Structure-aware encoder**：8 个训练任务，含 bimodal history；首层 self-attention 增加 token distance、item distance、source-level bias 三种相对偏置，区分 item 边界与层级来源，仅 498 个标量。
- **Anchored Level-Adaptive Distillation**：从 frozen teacher 聚合 gold prefix 下合法分支 item scores 得到教师分支分布；蒸馏权重 = fixed anchors L1/L2 0.10/0.075 + bounded adaptive residual，残差由 teacher 超过 student 与 catalog prior 的最小 gap 经 EMA 动态决定，L3-L4 anchor 为 0。
- **推理**：4 个 streams 独立 trie-constrained beam size 20，stream-local normalization 后等权融合；也提供两流与 beam/cap 控制。

**关键实验**：
- 数据集 Amazon Instruments/Arts/Games，商品数 6,250/9,416/13,839；对比 MISSRec、VIP5、TIGER、MQL4GRec、MACRec、SynGR。
- 全量 15 个 dataset-metric 均取得最高均值；相对最强外部 baseline 平均相对增益 9.4274%，HR@10/NDCG@10 六项配对检验经 Holm 校正后显著。
- 诊断：Arts 上 RoFiGR 的 L1 accuracy text/image 从 17.73/17.26 升至 22.53/21.55，L1:2 从 10.29/9.83 升至 14.23/13.49；行为邻居 prefix sharing 显著提升且无空 L1 分支。
- 效率：RoFiGR 额外增加 58 分钟 teacher 准备，四流 beam20 延迟 56.7-63.7ms。

**最值得记住的一句话**：生成式推荐的早期 code 是 router，应该用协同信号与自适应蒸馏让粗路由留下对的人，而不是把监督均匀铺在所有层级。
