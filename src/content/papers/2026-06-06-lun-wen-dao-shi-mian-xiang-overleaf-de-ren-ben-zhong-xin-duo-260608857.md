---
title: 'PaperMentor: A Human-Centered Multi-Agent Writing Tutor for AI Research Papers
  on Overleaf'
title_zh: 论文导师：面向 Overleaf 的人本中心多智能体写作辅导系统
authors:
- Jiarui Liu
- Terry Jingchen Zhang
- Ryan Faulkner
- X. Angelo Huang
- Vilém Zouhar
- Dominik Glandorf
- Isabel Dahlgren
- Van Q. Truong
- Rishit Dagli
- Yuen Chen
affiliations:
- Carnegie Mellon University
- University of Toronto
- Vector Institute
- ETH Zurich
- Max Planck Institute for Intelligent Systems
arxiv_id: '2606.08857'
url: https://arxiv.org/abs/2606.08857
pdf_url: https://arxiv.org/pdf/2606.08857
published: '2026-06-06'
collected: '2026-06-11'
category: MultiAgent
direction: 多智能体写作辅导系统
tags:
- Multi-Agent
- Writing Assistant
- Skill Library
- Overleaf
- Actionable Feedback
one_liner: 构建专家技能库并协调 12 个专业 Agent，在 Overleaf 中提供可操作的论文修改建议
practical_value: '- **专家技能库（Skill Library）设计**：从资深研究者写作建议中提炼领域技能，并注入 Agent prompt，可迁移到电商场景中构建商品文案审核、客服应答等专用
  Agent 的行为准则。

  - **多智能体协同架构**：将写作任务拆解为格式合规、措辞准确、术语一致等 12 个子任务，各 Agent 并行工作，这一模式可用于复杂推荐解释生成、多维度内容审查等场景。

  - **工具链嵌入与交互设计**：以 Overleaf 原生行内批注形式提供建议，不破坏用户主流程，类似思想可直接用在内部文案编辑、CRM 消息审核工具的 AI
  增强上。

  - **人本中心原则**：AI 只提建议，写作仍由人完成，这种保留人工决策的设计适合电商中需要品控把关的环节，如大促文案、政策通知的 AI 辅助撰写。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：早期科研工作者往往缺乏高质量的论文写作反馈，现有 AI 工具多局限于语法纠错或给出笼统分数，难以提供具体、可执行的修改建议。

**方法**：PaperMentor 构建了一个专家技能库（Expert Skill Library），沉淀资深研究者的写作建议，并部署 12 个专业化 Agent，分别负责格式合规、措辞精确度、术语一致性等不同维度。系统以 Overleaf 原生行内批注的形式输出建议，完全保留人类作者对写作的控制权。

**结果**：用户研究（n=14）显示，90.6% 的生成批注被评为“可操作”，67.5% 被评为“有效”，显著优于未使用技能库的 GPT-5.2 基线。系统已开源。
