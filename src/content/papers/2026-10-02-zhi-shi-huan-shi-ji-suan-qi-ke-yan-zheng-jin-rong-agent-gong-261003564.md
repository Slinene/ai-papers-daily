---
title: Knowledge or Calculator? Decomposing the Skill Premium in Verifiable Financial
  Agent Workflows
title_zh: 知识还是计算器？可验证金融 Agent 工作流中技能溢价的分解
authors:
- Jermyn Zhen Yong Bek
- Zhuang Qiang Bok
- Zhongtian Sun
affiliations:
- Independent Researcher
- Deep Insight Labs
- University of Kent
- University of Cambridge
arxiv_id: '2610.03564'
url: https://arxiv.org/abs/2610.03564
pdf_url: https://arxiv.org/pdf/2610.03564
published: '2026-10-02'
collected: '2026-10-05'
category: Eval
direction: Agent 工作流评测 · 技能溢价分解
tags:
- Agent
- LLM
- Evaluation
- Tool Use
- Skill Premium
- Financial AI
one_liner: 用 2603 个金融 episodes 分解 agent 技能溢价：策展工具 +19.5、文档 +5.6，现场生成几乎无效
practical_value: '- 将高频、可标准化的 agent 子任务沉淀为 curated skill package（可执行工具 + 规范输出 schema），不要依赖
  agent 单次生成；实验表明现场生成几乎无增益且更耗 token/turn。

  - 数值密集型流程（如预算分配、CTR/ROI 校验、竞价计算）优先提供 executable tools，而非文档说明；工具单独带来 +19.5 分，文档仅
  +5.6 分。

  - 涉及严格输出结构（如商品标签、推荐理由模板、广告文案字段）的场景，把 output schema 与操作手册作为 curated resource 注入能改善
  adherence；但工具+文档组合收益次可加，不要盲目叠加资源。

  - 建立 agent 工作流评测时使用任务特定确定性 verifier 和可再生成 ground truth，避免耗时 LLM-as-judge 且保证结果可复现。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：财务 AI agent 不仅需要检索事实，还需要正确的量化执行、可靠使用程序资源、可审计的结构化输出。现有评估缺乏对可验证技能运用的系统衡量。

**方法**：构建 FinSkillBench，包含 2,603 个 point-in-time episodes，覆盖投资组合构建、风险管理、基本面分析 12 个子任务，配备隐藏可再生成 ground truth 与任务特定确定性 verifier。在 9 个模型、3 种资源条件下运行 17,820 个 episodes，对比 curated skill packages 与单 episode 内生成技能；随后分别授予人类编写的程序文档和可执行领域工具，分解技能溢价。

**关键结果**：成对分析显示 curated skill packages 平均提升 +16.2 分（0.366→0.528），而 episode 内生成技能仅 +0.5 分且消耗更多 token 和轮次。分解 curated 溢价：文档单独 +5.6 分，工具单独 +19.5 分，二者组合呈次可加。效果强工作流依赖：可执行工具主导数值密集工作流，文档在程序或输出 schema 瓶颈时更重要，解释性任务两者皆有增益。10 个评分变体与 cluster bootstrap 分析显示符号稳定，独立第二 harness 复现方向模式。
