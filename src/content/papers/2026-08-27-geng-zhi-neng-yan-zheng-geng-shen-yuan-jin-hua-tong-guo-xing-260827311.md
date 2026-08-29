---
title: 'Verify Smarter, Evolve Further: Efficient Harness Evolution through Behavior-Aware
  Verification'
title_zh: 更智能验证，更深远进化：通过行为感知验证实现高效 Harness 进化
authors:
- Jinghan Xu
- Yikai Zhang
- Aili Chen
- Weiyuan Li
- Jiaqing Liang
- Deqing Yang
affiliations:
- School of Data Science, Fudan University
- Shanghai Key Laboratory of Data Science
- College of Computer Science and Artificial Intelligence, Fudan University
arxiv_id: '2608.27311'
url: https://arxiv.org/abs/2608.27311
pdf_url: https://arxiv.org/pdf/2608.27311
published: '2026-08-27'
collected: '2026-08-29'
category: Agent
direction: Agent 自进化 · 行为感知验证
tags:
- Agent Harness
- Self-Evolution
- Behavior-Aware Verification
- Budget-Aware
- Attributable Evidence
one_liner: 提出预算感知的 HARNESSLENS 框架，用行为相关任务和可归因证据门控筛选候选修改，显著提升 harness 进化样本效率
practical_value: '- 评估候选修改时，不要用固定验证集评估所有候选；根据候选意图选择相关任务（supporting trajectories +
  相关目标/工具），使信号不被无关任务稀释，回归检测更敏感。

  - 采用可归因证据门控：要求观察到的改进能归因到具体行为变化（如 recovered / stable success），仅聚合指标提升不足以接受修改，避免噪声导致接受有害修改。

  - 预算感知控制器：设定总交互预算，每次迭代前检查是否能覆盖完整验证+确认轮次，否则停止，避免评估不充分。

  - 轨迹诊断与经验复用：把每次 rollout 轨迹转化为可复用经验和缺陷，支持后续候选生成和验证，提高样本效率。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
Agent harness 决定 LLM agent 如何感知任务、使用工具、在环境中行动，手动配置难以迁移，需要自动化进化。现有 propose-and-verify 方法对所有候选修改使用固定或随机任务集验证，导致大量无关 rollout，聚合分数稀释修改信号，难以发现具体回归。因此需要行为感知验证，根据每个候选修改的预期行为选择验证任务并归因行为变化。

## 方法关键点
- HARNESSLENS 包含三阶段：Context Exploration（任务空间探索，按主要用户目标分组任务；harness 空间探索，识别可编辑组件及其更新机制）、Trajectory Diagnosis（从初始和验证 rollout 提取可复用经验和反复缺陷，生成证据支持的修改提案）、Harness Evolution（迭代选择提案、行为感知验证、审查更新）。
- 行为感知验证：根据提案支持轨迹、任务目标、约束、工具需求选择相关任务，并加入潜在回归任务；每个验证批次至少5个不同任务，控制器根据剩余预算固定 trial 数量。
- 可归因证据门控：比较当前 harness 与候选 harness 的配对轨迹，将任务行为变化标记为 recovered / stable success / regressed / still failing / mixed；仅当存在可归因正向证据且无可归因回归时才进入确认轮，最终需确认批次主要指标改进才接受。
- 预算感知：总交互预算 B=200 单位，包括任务 rollout 和 LLM session；控制器在每轮迭代前检查是否能覆盖完整两轮验证+确认，否则停止，避免投入不足成本的验证。

## 关键结果
- 三个 agent harnesses（OpenCode, Codex, Pi）与四个基准（τ2-bench Retail, τ3-bench Banking Knowledge, Terminal-Bench 2.0, BIRD Mini-Dev Challenging），使用 deepseek-v4-flash-preview。
- 对比 baseline：初始 H0、Self-Harness、Meta-Harness、HarnessFix；HARNESSLENS 预算 200 单位（包括 LLM sessions 和 rollouts），而 baselines 配置的 rollout 数量分别为 4800、660、300。
- 结果：HARNESSLENS 平均 held-out 性能提升 7.6–13.6%，在 12 个 harness-benchmark 对中 8 个最佳或并列最佳；从不低于 H0。具体：OpenCode 平均 41.83→47.53，Codex 40.94→44.06，Pi 45.49→49.67。
- 消融：移除行为感知批选择（Fixed/Random/RHO-based）或可归因门控（Metric-Only Gate）都显著减弱性能，证明两个机制互补。

> 行为感知验证 + 可归因证据门控，让 harness 进化在小预算下更可靠，避免固定验证集稀释信号和伪回归。
