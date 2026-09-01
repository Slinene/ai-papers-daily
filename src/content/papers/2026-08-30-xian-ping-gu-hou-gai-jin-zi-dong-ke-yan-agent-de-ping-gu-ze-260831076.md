---
title: 'Learning to Evaluate Before Improving: Automatic Rubric Induction for Automatic
  Research Agents'
title_zh: 先评估后改进：自动科研 Agent 的评估准则自动归纳
authors:
- Xuehai Wang
- Haowei Qin
- Tongxin Liu
- Junkai Li
- Buqiang Xu
- Jintian Zhang
- Yijun Chen
- Zirui Xue
- Shumin Deng
affiliations:
- Zhejiang University
- University of Electronic Science and Technology of China
- Beijing University of Posts and Telecommunications
- Zhejiang University of Technology
arxiv_id: '2608.31076'
url: https://arxiv.org/abs/2608.31076
pdf_url: https://arxiv.org/pdf/2608.31076
published: '2026-08-30'
collected: '2026-09-01'
category: Agent
direction: 自动科研 Agent · 评估引导迭代
tags:
- LLM agents
- rubric induction
- evaluation-first
- iterative revision
- scientific research
- criterion verification
one_liner: 执行前自动归纳任务专属评估准则，引导科研 Agent 执行并逐条验证修订，跨基准平均提升 2.08–16.8 分
practical_value: '- 对电商/推荐 Agent 的开放任务（如 query 改写、推荐解释生成、push 文案选词），可先用 rubric induction
  把模糊指令拆成可逐条校验的原子目标，例如相关性、多样性、意图覆盖，再让 Agent 执行，减少后续返工。

  - 评估先行架构可以集成到现有 RAG/推荐流程：执行前生成评估标准，执行中逐条对照验证，相当于把 LLM-as-judge 前移，避免全量重写。

  - 迭代修订只针对未满足的准则做定向修改，比直接重生成更省 token 且能保持输出稳定性，适合低延迟的线上 Agent 服务。

  - 跨多个 backbone LLM 和 agent harness 的稳定增益说明先验 rubric 作为控制机制不依赖特定模型，可做电商 Agent 的平台化评测与跨系统迁移。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：开放科研任务指令不完备，自主科研 Agent 可能遗漏关键分析、用错方法或给出证据不足的结论，因为任务缺少明确的成功标准和验证依据。

**方法关键点**：AutoSciRub 采用评估先行框架，在执行科研流程前自动归纳任务专属的可执行 rubric。框架将欠规格指令分解为原子科学目标，结合相关文献和任务可见数据，合成具体、可操作、可验证的 criteria。这些准则让隐性的实验与论据要求显性化，指导后续实验和分析。在修订阶段，rubric 引导的逐条验证能识别未满足的准则，从而对研究报告及其支撑产物进行定向改进。

**关键结果**：在 ResearchClawBench 上，固定 Codex harness 时跨三个 backbone LLM 平均提升 2.08 分；固定 DeepSeek-V4-Flash backbone 时跨三个 agent harnesses 平均提升 2.95 分。在 AstaBench E2E Discovery 随机 20 任务子集上，跨三个 agent harnesses 平均提升 16.8 分，同时成功完成任务数保持或增加。
