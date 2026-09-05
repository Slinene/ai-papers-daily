---
title: 'VeriPhy: Agentic Physical Reasoning for World Model Evaluation and Refinement'
title_zh: VeriPhy：面向世界模型评估与改进的可审计物理验证智能体
authors:
- Wenzhuo Xu
- Yuchen Zhu
- Chongjian Ge
- Xuan Shen
- Jing Shi
- Jason Kuen
- Yongxin Chen
- Molei Tao
- Christopher McComb
- Noelia Grande Gutiérrez
affiliations:
- Carnegie Mellon University
- Georgia Institute of Technology
- Northeastern University
- Adobe Research
arxiv_id: '2609.03153'
url: https://arxiv.org/abs/2609.03153
pdf_url: https://arxiv.org/pdf/2609.03153
published: '2026-09-01'
collected: '2026-09-05'
category: Eval
direction: Agentic 物理推理验证与证据溯源
tags:
- Agentic Verification
- Physical Reasoning
- Video Generation Evaluation
- Provenance
- Multimodal Eval
- World Model
one_liner: 用类型化物理义务和冻结专家证据做可溯源三态裁决，覆盖 228/304 个真实生成缺陷
practical_value: '- 在商品短视频/广告创意质检中，可借鉴「先用纯文本 planner 生成 typed obligations 和静态 plan，再调用冻结专家工具」的架构：先定义必须验证的物理/视觉义务（如商品完整露出、文字可读、动作合理），避免
  LLM 自由观察导致的遗漏和幻觉。

  - 把每次模型判断封装为携带 provenance 的 evidence record，并输出 supported/contradicted/unknown 三态，而不是
  scalar score；这样业务审核、badcase 复盘、合规审计能定位到具体帧/轨迹/OCR 证据，便于追责和修正。

  - 将 critic verdict 作为 refinement 接口写回生成：在广告文案/视频生成中，不要只用总分 reward，而用结构化失败证据（哪句文案、哪个时刻、哪条义务
  violated）驱动 prompt/policy 更新。

  - 用 frozen low-level expert（OCR、分割、计数等）而非端到端大模型做测量，可降低幻觉并复用现有服务；在商品属性校验、广告落地页一致性检查中可落地。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：生成视频视觉流畅并不等于物理可靠，单一质量分无法指出违反的物理义务或失败时刻。

**方法关键点**：VeriPhy 用纯文本 planner 在观察任何帧之前，将 prompt 编译为带类型的物理义务和静态校验的执行计划；执行时只调用声明的冻结低层专家（分割/跟踪、计数、11 类物理测量、深度、OCR、音频事件检测）。每个动作返回携带 provenance 的证据记录，其 payload 要么是带类型的测量，要么是显式标记的学习状态。带类型的 resolver 和固定组合把可用证据映射为三态：supported/contradicted/unknown，展示为 plausible/implausible/abstain；因此每个判断都可追溯到产生它的证据。

**关键结果数字**：在 1500 条 clip 的人工标注缺陷库中，149 条核心 clip 含 304 个缺陷记录；VeriPhy 覆盖 228 个，高于给定同样 clip 和 claim 的 question-decomposition evaluator 的 164 个；monolithic prompting 同一 backbone 为 222 个。关键差异不是 recall，而是每个决策保留证据与 provenance，使其逐条可审计，并可作为 critic verdict 写回生成的接口。
