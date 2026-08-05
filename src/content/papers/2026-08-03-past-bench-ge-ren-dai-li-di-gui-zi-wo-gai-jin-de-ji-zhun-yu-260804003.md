---
title: 'PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in
  Personal Agents'
title_zh: PAST-Bench：个人代理递归自我改进的基准与诊断
authors:
- Shuhan Xue
- Zixin Ding
- Yichen Shen
- Yinjie Wang
- Zhenfei Yin
- Yingcheng Wu
- Yuxin Chen
- Mengdi Wang
- Ling Yang
arxiv_id: '2608.04003'
url: https://arxiv.org/abs/2608.04003
pdf_url: https://arxiv.org/pdf/2608.04003
published: '2026-08-03'
collected: '2026-08-05'
category: Agent
direction: 个人代理递归自我改进评估与诊断
tags:
- benchmark
- agent
- recursive self-improvement
- diagnostic
- memory
- personalization
one_liner: 构建受控实验揭示代理改进并非必然源于正确的经验路径，并设计 Hermes+ 强化 save-retrieve-update 机制
practical_value: '- 评估个性化推荐 Agent 的长期效果时，可借鉴 PAST-Bench 的控制变量设计：对比开启与关闭记忆时的任务增益，并诊断增益是否来自预期的
  save-retrieve-update 路径，避免被模型原生能力或统计偏倚误导。

  - 推荐系统的用户状态管理可借鉴 Hermes+ 的五项干预：如遗忘机制处理过期偏好、时序感知检索捕捉兴趣漂移、优先级队列管理记忆容量，防止陈旧信息干扰。

  - 在构建持续学习的 Agent 时，应重点应对“条件变化”场景（如用户偏好转换），主动替换而非累积过时状态；PAST-Bench 的更新维度测试可移植用于验证此类机制。

  - 如需分析 Agent 框架对经验复用的贡献，可分离基座模型与框架的影响，PAST-Bench 提供跨模型和框架的衡量方式，帮助定位架构瓶颈。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：个人 AI 代理能否将累积经验转化为持续行为改进，缺乏系统性诊断。现有评估多聚焦单会话表现，忽略代理是否真正通过记忆与技能复用实现递归自我进步。PAST-Bench 旨在其补这一空白。

**方法关键点**：设计受控任务序列（26 场景、204 剧集），在同一任务家族下开启/关闭经验保留，对比后期任务增益。围绕记忆、过程复用、信息收集、更新四大能力，不仅测量增益幅度，更诊断增益是否遵循保存→检索→更新的预期路径，排除混淆因素（如模型原生能力）。在 7 个基座模型、4 个代理框架上测试，揭示改进真实但能力间不均衡，且同增益幅度下路径证据差异显著。基于此提出 Hermes+，在代理循环各阶段插入五项干预（优先级记忆、时序感知检索、过期状态替换等）。

**关键结果**：Hermes+ 平均增益提升约 12%，更新类任务增益提升约 20%，路径证据更清晰，但效果仍依赖于底座模型与能力类型。PAST-Bench 与 Hermes+ 为持久化代理从体验中系统性改进提供了可诊断的评估基础。
