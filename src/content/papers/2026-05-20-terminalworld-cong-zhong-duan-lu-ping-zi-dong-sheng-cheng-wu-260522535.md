---
title: 'TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks'
title_zh: TerminalWorld：从终端录屏自动生成真实任务评估基准
authors:
- Zhaoyang Chu
- Jiarui Hu
- Xingyu Jiang
- Pengyu Zou
- Han Li
- Chao Peng
- Peter O'Hearn
- Earl T. Barr
- Mark Harman
- Federica Sarro
affiliations:
- University College London
- Nanjing University
- Tencent
arxiv_id: '2605.22535'
url: https://arxiv.org/abs/2605.22535
pdf_url: https://arxiv.org/pdf/2605.22535
published: '2026-05-20'
collected: '2026-05-23'
category: Eval
direction: 面向终端 Agent 的可扩展评估基准
tags:
- Terminal
- Agent
- Benchmark
- Data Engine
- Real-World Evaluation
one_liner: 通过逆向工程 8 万终端录屏，构建可扩展的真实终端任务基准，揭示现有 Agent 最高仅 62.5% 通过率。
practical_value: '- **从真实录屏构建评估数据引擎的范式可复用**：在电商场景中（如 CLS 日志、运维操作记录、推荐流程重放），可逆向生成高保真的
  Agent 评估任务，避免人工设计的主观性和偏差。

  - **多步工作流评估揭示真实能力短板**：基准包含超 50 步的任务，类似电商订单处理、多系统查询的复杂流程，可用于测试 Agent 在长程依赖、错误恢复上的表现。

  - **弱相关验证现有基准的局限**：与 Terminal-Bench 仅 0.20 相关性提示自建基准可能更贴近线上真实分布，在评估生成式推荐或 Agent
  时，应考虑从生产数据采样而非完全依赖通用榜单。

  - **自动化质量保证思路**：采用环境重建、输出校验与人工验证的混合流程，可借鉴到推荐系统的离线回测范式，提升对生成结果的可靠性评估。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有终端 Agent 基准多由专家手动设计，容易偏向人为制造的高难度任务，难以反映真实世界工作流的分布与难度，缺乏可扩展的评估方案。

**方法**：提出 Termworld，一个可扩展的数据引擎，自动从“野生”终端录屏中逆向生成高保真评估任务。处理 80,870 条录屏后，得到 1,530 个通过自动验证的任务，覆盖 18 类真实场景、1,280 个不同命令，任务步数从日常短操作到 50 步以上的复杂工作流。从中精选 200 个经人工复核的代表性任务构成 Verified 子集。在 Verified 上对 8 个前沿模型（含 SWE-agent、OpenHands 等）和 6 种 Agent 框架全面评测。

**关键结果**：当前最强系统最高通过率仅 62.5%，暴露出在真实终端工作流中的可靠性缺陷；该基准与现有专家设计的 Terminal-Bench 分数仅弱相关（Pearson r = 0.20），说明其捕捉到了不同的真实能力维度。数据与代码已开源。
