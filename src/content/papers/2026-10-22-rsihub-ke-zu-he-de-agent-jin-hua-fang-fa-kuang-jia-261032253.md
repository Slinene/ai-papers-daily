---
title: 'RSIHub: A Composable Framework for Agent-Evolution Methods'
title_zh: RSIHub：可组合的 Agent 进化方法框架
authors:
- Zimu Wang
- Xiaobo Wang
- Siyu Ye
- Jiaqi Li
- Silin Chen
- Yuling Shi
- Ruobing Wang
- Jingjing Zhang
- Chaofan Wang
- Kai Wu
affiliations:
- University of California, Berkeley
- University of Science and Technology of China
- Douyin Group
- Shanghai Jiao Tong University
- Beijing Institute for General Artificial Intelligence
arxiv_id: '2610.32253'
url: https://arxiv.org/abs/2610.32253
pdf_url: https://arxiv.org/pdf/2610.32253
published: '2026-10-22'
collected: '2026-10-26'
category: Agent
direction: Agent 进化框架与实验治理
tags:
- Agent Evolution
- Evaluation
- Provenance
- Self-Improvement
- LLM Agents
- Framework
one_liner: 开源框架将 Agent 进化策略与执行评估解耦，支持公平对比、溯源与受保护评测
practical_value: '- 在电商/广告 Agent 迭代中，把「策略改动面」和「评估面」分开：对 prompt、工具、编排做自动进化时，将评测器、数据切分、认证记录放在框架侧，禁止
  mutate 触碰评估配置；这能避免上线 Agent 优化时因评测漂移导致错误归因。

  - 借鉴 train/gate/sealed 三分法：用 train 产生反馈、gate 做准入、sealed 做 held-out 报告。搜索推荐场景中，可对应历史反馈窗口、回放准入窗口、未来线上
  sealed 时段；防止对历史日志过拟合，暴露 query 改写/文案生成的泛化问题。

  - 建立轻量 provenance/lineage：每个候选版本绑定 commit、recipe snapshot、模型版本、数据集指纹、split 与得分，便于回溯和审计；框架独占开销
  <0.02% 生成时间，可集成进现有 MLOps。

  - 复用 recipe+operator 组合模式：把进化策略写为算子，用配置声明 mutable surface，能让 A/B 对比不同 prompt/策略搜索算法时少写端到端实验代码，团队可快速替换单个策略组件。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
Agent 进化方法通过执行反馈改进 prompt、技能、工具与编排，但各方法重复建设相同实验设施，且评估/记录常和策略耦合，导致改进归因困难、跨方法比较不可靠。需要统一框架把「进化策略」与「执行、评估、溯源」解耦。

## 方法关键点
- Recipe 抽象：用配置文件绑定生命周期五个必需算子（Select、Rollout、Mutate、Gate、Record）和可选算子（Analyze、Validate、Novelty、Reflect），并声明 mutable surface；AHE、Hyperagents、A-Evolve、GEPA 均以 recipe 表达，不改框架核心。
- Protected runtime：框架拥有 eval、archive 与 certified fields；mutate 只能改声明的目标资源；实验数据固定为 train/gate/sealed 三部分，sealed 不参与反馈。
- 候选生命周期：每代从 archive 选 parent、rollout 收集证据、mutate 提变更、guardrail 校验 diff、gate 评估、absorb 决定是否入 archive；支持中断恢复与 lineage。
- Agent-driven 模式：外层 agent 可在迭代间改写 recipe 算子绑定，但评测器、sealed split、认证记录仍受框架保护。

## 关键结果
- Terminal Bench 2 上 MiniSWE 基线 56.2%，Hyperagents/A-Evolve 到 69.7%（+13.5pp）；Codex 基线 69.7%，AHE 到 71.9%（+2.2pp）。
- τ3 Banking 上 Codex 基线 24.7%，AHE 到 34.0%（+9.3pp）；但 MiniSWE 的 Hyperagents 总体 +5.2pp 同时 sealed 掉 2.1pp，说明总体提升可能掩盖 held-out 损失。
- 方法排名随 agent、benchmark、split 变化；不同方法无一致赢家。
- 执行保真：framework 直接执行与无框架执行差异约在 −2.6~+3.4pp，任务级 excess disagreement 0.2~6.0pp。
- 完整性：420/420 故障注入与边界试验通过；框架独占耗时中位数约 0.02% 生成时间；四方法集成仅 47–61 行 recipe 配置、0 框架源码改动。

## 最值得记住
「更高的 overall pass@1 可能掩盖 sealed/held-out 回归；把 train/gate/sealed 拆分和 provenance 作为一等公民。」
