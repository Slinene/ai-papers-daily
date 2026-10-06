---
title: How Sparse Probability Maps Shape Mixture-of-Experts Routing
title_zh: 稀疏概率图如何影响 MoE 路由训练行为
authors:
- Tomás Brogueira
- Marcos Treviso
- Miguel Couceiro
affiliations:
- Técnico, Universidade de Lisboa
- INESC-ID
- Instituto de Telecomunicações
- ELLIS Unit Lisbon
- Gandara AI
arxiv_id: '2610.06677'
url: https://arxiv.org/abs/2610.06677
pdf_url: https://arxiv.org/pdf/2610.06677
published: '2026-10-05'
collected: '2026-10-06'
category: Training
direction: MoE 路由 · 稀疏概率图训练行为
tags:
- MoE
- sparse routing
- entmax
- sparsemax
- normmax
- load balancing
one_liner: 通过可控实验揭示稀疏概率图的零输出能力不会自动带来 token 级专家参与，参与由阈值与 learned score 分布共同决定
practical_value: '- 若线上大模型采用 MoE，不要指望单独换用 sparse map 实现动态专家数；必须同时控制 router score scale（如学习
  temperature 或显式正则化），否则稀疏图可能在训练后回到稠密行为。

  - 推理阶段弹性专家预算：sparsemax 等稀疏图在 K 从 2 增到 8 时几乎不增加 loss（0.02 nats vs softmax 0.58），适合电商在线服务根据负载动态调整专家数而不显著损害效果。

  - 负载均衡目标需适配 sparse map：使用 full probabilities 时零概率专家得不到平衡梯度，建议在 sparse map 下测试不同的
  auxiliary probability（如 softmax 概率）或损失权重，实际效果不一定改善，需要验证。

  - 评估路由时区分 nominal load 与 contributor load，后者剔除零权重 filler，更能反映真实计算分布；normmax 名义负载均匀但实际
  contributor load 明显不平衡，工程实现应统计 contributor load 而非 nominal load。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：MoE 路由器通常用 softmax + top-K，每 token 固定使用 K 个专家，截断会丢弃大量概率质量。稀疏概率图（sparsemax、α-entmax、normmax）能给专家分配精确零值，使贡献者数量自适应，但训练中 router scores 会与 map 共适应，稀疏性未必存活。论文通过匹配的 300M/1B top-2 MoE LM 系统研究这一问题。

**方法关键点**：
- 训练 300M 和 1B 两个尺度，Llama 3 风格 backbone，每两层替换一层为 MoE，分别用 softmax、1.5-entmax、sparsemax、2-normmax 作为 router 概率图，其余架构、数据、负载均衡目标一致。
- 度量指标：discarded mass（未被选中专家的概率质量）、contributing experts K+（实际非零权重专家数）、nominal/contributor load CV、score scale 和 top-2 gap 分布。
- 每个稀疏图有固定的 singleton 阈值：1.5-entmax 的 top-2 gap ≥ 2 时只保留一个专家，sparsemax 和 normmax-2 阈值均为 1。

**关键结果数字**：
- 1B 模型：1.5-entmax 比 softmax 丢弃质量少 30%（δ=0.462 vs 0.661），但 K+ 几乎保持 2；sparsemax 保留最多质量（δ=0.153），K+=1.93；normmax-2 有 21.3% token 只用一个专家，K+=1.79。
- 训练中 router scores 适应 map：所有稀疏路由器 score RMS 仅 0.32-0.38，远小于 softmax 的 0.86；1.5-entmax 的 gap 99 分位 1.45，低于阈值 2，因此几乎不触发单专家。
- sparsemax 和 normmax 共享阈值 1，但 learned gap 分布不同（normmax 中位 gap 0.61 vs sparsemax 0.40），导致参与率差异。
- 推理时增加 K：softmax 从 K=2 到 K=8 损失增加 0.58 nats，sparsemax 仅增加 0.02；但降低 K=1 时所有图都损失约 0.10。
- 负载均衡：1.5-entmax 的 CV 最低，normmax 名义 CV 低但 contributor CV 高；用 softmax 概率做辅助负载均衡反而使 CV 上升。

最值得记住的一句话：MoE 路由的自适应专家参与必须联合设计 probability map 的阈值与 router score 分布，而不是只换 map。
