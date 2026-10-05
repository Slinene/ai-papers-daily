---
title: Scaling Trajectories for Complex Tasks through Recursive Self-Rewrite
title_zh: 递归自重写扩展复杂任务成功轨迹
authors:
- Zongxia Li
- Yucheng Shi
- Zhongzhi Li
- Junyao Yang
- Ruhan Wang
- Chengsong Huang
- Fuxiao Liu
- Haitao Mi
- Jordan Boyd-Graber
- LeoweiLiang
affiliations:
- Tencent HY LLM Frontier
- University of Maryland, College Park
- University of Georgia
- National University of Singapore
- Indiana University
arxiv_id: '2610.02826'
url: https://arxiv.org/abs/2610.02826
pdf_url: https://arxiv.org/pdf/2610.02826
published: '2026-10-01'
collected: '2026-10-05'
category: Training
direction: 轨迹重写 · 自改进 SFT
tags:
- Trajectory Rewriting
- Self-Improvement
- SFT
- Multi-Harness
- Agent Training
one_liner: 用 planner-critic-executor 递归重写多 harness 成功轨迹，将 2k 源轨迹扩至 11k，SFT 后 terminal
  任务 pass@3 全面提升
practical_value: '- 数据合成去 harness 特定干预：引入 critic 自动检查 verifier leakage / solution
  leakage，可借鉴到推荐 Agent 训练数据生成中，避免把策略特有字段、评估答案或工具返回信号写进 SFT 样本，提升线上一致性。

  - 成功轨迹规模化：用 planner 把少量成功 case 抽取为 runbook，executor 在新 sandbox 重放生成多样化轨迹，适合电商搜索/推荐中稀缺的成交路径、高转化
  query 改写样本扩增。

  - 多策略并行收集后统一蒸馏：三个 harness 联合比单一最强 harness 多解决 34.3% 任务；在业务中可并行跑多路召回/排序/工具链，仅保留成功结果训练
  base 模型，避免单管线能力偏置。

  - 过程奖励过滤：重写后 process reward 上升说明中间步骤质量提高；对长程推荐/Agent 任务，可用过程奖励而非只看最终结果来做数据筛选。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：困难任务的成功轨迹可提供监督信号，但不同 harness（工具/控制器/工作流）中包含部署时不可用的干预与约定，直接 SFT 易造成训练-部署不一致。

**方法**：RSR 用单个基础模型 Qwen-3.8-27B 在多种 harness 下发现成功解，并通过 planner-critic-executor 递归重写。Planner 将成功过程抽取为 runbook；Critic 检查 verifier/solution leakage，不合格则用 critique 反馈重新生成；Executor 在全新 sandbox 中按合格 runbook 执行，从而将 harness-specific 轨迹重建为通用 harness 下的可复用轨迹。

**结果**：在约 3K 自收集 terminal 任务上，三个 harness 联合解决 759 个任务，比最强单 harness 多 34.3%。RSR 把 2,001 条成功源轨迹扩展为 11,094 条高质量轨迹。SFT 后，Terminal-Bench 2 pass@3 从 57.0% 到 74.2%，TB4 从 1.5% 到 9.1%，自建 Hard 从 39.0% 到 63.0%，Software TB 从 3.0% 到 6.0%；Long-Horizon 过程奖励从 0.21 提升到 0.29。
