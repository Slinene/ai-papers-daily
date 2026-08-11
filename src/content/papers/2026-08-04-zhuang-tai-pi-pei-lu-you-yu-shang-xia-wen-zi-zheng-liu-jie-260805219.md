---
title: 'When Privileged Guidance Misaligns: State-Matched Routing and Contextualized
  Self-Distillation for Multi-Turn Agents'
title_zh: 状态匹配路由与上下文自蒸馏解决多轮 Agent 特权指导失配
authors:
- Junzhuo Liu
- Weiwei Li
- Jun Ling
- Peng Wang
affiliations:
- University of Electronic Science and Technology of China
arxiv_id: '2608.05219'
url: https://arxiv.org/abs/2608.05219
pdf_url: https://arxiv.org/pdf/2608.05219
published: '2026-08-04'
collected: '2026-08-11'
category: Agent
direction: Agent 多轮训练中状态感知的蒸馏策略
tags:
- State-Matched Distillation
- On-Policy Distillation
- Multi-Turn Agents
- Privileged Guidance
- Self-Distillation
one_liner: 提出状态匹配路由决定何时使用特权轨迹蒸馏，并构造状态上下文化教师语境，显著提升多轮策略效果
practical_value: '- **多轮 Agent 训练中谨慎使用特权轨迹**：在对话推荐、搜索等交互式 Agent 中，若用成功日志作为特权指导，直接对全部轮次施加蒸馏会因状态不匹配而降低有效策略概率。可借鉴状态匹配路由思想，仅在与当前执行进度兼容的轮次上使用特权信号。

  - **构建轻量结构化状态签名**：不必学习状态匹配模型，用手工设计的确定性规则（如位置、库存、页面类型、已选选项）即可快速判断当前状态是否与参考轨迹的某个前置状态兼容，适合工业落地时的快速迭代。

  - **教师上下文中加入状态摘要与候选动作**：在蒸馏时，除完整成功路径外，添加当前状态的简要总结和匹配到的候选下一步行动，比单纯给完整路径更能引导教师产生正确偏好。这可以用于电商导购
  Agent 的多轮决策优化。

  - **路由与上下文解耦设计**：控制实验表明，仅路由掉不匹配轮次（减少蒸馏噪声）就能带来主要收益，而加入状态上下文化上下文能进一步小幅提升。工程实现时可先做简单的路由遮挡，再逐步增强上下文。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
在多轮 Agent 的 on-policy 蒸馏中，常用成功轨迹作为特权信息重新评分学生回答。但交互环境中学生的早前动作会改变执行状态，导致学生到达的轮次状态可能与参考轨迹中的状态不一致（**状态-参考失配**）。此时继续使用完整成功路径蒸馏，会使教师在不兼容状态下评分，可能降低学生正确恢复动作的概率。本文通过固定状态干预实验证实：在同一任务路径上，对匹配轮次施加蒸馏提升教师对学生动作的偏好，而失配轮次则造成负面影响。

### 方法核心
- **状态匹配路由 (State-Matched Routing)**：利用手工构建的环境适配器，根据当前学生轮次的执行状态（位置、库存、页面类型、已选选项等）与参考轨迹中各前置状态进行结构化匹配，并检查候选动作是否在当前可行动作集中。若存在兼容位置，则该轮次标记为 matched，施加蒸馏损失；否则只使用 GRPO 损失。
- **上下文化自蒸馏 (Contextualized Self-Distillation)**：对 matched 轮次，教师上下文由三部分组成：完整成功路径、当前状态摘要（一行文本总结）、匹配到的候选下一步动作。相比无条件给出完整路径，这种局部上下文显式关联了当前进度与应执行的下一步，使教师提供更精准的 token 级偏好。
- **与 GRPO 联合优化**：所有轮次仍通过 GRPO 学习结局奖励，蒸馏损失仅叠加在 matched 轮次上，且分母保持全部轮次的响应 token 数，从而路由掉部分轮次会自然减少蒸馏信号的权重，不改变单轮优化强度。

### 关键结果
在 ALFWorld (具身家务) 和 WebShop (在线购物) 基准上，使用 Qwen3-1.7B 模型：
- SMRC-SD 将 ALFWorld 任务成功率 (Average@4) 从 FullPath-SD 的 0.746 提升至 0.865，WebShop 的 Acc 从 0.574 提升至 0.693。
- 控制实验显示，仅进行路由 (match-only) 就提升至 0.836，再叠加上下文化指导达到 0.865。
- 随机选择同等数量的轮次进行蒸馏仅得 0.723，证明收益来自匹配身份的筛选，而非稀疏性。
- 结构化状态匹配器相比纯历史匹配器可提升覆盖率，并保证 100% 的可执行性审计。

> 可执行参考轨迹应被视为条件计划，其局部有效性必须在用于多轮策略监督前得到验证。
