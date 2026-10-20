---
title: Learning Complementary Agent Groups via Task Hypergraphs for Next-POI Recommendation
  with Missing Modalities
title_zh: 基于任务超图学习互补智能体组用于缺失模态下一兴趣点推荐
authors:
- Jinze Wang
- Yuze Liu
- Liang Yuan
- Gaoyuan Du
- Xiaohang Xu
- Yong Xiang
- Jiong Jin
affiliations:
- Swinburne University of Technology
- Australian Catholic University
- University of Tennessee
- University of Tokyo
- Deakin University
arxiv_id: '2610.25801'
url: https://arxiv.org/abs/2610.25801
pdf_url: https://arxiv.org/pdf/2610.25801
published: '2026-10-19'
collected: '2026-10-20'
category: RecSys
direction: 多 Agent 任务超图驱动的 POI 重排
tags:
- MultiAgent
- LLM
- POI Recommendation
- Missing Modalities
- Hypergraph
- PPO
one_liner: 用任务超图动态选择互补 Agent 组，在缺失多模态 POI 重排中带来 8.4–9.1% NDCG@20 相对提升
practical_value: '- 可把重排拆成明确任务类型（全局状态更新、候选对比、缺失模态补偿），再用超边记录 task-target-members，既便于策略学习，也便于做成本约束和消融。

  - 采用固定角色 Agent + 共享冻结 LLM + 角色级 LoRA，并用任务局部状态隔离多任务执行，适合在线 Serving 中复用同一 LLM 骨干而不互相污染。

  - 广播候选级共享结果再指导下轮操作，比各 Agent 独立评分后融合或单控制器顺序取证据更有效；在复杂候选排序场景可以用类似的成员间共享证据机制。

  - 两阶段训练值得复用：先监督 warm-up 学 executor 和 ranking head，再固定 executor 用 PPO 学 task/member/operation/stopping
  策略，并把 computation cost 直接加入 reward，得到可解释的质量-成本曲线。

  - 缺失模态处理建议显式保留 mask，区分“缺失”和“零值特征”，只利用可用证据更新候选状态，不改原始模态；这比丢弃 mask 或插补更稳健。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
多模态 POI 推荐中文本和图片经常缺失，而同一缺失条件下，不同用户历史会导致不同的最优证据组合：轨迹、时空、偏好或文本分析。已有 LLM Agent 方法要么使用固定 Agent 组，要么单控制器顺序获取证据，难以按请求和任务选择互补的 Agent。

**方法关键点**
- 每个请求构建 task hypergraph：节点是 6 个固定角色 Agent（长期偏好、短期轨迹、时空、文本、视觉、协同检索），超边表示一个任务实例，记录任务类型、目标候选和成员。
- Policy 先选任务类型与目标：request-state update、candidate comparison、semantic compensation；再用 Set Transformer 对已选成员集合建模，逐成员邀请，形成互补组。
- 执行阶段成员共享候选级结果；共享消息经 GRU 更新候选/任务状态，并指导下轮操作类型选择。任务结束后更新参与 Agent memory 和候选 state。
- 共享 ranking head 在 base ranking 上产生 correction；两阶段训练：先监督 warm-up 学习 executor 和 ranking head，再固定 executor 用 PPO 学 task/member/operation/stopping 策略，reward 包含排名 utility 减去 computation cost。

**关键实验**
在 Gowalla-CA、Foursquare-NYC/TKY 三个自然缺失 benchmark 上，对比 Flashback/STAN/GETNext/LRMM/HMoRec/MAGNET/HyperAgent4POI/MMA/Agent4POI 等。CATH 的 NDCG@20 相对最强基线 HyperAgent4POI 提升 8.4–9.1%（绝对值 +2.0–2.5pp）；联合 50% masking 下仍保持 +2.6pp。消融显示 set-conditioned 组选择优于独立评分和 direct group，共享证据交换优于 no-exchange + fusion 和单控制器。成本曲线表明 0.61 normalized cost 下达到 .301 NDCG。

**最值得记住的一句话**
把 Agent 选人问题建模为任务超图上的组选择，并用共享候选级证据驱动组内后序操作，是平衡效果与计算成本的关键。
