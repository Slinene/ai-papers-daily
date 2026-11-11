---
title: Program-Aided Patchable Skill Evolution
title_zh: 程序辅助的可补丁化技能演化
authors:
- Jiahao Wang
- Yuqi Xiong
- Qing Yang
- Zhipeng Xu
- Zhenghao Liu
- Zulong Chen
- Yubin Bao
affiliations:
- Northeastern University
- Alibaba Group
arxiv_id: '2611.14019'
url: https://arxiv.org/abs/2611.14019
pdf_url: https://arxiv.org/pdf/2611.14019
published: '2026-11-10'
collected: '2026-11-11'
category: Agent
direction: Agent 技能演化 · 可执行程序解耦
tags:
- Agent Skills
- Skill Evolution
- Program-Aided
- Patchable
- Spreadsheet
- LLM
one_liner: 将可执行程序与自然语言技能解耦，通过可补丁协同演化提升 Agent 技能精度与跨模型迁移性
practical_value: '- 在电商导购、广告文案生成、搜索 query 改写等 Agent 技能库中，把可复用的过程逻辑（数据清洗、格式转换、API 调用流程）抽成独立
  Python 函数，与自然语言策略文档分离维护；更新时只 patch 代码或文档，不用重写整个技能。

  - 采用 create/repair/delete + 行级编辑的补丁 DSL，并配合 held-out validation gate 决定是否接受更新，能防止技能演化过拟合到少量训练样本；促销活动规则、话术模板等频繁变更场景可直接复用。

  - 为技能演化 proposer 提供按需读取工具（read_trajectory/read_skill/read_patch），而不是一次性塞入所有轨迹，能降低上下文噪声并避免超过
  context window；对长轨迹 Agent 调试与经验沉淀很有价值。

  - 跨模型可迁移性结论：强模型演化出的程序化技能可被不同 backbone 复用，建议用强模型离线生成技能，在更便宜或更快的推理模型上部署，降低线上成本。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
Agent skills 作为不修改模型参数即可注入领域知识的手段，已在复杂交互任务中展现价值。但现有 skill evolution 方法主要用自然语言文档表达技能，将过程逻辑与描述性知识耦合在一起。这种耦合让局部修改困难：更新某个行为规则时容易扰动其他部分，限制了技能补丁的精度和可维护性。

**方法关键点**  
PASE 将可复用过程逻辑从自然语言技能中解耦，抽成独立可执行程序，形成 skill-program pairs。具体包括：
- 技能文档保留高层策略和描述性知识，程序承载可执行工作流；推理时 agent 可以显式调用程序获取 observation，保持自然语言灵活性。
- 演化过程采用 patch-based 机制：ReAct proposer 从成功与失败轨迹中反思，生成 update patch，支持 create / repair / delete 三类操作，可单独更新 skill 文档、关联程序或两者，且支持行级 +/- 编辑。
- 自适应上下文读取：提供 read_trajectory、read_skill、read_patch、finish 四个工具，按需检索轨迹、当前技能和历史补丁，避免一次塞入全部上下文造成噪声和超窗。
- Gated validation：候选补丁在 held-out 验证集评估，只有性能提升才接受，防止过拟合训练集。

**关键结果**  
在 SpreadsheetBench、Domain-Spreadsheet、WikiTableQuestions、HiTab 上，PASE 在 Qwen3.6-27B、Qwen3.7-Plus、Gemma4-31B 三个 backbone 上一致超越 No Skill、Human Skill、LLM Skill、Trace2Skill、EvoSkill。以 Qwen3.6-27B 为例，SpreadsheetBench Verified 从 EvoSkill 68.10 提升到 82.98；Domain-Spreadsheet 从 46.92 提升到 50.76；TableQA 从 72.18 提升到 74.10。消融显示程序演化、自适应读取、技能更新都有贡献；62.2% 的更新涉及程序，最终技能文档长度也显著短于纯文本演化方法。跨模型迁移实验表明 PASE 技能在不同 creator-user 组合下至少提升 3.07%，且强 creator 演化出的技能可被更弱或异构模型有效复用。

**最值得记住的一句话**  
把可执行过程逻辑从自然语言技能中解耦、以程序化补丁方式演化，是提升 Agent 技能可维护性、稳定性和跨模型迁移能力的关键。
