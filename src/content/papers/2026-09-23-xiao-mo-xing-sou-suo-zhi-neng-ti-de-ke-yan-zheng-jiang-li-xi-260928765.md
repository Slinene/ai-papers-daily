---
title: Reinforcement Learning with Verifiable Rewards for Small Search Agents
title_zh: 小模型搜索智能体的可验证奖励强化学习
authors:
- Gaurisankar Jayadas
- Aske Plaat
- Álvaro Serra-Gómez
- Sandheep P
affiliations:
- Leiden Institute of Advanced Computer Science, Leiden University
arxiv_id: '2609.28765'
url: https://arxiv.org/abs/2609.28765
pdf_url: https://arxiv.org/pdf/2609.28765
published: '2026-09-23'
collected: '2026-09-27'
category: Training
direction: RLVR小模型搜索Agent训练
tags:
- RLVR
- GRPO
- Reward Shaping
- Small Language Models
- RAG
- Search Agent
one_liner: 在0.8B模型上证明RLVR可训练搜索Agent，且稀疏EM奖励最差，token-F1部分信用奖励带来3.8倍提升
practical_value: '- 在资源有限、用小模型做 agentic search/RAG 时，奖励函数不要直接用 exact match 稀疏奖励。改用
  token-F1 部分信用奖励（可加格式地板），避免 GRPO 组内优势因零方差而失效。

  - 训练与评估共享同一套 prompt 模板、工具接口和解析器，确保格式分布一致；检索到的 token 必须 mask，防止模型学预测语料。

  - 使用模型家族原生工具调用格式（如 Qwen 的 nested-XML）而非自定义标签，能降低冷启动难度；用量化检索索引（IVF+SQ8）替代 flat index，内存从
  65GB 降到 16GB 且 recall 基本不降，利于训练时多轮 rollout。

  - 若在电商搜索/推荐场景训练 Agent 做多跳查询或商品属性推理，可借鉴隐式长度惩罚：生成上限本身会形成对过长 rollout 的惩罚，但训练 reward
  与真实业务指标要区分，格式奖励可能让训练曲线虚高。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：RLVR 在数学、代码等可验证领域效果显著，但开放域 QA 奖励噪声大，小模型初始策略差，奖励形状更关键。已有 reason-over-search 配方在大模型（3B-32B）上有效，sub-1B 需依赖蒸馏，且奖励形状未作为控制变量。本文在 0.8B 模型上从自身初始化训练，检验可行性并消融奖励形状。

**方法关键点**：
- 模型 Qwen3.5-0.8B，GRPO 训练，无 critic，G=5, clip ε=0.2, KL β=1e-3。
- 训练数据仅用 MuSiQue（2-4 hop）；检索 Wikipedia-2018，E5-base-v2 编码，IVF4096-SQ8 量化索引，top-5。
- 三个奖励形状消融：EM-only（Search-R1 稀疏奖励）、F1+format（ReSearch 带 0.1 格式地板）、F1-only（去掉地板隔离格式项）。
- 实现要点：使用 Qwen 原生 nested-XML 工具调用；检索 token 全部 mask；训练与评估共享 prompt/工具接口；固定其他组件，只改奖励。

**关键实验**：
- 七基准测试：NQ, TriviaQA, PopQA, HotpotQA, Bamboogle, 2WikiMultiHopQA, MuSiQue，共 51,713 行/checkpoint。
- 未训练 floor EM 0.092；最佳 F1-only seed44 step310 达到 0.352，提升 3.8 倍。
- 在 matched horizon（step≤180），EM-only 在三个 seed 全部最差，均值 0.271 vs F1+format 0.307、F1-only 0.305；EM-only 甚至在它直接优化的 EM 指标上也最差。
- 三个 seed 精确检验 p≈0.037/0.074/0.111；F1 奖励还带来 rollout 压缩，token 总量减半。

**最值得记住的一句话**：在 sub-1B 模型的 GRPO 搜索 Agent 训练中，稀疏 exact-match 奖励是错误起点，应使用带部分信用的 token-F1 奖励并配合格式地板与检索 token mask。
