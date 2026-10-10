---
title: Can AI Agents Make Open-Ended Scientific Discovery? Evidence from Station
title_zh: AI 智能体能否进行开放式科学发现：来自 Station 的证据
authors:
- Wenyu Du
- Stephen Chung
affiliations:
- DualverseAI
- University of Hong Kong
- University of Cambridge
arxiv_id: '2610.08927'
url: https://arxiv.org/abs/2610.08927
pdf_url: https://arxiv.org/pdf/2610.08927
published: '2026-10-05'
collected: '2026-10-10'
category: MultiAgent
direction: 多智能体科学发现环境与探索机制
tags:
- AI Agents
- Open-ended Scientific Discovery
- Multi-agent
- Supervisor
- Meta Reflection
- Exploration
one_liner: 提出多智能体开放世界环境 Station，结合 Supervisor 与 Meta Reflection，使智能体在无明确指标下重新发现 ICLR
  论文结论达 62.7%
practical_value: '- 在缺乏明确 reward 的开放任务中（如新颖 query 生成、创意素材探索），可引入 Supervisor 角色定期评估当前方向，避免多智能体在无反馈下长时间漂移。

  - 周期性 Meta Reflection 相当于对整体进展做“复盘”，把长期模糊目标分解为阶段性可验证子问题，适合推荐系统冷启动或长尾挖掘这类短期指标不佳但长期有价值的场景。

  - 多智能体科学生态模拟的思路可迁移到用户行为沙盘或策略仿真中：让多个 agent 扮演不同角色（如搜索、浏览、购买）来暴露策略盲区。

  - 将论文结论拆解为可独立验证的 criteria 的评估方法，可借鉴到业务中用 LLM 做开放式优化时，把模糊业务目标拆成可检验的假设清单并自动追踪覆盖率。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现有 AI 科学发现多依赖明确指标或固定流程，开放式任务缺乏可优化 feedback，是否具备自主探索能力尚不明确。

方法关键点：论文提出 Station——一个多智能体模拟科学生态系统的开放世界环境。针对开放式任务缺少中间指标的问题，引入 Supervisor 机制和周期性 Meta Reflection：Supervisor 在智能体迷茫时提供方向性判断，Meta Reflection 定期汇总进展并调整探索策略。作者选取三篇 ICLR oral 论文的核心研究问题，隐藏原始结果并禁用网络访问，将论文发现拆解为独立 criteria，衡量智能体重新发现的比例。

关键结果：Station 平均重新发现 62.7% 的 criteria，远高于 Codex Multiagent-v2 的 15.4% 和 AI Scientist-v2 的 14.4–20.6%。消融与行为分析显示 Supervisor 与 Meta Reflection 共同提升了研究覆盖率和连续性。在两个无 oracle 论文的开放式任务中，智能体的部分发现与研究者在该模型知识截止日期后发表的结果高度吻合。
