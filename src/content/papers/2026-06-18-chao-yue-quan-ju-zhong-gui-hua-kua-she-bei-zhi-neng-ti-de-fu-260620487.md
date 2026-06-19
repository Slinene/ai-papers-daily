---
title: 'Beyond Global Replanning: Hierarchical Recovery for Cross-Device Agent Systems'
title_zh: 超越全局重规划：跨设备智能体的分层恢复
authors:
- Shu Yao
- Yuhua Luo
- Qian Long
- Jingru Fan
- Zhuoyuan Yu
- Yuheng Wang
- Lin Wu
- Yufan Dang
- Huatao Li
- Chen Qian
affiliations:
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
- Southeast University
- Tsinghua University
arxiv_id: '2606.20487'
url: https://arxiv.org/abs/2606.20487
pdf_url: https://arxiv.org/pdf/2606.20487
published: '2026-06-18'
collected: '2026-06-19'
category: MultiAgent
direction: 多设备 Agent 分层恢复框架
tags:
- Hierarchical Recovery
- Cross-Device Agent
- Multi-Agent
- Fault Injection
- Replanning
- LLM Agent
one_liner: 提出 H-RePlan 分层重规划框架，分离设备局部策略恢复与全局重规划，结合 HeraBench 故障注入基准，大幅提升多设备 Agent
  任务完成鲁棒性并降低 token 消耗。
practical_value: '- **分层故障隔离与恢复**：在电商搜索/推荐系统的多服务 Agent 编排中，可借鉴设备本地策略恢复与全局重规划分离的思路，区分
  API 故障、参数错误等局部可修复错误与需要重新规划跨服务流程的全局错误，避免代价高昂的全量重试。

  - **多策略执行器设计**：为每个服务节点（如召回、排序、广告投放）定义可互换的执行策略（例如 API 调用、脚本回退、GUI 模拟），当一种方式失败时快速切换，提升局部自愈能力，增强整体系统的容错性。

  - **故障注入测试基准**：参考 HeraBench 构建方法，为推荐/搜索 Agent 工作流注入策略级（如服务超时、数据格式错误）和设备级（如节点宕机）故障，系统评估
  Agent 在动态异常下的成功率与指令遵循度，指导鲁棒性优化。

  - **紧凑跨层抽象通信**：在全局编排器与局部执行器之间使用结构化故障信号（如错误码、策略空间状态），减少 LLM 对话轮次和 token 消耗，可用于多 Agent
  协作的轻量级信息传递设计。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现实跨设备任务常因动态故障失败，但现有系统只用粗粒度恢复（重试、重新分配、改全局计划），无法区分设备内可修复故障与需跨设备重规划故障，导致效率低、成本高。

**方法**：提出 H-RePlan 分层重规划框架，为每个设备配备多种可交替执行策略（API/CLI/GUI），将恢复划分为两层：设备本地策略恢复（探索同一设备的不同策略）和编排器级全局重规划（通过紧凑跨层故障抽象触发）。同时构建 HeraBench 基准，在 Linux 与 Android 设备间构造跨设备工作流，并注入策略级和设备级故障。

**结果**：H-RePlan 在任务完成率、指令遵循度和完美通过率上显著超越单策略和粗粒度基线，并使可靠端到端成功的平均 token 消耗大幅降低，证明了范围感知的分层恢复对鲁棒跨设备 Agent 的必要性。
