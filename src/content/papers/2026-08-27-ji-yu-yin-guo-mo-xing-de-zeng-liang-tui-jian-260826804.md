---
title: Incremental Recommendation via Causal Models
title_zh: 基于因果模型的增量推荐
authors:
- Athanasios Vlontzos
- David Gustafsson
- Michael O'Riordan
- Ciarán M. Gilligan-Lee
affiliations:
- Spotify
- Imperial College London
- University College London
- Hologen
arxiv_id: '2608.26804'
url: https://arxiv.org/abs/2608.26804
pdf_url: https://arxiv.org/pdf/2608.26804
published: '2026-08-27'
collected: '2026-08-28'
category: RecSys
direction: 因果推荐 · uplift 增量建模
tags:
- Causal Recommendation
- Uplift Modeling
- Deep Twin Networks
- Holdback
- Impression Efficiency
- Calibration
one_liner: 利用已有 holdback 数据扩展生产推荐模型为因果双头模型，以双阈值策略减少 7% 曝光且不损消费
practical_value: '- 复用现有随机 holdback/对照组流量做 uplift：不需要新数据，直接把生产多任务模型改成 shared-trunk
  + treated/organic 双 head，用分区 loss 保证两个输出语义清晰；适用于电商推荐、广告重定向、消息 push 等场景。

  - 警惕归因窗口不一致：点击/转化窗口和自然转化窗口不同时，不要直接相减估计 CATE；双阈值策略（预测转化高且自然转化低才投放）能绕过该问题，并给业务一个可解释的
  θ0 杠杆控制曝光量。

  - 阈值策略依赖校准：联合训练 holdback 数据能改善 treated head 校准，尤其高分段；建议上线前监控校准曲线，否则阈值调优不可靠。

  - 生产结果说明约 93% 曝光已是增量，可挖掘的非增量曝光约 7%；在效率优化项目里，先用 holdback 数据量化 always-takers 占比，再决定投入。'
score: 9
source: arxiv-stat.ML
depth: full_pdf
---

动机：推荐曝光是稀缺资源，传统模型最大化点击/播放概率，会系统性偏好高亲和用户（always-takers），他们即使没有推荐也会消费，导致曝光非增量。要识别增量，需回答反事实：没有推荐用户会怎么做？Spotify 已有 holdback 随机实验提供有机行为样本，但存在归因窗口不匹配：treated 用短直接响应窗口，holdback 用两天有机窗口，导致 CATE 直接相减无效。

方法关键点：
- 在现有多任务 shared-trunk 生产模型上扩展为 Deep Twin Network：保留共享 trunk，新增 holdback head 预测有机流概率 p0，原 treated head 预测推荐后流概率 p1。
- 采用分区 loss：treated 样本只更新 treated head 和共享 trunk，holdback 样本只更新 holdback head 和共享 trunk，避免两种归因定义相互污染。
- 不直接估计 CATE，改用双阈值策略：仅当 p1 ≥ θ1 且 p0 ≤ θ0 时投放推荐；θ0 直接控制效率与触达的权衡。
- 完全复用现有随机 holdback 数据，无需新增数据收集。

关键实验：在 Spotify Home 推荐位进行生产级 A/B 测试，百万用户，三臂：Control（生产模型按 p1 阈值）、Treatment-Model（新模型按 p1 阈值）、Treatment-Causal（双阈值）。对比 Treatment-Causal vs Treatment-Model：推荐曝光减少 7.1%（95% CI [-7.2%, -6.9%]），推荐内容消费变化 -0.37%（[-0.86%, +0.21%]）不显著。校准曲线显示，联合训练 holdback 数据改善了 treated head 校准，尤其高预测概率区；holdback head 也校准良好。

最值得记住的一句话：不要将模型预测概率直接当作增量；在业务中利用已有 holdback 随机流量和双阈值解耦“会不会点击”与“不推也会不会点”，能在不损失消费的前提下砍掉非增量曝光。
