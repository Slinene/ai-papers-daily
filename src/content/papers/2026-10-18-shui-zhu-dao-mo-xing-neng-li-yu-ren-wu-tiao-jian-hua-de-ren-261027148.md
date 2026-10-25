---
title: Who Takes the Lead? Model Ability and Task-Conditioned Collaboration with Humans
title_zh: 谁主导？模型能力与任务条件化的人机协作
authors:
- Weien Li
- Haochen Liu
- Zeyu Li
- Rui Song
- Zixuan Dong
- Ye Yuan
affiliations:
- McGill University
- MIT - Massachusetts Institute of Technology
- University of Cambridge
- University of Toronto
- Mila - Quebec AI Institute
arxiv_id: '2610.27148'
url: https://arxiv.org/abs/2610.27148
pdf_url: https://arxiv.org/pdf/2610.27148
published: '2026-10-18'
collected: '2026-10-25'
category: Agent
direction: Agent 人机协作与任务条件控制分配
tags:
- Human-AI Collaboration
- LLM Agents
- Control Allocation
- Shared Autonomy
- Model Evaluation
one_liner: 在共享控制迷宫中证明强模型能根据人类相对优势选择性分配控制，而非简单减少人类参与。
practical_value: '- 在构建搜索/推荐 Agent 时，不要用“人类介入率”作为协作质量指标；应评估 agent 在给定上下文下的相对能力（如用户偏好的可预测性、数据稀缺性），动态决定是否请求用户、自主执行或完全移交，类似路由机制。当用户侧有信息优势（如长尾个性化、实时意图）时引入人工，常规高频查询则
  agent 自主处理。

  - 借鉴共享控制接口设计：让 agent 每步输出显式控制决策（act/request/handoff），便于监控和在线评估；用 solo 性能作为先验，对低能力模型或低置信场景增加
  human-in-the-loop fallback。

  - 任务条件化协作可作为离线评估框架：构造“人类优势/均势/agent优势”的模拟环境，量化不同 LLM 的协作策略，用于选型或提示词调整，避免上线后才发现 agent
  过度求助或过度自主。

  - 实验发现强模型在人类无优势时几乎不求助，仅在人类路线更短时约80%初始决策涉及人类，说明可设置阈值或条件策略：只有当用户信息增益显著大于 agent 能力时才触发人类参与。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：随着 LLM agent 能力增强，它们可能减少求助人类，但这不一定是协作失败，可能是正确分工。仅凭人类参与率无法区分。需要系统研究 agent 能力和任务优势如何影响控制分配。

**方法**：设计共享控制迷宫，agent 控制一个 avatar，人类控制另一个，共同目标是最少团队回合到达目标。agent 每回合决定自己行动还是交给人类；初始位置设定人类最短路径优势（人类优势/均势/agent优势），任务其他不变。评估 GPT 5.6 Sol、Command A+、Qwen 3.8 27B、Command R 四个模型，先测单智能体 solo 能力（单 avatar 全图可见），再与人类参与者进行三种优势条件下的 co-play。

**关键结果**：四个模型中，solo 性能越强，越表现出选择性、路线条件化的人类参与：能可靠独立解决迷宫的模型在人类无优势时几乎总是自己行动，而当人类路线更短时在约80%的初始决策中涉及人类。solo 性能明显较弱的 Command R 没有这种选择性。结论：强模型会根据任务条件和相对优势动态分配控制，而非简单减少人类参与。
