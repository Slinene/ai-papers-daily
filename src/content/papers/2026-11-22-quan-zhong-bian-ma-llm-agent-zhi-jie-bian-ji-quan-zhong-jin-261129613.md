---
title: 'Weight Coding: Evolving Web-Scale Recommenders through Direct Weight Edits
  with LLM Agents'
title_zh: 权重编码：LLM Agent 直接编辑权重进化大规模推荐系统
authors:
- Junpeng Hou
- Jiaxing Qu
- Derek Cheng
- Jaewon Yang
- Abhinav Naikawadi
- Karthik Subbian
affiliations:
- Pinterest, Inc.
arxiv_id: '2611.29613'
url: https://arxiv.org/abs/2611.29613
pdf_url: https://arxiv.org/pdf/2611.29613
published: '2026-11-22'
collected: '2026-11-24'
category: RecSys
direction: LLM Agent 直接编辑推荐模型权重
tags:
- Weight Editing
- LLM Agent
- Recommender Systems
- Gradient-Free Optimization
- Two-Tower Retrieval
- Model Evolution
one_liner: 提出 Weight Coding，用 LLM Agent 直接编辑推荐模型权重，仅用约 1/4 微调 GPU 小时将 Image Search
  召回 R@10 最大提升 15 个百分点
practical_value: '- 对电商/推荐系统的召回或排序模型，可以绕过全量微调，直接编辑 LayerNorm gain、branch output、shared
  bias 等少量参数实现快速迭代；该方法在 Pinterest 上仅需约 1/4 GPU 小时，适合高频实验。

  - 构建缓存评估引擎：缓存模型前向结果，编辑后仅重算受影响模块，避免反向传播，支持进化策略快速搜索；可复用到大规模推荐模型的 post-hoc 优化。

  - 使用 steer edit 加一个标量控制新鲜度/商品曝光：在召回头 bias 上沿概念方向（如 fresh/non-fresh item embedding
  差值）调整，可精准控制 top-N 中特定 segment 占比，替代部分预检索排序策略。

  - LLM Agent 工作流（scan → filter → edit/search → validate）适合作为自动化模型开发框架，结合工程师审核上线，可降低人工调参成本；注意独立编辑组合时需重新搜索适配，否则可能互相抵消。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

动机：
传统大规模推荐系统演化主要靠重训练或微调，每次迭代需要数天、数百 GPU 小时，且梯度更新间接移动大量权重，难以对特定业务目标进行精细控制。权重本身是更直接的切入点，但缺乏系统性方法。

方法关键点：
- Weight Coding 将模型演化视为对权重的可执行编辑，LLM Agent（Opus 5.5）分析模型结构和参数，在评估反馈引导下提出、执行并迭代编辑。
- 提供可复用的编辑原语：rescale、reset、remove、compress、interpolate、steer、search，编辑粒度从单个 bias 到整个模块。
- Agent 工作流：scan（扫描模块级编辑）→ filter（过滤跨日反转的编辑）→ edit/search（稳定效果指导假设或进化策略搜索少量参数）→ validate（保留 held-out 天数、多指标、悲观 tie-breaking 等避免奖励黑客）。
- 缓存 edit-evaluate 引擎只做前向计算，缓存中间输出，编辑后局部重算，极大加速搜索；ES 搜索约 190k 候选，仅需 8.6 GPU 小时/轮。

关键实验：
- 主模型 Pinterest Image Search 147M 两塔检索器。直接重置 DHEN 模块的 LayerNorm 增益和 offset 获 +10.1 个百分点 recall@10；搜索 5 个 mixing 矩阵（2064 参数）获 +13.7；结合 head bias 重新搜索得 L07，提升 15.0 个百分点（+24% 相对），held-out 日最差 +13.8，GPU 小时仅为微调 24.6%。
- 随机初始化整个 13.6M DHEN 模块后，仅搜索 2448 个 mixing/LayerNorm 参数仍超生产 9.8 点，说明可重建有效计算。
- 跨漏斗：PinRec 生成式检索无序 R@1 +2.31 点（bias 编辑与 checkpoint 插值）；1.37B 排序器通过削弱 expert 提升 utility NDCG +0.53%。
- 在线 A/B：save 型目标搜索使 saves per user 提升 8.4%–10.7%，关闭/长点击等指标符合目标。

最值得记住的一句话：
直接编辑少量关键权重可以在不重新训练的情况下显著改进生产推荐模型，并实现精准的业务行为控制。
