---
title: How Many Tools Should an LLM Agent See? A Chance-Corrected Answer
title_zh: LLM Agent应看到多少个工具？用机会校正指标回答
authors:
- Vyzantinos Repantis
- Ameya Gawde
- Harshvardhan Singh
- Joey Blackwell
affiliations:
- Meta Platforms
arxiv_id: '2605.24660'
url: https://arxiv.org/abs/2605.24660
pdf_url: https://arxiv.org/pdf/2605.24660
published: '2026-05-23'
collected: '2026-05-26'
category: Agent
direction: 工具选择深度自适应与评估
tags:
- Tool Selection
- Adaptive Depth
- Chance-Corrected Metric
- Reinforcement Learning
- LLM Agents
- Bits-over-Random
one_liner: 提出Bits-over-Random（BoR）度量评估工具搜索深度，并用作RL奖励学习自适应截断，显著降低提示长度同时保持覆盖率。
practical_value: '- 在电商工具检索或推荐候选集裁剪中，可用 BoR 替代固定 Top-K 评估检索深度，自动惩罚过度展示而无需手工设计惩罚项。

  - 将 BoR 作为强化学习奖励，训练轻量策略网络动态决定每个 query 展示多少工具/物品，实现自适应截断，减少 LLM 调用成本和上下文干扰。

  - 下游验证表明：更短的候选列表能显著提高 LLM 选择正确工具的概率（93.1% vs 87.1%），尤其在中等难度查询上（76.8% vs 60.9%），这对多工具
  Agent 或生成式推荐中的物品选择有直接借鉴。

  - BoR 的自修剪特性依赖检索器质量；当检索器极弱时（如 BM25 在语义场景下）自适应深度会退化为展示全部工具，需结合更强的语义匹配或多路召回。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
LLM Agent 框架中，向模型展示多少个候选工具（搜索深度 K）是一个关键但常被忽视的设计选择。固定 K 无法适应不同查询难度，展示过多工具浪费 token 且干扰模型选择，展示过少则可能遗漏正确工具。当前缺少评估搜索深度是否恰当的标准化指标，亟需一种机会校正的评价方法。

**方法关键点**
- 引入 Bits-over-Random (BoR) 指标：`BoR = log2(Pobs / Prand)`，其中 `Prand` 基于超几何分布计算随机选中至少一个相关工具的概率。BoR 衡量系统相对于随机选择的信度增益，天然具备深度惩罚：K 越大，`Prand` 越高，BoR 越低，无需额外设计深度惩罚。
- 将深度选择建模为 MDP：状态包括已见工具的相似度得分、当前深度、注册表大小等；动作为 STOP 或 CONTINUE；使用 BoR 作为每 query 的奖励信号，成功展示正确工具时奖励为 `-log2(Prand)`，否则为 0，加上一个很小的连续步长代价。
- 训练轻量 RL 代理（DQN 或表格 Q-learning）学习自适应截断策略，作为指标特性的探针，而非生产架构。

**关键实验结果**
- 在 BFCL（370 个真实工具）上，BoR 代理以平均 K=7.4 达到 90.3% 覆盖，仅比固定 K=50 的 90.8% 低 0.5 个百分点，深度降低 7 倍。
- 在 ToolBench（3,251 个工具，N=50）上，固定 K=5 总覆盖 64.7%，BoR 代理总覆盖 61.9%，但在困难查询（金标排名 6-20）上 BoR 找到 16.7%，而固定 K=5 找到 0%。
- 下游工具选择验证（Claude Sonnet 4.6）：BoR 代理的短列表使模型选择正确工具的比例达 93.1%，而固定 K=5 仅 87.1%；在中等难度查询上差距扩大至 76.8% vs 60.9%，证实减少干扰可以提升 LLM 决策准确率。
- 检索质量影响自适应行为：在同一 MetaTool 数据集上，BM25（弱检索器）使 BoR 代理展开至 K=80.7，而嵌入模型（MiniLM）则仅需 K=2.3，且全自动调整，无需人工调参。

**最值得记住的一句话**
BoR 将“展示更多工具”的高随机成功概率转化为递减的奖励，使强化学习策略自然学会根据查询难度和检索器质量自适应截断，无需任何任务相关的深度惩罚项设计。
