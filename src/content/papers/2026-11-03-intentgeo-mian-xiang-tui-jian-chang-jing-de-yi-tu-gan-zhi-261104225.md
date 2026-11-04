---
title: 'IntentGEO: Intent-aware Generative Engine Optimization for Recommendation'
title_zh: IntentGEO：面向推荐场景的意图感知生成式引擎优化
authors:
- Runlin Lei
- Shiqi Zhang
- Xiaokui Xiao
- Zhewei Wei
affiliations:
- Renmin University of China
- National University of Singapore
arxiv_id: '2611.04225'
url: https://arxiv.org/abs/2611.04225
pdf_url: https://arxiv.org/pdf/2611.04225
published: '2026-11-03'
collected: '2026-11-04'
category: GenRec
direction: 生成式推荐 · GEO 内容优化
tags:
- Generative Engine Optimization
- LLM
- Recommendation
- Prompt Optimization
- Intent-aware
- Citation Rank
one_liner: 提出 AMO，用固定推荐指令核心加学习追加策略，防止 prompt drift，提升多意图下 item 可见性
practical_value: '- 做 LLM 生成式推荐/电商 GEO 时，不要只评 topic-level 查询；用 P 系列（需求具体度）和 Q 系列（决策阶段）构造多
  intent slots，能暴露改写策略在强匹配请求下的负收益（P5 普遍负增益）。

  - Prompt optimization 容易把显式推荐指令漂移成促销话术（keywords/call-to-action），可借鉴 AMO 的 anchored
  结构：固定推荐核心（事实留存、推荐理由），只学习可追加的改写策略，避免 seed 性能被优化破坏。

  - 工程上可直接复用 citation-conditioned reward：用保留引用 rank 前后差、新引用、丢失引用的差分信号做 meta-optimizer
  的反馈和验证，比全 prompt 优化更稳定。

  - 若业务要接 agentic 推荐链路或闭源助手（如豆包 API），同一份改写可不重新训练直接迁移；AMO 在 agentic 和 Doubao 下均保持最高均值
  rank gain，说明 anchored prompt 有较好跨界面复用性。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
LLM 聊天和生成式引擎正成为推荐新入口，商品/内容提供方需要 GEO 来提升生成答案中的引用可见性。已有 GEO 研究主要是 content-centric，只评估通用查询；但推荐场景下同一个商品描述要服务不同用户意图——需求的粗细、探索还是最终选择。该工作把意图拆成 need specificity 和 decision progression，评估共享改写在不同意图下是否仍然有效。

**方法关键点**  
- 定义 IntentGEO：P 系列 5 级需求具体度，Q 系列 5 级决策推进，共 10 个 intent states；固定候选池比较 original vs rewritten 的 Delta Rank。  
- 诊断发现 MetaOpt 从 RecGEO seed 优化后，显式推荐指令消失，普遍转向 keywords/call-to-action 等促销策略，即 prompt drift。  
- 提出 AMO（Anchored Meta-Optimization）：把推荐核心指令 C 固定，只学习追加策略 A；优化目标为 citation reward，验证选最佳 [C;A]；初始化 A 为空，从 core 开始搜索。

**关键实验**  
Books/Retail/Videogames/Ragdoll 四域，200 test instances 扩展 2000 requests；gpt-4o-mini 为主骨干。AMO 总体平均 rank gain 1.12，比最强手工基线 RecGEO 的 0.95 高 18%，比最强学习基线 MetaOpt-Prog 的 0.83 高 35%；在 10 个 intent 状态中 9 个最优。消融：Core only 0.98，full-prompt opt 0.74，AMO 1.12。质量上 Salience 4.99，但 Consist 4.01 低于部分基线。Agentic 推荐中 AMO 0.832 vs RecGEO 0.730；Doubao 在线 API 上 AMO 1.048 vs AutoGEO 0.906。

**最值得记住的一句话**  
可见性优化要区分『保留推荐证据』和『学习可追加策略』，否则 prompt 优化会漂向促销话术并伤害强匹配请求。
