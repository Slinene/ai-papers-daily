---
title: 'MemFold: Learning Compact Soft Memory for Long-Context Personalization via
  On-Policy Optimization'
title_zh: MemFold：用在线策略优化学习紧凑软记忆的长上下文个性化
authors:
- Jingxuan Wu
- Yuzhe Yang
- Yiqiao Huang
- Chengzhi Liu
- Qingni Wang
- Chengxuan Qian
- Shutong Wu
- Jiawei Zhang
- Xin Eric Wang
affiliations:
- University of California, Santa Barbara
- University of North Carolina at Chapel Hill
- Harvard University
- University of Wisconsin–Madison
arxiv_id: '2609.36435'
url: https://arxiv.org/abs/2609.36435
pdf_url: https://arxiv.org/pdf/2609.36435
published: '2026-09-28'
collected: '2026-10-03'
category: Agent
direction: LLM 长期个性化记忆压缩与强化优化
tags:
- Soft Memory
- On-Policy Distillation
- GRPO
- Personalization
- Long-Context
- LLM Agents
one_liner: 固定预算软记忆+置信门控在线蒸馏，按下游行为而非文本重构优化长程个性化记忆
practical_value: '- 用户长期画像/行为序列记忆：先用 writer 抽取 query 相关的结构化文本记忆，再压缩为固定数量 soft tokens（如
  K=256），reader 只消费 K 个向量，推理成本不随历史长度线性增长；适合电商/广告 Agent 在长会话中保持个性化且控制 context 开销。

  - 在线策略蒸馏：用冻结的 full-text reader 作为 teacher，只对学生自己采样 token 计算置信门控 σ(β(ℓ_T−ℓ_θ)) 来加权
  student 的 token likelihood；无需 teacher 自回归生成，能对推荐文案/回复中局部违背用户偏好的 span 提供密集监督。

  - 把标量 reward（点击/转化/偏好命中）与 token 级信号结合：GRPO 负责整体结果，OPD 定位“整体流畅但某个推荐项违背偏好”的错误；工程上同组
  reward 方差接近 0 时把 advantages 置 0，避免无效更新。

  - 训练期固定 memory snapshot 和 teacher，防止 RL 更新导致记忆漂移；上线前可用 shuffled/null memory 干预验证模型确实依赖实例特定记忆，而不是只背任务先验。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长程助手面对的历史信息混杂了持续偏好、临时约束、显式修改及背后原因。文本记忆可读可编辑，但 reader 输入会随历史增长；压缩为固定数量隐向量固定了接口，但常见目标仍是重构文本或模仿参考答案，监督发生在模型未生成的序列上，无法直接优化下游个性化行为。因此，问题不在表达形式，而在优化目标错位。

### 方法关键点
- 记忆接口：writer 先产生 query 相关的结构化文本记忆 M（证据、时间关系、派生事实）；compressor 用 backbone 前 4 层编码 M，Perceiver 式聚合为 K 个 soft token Z；reader 只消费 Z。
- 在线 rollout：学生从 πθ(·|x,Z) 采样 G 个回复，任务奖励为 0/1 选项匹配，计算 group-relative advantage，做 GRPO。
- 置信门控在线蒸馏（OPD）：冻结的初始化 reader 作为 teacher，用文本记忆 M 对学生已采样 token 重新打分；gate = sg[σ(β(ℓ_T−ℓ_θ))] 只加权学生自己 token 的 log-likelihood，期望构成向文本记忆 reader 的有界 reverse KL，不允许教师自回归生成，推理时完全移除。
- 初始化与训练：先做 compressor 重构、表征 warmup、辅助推理、reader 初始化，再进入在线优化；训练中缓存 M_init 并冻结 teacher/compressor。

### 关键结果
在 Qwen2.5-3B/7B、Qwen3-4B 上取得 PersonaMem-32K/128K 最高 accuracy。3B 上 32K/128K 为 70.0/88.4，优于 GRPO 的 68.0/58.4、MemGen 54.0/66.1 和 Full Text 46.0/21.9；7B 为 88.0/94.4，Qwen3-4B 为 84.0/89.4。跨域 PrefEval/LongMemEval 无需目标域训练即可迁移。消融显示 GRPO 贡献主要任务提升，OPD 提供额外增益；shuffled/null memory 干预使准确率从 84.0/89.4 降至 58.0/58.9 左右，证明模型依赖实例特定记忆。预算 K 在 128–512 较平坦，K=256 最优，端到端 token 成本随 K 变化不足 1%。

> 紧凑记忆应以其支撑的下游行为来评判，而不是它能否还原文本；教师只对学生采样 token 做有界重排，而不是把教师分布当作模仿目标。
