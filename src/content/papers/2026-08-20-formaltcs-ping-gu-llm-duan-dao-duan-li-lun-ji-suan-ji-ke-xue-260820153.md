---
title: 'FormalTCS: Benchmarking End-to-End Frontier Formal Theoretical Computer Science
  Research of Large Language Models'
title_zh: FormalTCS：评估 LLM 端到端理论计算机科学研究能力的基准
authors:
- Dingzirui Wang
- Xuanliang Zhang
- Keyan Xu
- Qingfu Zhu
- Wanxiang Che
affiliations:
- Harbin Institute of Technology
arxiv_id: '2608.20153'
url: https://arxiv.org/abs/2608.20153
pdf_url: https://arxiv.org/pdf/2608.20153
published: '2026-08-20'
collected: '2026-08-23'
category: Eval
direction: LLM 端到端科研能力评估
tags:
- FormalTCS
- autoformalization
- LLM benchmark
- theoretical computer science
- Lean theorem proving
- research automation
one_liner: 构建专家验证的 FormalTCS 基准，评估 LLM 在 STOC/FOCS/SODA/COLT 前沿 TCS 研究上的端到端能力，揭示自动形式化与科研品味是主要瓶颈。
practical_value: '- 自动形式化是瓶颈：将自然语言需求转化为精确形式规范（如 SQL、DSL、策略规则）的能力远弱于在给定规范下的执行/证明能力。搭建
  Agent 系统时，不要假设 LLM 能直接从模糊需求生成可执行逻辑，应设计中间表示或人工辅助的形式化步骤。

  - 生成-过滤-证明流水线：采用“生成候选 → 自动过滤（规则/模型）→ 外部验证器（编译器、单元测试、仿真器）”的架构，将 LLM 生成和严格验证解耦，能显著提升最终输出质量。在推荐系统中，可用于自动生成策略规则、特征工程代码或查询重写规则，并用离线评估/在线
  A/B 过滤。

  - 评估基准设计：区分“给定形式化陈述的证明能力”与“从自然语言到形式化的转换能力”，避免用端到端指标掩盖子任务瓶颈。在业务中评估 LLM 能力时，应拆解为意图理解、结构化生成、逻辑推理等子任务分别评测。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有 TCS 基准不贴近真实研究场景，缺乏端到端评估。

**方法关键点**：FormalTCS 包含 175 个实例，源自 2025-2026 年 STOC/FOCS/SODA/COLT 接收论文，保留论文特定的定义、假设和证明依赖，专家验证 Lean 形式化和证明。评估多个领先 LLM 在自动形式化（自然语言定理陈述转 Lean）和给定形式化陈述下的证明能力。进一步开发自动 TCS 研究框架，包括生成、形式化、过滤和证明新声明。

**关键结果数字**：自动形式化是最主要瓶颈：最佳模型在自动形式化上仅得 11.5 分，而证明人工形式化陈述的 Pass@8 为 28.6。自动生成 64 个新声明，只有 6 个通过专家评估和证明验证，表明科研品味是另一重大障碍。
