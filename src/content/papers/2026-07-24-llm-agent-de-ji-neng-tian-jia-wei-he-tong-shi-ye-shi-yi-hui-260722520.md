---
title: 'The Regression Tax: Decomposing Why Skills Help and Hurt LLM Agents'
title_zh: LLM Agent 的技能添加为何同时也是一种“回归税”
authors:
- Darshan Tank
- Baran Nama
affiliations:
- Sentient Labs
arxiv_id: '2607.22520'
url: https://arxiv.org/abs/2607.22520
pdf_url: https://arxiv.org/pdf/2607.22520
published: '2026-07-24'
collected: '2026-07-27'
category: Agent
direction: Agent 技能评估与回归机制分析
tags:
- agent skills
- regression
- grounding displacement
- skill-description osmosis
- verification displacement
- paired evaluation
one_liner: 添加技能库带来的回归抵消了 59% 的增益；三种回归机制以 grounding displacement 为主，且技能描述即使不被调用也可通过上下文渗透改变行为
practical_value: '- **评估技能库时必须分解增益与回归**：不要只看净通过率，应同时报告新解决的任务数和被破坏的任务数。两个净效果相同的技能库，回归少的那个更可靠。

  - **警惕技能描述的“渗透”效应**：即使某个技能从未被调用，仅因其描述常驻系统提示（system prompt），也会改变 agent 的行为，导致原本正确的任务失败。评估时应额外增加“仅描述存在”的对照条件，以隔离该影响。

  - **强化 grounding 与 verification 环节，而非仅优化过程方法**：回归和残余失败主要出现在输入解读（grounding）和输出检查（verification）阶段，而现有技能库过度关注方法步骤。在编写技能时，应增加具体的查表读表指引、定义澄清和可执行输出校验，而不是只给通用流程。

  - **利用配对轨迹对比定位问题**：将同一任务在有/无技能下的执行轨迹进行对比，可以清晰区分失败发生在哪个阶段（读错输入 vs. 算对但校验缺失），从而更有针对性地修复技能而非盲目删除整个技能库。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：当前给 LLM Agent 添加程序性技能普遍用平均任务成功率提升来评价，但该指标掩盖了一个重要代价——技能也会让一些原本能解决的任务变失败（即回归）。理解回归为何发生、技能在哪些阶段造成干扰，对于设计更可靠的 Agent 系统至关重要。

**方法关键点**：
- 在 OfficeQA‑Pro（财报问答）和 SpreadsheetBench（电子表格操作）两个办公自动化基准上，用三组模型‑脚手架组合（OpenCode‑MiniMax‑M2.7, Codex‑GPT‑5.4‑mini，Claude Code‑Sonnet‑4.6）执行近 6000 次实验，固定任务集，对比无技能、三种由不同生成器（Anthropic, OpenAI, 自研）从同一批故障信号生成的技能库。
- 定义四种配对结果：增益（无技能失败、有技能通过）、回归（无技能通过、有技能失败）、残余失败（都失败）、保留（都通过）。净效应 = 增益数 − 回归数。
- 通过配对轨迹分析，提出三种回归机制：(i) **技能描述渗透**——技能描述一直存在于上下文中，即使主体未被调用也会改变回答；(ii) **grounding 位移**——调用技能后，过程指引覆盖了 agent 原本正确的信息定位，导致读错数据、表或定义；(iii) **verification 位移**——技能压制了 agent 原本会执行的输出检查，导致正确计算但未校验而失败。

**关键结果数字**：
- 在全部 18 个条件下，共观察到 553 次增益转换和 324 次回归转换，回归抵消了 59% 的总增益；OfficeQA‑Pro 上回归占增益的 66%，SpreadsheetBench 上占 56%。
- 81 个可编码的 OfficeQA‑Pro 回归中，72.8% 为 grounding 位移，17.3% 为渗透，仅少数涉及 verification。
- 对 SpreadsheetBench 的公式类任务执行重打分后，发现 226 个被原分值判错的公式实际正确（恢复 11–49 个任务条件），说明失败往往在输出校验阶段，而非过程方法本身。
- 五个名义显著条件中只有三个通过 Bonferroni 校正（全部在 Claude Code 的 SpreadsheetBench 上），显示技能的正净增益并不稳健。

**一句话结论**：技能评估必须分解为增益和回归，回归主要源于 grounding 被覆盖和描述渗透，而残留失败同样集中在 grounding 与 verification 两端，技能设计应更重视输入精准定位和输出验证，而非仅优化执行步骤。
