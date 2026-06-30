---
title: 'TACO: Tool-Augmented Credit Optimization for Agentic Tool Use'
title_zh: TACO：工具增量信用优化，让视觉 Agent 学会何时用工具
authors:
- Mingkuan Feng
- Jinyang Wu
- Hao Gu
- Fangrui Lv
- Ruihan Jin
- Chuyuan Zhang
- Zhengqi Wen
- Jianhua Tao
affiliations:
- Tsinghua University
- Institute of Automation, Chinese Academy of Sciences
arxiv_id: '2606.30251'
url: https://arxiv.org/abs/2606.30251
pdf_url: https://arxiv.org/pdf/2606.30251
published: '2026-06-28'
collected: '2026-06-30'
category: Agent
direction: Agentic Tool Use 的信用分配优化
tags:
- tool-augmented learning
- credit assignment
- GRPO
- visual agent
- probe-based reward
- outcome gating
one_liner: 用差分答案探测奖励和结果门控路由，在不依赖外部评判模型下精准分配工具调用的信用，显著提高 Agent 的工具使用效率与准确率
practical_value: '- **工具调用差分奖励**：在电商 Agent 需要调用外部 API（如商品查询、实时定价）时，可在调用前后用探针解码回答，计算正确性差分作为该次调用的即时贡献信号，避免仅用最终结果奖励导致的盲目调用或惩罚。

  - **结果门控路由**：借鉴 OGAR 思想，将最终推荐/回答的强化优势仅路由到实际负责该结果的 token 段（如工具代码、后推理），对冗余调用不予奖励，对必要的失败调用不给予惩罚，从而在搜索推荐
  Agent 中抑制无用的 API 消耗。

  - **防御奖励黑客**：采用差分而非绝对值构建工具调用奖励，可抵消模型提前在推理中泄露答案、虚高探针分数的作弊行为，这一设计可直接用于需要自监督信号的多步 Agent
  训练。

  - **两阶段训练流程**：先通过 SFT 冷启动教会模型基本工具交互格式，再用 RL 精细优化工具使用策略，适合从指令基础模型出发构建工具增强的推荐/对话 Agent。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现有代码工具视觉 Agent 的强化学习仅以最终回答正确性为奖励，无法区分工具调用是有用、冗余还是误导。这导致 Agent 过度调用工具，或对有害调用未能惩罚，且已有过程奖励需要外部评判模型或无法分离调用贡献。亟需一种自监督、无需外部评判、且能精确归因每个工具调用价值的学习信号。

**方法关键点**：
- **TACO 整体框架**：在 GRPO 基础上引入两个耦合通道。
- **差分答案探测奖励 (DAPR)**：在工具调用前后分别插入探针 (`<answer>` token) 贪婪解码答案，用规则检查器评分，取差分 ∆ = r(a2) − r(a1)。正值代表有用调用，负值代表误导调用，零代表无影响，无需任何外部评判模型。
- **结果门控优势路由 (OGAR)**：根据 ∆ 将最终答案的优势仅分配给负责的 token 段：有用调用时奖励整个轨迹；冗余调用时不给予工具分支奖励；误导调用时将惩罚限制在工具分支，保护前置推理；必要但失败时不惩罚工具分支，鼓励探索。门控无参数、无额外成本。
- **训练**：两阶段 SFT→RL，SFT 建立 Think–Code–Answer 格式，RL 使用分组 GRPO 更新，α1=1.0，α2=0.15，无 KL 惩罚。

**关键结果**：
- 在 7B 规模下，TACO 在 12 个感知、推理、通用多模态基准上达到平均 68.1 准确率，超越所有可比代码工具 Agent（如 PyVision 63.7）及 GPT-4o (58.5)，且运行延迟最低（例如 V∗ 上 89.6% @ 2.3s vs 88.7% @ 3.6s）。
- 消融实验：移除 DAPR 降至 67.5，移除 OGAR 降至 70.0，两者互补且必要。
- 模型泛化：同样方法在 Qwen3-VL-8B 上也能提升 5.9 个点。
- 训练动态：差分奖励设计有效抵御探针作弊，同时保持策略熵与探索，最终实现工具按需调用，而非盲目增加调用次数。
