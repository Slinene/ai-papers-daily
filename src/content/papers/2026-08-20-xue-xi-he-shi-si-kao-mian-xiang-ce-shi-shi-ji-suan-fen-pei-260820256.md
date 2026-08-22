---
title: 'Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation'
title_zh: 学习何时思考：面向测试时计算分配的自适应推理
authors:
- Gijs Kassenaar
- Zhao Yang
- Vincent François-Lavet
affiliations:
- Vrije Universiteit Amsterdam
arxiv_id: '2608.20256'
url: https://arxiv.org/abs/2608.20256
pdf_url: https://arxiv.org/pdf/2608.20256
published: '2026-08-20'
collected: '2026-08-22'
category: Reasoning
direction: LLM 自适应推理 · GRPO 自路由
tags:
- GRPO
- adaptive reasoning
- test-time compute
- self-routing
- token efficiency
one_liner: 1.5B 蒸馏推理模型在 GRPO 内学会用首个 token 自路由 NoThink/Short/Long 三模式，平均响应长度减少 41%
  且保持精度-长度帕累托前沿
practical_value: '- 在电商搜索 query 理解、推荐解释、智能客服等 LLM 推理服务中，可部署“首个 token 路由”让主模型自行选择 NoThink/Short/Long，无需额外
  router 网络；简单流量占多数时可节省 50%+ 推理成本，精度损失极小。

  - 训练多模式策略时，用硬 token cap 把路由标签与行为绑定：给短模式设 1024/3000 上限，超过即判错，防止模型选短模式却输出长链，同时保留 Long
  模式处理难题。

  - 在 GRPO 中加入负载平衡项防止模式坍塌：advantage 里加 β_bal*(p* - f_mode)，并做非对称门控——只惩罚错误过载模式的 rollout、只奖励正确欠载模式，不破坏正确样本梯度。

  - 先离线分析业务任务难度分布再上路由；若难度同质（如 Countdown 负例），路由学不到价值差距，会坍塌为单一模式。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**
强化学习训练的推理 LLM 通常使用固定 token 预算，导致简单问题过度思考、难题思考不足。现有折扣方法对所有 prompt 施加统一长度惩罚，缺乏自适应性。本文旨在让模型自主决定每个问题需要多少推理计算。

**方法关键点**
- **三模式自路由**：模型首个 token 输出 NoThink/Short/Long 之一，分别对应快速回答、简短推理、长推理；无独立 router，路由 token 作为主策略一部分端到端训练。
- **硬 per-mode token 上限**：NoThink 1024、Short 3000、Long 不限，强制行为与标签一致，防止路由坍塌。
- **奖励塑形**：每个模式有基础奖励 b 与长度折扣 γ，使每个模式在特定长度区间内奖励最优；NoThink/Short 折扣衰减，Long 恒定 1.0。
- **优化细节**：去掉 KL 惩罚、采用 token-mean 损失聚合、禁用 std 归一化只保留 mean-centering，避免“归一化放大”问题。
- **负载平衡项**：直接在 advantage 上加 β_bal*(p* - f_mode)，目标份额 p*=1/3，并用正确/错误非对称门控防止扰动精度信号。
- **强制 rollout warmup**：前 45 步每组强制三分模式 rollout，促进路由 token 出现。

**关键实验与结果**
- 在 DeepSeek-R1-Distill-Qwen-1.5B 上用 MATH 训练，三模式稳定不坍塌，路由熵近理论上限 ln 3。
- 路由按难度排序：NoThink/Short 处理简单题，Long 集中难题；与未见过的 MATH-500 难度等级单调一致。
- MATH-500 准确率 0.782 vs base 0.796，平均响应长度从 4796 降到 2811 tokens，减少 41%。
- GSM8K 上减少 76% tokens，且精度高于同长度固定模式；AIME 上仅减 13%，匹配帕累托前沿。

**最值得记住的一句话**：自适应路由是 token 效率机制而非精度机制——它大幅压缩平均响应长度，同时将策略置于精度-长度帕累托前沿之上。
