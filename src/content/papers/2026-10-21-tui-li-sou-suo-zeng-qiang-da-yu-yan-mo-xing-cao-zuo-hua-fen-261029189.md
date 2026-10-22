---
title: 'Reasoning-Search-Augmented LLMs: An Operational Taxonomy, Benchmark Analysis
  and Controlled Evidence Synthesis'
title_zh: 推理-搜索增强大语言模型：操作化分类、基准分析与受控证据综合
authors:
- Biswas Poudel
- Nilson Chapagain
- Amit Kumar
- Xianshun Jiang
affiliations:
- Texas A&M University, College Station, TX, USA
- Texas A&M University–Corpus Christi, Corpus Christi, TX, USA
arxiv_id: '2610.29189'
url: https://arxiv.org/abs/2610.29189
pdf_url: https://arxiv.org/pdf/2610.29189
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: Agent 化推理-搜索增强 LLM 架构分类
tags:
- LLM
- RAG
- Reasoning
- Search Agent
- Taxonomy
- Benchmark
one_liner: 提出四架构轴+学习信号分类框架，系统梳理推理-搜索Agent设计与消融证据
practical_value: '- 构建电商搜索/客服 Agent 时，把检索从一次性 RAG 上下文改成迭代循环中的动作：显式维护 plan→query→retrieve→verify→stop
  状态机，可显著减少无依据答案；在商品知识库、用户评论等多源检索时，按 grounding strictness 分级校验（如硬性要求引用来源 vs 仅启发式）。

  - 训练搜索策略时优先用偏好优化或 RL 而非仅 prompt：同一架构下学习信号会显著改变搜索时机、停止条件和最终答案的 groundedness，业务数据允许时直接建模质量-成本
  tradeoff。

  - 做离线评估不要跨论文直接比较 SOTA：不同 backbone、retriever、corpus 协议不可混用，应关注 controlled within-study
  ablation；同时把 benchmark 难度与 RSA-loop 需求分开统计，避免简单题目屏蔽搜索行为差异。

  - 将检索耦合、控制器、知识源、grounding strictness 作为显式设计维度，便于在电商场景中快速替换组件（如从向量库切到商品图谱）并定位性能瓶颈。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM 受限于固定参数和有限上下文，静态检索仍可能生成与证据矛盾的内容，导致幻觉和过时信息。

**方法关键点**：综述将 step-by-step reasoning 与 interactive search 耦合的框架，这些系统把检索作为迭代 agentic loop 中的动作，交替执行规划、查询、检索、集成、验证与停止；提出四个架构轴：检索耦合、控制器设计、知识源、grounding 严格度；把学习信号（prompting、监督、偏好优化、强化学习）作为横切维度，强调同一架构不同训练方式会产生不同搜索/停止/grounding 行为；进一步区分 benchmark 难度与 RSA-loop 需求，综合受控消融研究和质量-成本差异，避免跨异构模型/检索器/语料/评估协议的错误汇总。

**关键结果**：没有给出新实验数据，主要贡献是提供统一分类视角和证据综合，帮助研究者厘清设计选择对行为和效率的影响。
