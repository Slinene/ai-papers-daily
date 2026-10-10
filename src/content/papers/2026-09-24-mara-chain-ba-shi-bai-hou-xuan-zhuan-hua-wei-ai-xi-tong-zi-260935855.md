---
title: 'Mara Chain: Rethinking Failure as a Stepping Stone for AI System Auto-Evolution'
title_zh: Mara Chain：把失败候选转化为 AI 系统自进化的垫脚石
authors:
- Yubin Lyu
- Fu Li
- Jiawei Fei
- Yang Zhao
- Weixing Mei
- Yinan Wu
affiliations:
- Ant Group
- Beijing Intelligent Game and Decision Lab
- Beijing Defense Innovation Institute
arxiv_id: '2609.35855'
url: https://arxiv.org/abs/2609.35855
pdf_url: https://arxiv.org/pdf/2609.35855
published: '2026-09-24'
collected: '2026-10-10'
category: Agent
direction: Agent 自进化 · 失败驱动优化
tags:
- Agent Optimization
- Failure-Driven Refinement
- Pareto Top-N
- Self-Evolution
- LLM
one_liner: 保留被拒候选并做链式细化，在技能、harness 与检索管道优化上大幅提升样本效率与最终性能
practical_value: '- 在 LLM 驱动的 prompt/skill/harness 离线优化中，不要直接丢弃未达阈值的候选；保留其 rollout
  日志、错误分析、变更历史，用深度受限（如 d=5）的链式 refine 沿同一 lineage 继续改，尤其适合长链路、失败模式顽固的任务（如 query 改写、RAG
  检索管道、多步 agent workflow）。

  - 候选池管理上，用 per-instance Pareto 支配过滤保留互补性强的候选，再用 Top-N 按平均验证分数截断，防止高维 pass/fail 指标下候选池无限膨胀；N
  建议取 3 或更小。

  - 工程实现将全部 rollout 原始数据、分数、分析和 changelog 落盘为 filesystem-backed memory；proposer 的
  analyze 阶段读原始记录，mutate 阶段读压缩后的 analysis + changelog，避免长上下文和原始数据污染。

  - 设计 artifact schema 时，为不同表示（prose < script < extension）设置可靠性先验，当证据显示修改被绕过时，引导 proposer
  升级到更高可靠性的表示（如把自然语言提示改成可执行脚本），使优化产物可控、可执行。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
现有 propose–evaluate–select 范式把未达标的候选直接丢弃，但这些失败候选往往包含部分修复、正确方向或有价值的排除证据。丢弃导致后续提案反复重蹈同一失败模式，形成“persistent failure barriers”，尤其在长 horizon 任务上浪费大量 rollout 预算却无法突破。

## 方法关键点
- **Mara Chain Reflective Refinement**：候选未通过 acceptance bar 时，不丢弃，而是保留其 rollout traces、残差失败、结构化分析和变更历史，形成一条深度受限的 lineage（默认 d=5）。链上每步基于累积证据产生后代，并在同一 minibatch 上评分；只有后代超过父代才进入验证，否则整条链被丢弃。
- **Pareto-filtered Top-N 选择**：外层候选池先用 per-instance 弱 Pareto 支配过滤保留互补性强的候选，再按平均验证分数做 Top-N 截断（本文 N=3），防止高维验证分数下候选池无限膨胀。
- **通用 artifact schema**：任意可映射为目录结构的 tunable artifacts（skill、harness、retrieval pipeline）都能用同一流程优化；可靠性先验 prose < script < extension，引导 proposer 从自然语言升级到可执行代码。
- **Filesystem-backed memory**：所有原始 rollout 数据、分数、分析和 changelog 持久化，proposer 的 analyze 阶段读原始记录，mutate 阶段读压缩后的 analysis + changelog。

## 关键实验结果
- AppWorld skill 优化：相对 GEPA/ACE/SkillOpt-Lite 最高 +20.5% 相对性能；达到 0.8 验证分仅需 3,280 rollouts，而 GEPA 需 9,514（少 65.5%），最终分数 0.87 vs GEPA 0.805。
- TerminalBench 2.1 harness 优化：pass rate 71.9%，比 AHE/Codex/Kira base 的 51.7% 高 20.2 pp，比 Meta-Harness/OpenCode 的 49.4% 高 22.5 pp。
- MuSiQue retrieval pipeline 优化：test nDCG@10 提升 +0.104，Recall@10 提升 +0.131。
- 消融显示增益集中在难任务（Challenge TGC +4.8pp，TB2.1 +14.6pp），Mara Chain 与 Top-N 选择协同；跨 GLM-5、DeepSeek-V4-Pro、Qwen3.5 泛化。

## 最值得记住的一句话
失败的候选不是死胡同，而是下一步的垫脚石；保留并链式 refine 它们，比每次重新诊断更有效。
