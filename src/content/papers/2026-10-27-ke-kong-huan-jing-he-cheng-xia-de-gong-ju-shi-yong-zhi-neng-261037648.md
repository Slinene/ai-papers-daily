---
title: Scaling Laws for Tool-Use Agents via Controllable Environment Synthesis
title_zh: 可控环境合成下的工具使用智能体扩展律
authors:
- Andrew Szot
- Samira Abnar
- Omar Attia
- Abbas Kazerouni
- Michael Kirchhof
- Cheng-Yu Hsieh
- Raviteja Vemulapalli
- Alexander Toshev
affiliations:
- Apple
arxiv_id: '2610.37648'
url: https://arxiv.org/abs/2610.37648
pdf_url: https://arxiv.org/pdf/2610.37648
published: '2026-10-27'
collected: '2026-10-28'
category: Agent
direction: 可控环境合成与工具使用 Agent 扩展律
tags:
- Synthetic Environments
- Tool-Use Agents
- Scaling Laws
- Data Composition
- Supervised Fine-Tuning
- LLM Agents
one_liner: 提出 SynthAPI 可控合成工具环境，发现工具与数据库多样性比任务数量更关键，并推导可预测扩展律
practical_value: '- **构建电商/推荐 Agent 训练集时，优先扩展工具与数据库状态多样性，而非单纯堆任务数量**：当数据预算大于约 4k 任务时，增加
  app/工具数（A）、每个任务的初始数据库实例数（S）、以及干扰数据深度（D）比新增任务 prompt（T）更有效；在商品搜索、下单、售后等多步工具场景可直接复用此结论。

  - **用可执行环境合成代替 LLM 模拟 API 响应**：SynthAPI 生成 Python db schema + API + verifier + oracle
  solver，所有轨迹可执行、可验证，避免模拟复杂状态转换出错；适合电商/推荐中涉及库存、价格、用户画像等有状态变更的场景。

  - **采用 meta-tools 按需加载工具接口**：agent 通过 list_apps/list_tools/get_tool_documentation
  动态发现工具，降低上下文开销并提升对新工具集的泛化；搜索推荐 Agent 可设计类似工具发现层，按需检索可用商品/内容 API。

  - **用 scaling law 指导数据预算分配**：拟合 P(A,T,S,D) 形式的性能预测模型，可在小规模 grid search 后外推到大算力预算，避免盲目生成数据；团队可在自有合成
  pipeline 上复现此方法。'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
多步工具使用 Agent 的训练依赖高质量、多样化的交互数据，但现有合成方法主要关注数据量，未系统分析工具、任务、数据库状态三者的组成如何影响下游泛化。

### 方法关键点
- **SynthAPI pipeline**：LLM 先生成 app（db.py 数据类 + apis.py API 函数），再生成任务指令、verifier、oracle solver、初始数据库状态与干扰数据；所有任务可执行且带验证器。
- **四个控制轴**：A（应用数/工具多样性）、T（每应用任务数/指令多样性）、S（每任务指令的数据库实例数/数据画像多样性）、D（每数据库状态的干扰数据批次深度）。
- **训练协议**：用 GLM-5.2 专家收集成功轨迹，SFT 蒸馏到 Qwen3.5 系列；共生成 458,752 个任务，训练 849 个模型。
- **扩展律**：提出
  `P(A,T,S,D) = σ(c0 + cA log2(A·S·D)) · σ(b0 + bT log2 T)^ν`，
  将性能上界与工具/数据库多样性绑定，任务数控制收敛速度。

### 关键实验与结果
- 在 AppWorld、BFCLv3 Multi-Turn、ASTRA-Bench、SynthAPI-Holdout 上评估。
- 数据组成 scaling law 在 top 25% FLOPs 外推集上 MAE 0.0285，而只按任务数量的 scaling 模型 MAE 0.1706。
- 固定预算下，SynthAPI-Opt（A=64,T=128,S=4,D=4）一致优于 SubOpt（A=32,T=1024,S=1,D=2）。
- SynthAPI-Big 平均超过 Nemotron-Agentic 30.5 个百分点；AppWorld Test-C 上 4B 达 66.4（vs SimSAT 58.8），9B 达 77.0（vs 65.4）；BFCL 上比最强 baseline 高 2.0–3.7 点。

**最值得记住的一句话**：在工具使用 Agent 的训练数据扩展中，工具和数据库状态的多样性比任务数量更重要，且最优数据组成随算力预算动态变化。
