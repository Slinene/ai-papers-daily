---
title: 'Beyond Self-Critique: Epistemic Convergence Control for Multi-Agent Research
  Verification'
title_zh: 超越自我批判：多智能体研究验证的认知收敛控制
authors:
- Chrisantus Eze
affiliations:
- Oklahoma State University
arxiv_id: '2611.27839'
url: https://arxiv.org/abs/2611.27839
pdf_url: https://arxiv.org/pdf/2611.27839
published: '2026-11-20'
collected: '2026-11-23'
category: MultiAgent
direction: 多智能体协作验证与收敛控制
tags:
- Multi-Agent
- Convergence Criterion
- Hallucination
- Evidence Grounding
- NLI
- LLM Debate
one_liner: 提出非对称角色架构与 Belief-Delta 收敛准则，降低多智能体验证中的自评偏差并节省推理计算
practical_value: '- 非对称角色设计可迁移到推荐系统多智能体审核：让 Advocate/Skeptic/Arbitrator 承担相反认知指令，降低同模型角色间嵌入相似度，减少自评偏差，适用于商品描述安全审查、广告文案合规校验等场景。

  - Belief-Delta 收敛准则替代固定迭代轮次：在需要多轮生成/评审的流程（如商品标题优化、搜索词改写）中，用相邻轮信念差异阈值提前停止，可显著降低 LLM
  调用成本，实验中减少 2.4 倍调用且零过度迭代。

  - NLI 审计器作为幻觉防护：对模型输出中引用的证据（如商品卖点、用户评论摘要）用独立 NLI 分类器校验，确保锚定真实片段，可集成到 RAG 问答或生成式推荐的证据追溯模块。

  - 组合方案可复用到电商事实核查：将对抗式辩论与证据审计结合，在知识密集型场景中降低虚假信息风险，同时提供可追溯的验证链路。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

动机：多智能体 LLM 辩论用于科学声明验证时，来自同一基座模型的角色共享潜在表示，导致结构性自我批判偏差；固定轮次协议要么过早停止、要么在收敛后浪费推理计算。

方法：提出 VerifyAgent 框架。首先引入非对称角色架构——Advocate（倡导）、Skeptic（质疑）、Arbitrator（仲裁），赋予对立认知指令，显著降低角色嵌入相似度（0.852 vs 对称 MAD 的 0.918），并发现更多争议主张（22.0% vs 15.4%）。其次提出 Belief-Delta (∆B) 收敛准则，基于证据变化判断是否终止迭代，消除过度迭代（0.0% vs Fixed-3 的 62.5%），并将 LLM 调用次数降低 2.4 倍。最后将每个支持主张锚定到逐字文献片段，由独立 NLI 分类器审计，幻觉率 21.7%（对比 Self-Refine critic 的 25.9%，p=0.61），同时建立可审计的证据基础。

结果：在 DeepSeek-R1-32B 上，跨 40 个研究假设共 200 次运行，VerifyAgent 在计算效率与严格认知验证之间取得平衡。
