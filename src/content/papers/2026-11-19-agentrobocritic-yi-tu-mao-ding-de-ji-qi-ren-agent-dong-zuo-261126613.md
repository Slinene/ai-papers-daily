---
title: 'AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct
  Robot Control'
title_zh: AgentRoboCritic：意图锚定的机器人 Agent 动作级评估
authors:
- Yiyang Du
- Yuxuan Kuang
- Qitao Zhao
- Yixuan Wang
- Zhanqiu Guo
- Yi Xu
- Xin Li
- Wenbin He
- Liu Ren
- Chenyan Xiong
affiliations:
- Carnegie Mellon University
- University of Illinois at Urbana-Champaign
- Bosch Research North America & Bosch Center for Artificial Intelligence (BCAI)
arxiv_id: '2611.26613'
url: https://arxiv.org/abs/2611.26613
pdf_url: https://arxiv.org/pdf/2611.26613
published: '2026-11-19'
collected: '2026-11-21'
category: Eval
direction: 具身 Agent 动作级评估与失败模式分析
tags:
- Agent Evaluation
- Action Critique
- Failure Mode
- Multimodal Agent
- Robot Control
- Intent Grounding
one_liner: 提出 intent-grounded 批评框架，对 frontier agent 的机器人直接控制做动作级失败模式分析，并微调开源 critic
  提升评估精度
practical_value: '- 在推荐/搜索 Agent 链路中，为每个决策步骤（query 改写、召回策略选择、精排干预等）强制输出 local intent，再用
  critic 对照 intent 做动作级评估，替代只看最终转化/点击的粗粒度评价，快速定位失效环节。

  - 构建业务专属的失败模式分类（如召回不足、意图误解、排序偏差、拒答不当），用 frontier LLM 先标注少量样本，再蒸馏微调开源小模型做 critic；论文中
  accuracy 从 32.58% 到 74.24%，说明该路径可低成本获得可用评估器。

  - 借鉴闭环恢复分析：对 Agent 的局部执行失败（如 API 调用出错、用户负反馈）设计重试与降级策略，并通过 critic 区分可恢复/不可恢复模式，避免无限重试或错误回退。

  - 动作级标注数据集与 critic 可作为 reward model 或 RLHF 的辅助信号，在线上 Agent 策略迭代中提供细粒度 reward shaping。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：Frontier multimodal language agents 已能直接输出低层数值动作控制机器人，但现有 benchmark 只报 episode-level 成功率，无法解释成功路径或失败根因。需要动作级分析来揭示能力边界。

**方法关键点**：引入 AgentRoboCritic，一个意图锚定的批评框架：策略 agent 在每个动作旁声明 local intent，critic 对照该 intent 评估动作结果与失败模式。在 12 个 manipulation benchmarks 上对 frontier agents 做系统动作级分析；人工标注 400 个动作验证 critic，并发布 12,844 个动作标注数据集，微调开源 critic Muse-Glimmer-30B。

**关键结果**：动作级分析显示 frontier agents 具备闭环恢复局部执行失败、跨场景可靠语义 grounding、以及无任务适配的 zero-shot manipulation 能力；局限包括 grasping/alignment 等物理执行瓶颈和失败模式恢复不均衡。微调后 critic 的 failure-mode accuracy 从 32.58% 提升至 74.24%，大幅降低动作级分析成本。
