---
title: 'AutoMaster: Autonomous Post-Training by Making the Same Model a Better Teacher'
title_zh: AutoMaster：自主后训练，让同一模型成为更好的教师
authors:
- Guoxin Chen
- Shuang Sun
- Fanzhe Meng
- Xinyu Tang
- Ruihua Song
- Wayne Xin Zhao
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
arxiv_id: '2611.26510'
url: https://arxiv.org/abs/2611.26510
pdf_url: https://arxiv.org/pdf/2611.26510
published: '2026-11-18'
collected: '2026-11-20'
category: Training
direction: LLM Agent 自主后训练与行为塑造
tags:
- Skill-FT
- Autonomous Post-Training
- Teacher Distillation
- LLM Agent
- Behavioral Shaping
one_liner: 用技能引导教师 rollout 并自主选择训练轨迹，三个领域较 Vanilla SFT 平均提升 1.42–8.99 个百分点
practical_value: '- 借鉴 Skill-FT：在生成训练轨迹时，给教师模型 system prompt 注入明确行为原则/技能（如“追溯失败根因再改代码”“检索证据不足时不要瞎猜”），比只用成功轨迹更能提升学生；电商/搜索
  Agent 训练可围绕“先校验 query 改写是否符合业务规则”“推荐理由必须有证据支撑”设计 skill。

  - 保留 skill 上下文做 SFT：训练输入中保留技能指令，即便线上推理不注入技能，也能更好内化行为规则（所有 6 个设置平均高 2.15–4.01pp）；在推荐/Agent
  数据构建时，不要把 prompt 和输出拆得太干净，保留行为条件有助于模型学会何时应用。

  - 数据选择与行为塑造解耦：Agent 同时选择轨迹和设计 skill；消融显示只选数据或只加 skill 都可能不如 vanilla SFT，合并才有效。业务中可对同一批
  teacher rollouts 做两件事：curate 有目标行为的数据 + 用 skill 引导 teacher 生成稀缺行为。

  - Agent 化后训练闭环：用 MCP 工具 + 共享 checkpoint 存储 + 自动化评估调度，让 LLM agent 多轮实验；在搜索/推荐 Agent
  迭代中，可把“教师 rollout → SFT → 线上评估 → 诊断失败轨迹 → 修改 skill/数据”做成自动流水线，降低人工调数据成本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：LLM agent 后训练通常对成功轨迹做 SFT，但任务成功不等于行为正确——教师轨迹可能包含无依据假设、重复和表面验证；成功轨迹会把这些不良习惯一并教给学生，而有效行为却可能稀缺。

方法关键点：
- Skill-FT：在 teacher rollout 时把自然语言技能（如“执行数值决策”“先找证据再改结论”）追加到 system prompt，抑制坏习惯并诱导低代表性的有效行为；
- AutoMaster：LLM agent 通过轨迹分析设计/分配技能，先在少量任务上 pilot 测试，再规模化 rollout，并根据行为与结果选择训练轨迹；
- 外层多轮：每轮从同一初始 checkpoint 做全参 SFT，评估学生后根据分数和失败轨迹修正技能或数据选择；
- 训练时保留 skill 指令：即便评估时无 skill，让学生看到行为规则及其适用条件，促进内化。

关键实验：在 Terminal-Bench 2.1、BrowseComp、Doc2Repo 三个领域，用 Qwen3.5-4B/9B 做学生，固定 DeepSeek-V4-Pro 做教师、固定 1000 任务池和 512 条 SFT 配方。AutoMaster 较 Vanilla SFT 平均提升 1.42–8.99 个百分点；消融去除 skill guidance 或 data selection 均下降；Task-Matched SFT 仍低 1.08–10.11pp；Keep skill context 比 Remove 平均高 2.15–4.01pp。

最值得记住：成功轨迹蒸馏低估了固定教师的上限——通过 skill 塑造教师行为并保留行为上下文，能显著提升学生能力。
