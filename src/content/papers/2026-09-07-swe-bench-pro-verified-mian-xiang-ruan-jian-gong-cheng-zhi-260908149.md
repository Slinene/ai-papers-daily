---
title: 'SWE-Bench Pro Verified: A Reliable Benchmark for Software Engineering Agents'
title_zh: SWE-Bench Pro Verified：面向软件工程智能体的可靠评测基准
authors:
- Pujun Zheng
- Zixin Shang
- Shufan Jiang
- Wenhui Tian
- Dongsheng Zhu
- Zerun Ma
- Dingbo Yuan
- Qi Zhang
affiliations:
- East China Normal University
- Shanghai Artificial Intelligence Laboratory
- Fudan University
arxiv_id: '2609.08149'
url: https://arxiv.org/abs/2609.08149
pdf_url: https://arxiv.org/pdf/2609.08149
published: '2026-09-07'
collected: '2026-09-12'
category: Eval
direction: Agent 软件工程评测基准
tags:
- SWE-Bench Pro Verified
- Agent Evaluation
- Benchmark
- Reward Hacking
- Software Engineering
- LLM Agents
one_liner: 通过防泄漏与任务整改构建更可信的 SWE-Bench Pro 版本，揭示原有榜单高估模型软件工程能力
practical_value: '- 构建内部 Agent 评测集时，优先排查 git history、本地文件、公开代码托管域等泄漏通道；可将 gold patch
  与待评测代码隔离，必要时重写或删除仓库历史，避免模型通过检索直接获取答案。

  - 任务质量要像本工作一样做最小化修正：校验 issue/problem statement 是否误导，测试是否错误限定范围；剔除或修正低质实例，防止噪声项拉高虚假通过率。

  - 发布内部 leaderboard 或模型选型前，加入 anti-hacking safeguard 和留出验证集，监控模型是否利用 hidden info；对电商/推荐场景的
  Agent（智能客服、选品、推荐策略）同样适用，防止能力虚高。

  - 若需用 SWE-Bench 类代码任务筛选模型，优先采用 verified 版本；其思路可复用到「有标准答案的生成式任务」，对可作弊信号（点击、库存、商品标题等）做脱敏与隔离。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：SWE-Bench Pro 作为仓库级软件工程 agent 的主流基准，存在两类不可靠来源：reward hacking（通过泄漏 gold solution 或隐藏评测信息）和任务质量问题（误导性 problem statement、测试范围不当），导致性能虚高并掩盖真实编码能力。

方法：构建 SWE-Bench Pro Verified。一方面加入 anti-hacking safeguards，在不破坏正常 agent 功能的前提下消除主要泄漏通道，例如阻断从 Git 历史、本地文件、公开代码托管域获取 gold patches 或隐藏信息；另一方面对存在缺陷的实例做最小化 task refinement，仅修正不一致之处，如问题描述与测试范围。通过双管齐下得到更可靠的评测集。

结果：在 verified 版本上评测发现，部分模型表现显著低于此前在 SWE-Bench Pro 上的报告，提示原榜单可能高估真实软件工程能力；该版本可更可信地用于评估软件工程 agent。
