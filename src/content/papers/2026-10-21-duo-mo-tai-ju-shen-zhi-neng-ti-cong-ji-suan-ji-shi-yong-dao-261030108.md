---
title: 'Multimodal Embodied Agents: A Unified Capability-centric Perspective from
  Computer-Use to Robot-Use'
title_zh: 多模态具身智能体：从计算机使用到机器人使用的统一能力中心视角
authors:
- Yanzhe Chen
- Ziyi Yang
- Jifeng Zhu
- Qiming Huang
- Ruihe An
- Peiyao Xu
- Hesen Yang
- Runda Liu
- Chang Gong
- Zhijun Cao
affiliations:
- Show Lab, National University of Singapore
arxiv_id: '2610.30108'
url: https://arxiv.org/abs/2610.30108
pdf_url: https://arxiv.org/pdf/2610.30108
published: '2026-10-21'
collected: '2026-10-25'
category: Agent
direction: 多模态具身 Agent 能力框架与评测
tags:
- Multimodal Agents
- Embodied AI
- Capability Framework
- Evaluation
- Robot Learning
one_liner: 提出 PAPAV 五功能框架，统一比较计算机使用与机器人智能体，揭示 Anticipate 与 Verify 评测缺失
practical_value: '- 将推荐/搜索 Agent 按 Perceive、Anticipate、Plan、Act、Verify 拆解能力项，分别建立评估指标，而不是只看最终转化或任务成功，便于定位失败环节。

  - 在生成式推荐或 query 改写中，显式引入“动作影响预判”和“结果校验”模块：生成候选前先做效果预估与风险检查，生成后主动验证用户反馈，弥补现有链路只优化
  Act 的不足。

  - 对自动操作类 Agent（如电商后台自动化、广告账户操作），可借鉴其按功能而非架构的评测思路，设计分能力测试集，尤其覆盖不可逆动作前的 Anticipate
  与执行后的 Verify。

  - 整体为框架综述，无具体算法可迁移；核心价值在评估维度与系统解耦思路，可作为 Agent 评测设计参考。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：多模态智能体（MMAs）多用于计算机操作，机器人系统（RSs）受物理动态约束耦合感知与执行；论文将它们统一为多模态具身智能体（MMEAs），即耦合多模态任务推理与物理动作、根据反馈修正决策的目标导向系统，并追问从 computer-use 到 robot-use 的关键变化。

**方法关键点**：提出 PAPAV 框架，以五个功能——Perceive（感知当前状态）、Anticipate（预判动作效果）、Plan（规划可行路径）、Act（通过接口或身体执行）、Verify（验证结果）——统一描述三类系统；强调按功能而非架构比较。分析五个物理约束（部分可观测、动作不可逆、结果不可验证等）对设计的影响。

**关键结果**：跨 64 个基准分析显示，显式评估高度集中在 Act；只有 5 个基准评估 Anticipate，3 个评估 Verify，这两个能力往往被任务成功率掩盖。论文据此指出开放挑战，主张以全能力维度而非仅任务成功衡量进展。
