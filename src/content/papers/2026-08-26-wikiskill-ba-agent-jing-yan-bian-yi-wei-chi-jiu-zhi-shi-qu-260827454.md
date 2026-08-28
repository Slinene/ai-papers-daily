---
title: 'WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill
  Evolution'
title_zh: WikiSkill：把 Agent 经验编译为持久知识驱动技能进化
authors:
- Liyan Tang
- Cyrus Rashtchian
- Chun-Sung Ferng
- Andrew Tomkins
- Da-Cheng Juan
- Tu Vu
affiliations:
- Google Research
- Virginia Tech
arxiv_id: '2608.27454'
url: https://arxiv.org/abs/2608.27454
pdf_url: https://arxiv.org/pdf/2608.27454
published: '2026-08-26'
collected: '2026-08-28'
category: Agent
direction: Agent 技能进化 · 持久知识库协同
tags:
- Agent Skills
- Skill Evolution
- Persistent Knowledge
- LLM Agents
- Cross-model Transfer
one_liner: 提出 WikiSkill 框架，通过持久 wiki 知识层将 Agent 执行经验持续沉淀为可复用模式，显著提升技能进化效果与跨模型迁移性。
practical_value: '- 可借鉴三层知识架构：把线上推理产生的完整轨迹存成 raw 层，把失败/成功模式沉淀到 wiki 层，把可执行 SOP/工具用法写成
  skills 层；电商搜索推荐 Agent 在做 prompt/SOP 自动优化时，可以让知识持续累积而不是每次从零重新扫描。

  - 优化阶段限制 Inference Agent 访问 wiki，只允许 Skill Proposer 读取持久知识：直接给执行器 wiki 会让其借道 wiki
  绕过 skill，降低轨迹对 skill 优化的信息量；对应工程实现是训练/优化时隔离知识库与线上 agent，只在 proposer 侧使用。

  - 用 validation gating + skill-impact.md 审计：每次 skill 变更都在验证集打分，接受才保留，拒绝则回滚 skill
  但 wiki 不重置；记录 proposal diff、分数、是否接受，避免重复提交失败方案，适合电商推荐 Agent 的 prompt 自动化调优。

  - 跨模型迁移经验：小模型发现的通用工作流可以迁移到大模型、甚至超过后者自进化技能；在预算有限时，可让小模型产出/优化电商搜索的 query 改写或推荐解释 SOP，再部署到大模型，降低
  token 成本。'
score: 9
source: huggingface-daily
depth: full_pdf
---

动机：Agent skills 把领域知识封装成可复用模块，但自动发现技能时，洞察往往散落在优化历史中，难以跨迭代系统复用。现有方法如 EvoSkill、Trace2Skill、SkillOpt 都缺少一层独立、持续积累的知识表示，无法让后续更新站在前人肩膀上。WikiSkill 的核心思想是把执行经验编译成持久 wiki，与可执行技能协同进化。

方法关键点：
- 三层知识架构：raw/ 保存不可变执行轨迹；wiki/ 保存结构化的失败模式、成功策略、进化日志和 skill-impact.md 审计；skills/ 保存当前可执行程序性知识，每个 skill 有 SKILL.md 和 PURPOSE.md 关联 wiki 模式。
- 四组件闭环：Inference Agent 用当前 skills 跑 rollout；Wiki Maintainer 对 trace 做根因分析，把模式增量写入 wiki；Skill Proposer 以 ReAct 方式读 wiki 和 traces，原子式创建或修改单个 skill；Gating & Rollback 用验证集打分，通过则保留，否则回滚 skill，但 wiki 永不回滚。
- 关键设计：训练 rollout 阶段 Inference Agent 不访问 wiki，避免其直接依赖 wiki 执行任务，从而保证轨迹对技能的信号不被稀释；Wiki Layer 永久累积，提案的 diff、分数和接受结果写入 skill-impact.md。

关键结果：在五个 benchmark（LiveMath、SealQA、SpreadSheet、OfficeQA、ALFWorld）和五个模型上，WikiSkill 平均性能全部超过 EvoSkill、Trace2Skill、SkillOpt 和无技能基线；对 Gemini-3.5-Flash 平均提升 18.6 个百分点，对 Qwen-3.6-27B 提升 23.9 个百分点。技能进化与模型规模互补：Qwen-3.5-9B + WikiSkill 平均 47.4%，超过 Qwen-3.6-27B 无技能的 39.4%。跨模型迁移也很强：Qwen-3.5-4B 进化的技能把 Gemma-4-31B 在 LiveMath 上从 33.9% 拉到 73.1%，超过其自我进化技能 56.7%。消融显示，Skill Proposer 有 wiki 访问 +15.0 平均收益，而训练时 Inference Agent 访问 wiki 会让平均分从 63.7 降到 60.9。

最值得记住的一句话：把经验固化为独立的、反复积累的 wiki 知识，并把知识发现与执行解耦，是让 Agent 技能持续进化和跨模型迁移的关键。
