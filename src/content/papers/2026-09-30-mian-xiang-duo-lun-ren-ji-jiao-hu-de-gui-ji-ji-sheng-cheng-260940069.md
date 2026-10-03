---
title: 'Conversational Capture: A Trajectory-Level Framework for Evaluating Generative
  Engine Optimization in Multi-turn Human-Agent Interaction'
title_zh: 面向多轮人机交互的轨迹级生成式引擎优化评估框架
authors:
- Junwei Yu
- Jieyu Zhou
- Mufeng Yang
- Yepeng Ding
- Hiroyuki Sato
affiliations:
- The University of Tokyo
- UniConvo Inc.
- University of Tsukuba
- Hiroshima University
- National Institute of Informatics
arxiv_id: '2609.40069'
url: https://arxiv.org/abs/2609.40069
pdf_url: https://arxiv.org/pdf/2609.40069
published: '2026-09-30'
collected: '2026-10-03'
category: Eval
direction: 生成式引擎优化 · 多轮轨迹评估
tags:
- Generative Engine Optimization
- LLM
- RAG
- multi-turn evaluation
- conversational capture
- Pólya urn
one_liner: 提出轨迹级多轮评估框架，揭示早期引用带来的会话捕获效应及其对单轮排序的颠覆
practical_value: '- 电商/Agent 搜索助手评估不能只看单轮引用或点击：应构建多轮仿真器，将用户 query operator 与 history-conditioned
  retrieval 同时纳入。早期曝光的产品或品牌可能形成会话捕获，单轮排名会错估真实长期收益。

  - 可借鉴轨迹增益分解：把多轮收益拆为 direct、machine-side feedback、human-side feedback 三项，定位是检索历史偏差还是用户追问/信任带来的增量；在推荐或
  Agent 场景能指导 debias、reward shaping 与流量分配。

  - 用 Pólya urn / 强化过程做低成本离线消融，替代昂贵用户研究；尤其适合没有全链路线上数据时验证生成式推荐策略的累积效应。

  - 关注 compounding ratio 与 capture coefficient：若某商品/内容在对话早期被引用会显著提升后续被引概率，可主动利用该机制做新品冷启动，或反向做曝光公平性控制。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：GEO 通常按单轮评估：固定 query，衡量一次回答中的引用可见度。但人机信息搜寻是闭环——回答改变用户信念，影响下一轮 query，再决定检索内容。单轮指标可能系统低估或误判优化收益。

**方法关键点**：把多轮交互建模为两层闭环：机器侧历史条件检索（M1）与用户侧追问（M2）。定义轨迹级指标：累计会话可见度、轨迹增益的直接/反馈分解、反馈项的机器/人双侧拆分、capture coefficient、compounding ratio、misranking diagnostic。用 Pólya urn 强化过程理论证明：单轮评估下反馈项恒为 0；当 capture 形成，GEO 累计收益随对话长度超线性增长。

**关键结果**：模型推导示例中，T=10 时轨迹增益 L_T=2.68，直接项 1.20，反馈项 1.48（机器侧 0.85，用户侧 0.63）；compounding ratio ρ=2.23，超过 2；单轮与轨迹排名一致性仅 Kendall τ=0.4，单轮最优方法在轨迹排名中降至第三。
