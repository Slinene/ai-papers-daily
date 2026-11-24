---
title: 'MMMem: Self-Improving Agents with Task-Aware Multimodal Experience Consolidation'
title_zh: MMMem：任务感知的多模态经验整合自改进 Agent
authors:
- Yuxuan Chen
- Changwei Lv
- Yunfei Li
- Zhongjing Du
- Kehui Tan
- Zijun Liao
- Ruochong Zheng
- Hao Chen
- Can Deng
- Zheni Zeng
affiliations:
- Peking University
- Clemson University
- Nanjing University
- Tsinghua University
arxiv_id: '2611.30287'
url: https://arxiv.org/abs/2611.30287
pdf_url: https://arxiv.org/pdf/2611.30287
published: '2026-11-22'
collected: '2026-11-24'
category: Agent
direction: Agent 多模态记忆与经验整合
tags:
- Multimodal Memory
- Experience Consolidation
- Self-Training
- LoRA
- RAG
- Agent Memory
one_liner: 将已完成任务蒸馏为带来源链接的经验并写入外部记忆，同时用生成任务做 LoRA 自训练，提升多模态长程记忆问答
practical_value: '- **任务级经验记忆可迁移到导购/客服 Agent**：把每次会话的结论、任务上下文和支撑商品/来源 ID 结构化存成 experience，后续相似问题先召回
  experience 再核对原始证据，能减少反复推理错误，尤其适合电商导购中“这件商品尺码/材质/适用场景”等高频重复咨询。

  - **source-linked 多视图记忆组织方式可直接用于商品知识库**：原文、图片、OCR 页面、生成场景图都绑定同一 source ID，text+visual
  双路检索。电商商品库天然多模态，可为每个 SKU/类目生成合成场景图，把分散属性（颜色、外观、使用场景）聚合成一张图，提升视觉召回效果。

  - **离线性 warm-up 缓解冷启动**：基于商品/活动素材自动生成 QA，并预写 experience 到记忆区，使新会话一开始就能检索到任务相关经验。适合新店铺、新活动页或新文档库上线时快速构建可用记忆。

  - **self-training 同时训练“证据作答”和“经验总结”两个目标**：用 LoRA 共享参数训练，让模型既会从检索证据中找答案，也会把结论写成可复用经验。电商
  RAG 场景可借鉴此双目标训练，提升模型对检索结果的利用率和后续记忆沉淀质量。

  - **staged→retained 的复用驱动保留策略**：experience 先进入 staging 区，只有在后续任务中被采纳且答案引用其来源记录足够次数才转正，否则过期。这本质是一种基于实际价值的记忆淘汰策略，可用于
  Agent 记忆/缓存管理，避免无效经验膨胀。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
AI agent 在长期交互中积累对话、图片和文档，后续问题往往需要跨记录联合证据，但现有方法主要停留在存储与检索原始记录，任务解决过程中形成的理解没有被保留，导致相似问题重复犯错。多模态记忆需要把“任务结论 + 支撑来源”作为一等公民保存，并协调外部记忆与参数适应。

### 方法关键点
- **source-linked 多视图记忆**：保留原始文本、图片、页面渲染图，并生成融合多条线索的场景图，所有视图携带 source ID；text 与 visual 双路检索，命中生成图也能回溯到原始证据。
- **source-generated tasks**：从记忆节点自动生成问题、答案和支持记录 ID，覆盖单跳、多跳、时间、不可回答等类型，并生成关联问题序列。
- **两层知识对齐**：warm-up 用生成任务离线写出 experience 到外部记忆，冷启动即具备任务相关经验；self-training 用独立训练单元的数据更新 LoRA 参数，共享模型同时学习证据作答与经验总结两个目标。
- **task-aware online editing**：每次回答后，模型以第二个 call 写出结构化 experience，记录任务上下文、结论、支撑 source links 和 retention state；新 experience 先入 staging 区，后续任务采纳且引用源记录支持时逐步转正，过期无采用则淘汰。

### 关键实验
在 LoCoMo、Mem-Gallery、LooGLE v2 三个记忆基准上，用 Qwen3.5-9B 和 MiniCPM-V 4.5 两个 backbone 对比 8 个 baseline。Qwen3.5-9B 下，相对最佳 baseline 分别提升 36.9%、17.6%、15.2%；LoCoMo F1 从 A-Mem 的 48.09 提升到 65.84，Mem-Gallery F1 从 65.63 提升到 77.21。消融显示 self-training 和 warm-up 在所有设置下均带来一致提升，warm-up 在 LooGLE v2 上贡献最大（+6.62）。

### 最值得记住的一句话
把任务完成后的结论和它的证据来源一起沉淀为可检索、可复用、可淘汰的经验，是 agent 长期记忆从“存记录”走向“总结经验”的关键一步。
