---
title: Deep-learning Causal Retrieval Optimization for Efficient e-commerce Distribution
  in Pinterest
title_zh: 深度学习因果检索优化：Pinterest高效电商分发触发策略
authors:
- Junpeng Hou
- XianXing Zhang
- Sai Xiao
- Derek Cheng
- Darren Reger
- Olafur Gudmundsson
- Mehdi Ben Ayed
- Zhiqing Rao
- Huizhong Duan
affiliations:
- Pinterest, Inc.
- LinkedIn
arxiv_id: '2607.14161'
url: https://arxiv.org/abs/2607.14161
pdf_url: https://arxiv.org/pdf/2607.14161
published: '2026-07-14'
collected: '2026-07-17'
category: RecSys
direction: 因果学习 · 检索触发策略优化
tags:
- Causal Inference
- Uplift Modeling
- Offline Replay
- Multi-task Learning
- Retrieval Optimization
- E-commerce
one_liner: 将检索级触发决策建模为因果提升问题，利用随机化数据与双重稳健多任务学习，离线重放选择阈值，线上大幅缩减购物触发并提升整体参与度
practical_value: '- **触发决策因果化**：将“是否触发某类候选集”视为增量预估问题，而非相关性排序，可直接用于电商推荐中控制商品卡片、广告坑位的展示频次，避免过度分发损害用户体验。

  - **反事实数据收集与DR训练**：通过随机化Holdout流量获得无偏反事实数据，使用Doubly Robust伪结果训练uplift模型，配合多任务学习与事件级上采样，可复用到消息推送、广告投放等稀疏事件的触发决策中。

  - **离线重放评估与阈值选择**：基于随机化日志的线性时间复杂度重放算法，提供不同阈值下的业务指标曲线，与线上效果高度一致，无需频繁线上实验即可迭代策略，工程成本低。

  - **解耦学习与决策**：模型只学习潜在结果和提升信号，策略阈值通过离线重放选择，二者解耦，使产品侧可审计、可解释地调整触发力度，无需重新训练模型。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：Pinterest电商内容分发面临平衡问题——未加区分的购物触发在提升电商成交的同时，会降低Pin保存等非购物参与度。传统静态规则无法适应个性化需求，因此需要学习一种意图感知的触发策略，在检索早期决定何时触发购物候选生成器。

**方法关键点**
- **数据收集**：设立随机化Shopping Holdout，以50/50对每个请求随机决定是否触发购物CG，收集反事实日志。
- **模型架构**：基于DCNv2 + MMoE的多任务深度模型，输入包含用户、上下文、查询pin的预训练嵌入，同时预测处理组、对照组的潜在结果、倾向性得分和提升值。
- **训练损失**：核心由四项组成——校准后的结果BCE损失、倾向性损失（可选）、uplift与两臂结果差值的一致性正则，以及切换式双重稳健伪结果的MSE损失。
- **策略**：生产采用单值策略（SV，仅用触发组概率预测），uplift策略（DP）用作稳定性诊断，阈值通过离线重放确定。

**关键结果**
- **离线**：结合DR loss和更大模型后，在P@K等决策对齐指标上显著优于基线，离线重放预测与线上触发率误差<2%。
- **线上**：在Pinterest Closeup场景，最高可降低85%的购物触发，同时购物下层会话保持中性，站内成功策展+0.26%，中间漏斗会话+0.46%，Closeup表面Pin保存+1.10%，基础设施成本节省近50万美元/年。

**一句话**：通过随机化日志、双重稳健uplift训练和离线重放，可以在不牺牲核心指标的前提下，大幅缩减检索触发量并提升整体用户体验，为级联推荐系统的早退优化提供了完整且可复现的工业化方案。
