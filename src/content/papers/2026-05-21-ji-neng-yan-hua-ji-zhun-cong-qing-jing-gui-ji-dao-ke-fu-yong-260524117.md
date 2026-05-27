---
title: 'SkillEvolBench: Benchmarking the Evolution from Episodic Experience to Procedural
  Skills'
title_zh: 技能演化基准：从情景轨迹到可复用程序技能的评估
authors:
- Yingtie Lei
- Zhongwei Wan
- Jiankun Zhang
- Samiul Alam
- Zixuan Zhong
- Peizhou Huang
- Xin Wang
- Jingxuan Zhang
- Donghao Zhou
- Yunta Hsieh
affiliations:
- The Ohio State University
- The University of Chicago
- University College London
- University of Michigan
- Amazon
arxiv_id: '2605.24117'
url: https://arxiv.org/abs/2605.24117
pdf_url: https://arxiv.org/pdf/2605.24117
published: '2026-05-21'
collected: '2026-05-27'
category: Agent
direction: Agent 技能演化与经验复用评估
tags:
- agent skills
- experience reuse
- benchmark
- skill evolution
- procedural abstraction
- evaluation
one_liner: SkillEvolBench 诊断基准揭示 LLM 智能体难以从任务轨迹中抽象出可迁移的程序技能，原始轨迹复用常优于提炼技能。
practical_value: '- 在智能体经验复用系统中，**先保留原始轨迹**（类比 RAG 中的原始文档）可能比提前抽象为技能更可靠，抽象过程容易丢失上下文线索。

  - 技能更新策略上，**总是更新**（always-update）比仅失败时更新更有效，但需配合过滤机制防止程序漂移。

  - 评估经验转化时，必须区分**本地重放**（replay）和**冻结部署**（held-out transfer），单一学习成功率具有欺骗性。

  - 在操作流程自动化（如客服步骤、商品配置）中，可仿照其角色条件化设计，测试在分布偏移、对抗输入和技能组合下的鲁棒性。

  - **库容量不是越大越好**，强制资源捆绑（Tier-3）可能引入程序垃圾，重点应放在选择性保留稳定、可验证的程序片段。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
LLM 智能体在解决真实任务时会积累丰富的情景轨迹，但如何将一次性经验提炼为可复用的程序技能（如操作指南、脚本）仍是一个开放问题。现有工作多聚焦于经验复用或冷启动技能生成，缺乏对技能形成过程的诊断性评估——即从噪声轨迹中抽象出紧凑、可加载、可跨任务迁移的程序知识。

**方法**  
- **SkillEvolBench** 包含 6 个真实工作环境（代码调试、API 编排、数据处理、文档转换、研究综合、通信调度），每环境 5 个任务家族，每个家族 6 个角色条件任务：3 个用于**技能获取**（规范、丰富、变体），3 个用于**冻结部署**（上下文偏移、对抗捷径、技能组合）。  
- 协议：智能体在获取阶段根据轨迹和验证器反馈调用 **Skill Author** 更新外部技能库，之后冻结库，评估其在未见任务上的表现。  
- **对照条件**：无技能、原始轨迹检索、静态/可修订的 curated 技能、自生成技能（含零样本、经验诱导、总是更新等变体）。  
- 指标：学习成功率 LSR、重放成功率 RSR、评估成功率 ESR 及其分解（CSSR/ARSR/CompSR）。

**关键实验**  
- 在 10 个模型配置和 3 种智能体框架（Claude Code, Codex CLI, Gemini CLI）上测试。  
- 主要发现：技能条件可提升 LSR/RSR，如 Claude Sonnet 4.6 自生成经验下 LSR 提升 5.5 pp、RSR 提升 10.0 pp，但 ESR 及子指标改善不稳定，甚至下降。  
- **原始轨迹**（Raw Trajectory）在多数情况下优于提炼技能，尤其在 ESR、ARSR 和 CompSR 上，表明当前抽象过程丢弃了关键上下文。  
- 容量诊断：强制 Tier‑3 资源库增长未能稳定提升 ESR，反而可能引入程序杂草（如 Gemini 3 Flash ESR 从 35.6% 降至 27.8%）。  
- 成本‑成功率分析：总是更新的自生成技能（SelfGen‑Always）平均 ESR 提升 +0.44 pp，但收益高度依赖模型。

**核心结论**  
当前智能体倾向于将经验固化为局部补丁，而非可迁移的程序技能；从轨迹到技能的抽象瓶颈在于选择性保留——需要同时过滤偶然细节并保留支持未来调用、验证和组合的线索。
