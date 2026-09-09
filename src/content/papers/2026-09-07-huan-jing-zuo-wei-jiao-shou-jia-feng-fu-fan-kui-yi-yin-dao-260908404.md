---
title: 'Environments as Scaffold: Enriching Feedback to Bootstrap Self-Evolving Agents
  in Long-Horizon Tasks'
title_zh: 环境作为脚手架：丰富反馈以引导长程任务中自进化智能体
authors:
- Hongbang Yuan
- Zhuoran Jin
- Yixin Cao
affiliations:
- Fudan University
- CASIA
- Shanghai Innovation Institute
arxiv_id: '2609.08404'
url: https://arxiv.org/abs/2609.08404
pdf_url: https://arxiv.org/pdf/2609.08404
published: '2026-09-07'
collected: '2026-09-09'
category: Agent
direction: Agent 强化学习环境反馈设计
tags:
- Reinforcement Learning
- LLM Agents
- Environment Design
- Reward Sparsity
- Long-Horizon Tasks
- Feedback Enrichment
one_liner: 通过构建反馈增强环境，用环境侧观察丰富化缓解长程任务智能体 RL 训练中的奖励稀疏
practical_value: '- 在对话式搜索/导购 Agent 的 RL 训练中，不要只靠 SFT 预热；改造模拟环境，episode 早期提供动作级 hint，后期转为丰富观察（如商品属性、用户状态、剩余步骤），可有效缓解
  reward sparse。

  - 多步推荐/搜索任务可分段设置反馈策略：前期 action guidance 防止冷启动，后期 observation enrichment 鼓励自主探索更优路径，形成课程式退火。

  - 工程上注意 rollout 分组内反馈一致性（同一 group 的 critic/advantage 信号口径一致），否则 GRPO/PPO 类优化容易震荡；可在反馈模板中固定格式化字段。

  - 对在线学习推荐 Agent 的环境模拟器设计有借鉴：把部分先验知识编码进环境观察而非模型初始策略，训练后策略内化，推理时无需额外先验。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：LLM 在静态推理上很强，但作为 autonomous agent 在 long-horizon 任务上做 RL 训练时奖励极度稀疏；传统 agent 侧 SFT warm-up 受数据稀缺和探索受限制约。

方法关键点：将重心从 agent 侧移到 environment 侧，构建 Feedback-Enriched Environments (FEEs)。通过 pilot study 确立反馈设计策略：在单 episode 内部探索后期以及跨 episode 演化后期，环境反馈从 action guidance 切换到 observation enrichment，即前期给动作引导，后期丰富观察信息，形成脚手架式支撑。

关键结果：在 SciWorld 和 BFCL 上，用 Qwen3 不同尺度、GRPO/GSPO/DAPO 等 RL 算法实验，FEEs 相对标准环境一致提升。分析显示：训练熵波动降低、困难任务中状态空间探索更主动、环境引导被内化到策略权重而非仅推理时先验，且 intra-group 反馈一致性是稳定优化的关键边界。
