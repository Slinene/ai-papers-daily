---
title: Agentic On-Policy Distillation Implicitly Reshapes LLMs' ReAct Patterns
title_zh: Agentic 在线蒸馏隐式重塑 LLM 的 ReAct 模式
authors:
- Deyang Kong
- Zhaoyi Li
- Sijian Ren
- Yuan Wei
- Ying Wei
- Defu Lian
- Shikun Zhang
- Wei Ye
affiliations:
- Peking University
- University of Science and Technology of China
- Tsinghua University
- Zhejiang University
arxiv_id: '2611.19244'
url: https://arxiv.org/abs/2611.19244
pdf_url: https://arxiv.org/pdf/2611.19244
published: '2026-11-13'
collected: '2026-11-18'
category: Training
direction: LLM Agent 训练 · 选择性在线蒸馏
tags:
- On-Policy Distillation
- ReAct
- Agentic LLM
- Cross-Domain Transfer
- Selective Distillation
one_liner: 发现 OPD 跨域重塑 ReAct 模式并提出基于 RL 偏好变化的 selective OPD 缓解负迁移
practical_value: '- 在电商客服/导购 agent 做 OPD/MOPD 时，除了 task accuracy，应监控跨域交互行为指标：同 turn
  内请求用户信息与工具调用共现率、未获用户确认前执行订单修改的依赖违规率；这些行为指标能提前暴露负迁移。

  - 若需将某个任务（如售后）蒸馏进通用 agent，又担心破坏其他场景（如商品咨询），可采用 selective OPD：用 teacher 领域 RL 前后
  checkpoint 的 logprob 差 Δ 排序，保留高 Δ token，丢弃低 Δ tail（例如 5%），在保留源任务大部分收益的同时显著降低负迁移。

  - OPD 会改变 agent 的工具调用策略和推理路线（如数学推理中是否用代码工具），在推荐/电商 agent 中意味着蒸馏后需要重新评估工具调用率、检索 API
  使用率与准确率的 trade-off，不能只看最终效果。

  - 当没有目标域训练数据时，利用源域轨迹 + teacher 前后偏好差的 selective distillation 可作为无目标域监督的缓解手段，但需接受源域性能小幅下降，并在业务指标上做权衡。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
LLM agent 的核心能力依赖 ReAct 将推理、行动、观察串联。On-Policy Distillation (OPD) 已成为 post-training 标准步骤，但领域特化教师对学生跨域交互行为的影响尚不清晰。本文系统考察 OPD 如何重塑数学、ALFWorld、τ2-bench 上的推理路线、行动调整与观察获取。

**方法关键点**  
- 学生为 Qwen3-4B-Instruct-2507；四个训练域：GR（无工具数学）、CI（代码解释器数学）、ALFWorld、τ2-bench（模拟用户+账户工具）。  
- 分析 ReAct 轨迹：数学推理路线（工具调用 vs 自然语言推导）、行动反馈调整（重复率、no-op 后是否改变动作）、观察获取时机（同 turn ask-call 共现、是否违反用户信息依赖）。  
- 提出 selective OPD：对每个学生生成 token 计算 Δ = log p_post − log p_pre，其中 p_post/p_pre 分别是 teacher 领域 RL 前后 checkpoint 的概率；保留 Δ 排序 top 95% tokens 参与 OPD 损失，排除低 Δ tail，以保留通用 agentic 能力、丢弃任务特定 ReAct 模式。

**关键实验**  
- GR 蒸馏使 CI 数学工具尝试率从 70.4% 降至 14.4%，总准确率 16.7%→38.0%；CI 蒸馏保持 73.0% 工具尝试率，准确率 52.4%。  
- CI 蒸馏提升 ALFWorld 准确率 12.9%→40.2%，τ2 41.5%→51.0%，retail query 覆盖率 54.5%→67.5%；ALF 蒸馏使 τ2 从 41.5% 暴跌至 6.6%，ask-call 共现率 94.3%，依赖违规率 55.8%。  
- 仅 ALF 训练时，selective OPD top95% 将 τ2 准确率从 full OPD 的 11.5% 升至 29.9%，ALF 准确率 76.6%（full 87.6%），ask-call 共现率从 97.1% 降至 24.3%。

**最值得记住的一句话**  
评估 agentic OPD 要同时看 task accuracy 与 ReAct 行为指标；通过 teacher RL 前后 logprob 差异做 selective token mask 是无目标域数据时缓解负迁移的实用策略。
