---
title: 'SimRec: Learning to Search, Ask, and Recommend from Simulated Interaction'
title_zh: SimRec：从模拟交互中学习搜索、询问与推荐
authors:
- Yaxin Zhang
- Xingyu Wu
- Yuchen Yan
- Yuqin Dai
- Hong Zhao
- Lixing Shen
- Zhan Chen
- Jian Shao
- Yongliang Shen
affiliations:
- Zhejiang University
- Tsinghua University
- Hikvision Research Institute
arxiv_id: '2611.15426'
url: https://arxiv.org/abs/2611.15426
pdf_url: https://arxiv.org/pdf/2611.15426
published: '2026-11-11'
collected: '2026-11-13'
category: Agent
direction: 推荐 Agent · 模拟交互强化学习
tags:
- LLM Agent
- GRPO
- User Simulator
- Conversational Recommendation
- Tool-Integrated RL
- Multi-turn Interaction
one_liner: SimRec 用任务锚定用户模拟器和 GRPO 端到端训练推荐 Agent 的完整多轮交互策略，在 ESCI 和 Amazon C4 上显著提升
  NDCG@100
practical_value: '- 将推荐 Agent 的多轮交互当作策略训练而非固定 workflow：用 GRPO 对完整轨迹做 RL，奖励包含最终命中、自然检索
  NDCG、有效工具使用；该奖励结构可直接复用到商品搜索/导购 Agent。

  - 用户模拟器不要直接用目标 item 或完整画像，而是锚定当前任务需求并生成缺失反馈；这样避免泄漏 target 且更贴近真实交互。离线训练可先外部 LLM
  模拟，再尝试 self-play 但需注意复杂场景下 self-play 可能显著变差。

  - 工具设计上，把长期偏好、商品详情、候选检索拆成独立工具，由策略决定何时调用；偏好通过工具获取而非模拟器输入，能训练策略主动查证。适合电商导购 Agent 的工具集和状态设计。

  - 大目录稀疏奖励问题可通过训练时目标注入缓解：检索 miss 时在训练中随机将 target 插入可见列表以提供候选比较信号，但检索奖励仍基于未注入结果，评估禁用，防止泄漏。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
LLM 推荐 Agent 能搜索、询问、推荐，但现有方法依赖手工设计的工作流，训练只优化查询改写或列表排序等孤立组件，完整交互结果无法回传策略。这导致 Agent 很少验证候选、查询用户偏好、拒绝后恢复。SimRec 的目标是把“何时搜索、何时检查、何时询问、何时推荐”作为完整交互策略来训练。

## 方法关键点
- **任务锚定用户模拟器**：条件在当前任务需求 z_x 而非目标 item 或用户画像，反馈只说明缺什么，不泄露 target；支持外部 LLM 和共享参数 self-play。
- **工具集成动作空间**：Product Search、Item Detail、User Preference 三个工具，无固定顺序；长期偏好通过工具暴露，而非模拟器输入。
- **任务对齐奖励**：R(τ)=clip(λ_rec R_rec + λ_tool R_tool + R_fmt - P(τ))。R_rec=Hit + 自然检索 NDCG@K；R_tool 奖励有效工具调用；P 惩罚重复查询和过长轮数。
- **训练**：GRPO 在完整多轮轨迹上优化，token-wise KL 约束；训练时 target injection 在检索 miss 且超过 N 个用户轮后随机插入可见列表，评估禁用。

## 关键实验
在 ESCI 和 Amazon C4 上，SimRec 将 Qwen3-4B 的 NDCG@100 从 32.23 提至 35.42，Recall 72.03→77.91，Hit@1 21.20→24.08；Amazon C4 NDCG 22.94→24.72，超过更大的 LLM backbone 和 trainable baselines。BM25 弱检索下仍有效。消融：移除用户偏好 NDCG -3.55 pts，移除 item detail Hit@1 -3.72 pts；奖励消融显示 hit、retrieval、tool 奖励互补。行为分析：拒绝后恢复率 1.93%→4.34%，工具调用从 2.43 增至 5.19 次。

## 最值得记住的一句话
端到端训练推荐 Agent 的关键是让用户、工具、完整交互轨迹的奖励闭环，而不是优化单步组件。
