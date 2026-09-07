---
title: Testing Interchangeability in LLM Agent Teams
title_zh: 测试LLM智能体团队中的可互换性
authors:
- Jianxin Gao
- Tianyi Yu
- Linna Deng
- Runze Li
- Zining Wang
affiliations:
- China Agricultural University
- Tianjin University of Finance and Economics
- Jilin University
- Tianjin University of Science and Technology
arxiv_id: '2609.05279'
url: https://arxiv.org/abs/2609.05279
pdf_url: https://arxiv.org/pdf/2609.05279
published: '2026-09-04'
collected: '2026-09-07'
category: MultiAgent
direction: 多智能体协作 · 团队更换与协调效率
tags:
- LLM agents
- multi-agent teams
- interchangeability
- coordination efficiency
- agent swap
- emergent conventions
one_liner: 成队后交换角色匹配智能体，任务分损失小但沟通效率下降16–63%，历史越长影响越大
practical_value: '- 生产环境替换 agent/模型版本时，不要只看任务分、成功率；建议监控“单位进度的 communication/token
  开销”，角色替换会带来 16–63% 的隐性协调成本。可把 swap 后的 token 增量纳入回归测试。

  - 私有 notebook/长期共建历史会让智能体之间形成约定，替换旧成员会干扰 partner conventions；想支持热插拔的团队可限制私有记忆、定期重置共享约定或做去耦合，降低替换冲击。

  - 议程/planner 类关键 agent 被替换后，留存 agent 会承担更多沟通成本；架构上可把 planning 与执行解耦，避免替换关键角色影响全队协调效率。

  - Greedy decoding 同时降低团队 drift 和 swap penalty；如果团队需要更可互换、更稳定的替换行为，低温度/贪心解码是低成本工程手段。更长的
  formation history 会加大 drift，需在训练效率和替换稳定性之间权衡。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

动机：生产多智能体系统不断替换角色内智能体，框架与角色契约默认“能胜任该角色即可互换”。该工作直接检验这一假设是否成立。

方法：每个 setting 独立组建 8 个团队，使用同一 base model 在同一任务上运行，每个 agent 在 10 个 formation episodes 中维护私有 notebook；随后在角色匹配的团队之间交换 agent，并在 held-out 任务上测量变化。对照 placebo 复现 roster change 的干扰，但不更换实际占位者。另做三组消融：base model、decoding temperature、formation length。

关键结果：交换对任务分数损失较小，但单位进度所需通信增加 16%–63%；Hanabi 中被交换 agent 甚至比全新 agent 成本更高，体现与前任伙伴形成的约定干扰。Collab-Overcooked 中当设定议程的 agent 被替换，额外通信主要来自留下的一方。消融显示 swap penalty 与独立团队间 drift 同步：greedy decoding 同时降低两者，formation history 加倍则同时升高两者。智能体在任务结果上比在协调效率上更可替代，且更长 formation history 会放大替换效应。
