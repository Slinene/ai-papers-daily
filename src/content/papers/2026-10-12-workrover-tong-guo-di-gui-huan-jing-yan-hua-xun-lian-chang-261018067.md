---
title: 'WorkRover: Scaling Long-Horizon Cowork Agent Training Via Recursive Environment
  Evolution'
title_zh: WorkRover：通过递归环境演化训练长程 Cowork Agent
authors:
- Hang He
- Linting Wang
- Guanming Liu
- Bo Mao
- Jinxiu Liu
- Yiran Suo
- Maosen Zhou
- Zhiheng Xi
- Guanting Dong
- Zhou Shao
affiliations:
- Fudan University
- East China Normal University
- Renmin University of China
- Shanghai Qiji Zhifeng Co., Ltd.
- Shanghai Innovation Institute
arxiv_id: '2610.18067'
url: https://arxiv.org/abs/2610.18067
pdf_url: https://arxiv.org/pdf/2610.18067
published: '2026-10-12'
collected: '2026-10-14'
category: Training
direction: 长程 Agent 环境演化与信用分配训练
tags:
- Agent Training
- Environment Evolution
- Credit Assignment
- GRPO
- Verifier
- Long-Horizon
one_liner: 提出 WorkRover 框架，用递归环境演化与 Verifier 进度信用分配提升长程 cowork agent 训练，多个基准大幅超过基座
practical_value: '- 环境构建可借鉴 Harness 思路：在电商 Agent 任务平台里，把“上下文 / 任务 / 校验器”作为同一版本包管理，校验器必须绑定证据并接收
  valid alternatives；这样能减少“任务生成与评测脱节”导致的错误奖励。

  - FCR 的最小修复 + 组合回放适用于线上工作流配置变更：对 query 改写、推荐策略或工具配置做修改时，冻结原 intention / eval 规则，枚举少量组件修复组合，用固定种子回归验证，选最小可验证变更而非全量重生成，降低误伤。

  - VTCA 的 turn 级信用分配可直接迁移到长链路搜索 / 推荐 Agent：用确定性 workspace / 结果检查器计算每步可观测进度，不做中间 LLM
  Judge；通过工具输出或产物版本依赖决定哪些前置查询 / 读取步骤分享奖励，能缓解多跳检索、对比决策中的 sparse reward。

  - 训练数据 pipeline：SFT 用大模型生成轨迹 + 验证，RL 前先对 task-verifier 做一致性筛选，再保留少数高质量对，适合在电商业内部署低成本后训练。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：长程 cowork agent 的 RL 训练依赖大规模可执行环境，但自动合成的工作上下文、任务和验证器容易相互脱节；环境缺陷会让正确行为被判失败，而稀疏的 terminal reward 又无法指明哪些中间步骤真正有用。WorkRover 同时解决环境可靠性和 turn 级信用分配。

方法关键点：
- Harness-driven synthesis：联合构建 Work Context、Task、Verifier，Harness 追踪依赖，验证任务可行性；用 reference execution 证明可解，并用负样本和 valid alternatives 校准验证器。
- FCR：把 Context/Task/Harness/Verifier 的修复 proposal 冻结，枚举最多 16 个组合，按依赖闭包重建并用同策略 / 同预算 / 同种子回放；在契约和回归检查下选择改动最小的可验证修复。
- VTCA：用 frozen deterministic checker 对 workspace 状态做前后差分，正进度至少一半留在当前 turn，其余按 tool-output / artifact version 依赖分配给前置 turn，负进度不向前分摊；加权后加到 GRPO advantage 上。

关键结果：在 Qwen3.5-35B-A3B 上后训练，五个外部基准全部提升：JobBench +26.27pp，OfficeQA Pro +29.32pp，GDPval v2 +413.25 Elo；FCR 将自然缺陷安全修复率从 60.7% 提升到 70.3%，任务意图意外变化从 14.3% 降到 1.3%；VTCA 在所有基准上超过 episode-only GRPO。

最值得记住：长程 agent 训练要同时修环境和修奖励：环境修复用依赖闭包组合选择最小变更，奖励用可验证的 workspace 进度把 sparse terminal reward 转化为有依据的 turn 级信号。
