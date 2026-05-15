---
title: Dynamic Latent Routing
title_zh: 动态潜路由：低数据微调下搜索残差流引导码
authors:
- Fangyuan Yu
- Xin Su
- Amir Abdullah
affiliations:
- Thoughtworks AI Labs
arxiv_id: '2605.14323'
url: https://arxiv.org/abs/2605.14323
pdf_url: https://arxiv.org/pdf/2605.14323
published: '2026-05-13'
collected: '2026-05-15'
category: LLM
tags:
- LLM
- Discrete Latent Codes
- Post-training
- Dynamic Routing
- Steering Vectors
- Low-data Fine-tuning
one_liner: 通过搜索离散潜码作为残差流 steering 向量，DLR 在低数据微调中联合学习模型与路由策略，平均超出 SFT 6.6 个百分点
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
现有离散潜码方法（如 Pause Tokens、TokenAssorted）需要多阶段训练，将代码作为额外 token 插入序列，破坏预训练结构，导致低数据微调时始终落后于 SFT。

理论上，作者在时间变化奖励的 MDP 中提出 General Dijkstra Search (GDS)，证明最优目标导向策略可通过子策略的时间拼接获得。这启示了「搜索-选择-更新」法则：不依赖逐状态 Bellman 迭代，而是搜索并组合子策略。

## 方法关键点
**Dynamic Latent Routing (DLR)** 将 GDS 思路应用于 LLM 后训练，在一个阶段内同时学习离散码本、路由策略和模型参数：
- **Chunk-level steering**：将序列按固定 token 数分块，每块的路由策略头（线性层）输出离散代码，代码索引的 steering vector 直接加到指定层的所有隐藏状态上，保持输入序列不变。
- **搜索-选择-更新**：从路由头采样 N 个候选代码序列，选择最大化条件似然 \(p_\theta(x|a)\) 的序列，用该序列计算联合损失。
- **联合目标**：包含标准 LM 损失、信息增益（鼓励提升条件似然）、策略优化项和边际熵正则项，确保代码多样且有效。
- **神经网络松弛 GDS**：以可学习路由头替代优先队列，在每次训练步中隐式执行搜索-评估-更新。

## 关键实验结果
- **设定**：低数据微调（每个数据集仅 1 epoch），对比 SFT、Pause Tokens、TokenAssorted，覆盖 Qwen3 (0.6B–8B) 和 Llama3.2 (1B/3B) 共 6 个模型，4 个 QA 基准（GSM8K、ScienceQA、StrategyQA、CSQA）。
- **性能**：DLR 在全部 24 个 (模型, 数据集) 单元格中胜出，相对 SFT 平均提升 +6.6 pp，推理任务平均提升 +7.8 pp。
- **突出增益**：GSM8K 上 Llama1B +10.2 pp；ScienceQA 上 Qwen3-8B +18.8 pp，Qwen3-4B +12.9 pp。
- **路由分析**：代码向量余弦相似度低（≤0.28），利用率 31%–100%；n-gram 话题纯度随长度增加；消融特定代码造成话题特异性损失，验证了代码的因果作用。
- **算术案例**：在六位数加减任务上，代码自组织为进位/借位等已知子电路，消融全部代码使准确率从 95.5% 跌至 0.1%。

DLR 首次在低数据条件下同时实现性能反超 SFT 和可解释路由，为语言模型的组合式内部控制提供了实用机制。
