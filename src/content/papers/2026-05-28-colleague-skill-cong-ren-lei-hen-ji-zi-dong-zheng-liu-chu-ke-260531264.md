---
title: 'COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation'
title_zh: COLLEAGUE.SKILL：从人类痕迹自动蒸馏出可检查、可纠正的Agent技能包
authors:
- Tianyi Zhou
- Dongrui Liu
- Leitao Yuan
- Jing Shao
- Xia Hu
affiliations:
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2605.31264'
url: https://arxiv.org/abs/2605.31264
pdf_url: https://arxiv.org/pdf/2605.31264
published: '2026-05-28'
collected: '2026-06-01'
category: Agent
direction: Agent 技能自动化生成 · 专家知识蒸馏
tags:
- AI Skills
- Knowledge Distillation
- LLM Agents
- Persona
- Open Source
- Trace-to-Skill
one_liner: 提出双轨蒸馏流水线，将人类工作痕迹和交互证据转化为可移植、可检查、可版本管理的Agent技能制品
practical_value: '- 电商场景下，可将资深运营/选品专家的聊天记录、设计文档、审核备注蒸馏为Agent技能包，封装如商品筛选规则、风控阈值、沟通话术模板，实现专家知识的可复用与跨团队传递。

  - 双轨设计分离“能力”与“行为”，能力轨道存放业务规则、决策启发式，行为轨道约束交互风格与边界；在推荐Agent中可分别调控推荐策略与推荐理由的生成语气，避免能力与人格混淆。

  - 基于自然语言的修正和版本回滚机制：Agent上线后，业务人员用“这里不该推荐此类商品”等反馈直接修正技能包，系统自动归档旧版本并生成新版本，便于审计和快速实验。

  - 本地优先的治理与安装器：技能包可作为本地文件管理、删除和分发，支持主流Agent主机（Claude Code、Codex等），适合企业内部敏感知识的受控使用；画廊模式可构建内部技能市场。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
LLM代理需要承载人的专业知识、判断和交互风格，但这些知识通常散落在聊天记录、设计文档、代码审查等异构痕迹中，而非以清晰指令存在。现有记忆和人格系统仅能抓取碎片化证据，缺乏从痕迹到可检查、可修正、可在多宿主间移植的技能制品的端到端流程。论文聚焦于将人类痕迹蒸馏为受约束的、可治理的Agent技能包，而非身份模拟。  

**方法**  
- 定义个人锚定技能制品，要求具备可移植性、可检查性、可组合性、可纠正性和可治理性。  
- 设计双轨蒸馏流水线：能力轨道提取持久的工作方法、决策启发式、心智模型；行为轨道提取表达偏好、交互规则和修正历史，分别生成`work.md`与`persona.md`。  
- 生成符合Agent Skills标准的版本化技能包，包含组合入口、独立子技能（工作/人格）、安装清单及生命周期元数据。  
- 支持三种预设：同事（内部工作痕迹）、名人（公开资料+源边界）和关系（私有痕迹，强调同意与本地控制），通过同一制品流程适配不同证据和治理要求。  
- 提供自然语言反馈驱动的修正与回滚管理，形成“创建-检查-调用-修正-再安装”的闭环。  

**关键结果**  
论文主要贡献是系统设计与开源部署，而非任务性能对比。截至2026年5月，GitHub仓库约18.5k星标，公开画廊已收录215个技能、165位贡献者，累计超10万画廊星标，展示了从本地生成到社区分发的完整制品生态。  

**核心观点**  
“数字蒸馏的目标是产出可阅读、可修正、可安装、可收回的制品，而非仅听起来像目标人物的不透明提示。”
