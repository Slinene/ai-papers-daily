---
title: 'EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments'
title_zh: 'EvoArena: 追踪记忆演化以提升动态环境中的 LLM 代理鲁棒性'
authors:
- Jundong Xu
- Qingchuan Li
- Jiaying Wu
- Yihuai Lan
- Shuyue Stella Li
- Huichi Zhou
- Bowen Jiang
- Lei Wang
- Jun Wang
- Anh Tuan Luu
affiliations:
- National University of Singapore
- Singapore Management University
- University of Washington
- University College London
- University of Pennsylvania
arxiv_id: '2606.13681'
url: https://arxiv.org/abs/2606.13681
pdf_url: https://arxiv.org/pdf/2606.13681
published: '2026-06-10'
collected: '2026-06-12'
category: Agent
direction: LLM Agent 鲁棒性 · 环境演化与记忆进化
tags:
- LLM Agent
- Dynamic Environment
- Memory Evolution
- Patch-based Memory
- Benchmark
one_liner: 提出动态环境评测套件 EvoArena 和补丁式记忆机制 EvoMem，通过记录记忆变化轨迹让代理在持续演化的任务中更鲁棒。
practical_value: '- **记忆演化追踪**：将记忆更新记录为“补丁”，保留变更前后状态、原因和证据。电商推荐中用户偏好随时间变化，可记录每次偏好更新及触发上下文，用于更精准的长期用户建模。

  - **链式任务评估**：EvoArena 的链式准确率评估方法要求连续子任务全对才算成功，可借鉴到 Agent 流水线评测，衡量系统在持续变化环境下的端到端可靠性，而非仅看单步指标。

  - **版本化状态管理**：当系统规则或模型更新时，保留旧版本知识，避免新信息完全覆盖旧信息。在推荐策略迭代或 A/B 测试时，可回溯历史版本行为，支持更稳健的上线决策。

  - **补丁检索推理**：查询时检索相关历史变更，而不仅用最新记忆，可用于处理时间敏感或条件依赖的任务。例如根据当前上下文检索用户过去的偏好变化轨迹，辅助动态意图识别。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现有 LLM Agent 评测大多假设静态环境，但真实部署中接口、规则、代码和用户偏好会持续变化。Agent 需要知道哪些变了、哪些仍然有效，才能在不同版本下可靠行动。

**方法关键点**：
- **EvoArena 评测套件**：将终端工作流、软件工程、社交对话三个领域构造为**渐进演化版本链**，要求 Agent 在保持目标不变但环境约束变化的连续任务中解决问题。包含 Terminal-Bench-Evo（命令行工作流演化）、SWE-Chain-Evo（代码库里程碑演化）和 PersonaMem-Evo（用户偏好演化）。
- **EvoMem 记忆机制**：一种轻量级 git-like 的补丁记录方法。当记忆发生非增量式更新（如覆盖旧规则）时，生成包含前后状态、更新理由、触发证据的补丁，存入追加式历史。推理时从最新记忆和相关的历史补丁中检索，使 Agent 能基于环境演化轨迹做决策。
- **实现**：EvoMem 作为通用抽象层，无缝接入 Terminus2、OpenHands、A-Mem 等不同 Agent 记忆系统，仅监控记忆变更并补充补丁检索。

**关键实验结果**：
- 现有强大 Agent 在 EvoArena 上平均步级准确率仅 39.6%，链级准确率更低，说明环境演化带来明显退化。
- EvoMem 在 EvoArena 上平均提升 1.5% 步级准确率和 3.7% 链级准确率，在 GAIA 和 LoCoMo 标准基准上分别提升 6.1% 和 4.8%。
- 机制分析表明，当 Agent 真正利用检索到的补丁信息并体现在行动中时，增益更大，说明**操作化记忆演化轨迹是提升鲁棒性的关键**。
