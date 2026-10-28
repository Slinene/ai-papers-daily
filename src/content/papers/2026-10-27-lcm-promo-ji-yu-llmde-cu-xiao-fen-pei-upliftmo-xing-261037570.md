---
title: 'LCM-Promo: An LLM-Based Uplift Model for Promotion Allocation'
title_zh: LCM-Promo：基于LLM的促销分配Uplift模型
authors:
- Nesta Midavaine
- Floris Fok
- Paulo Mendes
- Joao Silva
- Önder Akaçık
- Dimas Lima
- Zülküf Genç
affiliations:
- Prosus
- iFood
arxiv_id: '2610.37570'
url: https://arxiv.org/abs/2610.37570
pdf_url: https://arxiv.org/pdf/2610.37570
published: '2026-10-27'
collected: '2026-10-28'
category: RecSys
direction: LLM 微调 · 促销 Uplift 建模
tags:
- LLM
- Uplift Modelling
- Promotion Allocation
- Monotonic Response
- Large Commerce Model
one_liner: 微调LLM预测转化阈值，构造单调促销响应曲线，线上转化+1%成本-6%
practical_value: '- 单token阈值解码构造单调响应曲线：促销/优惠券分配中，用LLM预测折扣标识符，将输出分布解释为潜在转化阈值PMF，通过累积概率得到自然单调的响应曲线，保证uplift估计的单调性，避免后处理强制单调。

  - 用上下文作为prompt输入代替分cell建模：将配送班次、日期、用户表示等直接序列化进prompt，替代传统EWMA按segment-promotion分cell预测，使分配空间从50
  segment扩展到1000+集群，从10钱包配置扩展到100万+促销组合，适合需要细粒度上下文的促销场景。

  - 工程化降本：预计算用户表示并缓存，每天批量推理两次，对用户分组后随机采样估计平均响应曲线，使用自托管vLLM + BESH批量端点，8张H200每天仅运行1小时即可支撑生产，证明了LLM在中等规模推理任务上的可行性。

  - 微调标签需与预训练目标兼容：waterfall augmentation（阈值顺序多标签软目标）因与next-token预训练目标冲突导致性能大幅下降，说明在LLM微调时不要随意改变输出分布形态，保持单token交叉熵更稳妥。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
促销分配是电商核心决策，需要精准估计用户在不同促销强度下的增量转化（uplift）。传统Segment-EMA按segment-promotion分cell做指数加权平均预测，每个新折扣、细分或上下文都需要独立探索，限制了粒度扩展。LLM天然擅长序列化用户表示和会话上下文，为促销uplift建模开辟了新路径。

**方法关键点**  
- 将促销响应估计转化为单token预测：4B参数稠密LLM微调后直接输出折扣标识符（或无购买标识符）。
- 解码时把下一个token分布重新归一化为潜在转化阈值T的概率质量函数，T=dk表示用户需要的最小折扣才转化，T=∞表示任何折扣都不转化。
- 通过累积概率得到单调非递减的促销响应曲线rk(x)=P(T≤dk|x)=Σqj(x)，从构造上保证单调性，且不购买质量使rK(x)<1。
- 输入提示包含system prompt、会话上下文（日期、配送班次）、预计算的LCM用户行为摘要、以及映射为字母标识符的折扣选项。
- 训练使用交叉熵，非转化者标签为a∅；推理时限制valid token集合并重新归一化。
- 评估的waterfall augmentation（将阈值顺序编码为多标签软目标）因与next-token预训练目标冲突而效果更差。

**关键实验**  
- 生产A/B测试：iFood巴西流失召回场景，一个月，90%对照组Segment-EMA，10%治疗组LCM-Promo，两臂使用相同预算约束和线性优化分配器。结果：转化率+1%，促销成本-6%，且分配空间从约50 segment扩展到1000+集群，从10种钱包配置扩展到100万+促销组合。
- 离线RCT评估：固定促销下对比Uplift Random Forest（causalml），AUUC和Qini相当，Uplift@30略低，验证了模型有效性但生产设置更复杂。
- 工程实现：每天两次批量推理（午餐/晚餐），用户分组后随机采样估计平均响应曲线，使用自托管vLLM + BESH，8张H200每天运行1小时。

**最值得记住的一句话**  
用LLM的单token预测构造单调uplift曲线，把促销响应建模转化为阈值分布学习，同时实现细粒度上下文扩展和生产成本控制。
