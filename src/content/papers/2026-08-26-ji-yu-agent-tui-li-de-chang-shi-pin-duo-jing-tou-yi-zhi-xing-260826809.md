---
title: 'Thinking on Shots: Consistent Multi-Shot Video Editing with Agentic Reasoning'
title_zh: 基于 Agent 推理的长视频多镜头一致性编辑
authors:
- Chenyang Wu
- Fuchen Long
- Binyuan Huang
- Xinlong Sun
- Xi Chen
- Chun-Le Guo
- Chongyi Li
affiliations:
- Nankai University
- Tencent
arxiv_id: '2608.26809'
url: https://arxiv.org/abs/2608.26809
pdf_url: https://arxiv.org/pdf/2608.26809
published: '2026-08-26'
collected: '2026-08-30'
category: Agent
direction: 视频编辑 · Agentic Reasoning
tags:
- Agentic Editing
- LLM+VLM
- Long Video Editing
- MMLVE
- Consistency
one_liner: 提出 Agentic 框架结合 LLM 与 VLM，解决长视频多指令编辑中的跨镜头一致性、指令解耦与时空结构零破坏问题
practical_value: '- 主要是视频编辑领域的学术贡献，与电商/搜索推荐业务直接关联较弱；但其中 **LLM + VLM 协同的 Agentic 任务分解**
  思路可迁移到多模态商品视频/短视频生成审核：将复杂指令拆解为多个子任务，分别由 LLM 做指令规划、VLM 做视觉校验，提升生成内容的一致性。

  - 提出的 **Cross-Shot Editing Consistency (CSEC)** 与 **Zero-Destruction on Spatiotemporal
  Structure (ZDSS)** 评估维度，类似推荐系统中“跨会话兴趣一致性”和“无侵入式推荐”，可借鉴其评估指标设计，度量多步交互或长周期推荐中的连贯性与非破坏性。

  - 长视频分段处理中避免实体碎片化的思想，可用于电商详情页视频自动剪辑或广告素材拼接：根据实体分布动态切分而非固定时长，减少实体断裂。

  - 整体业务可借鉴点有限，若团队涉及多模态内容生成或 AIGC 质量评估，可关注其 Agentic 编排与人工评估指标。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有视频编辑方法聚焦单镜头或短视频，难以处理长视频多指令编辑。固定时长分块会导致实体碎片化、编辑幻觉严重、时序连续性破坏。

**方法关键点**：
- 定义 **Multi-Instruction Multi-Shot Long-Video Editing (MMLVE)** 任务，围绕三个核心目标：跨镜头编辑一致性（CSEC）、多指令解耦（MID）、时空结构零破坏（ZDSS）。
- 提出 **Agentic 编辑框架**，利用 LLM 与 VLM 协同：先做 shot-level 视频解耦，再精确解析每条编辑指令，避免指令相互干扰。
- 构建 **MMLVE-Bench** 数据集，包含复杂真实时空动态、高密度异构指令、稀疏随机实体分布；并设计三个 MMLVE 专属评估指标。

**结果**：实验显示 MMLVE-Agent 优于闭源 SOTA（如 Seedance 2.0），能够消除编辑幻觉、保持跨镜头编辑一致性、实现无缝时空过渡。
