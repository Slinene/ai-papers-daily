---
title: 'Apodex 1.1: Scaling Agentic Intelligence for Complex Work'
title_zh: Apodex 1.1：用环境扩展与多智体协调扩展复杂工作能力
authors:
- Apodex Team
- B. An
- B. Li
- B. Wang
- B. Zhang
- B. L. Wang
- C. Feng
- C. Wei
- C. Xue
- C. Zhang
arxiv_id: '2608.23283'
url: https://arxiv.org/abs/2608.23283
pdf_url: https://arxiv.org/pdf/2608.23283
published: '2026-08-23'
collected: '2026-08-26'
category: MultiAgent
direction: 多智体协作与长程任务执行
tags:
- Agentic AI
- Multi-Agent
- Long-horizon
- Environment Scaling
- Verification
- AgentOS
one_liner: 以可验证交付为单位，通过环境扩展和可交互自组织 Agent Team 在小模型上逼近前沿长程任务能力
practical_value: '- 把长程推荐/广告分析 Agent 的内部计划外化成 Task Board：子任务、依赖、状态、结果引用都放在模型上下文之外，作为可被工具读写的共享协调状态；在
  context compaction 或超长会话中仍能恢复计划，避免依赖 message history。

  - 借鉴 verification asymmetry：对生成的商品卖点、活动复盘结论、搜索推荐归因等，只构造核对具体 claim、数字、出处和格式约束的验证器，要求反例或独立来源，而不是让验证者重写整份报告；反馈带
  claim 级定位，便于定向返工。

  - 借鉴 /inputs、/workspace、/outputs 命名空间与 provenance graph：把原始数据、中间实验、最终交付严格分离，发布必须走
  controlled delivery；避免把未验证的中间结果作为推荐策略、广告配置或活动方案上线。

  - 为推荐/Query 改写/运营 Agent 做可执行 sandbox 和 verifier：用“正向构造便宜、逆向求解昂贵”的方式扩展文件、搜索、代码类可验证任务；先硬化
  verifier 再扰动任务，防止奖励黑客，提升 agentic RL 训练信号质量。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机

通用模型能推理，但复杂工作还需要持续与文件、信息源、代码环境交互，维护状态、从失败中恢复并完成可核验交付。论文把这种能力称为 working capability，主张其基本单位不是一次回答，而是可验证地完成的工作。

## 方法关键点

- 用统一任务合同 E=(W,W0,q,A,T,Ω,B,D,VD) 描述长程任务：workspace、目标、动作、状态转移、观察、预算、交付合同与 verifier。
- 两条扩展轴：Environment Scaling 扩大文件、搜索、代码三类可执行环境；Agentic Coordination Scaling 训练分解、委派、异步结果集成、重规划等行为。
- Agent Team 1.1 将内部计划外化为显式 Task Board，支持异步人工干预、非对称验证、自适应 Max Team Effort 和 evidence-grounded synthesis。
- AgentOS 提供持久运行时：workspace 包含文件、检索证据、执行状态、artifact 索引和依赖图；/inputs、/workspace、/outputs 分离原始数据、中间产物与最终交付。
- 训练采用统一 SFT + agentic RL，从环境轨迹和协调轨迹学习；失败归因进入 Task Pipeline，指导下一轮环境构造。

## 关键结果

在 FrontierFinance 与 FrontierScience-Research 上，Apodex 1.1 Agent Team 分别达到 54.3 和 63.3，超过列出的对比系统；在 Professional Work GDPVal 上达到 78.8，接近 Claude Opus 5 的 89.4；35B 参数的 Mini 版本也保持较强长程工作能力。

## 最值得记住的一句话

复杂工作的单位不是回答，而是可验证的交付；规模化的路径是把可执行环境和协调过程都变成训练轨迹。
