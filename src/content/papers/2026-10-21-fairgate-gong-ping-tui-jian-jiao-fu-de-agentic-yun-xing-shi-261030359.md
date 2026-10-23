---
title: 'FAIRGate: Agentic Runtime Policy Selection and Verified Repair for Fairer
  Recommendation Delivery'
title_zh: FAIRGate：公平推荐交付的 Agentic 运行时策略选择与验证修复
authors:
- Navkar Jain
- Enock Ayiku
- Kenneth Fletcher
affiliations:
- University of Massachusetts Boston
arxiv_id: '2610.30359'
url: https://arxiv.org/abs/2610.30359
pdf_url: https://arxiv.org/pdf/2610.30359
published: '2026-10-21'
collected: '2026-10-23'
category: RecSys
direction: Agent 策略选择 + 公平推荐交付控制
tags:
- Fairness-aware Recommendation
- Agentic Policy Selection
- Exposure Fairness
- Verified Repair
- LLM Auditability
- Runtime Control
one_liner: 在推荐 top-K 交付中加 agentic 策略选择层，从预定义公平策略库按运行时上下文选择并执行验证修复
practical_value: '- 在电商/广告重排层引入「固定 policy library + LLM 只做选择」的模式，避免 LLM 直接改排序；策略可定义为长尾曝光、品类/商家曝光平衡、集中度上限、校准保护、弃权。

  - 用 deterministic validator 做最后把关：相关性损失、元数据覆盖、校准漂移、审计 trace 全部检查，不满足就 abstain/relax，防止公平优化过度损伤
  GMV/CTR。

  - 审计 trace 设计成 typed evidence keys，文案只从验证过的 trace 生成，可大幅降低 LLM 幻觉和敏感属性泄漏；在合规审计、可解释推荐中可直接复用。

  - 实现上用结构化生成/JSON schema 约束 agent 输出，并要求策略选择必须引用具体 metric trigger，使线上策略选择可回放、可诊断，避免
  LLM 自由输出公平判断。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
线上推荐不同请求的候选池、物品元数据、曝光欠账、用户偏好和效用预算都在变化，固定公平干预（训练目标或静态重排）难以应对。纯 LLM agent 灵活但易产生不稳定、不可审计的公平判断。因此需要把公平交付建模为受控的运行时策略选择问题。

**方法关键点**
- 在 base ranker 与最终 top-K 之间设置 FAIRGate 控制层，维护预定义 policy library：长尾曝光下限 PT、物品组曝光平衡 PG、集中度控制 PC、校准保护 PCal、弃权 PA。
- Agent 只从库中选策略并引用 metric trigger，不能发明公平目标；输出为 JSON-like 结构化对象。
- 修复规划给定 swap 计划、相关性下限、优先级和回退路径；目标函数为 S(i,u)=αs_u(i)+βd_T(i)+γd_G(i)-λΔCal(i,u)。
- 确定性 executor 执行候选替换，validator 检查相关性损失、可行性、元数据覆盖、校准漂移和审计约束；通过则 deliver，否则 relax 或 abstain。
- narration agent 只接收 verified audit trace 生成证据链接解释，降低无依据公平声明。

**关键结果**
在 MovieLens 1M 1000 用户采样、BPR-MF 为基座、K=10、Llama 3.1 8B 的设置下：
- Agentic FAIRGate 将 LT-Cov@10 从 0.1055 提升至 0.1282（+21.52%），Policy Pass 从 fixed-order 0.0910 提升至 0.6070，NDCG@10 0.0233 接近 fixed-order 0.0236。
- 消融显示 validator 拒绝率 0.0170，fixed policy order pass 为 0.0000 且 NDCG 损失更高。
- 策略选择分布：PG 601/1000、PC 310、PCal 88、PT 1，说明上下文相关选择确实发生。
- 审计接地解释将 unsupported claims 从 1.0000 降到 0.0959，evidence coverage 0.9129。

**最值得记住的一句话**
公平推荐交付可以做到「策略选择层自适应、执行层确定性、解释层可审计」。
