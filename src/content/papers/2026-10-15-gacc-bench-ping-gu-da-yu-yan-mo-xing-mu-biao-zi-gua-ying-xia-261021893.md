---
title: 'GACC-Bench: Benchmarking Goal-Adaptive Context Compression Ability across
  Large Language Models'
title_zh: GACC-Bench：评估大语言模型目标自适应上下文压缩能力
authors:
- Weiting Liu
- Zhiyu Pan
- Shuhong Wang
- Zhenquan Yao
- Jungang Li
- Li Zhao
- Jian Jiang
- Jianfeng Feng
- Ai Han
- Wenlian Lu
affiliations:
- Fudan University
- Huazhong University of Science and Technology
- JD.com
- Harbin Institute of Technology
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2610.21893'
url: https://arxiv.org/abs/2610.21893
pdf_url: https://arxiv.org/pdf/2610.21893
published: '2026-10-15'
collected: '2026-10-18'
category: Eval
direction: LLM 上下文压缩评估基准
tags:
- context compression
- LLM
- benchmark
- goal-adaptive
- agent traces
- long context
one_liner: 提出 GACC-Bench 基准，评估 LLM 在给定高层目标下压缩长上下文时保留目标相关信息的能力，发现与完整上下文仍有显著差距
practical_value: '- **Agent 长会话上下文压缩**：在电商导购、客服 Agent 等长对话场景中，压缩上下文时显式传入当前用户意图或任务目标，能显著提升压缩后的信息保留质量，减少
  token 成本。

  - **压缩评估方法可复用**：采用“固定 reader + 同一压缩上下文回答多个问题”的评估方式，能更真实地衡量压缩是否保留了目标相关的多角度信息，而非只看单一问答准确率。

  - **目标相关性约束**：目标引导压缩优于无目标压缩，而错误目标会降低性能，说明业务中需确保压缩时的目标描述与实际下游任务一致，避免引入噪声。

  - **多目标分组评估**：将同一上下文下的多个问题按共享目标分组，可以检测压缩是否遗漏某个目标维度的信息，适合用于诊断生产环境中压缩策略的薄弱环节。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM 在长期任务（如 coding assistant、agent 会话）中上下文不断累积，需要在具体下游问题未知时进行压缩，且必须保留与高层目标相关的信息。现有评估缺乏对目标自适应压缩能力的系统基准。

**方法**：构建 GACC-Bench，包含 500 个高层目标、2,571 个问题，覆盖 281 个文档与 agent-trace 上下文，来自 7 个领域集合，全部经人工专家审核。压缩器接收源上下文、目标描述和长度预算，但看不到评估问题；固定 reader 用同一压缩上下文分别回答所有关联问题。

**关键结果**：评估 10 个 LLM 压缩器后，即使最佳模型也与完整上下文性能存在显著差距，尤其在支持同一目标下所有问题都正确时差距更明显；与目标无关压缩相比，目标引导压缩一致提升准确率，而错误目标条件会降低准确率。
