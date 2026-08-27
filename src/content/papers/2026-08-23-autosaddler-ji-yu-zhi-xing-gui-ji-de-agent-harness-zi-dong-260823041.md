---
title: 'AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent
  Execution Traces'
title_zh: AutoSaddler：基于执行轨迹的 Agent Harness 自动优化框架
authors:
- Sungho Park
- Wonjoong Kim
- Rongyuan Tan
- Jue Zhang
- Wook-Shin Han
- Pengfei Gao
- Chanyoung Park
- Yongqiang Yao
- Rao Fu
- Elsie Nallipogu
affiliations:
- POSTECH
- KAIST
- Southern University of Science and Technology
- Microsoft
arxiv_id: '2608.23041'
url: https://arxiv.org/abs/2608.23041
pdf_url: https://arxiv.org/pdf/2608.23041
published: '2026-08-23'
collected: '2026-08-27'
category: Agent
direction: Agent Harness 自动优化 · 离线学习
tags:
- Agent Harness Optimization
- Failure Diagnosis
- Prompt-Tool-Middleware Patching
- EvoDAG
- Generalization-Aware Selection
one_liner: 将 Agent Harness 优化形式化为离线学习，通过深度诊断、结构化 Patch 与泛化感知选择，在三个基准上提升 9-10 个百分点
practical_value: '- 把 agent 的 system prompt、工具描述、中间件逻辑统一视为可优化代码，建立 mini-batch 离线优化流程：用失败轨迹批量诊断并生成
  patch，在同一批上验证提升，再上验证集评估，避免只在单条轨迹上打补丁。

  - 采纳结构化 patch 分类（Prompt/Tool/Middleware）并分阶段调度：先允许修改工具实现和 agent loop 等能力层，后期转向提示词/hook
  文本；这样能迫使优化过程探索高价值能力改动，而不是只做表面 prompt 文本微调。

  - 保留 harness 演化图（EvoDAG）作为优化记忆，允许进化代理重组历史成功组件，而非只从最新版本继续；在多轮迭代优化推荐/导购 Agent 的 prompt
  与工具配置时，可跳出局部最优。

  - 评估 patch 时同时监测 fix rate 与 regression rate，尤其对高频工具或 hook 的修改要防止 over-scoped patch
  引入回归；用独立验证集过滤泛化差的更新，能显著减少线上事故。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
LLM agent 在长程任务上仍不可靠，局部失败会在多步交互中累积。外部 harness（prompt、工具配置、运行时控制逻辑）能显著提升鲁棒性，但手工设计成本高、搜索空间大、评估昂贵。自动优化 harness 成为关键需求。

**方法关键点**  
- 将 harness 优化形式化为离线学习，用 mini-batch 失败信号迭代更新。
- 三个核心组件：1) 诊断-修补会话：深度分析失败轨迹与 harness 代码，生成结构化 patch（Prompt/Tool/Middleware），分 capability/steering 两类，阶段调度先能力后引导；2) 反思会话：比较 patch 前后轨迹，归纳 fixed/regressed/still-failing/still-passing，提取教训；3) 进化会话：用 EvoDAG 记录 harness 演化历史，支持重组历史组件，避免局部最优。
- 泛化感知选择：mini-batch 提升后须在 dev set 上验证，只保留泛化的 patch。

**关键实验与结果**  
- 基准：GAIA2、SWE-Bench Pro、Terminal-Bench 2.0；对比手工 base harness 与自动基线 GEPA、Meta-Harness。
- 性能：AutoSaddler 分别提升 9.0 pp（53.0→62.0）、9.6 pp（37.3→46.9）、10.0 pp（40.0→50.0），均超过最强自动基线 7.4/4.4/6.7 pp。
- 效率：GAIA2 开发集达到 72.3% 仅需约 1k 次执行，基线在约 2.8k 次后饱和于 64.6%/61.5%；按学习轨迹数，AutoSaddler 仅用 147 条轨迹达到最佳，比 Meta-Harness 少约 10 倍。
- 消融：去掉深度诊断、结构化干预、泛化感知选择，性能分别降到 57.8/56.9/50.6，证明三者缺一不可；泛化感知选择贡献最大（-11.4 pp），其核心是降低回归率而非提高 fix rate。
- 定性：结构化干预使 capability patch 占比从 4% 升至 25% 以上，接受率更高；泛化感知选择阻止过于宽泛的高频工具 hook 导致的大范围回归。

**最值得记住的一句话**：自动 harness 优化的关键是深度诊断、结构化干预、泛化感知选择；其中显式用验证集过滤 overly broad patch、监控 regression rate 是避免过拟合、实现持久提升的核心。
