---
title: LongCat-DeepResearch Technical Report
title_zh: LongCat-DeepResearch：基于ResearchSpec的多智能体深度研究报告系统
authors:
- Meituan LongCat Team
- He Zhu
- Yue Xu
- Wanli Wu
- Haolin Ren
- Yuxin Bian
- Jiarui Zhao
- Rongzhi Zhang
- Quanchi Weng
- Jinghao Cui
affiliations:
- Meituan LongCat Team
arxiv_id: '2609.36071'
url: https://arxiv.org/abs/2609.36071
pdf_url: https://arxiv.org/pdf/2609.36071
published: '2026-09-27'
collected: '2026-09-30'
category: MultiAgent
direction: 多智能体深度研究与长文生成
tags:
- Deep Research
- Multi-Agent
- ResearchSpec
- Long-form Report
- Planning
- Editing
one_liner: 用紧凑的ResearchSpec替代全文迭代，结合并行研究员与全局-局部编辑，提升深度研究报告质量
practical_value: '- 将早期迭代从完整文档转移到紧凑可执行的 **ResearchSpec**（章节范围、研究问题、必需实体、源线索），避免在巨大上下文中反复重写全文，适合改造现有
  agent 生成报告/方案的流程。

  - 采用 **并行独立研究者**：每个 section 单独上下文搜索、阅读、撰写，保留完整 section draft，不依赖共享压缩历史，可缓解长上下文中证据丢失；类似做法可迁移到多路召回或者子任务并行执行。

  - 编辑阶段**分离全局决策与局部文本生成**：Global Editor 只指定归属和冲突，Local Editor 基于 directive 修改既有 section，避免整篇重写带来的成本和不稳定，适合需要多轮修订的长文/方案生成。

  - 数据构建接口化：用同一套 harness 生成（query, ResearchSpec, traced sections, edit directives），再用于模型
  mid-training 和 post-training，实现系统能力与模型能力的迭代闭环。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
开放域深度研究要求 agent 探索大量外部证据并综合为长篇报告，但报告的证据需求无法预先完全指定。现有系统要么在单一扩大的上下文里交替推理检索起草，导致证据、中间推理和草稿争夺有限上下文；要么反复基于全文更新来反馈，容易锚定早期发现、再生无关文本。核心问题是：如何在保留研究-写作反馈的同时，不把所有调查集中在不断膨胀的草稿中。

**方法关键点**
- **ResearchSpec 代理**：多个 Planning Writer 并行搜索阅读，各自提出候选报告规范，Judge 合并、Critic 找缺失问题、Reviser 修订，形成紧凑的 ResearchSpec，记录每节范围、研究问题、必需实体/案例、来源线索，作为全局理解的可执行代理。
- **独立的 section 研究**：每个 Researcher 接收完整 ResearchSpec 和一个 section 分配，在独立上下文中继续搜集证据并撰写带引用的 section，完整保留其论点和细节，不压缩成给单独作家的摘要。
- **组装后编辑**：直接按 ResearchSpec 顺序组装 section（保留重复内容），Global Editor 读全文分配重复材料归属、标识冲突，Local Editor 根据指令定向修改指定 section，避免全文档重写。
- **数据构建**：从 CC-BY 综述文章或冻结多源简报生成问答和任务清单，通过原子事实搜索验证、确定性检查和联合语义评审构建研究任务；再由 harness 执行收集阶段轨迹，用于 LongCat 模型的 mid-training 和 post-training。

**关键实验**
- 在 DeepResearchBench 上 55.25，DeepResearchBench II 上 51.35，ResearchRubrics 上 79.83，分别超过最强对比系统 +0.30、+3.17、+5.62 分。
- 内部基准总分 76.04，仅次于 ChatGPT-DeepResearch 的 76.59，超过 Claude 和 Gemini。
- 消融：完整流水线（Full）在 DRB-II 和 RR 平均 63.91，优于简化规划（59.56）、单全局研究员（62.07）和无 Editor（63.30）。
- 模型-编排配置：同一旧模型从 ReAct/direct report（平均 47.04）到当前 harness（58.05）再到当前模型+harness（62.14）逐级提升，显示编排与模型能力互补。

**最值得记住的一句话**
将早期迭代从整个报告转移到紧凑可检查的 ResearchSpec 上，让全局协调与局部独立研究分离，是提升多智能体深度报告质量和可管理性的关键设计。
