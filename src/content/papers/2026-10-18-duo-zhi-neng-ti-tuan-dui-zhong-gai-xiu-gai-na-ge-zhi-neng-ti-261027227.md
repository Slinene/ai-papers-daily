---
title: Which Agent's Skill Should Change? Group-Relative Credit Assignment for Evolving
  Multi-Agent Teams
title_zh: 多智能体团队中该修改哪个智能体的技能？基于群体相对优势的信用分配
authors:
- Yanan Ma
- Yang Wang
- David Le
- Chenhan Yuan
- Yizheng Sun
- Guangwei Zhang
- Chenghao Xiao
- Chenghua Lin
- Imon Banerjee
affiliations:
- Mayo Clinic
- University of Manchester
- Alibaba Token Hub, Alibaba Group
- Shanghai University of Finance and Economics
arxiv_id: '2610.27227'
url: https://arxiv.org/abs/2610.27227
pdf_url: https://arxiv.org/pdf/2610.27227
published: '2026-10-18'
collected: '2026-10-22'
category: MultiAgent
direction: 多智能体技能演化与信用分配
tags:
- Multi-Agent
- Credit Assignment
- Skill Evolution
- GRPO
- LLM Agents
- Group-Relative
one_liner: GRSE 用同题多轨迹对比把团队 reward 归因到 agent-skill 并驱动技能修订，超越 MASkills
practical_value: '- 多 Agent 推荐/搜索流水线（召回-粗排-精排-生成文案）出现 Bad Case 时，不要默认归咎于最终生成 Agent；复用
  GRSE 的 group-relative 思路：同一 query 采样 4 条完整链路，比较高低 advantage 轨迹中每个 agent 的输入输出差异，定位真正需要修改的
  agent-skill。

  - 把业务规则/策略封装为自然语言 skill 库，只演化 skill 不动模型权重，适合在线迭代；用 structured failure diagnosis
  的 8 类失败类型 + 引用具体 step + edit action，让归因可验证、可执行，并通过 validation gate 防止指标回退。

  - 定期清理手写或迁移来的 skill 库：GRSE 证明 presence-based 信用会奖励“一路顺风但实际有害”的技能，而 group-relative
  信用能正确 prune harmful skill（实验中对植入有害技能全部正确识别）。可用于技能库的巡检和跨场景迁移。

  - 工程上注意：每组 G=4 轨迹训练 token 开销约 1.6-2.9x，但测试无额外开销；跨问题聚合时要按 distinct question 计数，避免重复采样同一问题虚高支持度；equal-reward
  groups 不丢弃，仍能提供一致失败/成功信号。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
多智能体团队共享 reward，难归因到具体 agent 行为；最终答案错误的 agent 未必是需要修改的 agent。MASkills 按 skill 在轨迹中出现与否给信用，导致 harmful skill 在成功轨迹中仅因存在而被奖励。需要行为级信用分配机制。

**方法关键点**  
- GRSE 保持模型参数和 agent 角色固定，只修改自然语言 skill library。  
- 每个训练问题采样 G=4 条完整团队执行，按 GRPO 公式计算组内相对 advantage；同问题同 skill 库，轨迹间差异指向决定性行为。  
- Group-relative critic 同时读 G 条轨迹，输出 agent-skill 信用（helped/redundant/harmful/neutral + utility）、agent 级反馈和结构化失败诊断。  
- 结构化诊断包含 8 类失败类型，强制引用失败/成功 step，动作限定 refinement/induction/no edit，并做检查保证引用一致。  
- 跨问题聚合按 distinct 问题计数，区分 skill 编辑与归纳证据；复用 MASkills 编辑算子和验证 gate，候选 skill 库验证集分数不回退才接受。  
- 空 skill 库开始，5 轮迭代；critic 为 Qwen3.8-27B，actor 为 Qwen3.8-27B 或 Gemma-4-31B-it。

**关键实验**  
- HotpotQA 和 LoCoMo 两个多跳/长程对话问答基准。  
- GRSE vs MASkills：HotpotQA Qwen3.8 83.7 vs 80.6 F1，Gemma4 82.8 vs 82.3；LoCoMo 除 open-domain 外全类别占优，多跳最大 +6.7 F1（Qwen3.8）。  
- 鲁棒性：从植入 3 有害/无关 skill 的库开始，GRSE 对 5 个 helpful/harmful skill 全部赋正确符号，恢复到 66.9 F1 接近干净库 66.7，而 MASkills 只有 58.4，低于起点。  
- 消融：去掉结构化诊断或 G=1 均掉点；equal-reward groups 仍提供一致失败/成功信号；跨任务迁移无损害。

**最值得记住的一句话**  
固定参数多智能体系统中，信用应来自“同 query 多条轨迹的行为差异”，而非“skill 是否出现在轨迹中”；这是把共享结果分解到 agent-skill 并驱动有效编辑的核心。
