---
title: 'From Head to Tail: Asymmetric Knowledge Transfer in Long-tail Recommendation
  with Generative Semantic IDs'
title_zh: 面向长尾推荐的生成式语义ID非对称知识迁移框架
authors:
- Chenyi Yan
- Ruocong Tang
- Xing Fang
- Yang Huang
- He Guo
- Jing Wang
affiliations:
- Alibaba Group
- Beijing University
arxiv_id: '2605.23310'
url: https://arxiv.org/abs/2605.23310
pdf_url: https://arxiv.org/pdf/2605.23310
published: '2026-05-22'
collected: '2026-05-25'
category: RecSys
direction: 长尾推荐 · 生成式语义ID
tags:
- Long-tail Recommendation
- Generative Semantic IDs
- Multimodal LLM
- RQ-VAE
- Asymmetric Knowledge Transfer
- CTR Prediction
one_liner: 用MLLM生成语义ID并聚类，以非对称对比学习从头部向尾部迁移知识，在线CTR+2.76%、GMV+3.47%
practical_value: '- **用语义ID实现软聚类，而不是硬分组**：通过RQ-VAE离散化MLLM嵌入生成层次语义ID，控制高碰撞率让相似物品/用户共享ID，形成自然语义簇。可借鉴到商品库冷启动与长尾物料分组，替代人工构建的统计分组。

  - **非对称对比学习防止噪声污染头部**：在簇内对比中，头部嵌入作为teacher，尾部嵌入作为student，使用stop-gradient + 非对称权重，让知识从头部流向尾部而不反向。推荐系统里任何“用头部经验辅助尾部”的场景（如新广告、新活动）都可复用这一模式。

  - **活动感知门控动态融合簇表示与个体表示**：将ID嵌入分解为簇级共享部分和个体特有部分，并用用户/物品交互活跃度特征学习融合权重。对于低活跃用户或曝光极少的新品，模型自动更依赖簇表示，从而缓解稀疏问题；在通用推荐模型中可视为一种动态冷热分离策略。

  - **簇级与实例级双视图特征聚合**：同时保留细粒度交互历史和簇粒度统计特征，并通过另一个活动感知门控自适应融合。工程上，簇级特征通过top-level语义ID做硬检索以控制在线耗时，值得迁移到需要“类似人群/商品群体”信息做特征增强的场景。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：电商平台的长尾问题不仅导致尾部物品和低活用户表征学习困难，传统方法还常因盲目融合尾部噪声而损害头部效果。现有方案或依赖稀疏的图传播，或使用低质样本增强，或孤立处理尾部，均未系统解决“如何让头部信号单向滋养尾部，同时避免尾部噪声反向影响头部”这一不对称知识迁移难题。

**方法关键点**：
- **两阶段语义ID生成**：先对齐多模态内容与协同信号的MLLM（GME-Qwen2-VL-7B）提取物品嵌入；再用有监督微调LLM（Qwen3-30B-A3B）基于历史行为序列推导用户兴趣表示；最后通过RQ-VAE离散化为层次语义ID，形成语义簇。
- **簇引导自适应嵌入**：每个ID分解为簇嵌入cᵢ（共享簇内共性）和个体嵌入dᵢ（保留ID特异信息）；设计非对称InfoNCE损失，头部→尾部方向使用更大权重且对头部梯度截断，确保知识单向迁移；加入软正交正则化防止信息冗余；用活动特征门控网络学习融合权重rᵢ，低活ID自动偏向簇嵌入。
- **层次化特征聚合与自适应融合**：分别按下钻实例级（细粒度ID特征+行为序列+目标注意力）和簇级（簇内均值特征+簇级序列检索+注意力）构建两套特征视图；再通过另一个活动感知门控网络自适应融合，预测最终CTR。

**关键实验**：在手机天猫点击日志数据集（3600万用户，3亿物品，2个月数据）上，定义<5次交互为用户尾部，曝光<10次为物品尾部，22.4%样本为长尾。AUC提升0.35%，GAUC提升1.53%，尾部样本提升更显著。在线A/B测试两周，10%流量，CTR+2.76%，GMV+3.47%。消融表明：去掉个体嵌入致AUC下降0.46%，去掉簇嵌入尾部GAUC下降1.2%，实例级特征移除引起AUC下降1.14%，验证了设计的必要性。

**最值得记住的一句话**：让头部知识单向浇灌尾部、同时保护头部不受噪声干扰的非对称迁移，是长尾推荐落地的关键，语义ID簇为这种迁移提供了天然载体。
