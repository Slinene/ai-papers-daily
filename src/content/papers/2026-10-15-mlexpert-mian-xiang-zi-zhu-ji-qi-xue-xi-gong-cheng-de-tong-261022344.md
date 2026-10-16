---
title: 'MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning
  Engineering'
title_zh: MLExpert：面向自主机器学习工程的通用智能体模型
authors:
- Shangheng Du
- Jinxin Shi
- Shuaiyu Zhang
- Yiming Wu
- Junpeng Zhao
- Shiyang Feng
- Xin Li
- Liang He
- Xiangchao Yan
- Bo Zhang
affiliations:
- East China Normal University
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2610.22344'
url: https://arxiv.org/abs/2610.22344
pdf_url: https://arxiv.org/pdf/2610.22344
published: '2026-10-15'
collected: '2026-10-16'
category: Agent
direction: Agent 后训练 · 长程 MLE 优化
tags:
- Agentic Model
- Post-training
- RLHF
- Long-horizon
- WIRL
- MLE
one_liner: 用层级SFT与执行窗口交互强化学习训练35B MoE，将MLE奖牌率从37.9%提至72.7%
practical_value: '- **执行窗口共享奖励**：面向需要多轮执行反馈的推荐/搜索 Agent（如自动调参、A/B 实验优化、query 改写迭代），把相邻两次实验结果之间的多步决策作为一个
  execution window，共用结果奖励，避免稀疏轨迹奖励导致的学习困难；局部性能趋势项可鼓励持续改进而非只追求终局最优。

  - **异步收集 + token 级策略修正**：在线 RL 中 rollout 策略与当前训练策略不一致是常态，WIRL 的 token-level policy
  correction（用记录 log-prob 计算比值并截断）可直接迁移到电商/搜索 Agent 的在线训练，降低等待开销。

  - **Outcome-guided 监督选择**：从长轨迹中提取“首次最优提交”之前的有效探索与失败恢复，截断峰值后退化尾段，能显著提升长程 agent 训练数据质量；可借鉴到推荐系统策略迭代数据清洗。

  - **交互 harness 设计**：维护 experiment tree、candidate 提交、invalidate_node 防止过拟合/数据泄漏，可作为多版本推荐策略管理或自动实验平台的工程蓝本。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：LLM 正从辅助科研走向自主开发与改进 AI 系统，机器学习工程（MLE）需要长程反复实验、反馈分析和方案修订，是递归自我改进（RSI）的落地场景。现有系统多由外部工作流控制实验序列，模型只负责局部代码生成；近期系统开始让模型自主组织实验，但训练面临三个问题：开放环境下缺少可执行环境、高质量长程监督难获取、昂贵实验反馈中间信号难利用。

**方法关键点**：
- **任务工厂与交互环境**：Kaggle-MLE Factory 将历史 Kaggle 竞赛转为可执行任务，提供公共工作区、隐藏测试集和统一评估接口。Interaction Harness 采用 ReAct 循环，让模型自主决定分析、修改、执行或回溯；状态存于 solution nodes 形成 experiment tree，支持 `execute_code` 启动实验、`update_answer` 维护提交候选、`invalidate_node` 剔除不可靠候选。
- **层级 agentic SFT**：先通用 coding/tool-use 轨迹打底，再用 MLE 与科学实验教师轨迹做领域适配。Outcome-guided 过滤以首个最优提交为锚点，截断峰值后退化尾部，保留峰值前探索。对工具反馈和继承历史只做条件上下文，仅对新增输出 token 计 loss。
- **WIRL**：把相邻实验结果间的多轮决策打包成 execution window，共享 outcome-based reward。奖励按执行错误、可评分性、奖牌阈值及局部趋势设置；异步收集窗口，用 token 级 policy correction 解决 rollout 与当前策略不一致；按窗口有效 token 数归一化，结合 PPO-style clipped loss、KL 与熵正则。

**关键结果**：在 MLE-Bench Lite 的 22 个任务上，MLExpert（35B MoE，基座 Qwen3.6-35B-A3B）把 Any Medal 率从 37.9% 提升到 72.7%，持平 Kimi-K3 和 GLM-5.3 等更大前沿模型；在 Claude Code 通用 harness 下仍达 69.7%，比基座高 27.3 个百分点。NatureBench Lite 上 Surpass-SOTA 从 0 升至 50.0%。AIME scaffold 优化 held-out 准确率从 23.3% 升至 43.7%；MLS-Bench-Lite 平均 verifier reward 从 0.322 升至 0.425。消融显示 General SFT、MLE SFT、WIRL 三阶段均带来增益；GRPO/PPO-style 反而低于 MLE-SFT，验证执行窗口设计。最值得记住：**把长程实验的中间执行反馈组织成 execution window 共享奖励，再配合异步策略修正，是让中小规模 MoE 在复杂工程优化上追平大模型的关键。**
