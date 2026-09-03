---
title: 'CORAL: An LLM-Native Harness for Production Recommender Systems'
title_zh: CORAL：面向生产推荐系统的 LLM 原生闭环优化框架
authors:
- Muhammad Rafay Azhar
- Yuhang Zhou
- Gilbert Jiang
- Yuchen Wang
- Rahul Sharma
- Matthew DeSousa
- Jiayi Liu
- Xin Guo
- Lizhu Zhang
- Xiangjun Fan
affiliations:
- Meta AI
arxiv_id: '2609.02730'
url: https://arxiv.org/abs/2609.02730
pdf_url: https://arxiv.org/pdf/2609.02730
published: '2026-09-02'
collected: '2026-09-03'
category: Agent
direction: Agent 闭环优化推荐系统控制面
tags:
- LLM Agent
- Recommender Systems
- Closed-Loop Optimization
- Resource Allocation
- A-B Testing
- Production Systems
one_liner: 用 LLM agent 闭环优化推荐系统控制面资源配置，以极低成本实现在线 A/B 验证的 engagement 提升或成本节省
practical_value: '- 可把 LLM agent 用于推荐系统资源/预算分配的闭环优化（召回源预算、流量分群 serving 档位、广告库存分配等）；关键是不让
  LLM 直接改线上参数，而是让它输出结构化 proposal，由确定性约束优化器投影到可行集。

  - 架构上模仿 observation / assessment / decision 三层记忆，保存最近 3 个 cycle 的原始指标、模型判断和决策结果，让
  agent in-context 根据自己上次动作的效果调整，不用 retrain；对非平稳线上环境有效。

  - 固定决策 cadence（如 3 天）并用 A/B 实验测每个配置的增量，把测量结果写回 memory 作为 attribution，避免噪声误导；初期可先在低风险控制面（预算
  multiplier、serving tier）小步跑，再逐步扩大自主范围。

  - 成本极低：每个 cycle 仅十几次 LLM 调用、几千 token，与用户量无关，适合亿级流量的电商/广告推荐；如果业务有硬资源约束，优先把 LLM agent
  用于配置优化而不是 per-item 生成。'
score: 10
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
生产推荐系统的性能不仅取决于排序模型，还取决于大量控制面参数——检索预算、serving 策略、缓存、分群 treatment 等。这些参数通常由工程师手工设定，迭代受限于人力和实验数量；随着内容、用户行为和上游模型漂移，配置会逐渐偏离最优，尤其对低信号和新用户更明显。LLM agent 在推荐中的应用多集中于排序或用户建模，较少直接闭环优化线上系统。

**方法关键点**
- 形式化为部分可观测、非平稳、带约束的持续优化：每轮 t 选择配置 s_t，在成本 c_t(s_t)≤B 下最大化 engagement J_t(s_t)。
- 控制单元为检索源预算 multiplier（连续）或用户分群 serving treatment（离散）；agent 观察 per-unit 指标及变化，结合 memory 中的 observation、assessment、decision 三类存储。
- 工具链包括分析、检索、归因、约束优化器和部署；LLM 只负责推理和提出有界调整，由确定性优化器投影到预算可行集，保证任何输出均不超预算。
- 固定 cadence k=3 天，memory horizon m=3；每个配置部署后通过 A/B 实验测量效果并写回 memory，下一轮 in-context 改进，无需微调。

**关键实验结果**
- 视频推荐检索预算分配：三轮循环，最终配置相比对照，全用户视频观看 sessions +0.16%、watch time +0.15%，最大市场 sessions +0.77%；新低信号用户 sessions +0.23%，均无额外 serving 成本。
- 服务容量分配：第一轮节省数百万美元年化容量支出，第二轮把节省扩大 44%，engagement 无显著下降。
- 每轮仅约 10 次 LLM 调用、数千 token，端到端成本约几十美元，与流量无关。

**最值得记住的一句话**
把 LLM agent 放在推荐系统的控制面而不是 item 面上，用闭环 A/B 反馈和约束优化器，能让资源配置随环境漂移自动调整，把工程师数周的调参周期压缩到几天。
