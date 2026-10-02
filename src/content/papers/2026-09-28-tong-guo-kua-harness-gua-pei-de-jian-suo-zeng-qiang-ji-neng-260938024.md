---
title: Retrieval-Augmented Skill Optimization via Cross-Harness Adaptation
title_zh: 通过跨 harness 适配的检索增强技能优化
authors:
- Jaewon Chu
- Ji Soo Lee
- Jihwan Park
- Dohwan Ko
- Jeehye Na
- Seunghun Lee
- Taehoon Lee
- Minseo Yoon
- Minseok Joo
- Yunyang Xiong
affiliations:
- Korea University
- KAIST
- Meta AI
arxiv_id: '2609.38024'
url: https://arxiv.org/abs/2609.38024
pdf_url: https://arxiv.org/pdf/2609.38024
published: '2026-09-28'
collected: '2026-10-02'
category: Agent
direction: Agent 技能优化 · 跨 harness 检索适配
tags:
- Agent Skill
- Retrieval-Augmented
- Cross-Harness Adaptation
- Skill Optimization
- LLM Agent
one_liner: 检索外部技能语料并用 Cross-Harness Adaptation 适配到目标任务与执行环境，同时强化技能初始化和失败驱动更新
practical_value: '- 构建内部“技能/策略语料库”（如大促玩法 SOP、不同平台投放经验、query 改写案例），按 heading 切成段落级索引；检索时用
  BM25 返回 top-K=5，避免整篇文档带来的无关信息，K 再增大会引入噪声。

  - 借鉴 Cross-Harness Adaptation：把外部知识/代码片段转成目标系统的对象、命令、单位，做三件事——删 source-specific
  名词、只保留当前 requirement 相关、工具参数行为必须被目标 harness 描述确认；这在多平台/多渠道（Web vs App vs 小程序、不同广告
  API）迁移 SOP 时尤其实用。

  - 用 RASI 做零 rollout 冷启动：新任务或新 agent 先由 LLM 从 task/harness 描述生成 requirement-query
  对，检索并适配成 lessons 后直接合成 skill，避免昂贵试错；实验显示即使只开放 1% 语料也有明显收益。

  - 更新阶段不要只依赖 rollout 文本梯度：从失败轨迹反推“缺失知识”并生成检索 query，用外部知识补充参数知识，候选 skill 必须过验证集才接受；在成本上可做到与
  TextGrad/WikiSkill 同等 rollout 数，甚至 API 成本更低。

  - 生产落地注意 benchmark 泄漏：按仓库级别把已知任务/数据集相关技能加入 blocklist，防止检索到作弊或过拟合片段。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
LLM agent 在固定 harness（工具、文件、评分）下的表现高度依赖技能文本。现有技能优化主要靠自身 rollout 迭代，忽略了公开技能库中海量程序性知识；直接检索复用又常因为来源 domain/harness 不匹配而负迁移。因此需要一种机制，把外部技能作为先验融入初始化与更新，同时解决跨 harness 适配。

## 方法关键点
- RASO 由 RASI（初始化，无 rollout）和 RASU（更新，有 rollout）构成，两个阶段共享“段落级检索 + Cross-Harness Adaptation”。
- 将技能文档按 heading 切成段落级索引，BM25 检索 top-K（K=5），提高信噪比。
- Cross-Harness Adaptation 用 LLM 把检索内容改写为目标 harness 可执行 lesson：删除来源域专有名词、只保留与当前需求相关、工具/参数行为仅在目标 harness 描述确认时保留。
- RASI：从 task/harness 描述生成 requirement-query 对，检索并适应为 lessons，再合成初始技能 s0，不需要 rollout。
- RASU：从失败轨迹生成 textual gradient 和检索 query，检索外部知识并适应为 lessons，与当前技能和梯度一起生成候选，验证集提升才接受。

## 关键实验
在 OfficeQA、SpreadsheetBench、ALFWorld、WebShop 四个 benchmark，GPT-5.6-Luna 和 Qwen-3.5-9B 两个骨干上评估。RASI 零 rollout 时比 retrieval-free 初始化 RFSI 在 OfficeQA 提升 +5.63、Spreadsheet +4.77、ALFWorld +3.24、WebShop +1.17（GPT-5.6-Luna）；RASO 相比最强技能优化 baseline 在 Spreadsheet 提升 +6.31、OfficeQA +3.49，并保持更低或相近 API 成本。消融显示 Cross-Harness Adaptation 带来一致收益（如 RASI 初始化在 OfficeQA +3.88、Spreadsheet +7.74），两个阶段互补；K=5 最优，更大 K 引入噪声。

## 一句话
外部技能语料的价值在于检索后做 target-harness 适配，而不是直接复用；把适配后的知识同时用于初始化和失败驱动的迭代更新，能稳定超越仅靠 rollout 反馈的优化方法。
