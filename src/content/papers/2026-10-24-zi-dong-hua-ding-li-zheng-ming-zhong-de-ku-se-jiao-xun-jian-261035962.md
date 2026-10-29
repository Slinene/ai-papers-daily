---
title: 'h1: A Taste of the Bitter Lesson in Automated Theorem Proving'
title_zh: 自动化定理证明中的苦涩教训：简单 Agent 循环
authors:
- Skander Moalla
- Ahmad Rammal
- Niket Patel
- Remi Munos
- Julia Kempe
affiliations:
- FAIR at Meta
- EPFL
- CERMICS, ENPC, Institut Polytechnique de Paris
- New York University
arxiv_id: '2610.35962'
url: https://arxiv.org/abs/2610.35962
pdf_url: https://arxiv.org/pdf/2610.35962
published: '2026-10-24'
collected: '2026-10-29'
category: Agent
direction: Agent 自反思 + 形式化验证
tags:
- Automated Theorem Proving
- Lean 4
- Test-time Compute
- Agentic Loop
- Reasoning
- Formal Verification
one_liner: 提出 h1，一个只靠高效 Lean 接口与验证反馈自反思的简单 agent 循环，在形式定理证明达到 SOTA 并追上复杂工作流
practical_value: '- 构建 LLM agent 做 query 生成、推荐文案或策略搜索时，不要先上规划/多智能体分解；先用单 agent + 可执行验证器（搜索
  API 结果、商品约束、SQL 执行）做自反思循环，用 pass@1/多采样衡量，效率和效果常超复杂编排。

  - 工具/环境接口的反馈延迟与信息质量是关键：把验证器返回做成结构化、可增量复用（如错误位置、候选修正），减少模型盲目重试；类比 h1 的 Lean 4 增量编译与错误上下文。

  - 做消融和 matched-model 对比：换更强模型或更多计算会混淆 workflow 收益；固定模型，对比简单 loop vs 复杂 agent 架构，避免苦涩教训。

  - 如果业务里有可靠执行环境（规则校验、线上仿真、评分器），把计算预算花在多次验证反馈循环（test-time compute）上，可能比重构提示/工作流更划算。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：非形式数学的进展主要靠前沿语言模型的 CoT 和 agentic reasoning 扩展，但形式定理证明仍依赖人为设计的规划、分解、专用证明器编排。这引出 bitter-lesson 问题：一个只扩展 test-time compute 的简单 agent loop 能否匹敌这些复杂工作流？

**方法**：h1 给模型一个高效 Lean 4 接口，通过 verifier feedback 和 self-reflection 反复工作，不引入分解或搜索结构。

**结果**：在 PutnamBench、FATE-X、FormalConjectures100-Solved 上达到 SOTA；在 FormalConjectures 中解决 8 个开放问题；在匹配模型下持平或超过 Goedel-Architect、AlphaProof Nexus；甚至 pass@1 常能解决开放问题。消融和与 Claude Code、AxProverBase 的 matched-model 对比表明，光有简单不够，高效 Lean 接口极大决定成本和成功率；图中 h1+Gemini 3.1 Pro 在 PutnamBench 约 $672/题达到 100% 解决率。建议在指定工作流前先用高效执行反馈评估前沿模型，否则可能再吃苦涩教训。
