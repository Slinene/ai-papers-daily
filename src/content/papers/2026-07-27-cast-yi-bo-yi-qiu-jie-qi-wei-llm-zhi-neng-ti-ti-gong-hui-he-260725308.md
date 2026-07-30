---
title: 'CAST: Game Solvers as Turn-Level Teachers for LLM Agents'
title_zh: CAST：以博弈求解器为 LLM 智能体提供回合级教学信号
authors:
- Yu Wang
- Yi-Kai Zhang
- Wentao Shi
- Ziang Ye
- Yuchun Miao
- Yueqing Sun
- Qi Gu
- Xunliang Cai
- Lan-Zhe Guo
- Han-Jia Ye
affiliations:
- University of Science and Technology of China
- Nanjing University
- Wuhan University
- Meituan
arxiv_id: '2607.25308'
url: https://arxiv.org/abs/2607.25308
pdf_url: https://arxiv.org/pdf/2607.25308
published: '2026-07-27'
collected: '2026-07-30'
category: Agent
direction: 基于求解器的回合级信用分配 · LLM Agent 训练
tags:
- LLM Agents
- Credit Assignment
- RLVR
- Game Solving
- Turn-Level Teaching
- Process Reward
one_liner: 将求解器状态价值变化转为回合级优势信号，缓解长程游戏中的信用分配难题
practical_value: '- **电商多步对话/搜索结果规划**：可用商品检索器、报价引擎等“可求解环境”的状态价值变化作为中间奖励，训练 LLM 进行多步推荐或搜索，缓解稀疏结局信号的反馈延迟。

  - **只用标量信号，无需 teacher logits**：业务中部署求解器只需输出标量价值，通信与计算开销远小于蒸馏完整分布，适合大规模 Agent 在线训练。

  - **探索引导**：通过 solver advantage 指示哪些候选 action 更有前途，可植入 Agent 的候选排序或树搜索中，提升探索效率，减少无效调用。

  - **泛化到未见场景**：论文在零样本迁移到 ALFWorld/WebShop 上有效，暗示类似方法可用于训练能泛化到新品类、新用户意图的电商任务型 Agent。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：训练 LLM 在长程决策游戏（如推箱子、扫雷）中行动时，仅依靠最终可验证奖励（RLVR）过于稀疏，训练缓慢且难以归因关键步骤。需要回合级过程信号，但现存来源（人工标注、LLM 批评）要么昂贵要么不准确。

**方法关键点**：CAST 利用外部游戏求解器（如 A* 搜索）的状态价值变化，计算动作对最终成功的推进程度，形成 solver advantage，并将其作为过程奖励注入 RLVR 的训练目标。理论表明，在 soft-optimal 求解器假设下，最大化该优势等价于 on-policy 蒸馏，但只需标量价值而非 teacher 的 logits，极大降低了成本。

**关键结果**：在 Sokoban、Minesweeper、Rush Hour 三个环境中，CAST 在所有训练过的基线（包括 RLVR 变体）上取得最好成绩，覆盖分布内与未见难度；在 ALFWorld 和 WebShop 的零样本迁移中，平均表现最优。
