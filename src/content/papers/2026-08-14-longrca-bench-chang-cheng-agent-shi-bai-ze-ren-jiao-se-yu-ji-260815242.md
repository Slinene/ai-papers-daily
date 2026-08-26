---
title: 'LongRCA Bench: Diagnosing Responsible Roles and Root Causes in Long-Horizon
  Agent Failures'
title_zh: LongRCA Bench：长程 Agent 失败责任角色与根因诊断基准
authors:
- Yunfei Zhang
- Boyu Feng
- Changhua Pei
- Zexin Wang
- Zhihuang Peng
- Xinlong Liu
- Hengyue Jiang
- Difeng Ma
- Jiayi Zhang
- Yongzhou Yao
affiliations:
- Computer Network Information Center, Chinese Academy of Sciences
- Hangzhou Institute for Advanced Study, University of Chinese Academy of Sciences
- Chongqing University
- Institute of Computing Technology, Chinese Academy of Sciences
- Singapore Management University
arxiv_id: '2608.15242'
url: https://arxiv.org/abs/2608.15242
pdf_url: https://arxiv.org/pdf/2608.15242
published: '2026-08-14'
collected: '2026-08-26'
category: Agent
direction: Agent 长轨迹故障根因定位
tags:
- Long-horizon agent
- failure attribution
- root-cause localization
- benchmark
- training-free
one_liner: 提出 LongRCA Bench 与训练无关的 RCTA 方法，将长轨迹 Agent 失败归因提升至 24.1% 精确根因步准确率
practical_value: '- 可直接复用 RCTA 的两阶段归因流程：对电商导购、多步推荐、客服自动化等长轨迹 Agent，先按 segment 做摘要并检索可疑步骤，再回溯上游
  handoff/指令做依赖定位；无需训练，便于在现有 LLM backbone 上快速部署。

  - 故障归因评估应拆分 responsible-role accuracy 与 exact root-step accuracy：业务中先定位出错的角色/环节（如召回、排序、工具调用、策略手写）往往比直接定位具体步骤更易落地，也适合做监控告警和归因看板。

  - 参考 LongRCA Bench 的构建方式：收集真实失败轨迹、避免注入错误、对最早决定性根因步骤做独立人工标注，可沉淀为自己的长会话 Agent bad
  case 离线回归库。

  - 注意连最强基线也仅 13.2% 精确根因步准确率，说明长轨迹精确定位很难；不要依赖 LLM 一次性全轨迹归因，优先用分段摘要+依赖回溯缩小范围后再核验。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：长程 Agent 执行失败时，只看最终结果无法知道错误在哪一步进入轨迹、由哪个角色负责；现有失败归因基准多聚焦短轨迹，难以覆盖数百步的真实执行。

**方法关键点**：构建 LongRCA Bench，含 5 个领域、1,140 条失败轨迹，无注入错误，提供独立人工标注的 responsible role 和 earliest decisive root-cause step；中位轨迹长度 145 步。提出 RCTA（Root-Cause Trajectory Attribution），训练无关：先按 segment 生成摘要并检索候选错误步骤，再回溯上游 handoff/指令。

**关键结果**：最强基线仅有 13.2% exact root-step accuracy；RCTA 在相同 backbone、基准和评分协议下达到 51.1% responsible-role accuracy、24.1% exact root-step accuracy。结果表明应将角色归因和精确根因步定位作为长轨迹故障诊断的两个独立评估目标。
