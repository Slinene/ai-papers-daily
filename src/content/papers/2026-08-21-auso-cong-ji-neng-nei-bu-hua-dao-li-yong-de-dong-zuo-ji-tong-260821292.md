---
title: 'AUSO: Action-Level Unified Skill Optimization from Internalization to Utilization'
title_zh: AUSO：从技能内部化到利用的动作级统一技能优化
authors:
- Huizu Lin
- Chengkai Huang
- Tianqi Gao
- Tao Huang
- Daijiao Liu
- Tongxin Li
- Xiaoyan Sun
- Lina Yao
affiliations:
- University of Science and Technology of China
- University of New South Wales
- Independent Researcher
- University of Chinese Academy of Sciences
- Xi'an Jiaotong-Liverpool University
arxiv_id: '2608.21292'
url: https://arxiv.org/abs/2608.21292
pdf_url: https://arxiv.org/pdf/2608.21292
published: '2026-08-21'
collected: '2026-08-24'
category: Agent
direction: Agent RL · 技能内部化与利用
tags:
- Agent Skills
- GRPO
- JSD
- Skill Utilization
- OOD Generalization
- LLM Agents
one_liner: 用 JSD 度量技能对策略动作分布的影响，以动作级信号重加权 GRPO，将技能从外部监督渐进转为按动作收益利用，提升 Agent 泛化
practical_value: '- 用动作级 skill sensitivity 替代轨迹级 skill routing：在电商导购/搜索 Agent 中，检索到的商品知识、query
  改写策略或用户记忆通常整条 trajectory 统一使用。可以仿照 AUSO，在同一个 visited state 分别计算“有技能/无技能”的策略分布，用
  JSD 得到动作级 sensitivity，再乘 GRPO advantage；只加强有利动作、抑制被技能干扰的动作，且不改变 advantage 符号。

  - 对 reward 稀疏、全失败组失效问题，可仅对 success rate=0 的任务组加入 skill-conditioned teacher JSD loss，并用
  ramp-up + smooth-decay 退火。这比一直加蒸馏更稳，能让 Agent 从专家技能中恢复而不过度依赖外部监督。

  - 在二元成功/失败的 rollout group 中，引入 p(1-p) uncertainty gate 控制动作级 credit assignment；全成功或全失败时门控趋近
  0，避免无信息差异的动作被错误加权。该轻量 trick 可直接嵌入现有 GRPO 流程。

  - 课程式阶段划分 2:5:3（内部化/探索/利用）可迁移到业务 Agent post-training：先蒸馏已有专家或策略知识，再做自主 RL，最后自适应利用外部工具/skill，尤其对
  OOD 流量收益明显。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM Agent 的技能学习大致分三类：外部化、内部化、混合。Skill0.5 等混合方法用 task-level success rate 将样本分为 hard/medium/easy 并套不同目标，但阈值附近 pass rate 可能只差 1/8 却被分配不同训练方式；更关键的是，同一 trajectory 内所有 action 被赋予相同重要度。技能可能帮助某些决策、干扰另一些决策，轨迹级信号过粗，无法回答“当前这一步是否应该使用技能”。

### 方法关键点
AUSO 以 GRPO 为持续优化主干，分三个阶段：
- **早期 teacher-guided internalization**：仅在任务组 success rate=0 时，用 skill-conditioned teacher 与 skill-free student 的动作分布 JSD 作为蒸馏信号；对 action span 内 token 级 JSD 取平均，组内标准化后用 tanh 调制权重，控制内部化 clip，防止高偏差 action 主导梯度。
- **中期 autonomous exploration**：去除 teacher 信号，只做标准 GRPO，巩固自主决策能力。
- **后期 action-level utilization**：对每个 visited state 分别计算“有技能/无技能”策略分布 JSD，得到 action-level information gain；组内标准化后，用 p(1-p) uncertainty gate 缩放，再乘 GRPO advantage。该重加权保持原 advantage 符号，只重分配更新强度，不制造额外 reward。

三者通过统一 JSD operator 串联：内部化阶段作为直接蒸馏 loss，利用阶段作为 GRPO credit modulation。

### 关键结果
在 ALFWorld、WebShop、SearchQA 上对比 prompt/记忆/RL/skill 等方法：WebShop ID 平均 49.7 vs Skill0.5 的 40.4，OOD 平均 51.2 vs 40.6；ALFWorld OOD 平均 67.9 vs 58.5，其中 Pick2 从 33.3 提升至 54.2；SearchQA 平均 47.5 vs Skill0.5 的 44.2。消融显示动作级内部化、动作级利用、uncertainty gate 均有效，阶段比例 2:5:3 最优。

### 最值得记住的一句话
技能不应按 trajectory 成功率路由，而应按动作级信息增益决定是否使用；JSD 是统一内部化和利用的同一信号，GRPO 始终是优化主干。
