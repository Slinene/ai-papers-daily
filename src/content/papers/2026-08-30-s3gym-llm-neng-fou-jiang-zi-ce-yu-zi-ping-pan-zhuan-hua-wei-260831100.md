---
title: 'S3Gym: Can LLMs Turn Self-Testing and Self-Judging into Self-Improvement?'
title_zh: S3Gym：LLM 能否将自测与自评判转化为自我改进？
authors:
- Jiajun Shi
- Siyuan Tao
- Yuhao Wu
- Zexuan Wang
- Jingyuan Zhang
- Jiaheng Liu
- Xinping Lei
- Xinrong Zhang
- Siyuan Fang
- Zhewen Tan
affiliations:
- ByteDance Seed
- M-A-P
- TokenWave.AI
arxiv_id: '2608.31100'
url: https://arxiv.org/abs/2608.31100
pdf_url: https://arxiv.org/pdf/2608.31100
published: '2026-08-30'
collected: '2026-09-03'
category: Agent
direction: Agent 自改进能力评估基准
tags:
- LLM Agents
- Self-Improvement
- Benchmark
- In-Context Learning
- Parameter Training
- Interactive Learning
one_liner: 提出 S3Gym 交互基准，分离自测/自评/自改进并对比三种经验利用路径，揭示自改进受任务结构制约
practical_value: '- 在对话式导购/搜索 Agent 中，把交互经验拆成两类：可复用策略走摘要记忆（如用户偏好规则、常见失败模式），精确状态依赖走原始历史/显式状态，避免用摘要丢失关键上下文。

  - 参数更新（微调/RL）自改进不稳定且易负迁移，业务上优先用上下文/记忆注入做快速迭代，参数训练必须配套严格 held-out 环境与小流量回滚。

  - 设计 agent 自改进评估时，把探索环境与线上评测分离，用可执行验证器做沙箱诊断；重点关注模型能否把反馈转化为策略，而非只看成功动作识别率。

  - 对推荐/广告场景的 Agent 策略优化，先判断任务结构：规则型任务可压成规则库，状态敏感任务保留轨迹；可借鉴 S3Gym 的评估协议做离线自我改进能力审计。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现有 LLM agent 评测多把模型当固定策略，难以回答智能体能否主动测试、评判并改进自身行为。

方法：S3Gym 将 Self-Testing、Self-Judging、Self-Improvement 三者解耦，在七个文本游戏上设置宽松探索与严格 held-out 评估分离，并提供可执行环境验证器；评估三条经验注入路径：History ICL、score-conditioned Summary Memory、Parameter Training。

关键结果：上下文经验可提升多个模型–游戏对，但最优路径强依赖任务结构；摘要记忆适于将经验压缩为可复用战略规则，但在需要精确状态依赖信息时往往不如原始历史；参数训练在部分任务增益明显，但存在不稳定和严重负迁移。结论：识别成功动作并不够，还需将反馈转化为可执行、可迁移的策略。
