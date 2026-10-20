---
title: 'HarnessPro: Recursive Harness Self-Improvement with Pareto Optimization for
  Performance-Cost Trade-offs'
title_zh: HarnessPro：面向性能-成本权衡的递归 Harness 自改进
authors:
- Zhuoshi Pan
- ZhiYuan Feng
- Yukuo Cen
- Honglin Lin
- Junru Lu
- Zhongxia Chen
- Shuo Yang
- H. Vicky Zhao
- Jie Tang
affiliations:
- Tsinghua University
- Z.AI Co., Ltd.
- Shanghai Jiao Tong University
- University of Warwick
- Kuaishou Technology
arxiv_id: '2610.26770'
url: https://arxiv.org/abs/2610.26770
pdf_url: https://arxiv.org/pdf/2610.26770
published: '2026-10-18'
collected: '2026-10-20'
category: MultiAgent
direction: Agent harness 多目标自进化
tags:
- Agent Harness
- Recursive Self-Improvement
- Pareto Optimization
- Cost-Performance Trade-off
- LLM-Generated Tests
- Multi-Agent
one_liner: 多智能体递归改进 agent harness，用 Pareto 选择产出 lite/medium/heavy 三档，同时提升 pass rate
  并降低执行成本
practical_value: '- 用固定 LLM 生成测试替代 LLM judge 评估候选轨迹：在无 ground-truth 的 agent 优化中，失败召回从
  41.7% 提升到 83.3%。做电商导购/客服 agent 的 harness 或 prompt 迭代时，先基于任务描述和初始轨迹生成回归测试，后续所有候选用同一套测试，避免
  LLM 判断过度乐观。

  - 产出 Pareto 前沿而非单一最优：用 normalized weighted squared-distance 按 (1,2)/(1,1)/(2,1)
  选 lite/medium/heavy 三档，分别对应严格成本、均衡、性能优先部署。线上可按预算分流：大促期切 lite，日常用 medium，高价值场景用 heavy。

  - 动态 routing + budget hooks 是降本关键：从任务描述选择 reasoning effort 和 tool call 预算，达到阈值后通过
  hook 提醒收敛或阻断额外调用；比全局降低 reasoning effort 更能保住 pass rate，适合在推荐/搜索 agent 中按 query 难度分档执行。

  - 压缩工具输出和精简 system prompt，保留 prefix 缓存：用类似 RTK 的日志折叠/长输出压缩减少重复上下文 token，是低成本但有效的工程优化。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
现有递归 self-improvement（如 RHO）通过更强探索和验证提升 pass rate，但往往伴随更高 token 消耗和延迟。实际部署中执行成本同样重要，因此论文研究：递归 harness 自改进能否在更低成本下提升任务成功率。

## 方法关键点
- 多智能体框架：trajectory analyzer 联合 G=3 条 rollout 诊断失败、无效探索和冗余开销；planner 按 cost/balanced/performance 三种优先级生成 harness 更新计划；editor 实现候选并 Git 管理。
- Label-free 评测：test synthesizer 根据任务描述和初始轨迹生成固定测试，不用 ground-truth 或官方测试；相比 LLM judge，失败召回从 41.7% 提升到 83.3%。
- 候选选择：过滤低于 initial pass floor 或被 Pareto 支配的候选；用 normalized weighted squared-distance 按权重 (1,2)/(1,1)/(2,1) 选出 lite/medium/heavy 三档进入下一轮。
- 训练任务用 DPP coreset 选 10 个，避免验证/测试集泄漏。

## 关键结果
在 Terminal-Bench 2、SWE-Bench Pro、ProgramBench 上，GPT-5.5+Codex 下 heavy 模式相对 RHO 平均 pass rate +2.0pp、成本 -26.1%。具体：Terminal-Bench 2 heavy 80.8% vs 76.3%，成本 -33.9%；SWE-Bench Pro medium 79.0% vs 80.0%，成本 -53.0%；lite 模式比 Vanilla 成本下降 17.7–57.4% 且 pass rate 更高。GLM-5.2+Claude Code 趋势一致；SWE heavy latency 从 520s 降至 412s。消融显示去掉 test synthesizer 掉点 3.4–10.0pp，去掉 planner 性能降且成本升。

**最值得记住的一句话：性能提升不必以更高执行成本为代价，cost-aware 递归 harness 进化能够同时推进 pass rate 与成本的 Pareto 前沿。**
