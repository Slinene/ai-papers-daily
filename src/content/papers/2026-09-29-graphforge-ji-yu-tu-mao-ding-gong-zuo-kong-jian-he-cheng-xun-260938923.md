---
title: 'GraphForge: Training Working Agents with Graph-Anchored Workspace Synthesis'
title_zh: GraphForge：基于图锚定工作空间合成训练工作智能体
authors:
- Qisheng Su
- Hanchen Wang
- Guanru Zhu
- Huicheng Jiang
- Qiuyinzhe Zhang
- Kou Shi
- Zhen Fang
- Ziao Zhang
- Qingnan Ren
- Zehui Chen
affiliations:
- University of Science and Technology of China
- Fudan University
- Shanghai Innovation Institute
- Shanghai AI Laboratory
arxiv_id: '2609.38923'
url: https://arxiv.org/abs/2609.38923
pdf_url: https://arxiv.org/pdf/2609.38923
published: '2026-09-29'
collected: '2026-10-02'
category: Training
direction: Agent 工作智能体训练数据合成
tags:
- GraphForge
- Working Agents
- Data Synthesis
- Evidence Graph
- Fine-tuning
- Rubric
one_liner: 用证据图从真实文件合成可验证的工作智能体训练数据，微调后多项基准显著提升
practical_value: '- 可用真实业务文件（商品目录、投放报表、用户日志）构建工作区，并用证据图显式编码文件间关系，确保多步任务每个要求都能追溯到具体支撑文件，避免模型编造数据，适合生成电商运营、广告投放、搜索优化等
  Agent 训练集。

  - 任务 rubric 与原始文件/单元格锚定，使奖励信号或拒绝采样筛样具备可审计性，降低 reward hacking 和评估噪声，可迁移到 RLHF/DPO
  等 Agent 优化流程。

  - SFT 后增加 rejection fine-tuning：用自身 rollout 并通过 rubric 筛选高质量候选，无需新增人工标注即可进一步提升 Agent
  效果，适合业务 Agent 的快速迭代。

  - 初始 rollout 可执行性检查 + revision agent 修复不可行任务，能自动清洗可能失败/不可完成的训练样本，降低坏样本对模型的影响。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：工作智能体需要读多文件、调用工具并产出交付物，其训练依赖真实文件上的可验证任务，但现有合成数据 pipeline 要么由模型生成文件导致失真，要么基于真实文件却缺少任务专属 verifier，难以保证结果质量。

**方法关键点**：GraphForge 从职业锚定种子出发控制多样性，为每个种子组装真实文件工作区，并构建证据图编码文件间关系。任务陈述和评估 rubrics 都从证据图派生，使每条任务要求有工作区文件支撑，每个 rubric 锚定验证所需的具体文件。初始 rollout 测试可执行性，revision agent 在采集轨迹前基于原始文件修复任务与 rubric。后续用 2,169 条 GraphForge 轨迹微调 Qwen3.6-27B，并在自身 rollout 上用证据锚定 rubrics 筛选候选做 rejection fine-tuning。

**关键结果**：仅 SFT 即把 GDPVal 提升 65.7 至 1445.7（OpenHands），Workspace-Bench-Lite 提升 7.7 至 63.7，SpreadsheetBench II 提升 13.7 至 24.0（Claude Code）。加入 rejection fine-tuning 后三项基准进一步改善，表明证据锚定 rubrics 提供有效的选择信号。
