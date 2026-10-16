---
title: 'Terminal-RSI: Recursive Self-Improving Terminal Agents via Recursive Self-Rewrite
  and Policy-Refine'
title_zh: Terminal-RSI：通过递归自改写与策略精炼实现终端智能体递归自改进
authors:
- Junyao Yang
- Zongxia Li
- Yucheng Shi
- Zhongzhi Li
- Ruhan Wang
- Ruiwen Zhou
- Haitao Mi
- Shuicheng Yan
- Leowei Liang
affiliations:
- Tencent Hy Frontier
- National University of Singapore
- University of Maryland, College Park
- University of Georgia
- Indiana University
arxiv_id: '2610.22192'
url: https://arxiv.org/abs/2610.22192
pdf_url: https://arxiv.org/pdf/2610.22192
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: 终端 Agent 递归自改进强化学习
tags:
- terminal agents
- RL
- self-improvement
- verifier
- reward shaping
- GAE
one_liner: 用递归自改写与策略精炼交替训练，把终端 Agent 验证反馈转成策略提升
practical_value: '- 可借鉴「验证轨迹重写 + 策略精炼」的交替训练范式：用业务中的 reward/verifier 信号找出成功或部分成功轨迹，先重写成更优示范再做策略更新，适合电商
  Agent 的任务完成型 RL。

  - TB-GAE 对多轮交互做 token 级信用分配时保留衰减：在搜索/推荐 Agent 的多轮对话 RL 中，可按 turn 边界做 skip-observation
  GAE，避免跨 turn 的 token baseline 偏移。

  - FDR 与 SPR 的奖励设计适合业务落地：按任务族做 dense progress reward 校准，同时把严格成功与有界部分奖励解耦，可减少 reward
  hacking 并稳定训练。

  - Warm-up Critic 与 stage-specific LR 可迁移到多阶段 RLHF/RLAIF：先预热 critic 再更新 policy，且不同阶段用不同学习率，能提升生成式推荐的训练稳定性。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
终端 Agent 需要把 verifier 的验证结果转成可用的策略更新，并把局部进展变成完整任务解决。现有方法在 token 级信用分配、跨任务族奖励校准和严格成功信号上仍不稳定。

**方法关键点**  
Terminal-RSI 交替执行两种阶段：Recursive Self-Rewrite (RSR) 对已验证轨迹做递归重写，Recursive Policy-Refine (RPR) 继承 critic 做递归策略精炼。奖励侧提出 TB-GAE：在 turn 边界做 skip-observation GAE，保留 token 级 baseline 并在交互 turn 间施加衰减；FDR 按任务族校准语义进展，SPR 把严格成功和有界部分奖励分离。训练上引入 Warm-up Critic、递归 critic handoff 和分阶段学习率，协同两个精炼阶段。

**关键结果数字**  
从 Qwen3.8-27B base 出发，经 RSR-1 → RPR-1 → RSR-2 → RPR-2 得到 Terminal-RSI-27B：Terminal-Bench 4.0 达 19.84%，TB 2.1 达 86.52%，TB 3.0 达 16.95%，TB Hard 达 79.00%。LHTB 上 process reward 由 0.21 升至 0.37，严格完成从 0/46 到 5/46；SWR100 成功率从 3.00% 翻倍到 6.00%。
