---
title: Adaptive Multi-Resolution Procedural Knowledge Compression for Large Language
  Models
title_zh: 大语言模型过程性技能的自适应多分辨率压缩
authors:
- Changyue Wang
- Weihang Su
- Qingyao Ai
- Yichen Tang
- Runzhong Qiao
- Xuancheng Li
- Min Zhang
- Yiqun Liu
affiliations:
- Tsinghua University
arxiv_id: '2606.12203'
url: https://arxiv.org/abs/2606.12203
pdf_url: https://arxiv.org/pdf/2606.12203
published: '2026-06-10'
collected: '2026-06-11'
category: Agent
direction: Agent 技能压缩
tags:
- skill compression
- procedural knowledge
- soft tokens
- LLM agent
- multi-resolution
one_liner: 提出多分辨率软令牌压缩框架 SKIM，通过渐进训练与离线自判实现技能压缩，在保持任务精度的同时大幅减少 token 消耗。
practical_value: '- 在 Agent 系统中，将冗长的技能描述（如电商工具的 API 文档、流程指引）压缩为少量连续软令牌，可显著降低每次调用的
  prefill 延迟和费用，且通过渐进训练与 LoRA 适配，能严格保持工作流中的条件依赖和工具调用逻辑，避免硬压缩导致流程断裂。

  - 多分辨率设计允许同一个技能存储 256/512 等不同预算的软令牌前缀，通过离线自判自动为每个技能‑模型对选择最优压缩率：简单技能用极少令牌，复杂流程用较高预算或回退至原文，这类似于电商推荐中根据复杂度动态分配
  embedding 维度。

  - 技能更新时只需一次前向传播即可重新压缩，无需梯度优化，使得频繁迭代的 Agent 技能仓库（如 ClawHub）能以类似软件构件的方式分发预计算的软令牌包，这对推荐系统中动态
  prompt 维护有借鉴意义。

  - 训练中使用 ReAct 轨迹模拟工具调用，并通过分解复杂技能为子技能训练多技能组合，这些合成数据方法可直接用于构建电商多工具 Agent 的压缩训练数据。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
LLM Agent 常通过“技能”（SKILL.md）复用过程性知识（工作流、工具协议），但这些技能文本动辄数千 token，每次调用都全部塞入上下文，造成巨大预填充延迟和成本。现有的文本压缩方法（如 LLMLingua、ICAE）以事实性文档为主要设计目标，压缩过程技能时容易割裂逻辑依赖，导致工具调用失败或流程错乱。因此需要一种专门针对过程性知识的压缩框架，在减少 token 的同时可靠保持可执行逻辑。

**方法**
SKIM 采用双模型软令牌架构：一个自回归压缩机读取技能全文，经前置的可学习 slot tokens 和 MLP 投影器，将技能映射为连续嵌入序列（软令牌），再注入目标 LLM 的输入。关键设计包括：
- **多分辨率**：同一个技能通过前缀截断得到 256/512 等不同预算的软令牌表示，并端到端按多分辨率损失训练，使压缩器同时学习多个 token 预算下的表示。
- **渐进训练**：阶段一用大量收集的技能文本做重建预训练；阶段二在 WikiHow 过程性问答数据上热身，对齐问答格式；阶段三用 GPT‑5.2 筛选高质量技能并生成问题，由目标模型自产答案（含 ReAct 轨迹与工具模拟），通过 LoRA 微调目标 LLM 以对齐压缩后的软令牌。
- **离线分辨率选择**：部署前，对每个技能生成 10 个诊断问题，用原文和不同压缩预算分别回答，由模型自判各预算的答案忠诚度，选择达到忠诚阈值（0.9）的最小预算，从而自动适配技能复杂度。

**实验与结果**
在 BigCodeBench、CHAMP、LogicBench、TheoremQA、ToolQA 五个数据集（均由 SRA‑Bench 提供标准技能标注）上，以 Qwen3-8B 和 Phi-4 作为目标模型。SKIM 在将技能 token 数压缩至原文的 30‑60% 的情况下，任务准确率普遍优于同等 token 预算的 LLMLingua-2、ICAE、500xCompressor 等基线，其中自适应分辨率（Adaptive）在多数场景下接近甚至超过全文性能。在添加检索干扰项的大上下文压力测试中，SKIM 也表现出更好的抗干扰能力。

**核心结论**
SKIM 证明，通过软令牌表示、过程性对齐和自适应预算选择，可以在大幅降低技能 prompt 开销的同时可靠保留执行流程，为 Agent 技能的高效部署提供了一条可工程化的路径。
