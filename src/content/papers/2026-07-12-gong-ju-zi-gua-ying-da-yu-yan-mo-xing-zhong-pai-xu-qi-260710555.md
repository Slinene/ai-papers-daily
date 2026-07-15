---
title: Tool-Adaptive LLM Reranker
title_zh: 工具自适应大语言模型重排序器
authors:
- Zichuan Liu
- Ruijin Hua
affiliations:
- Carnegie Mellon University
- Huazhong University of Science and Technology
arxiv_id: '2607.10555'
url: https://arxiv.org/abs/2607.10555
pdf_url: https://arxiv.org/pdf/2607.10555
published: '2026-07-12'
collected: '2026-07-15'
category: RecSys
direction: 点式重排序 · 自适应工具路由
tags:
- LLM Reranker
- Tool-Adaptive
- MDP
- Cost-Aware RL
- Pointwise Scoring
- Retrieval-Augmented
one_liner: 将点式重排序建模为 Agent MDP，通过成本感知强化学习动态调用工具，平衡精度与效率
practical_value: '- 动态工具调用机制：对于冷门商品、长尾查询或实时性要求高的推荐（如促销、库存变化），可训练重排序模型自行判断是否需要查询外部知识库（商品属性、实时价格、知识图谱），避免对所有请求都进行昂贵的外部检索，保持低延迟。

  - 两阶段训练范式：利用 KL 散度正则化防止 LLM 在微调判别性任务时丧失原生生成能力（灾难性遗忘），随后用 GRPO 优化延迟与准确性的权衡；这一方法可直接迁移到现有基于
  LLM 的评分模型训练中。

  - 非对称成本感知奖励：设计奖励函数时，对高置信度错误且未调用工具给予严厉惩罚（-1.0），对正确回答且绕过工具给予高奖励，迫使模型只在必要时调用工具；可应用于构建自适应推理链路的
  Agent 系统中。

  - 提示模板与推理流程：论文提供了最小化工具调用的系统指令和严格输出格式，以及基于 token 拦截的 MDP 推理 Algorithm 1，对实现类似的 Agentic
  Reranker 具有直接参考价值。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
LLM 用作重排序器时，纯参数化推理面对复杂或长尾查询易产生严重幻觉，而简单地对每个文档都调用外部搜索工具则会带来不可接受的延迟。现有方法要么完全拒绝工具，要么盲目调用，缺乏一种自适应机制让模型在自信时跳过工具、在不确定时检索外部知识。

**方法关键点**
- 将点式相关性评分形式化为 Agent MDP：模型生成推理轨迹，可输出 `<tool_call>` 触发外部搜索并获取证据，或输出 `<answer>` 直接给出二元相关概率，最终通过 `yes`/`no` token 的概率密度计算连续分数。
- 两阶段训练：
  1. Warm-up 阶段：用 MS MARCO 的双分类损失训练，同时加入 masked KL 散度正则化——对除最终评分 token 之外的所有 token 施加 KL 惩罚，防止模型遗忘生成能力。
  2. RL 阶段：采用 GRPO 和一非对称成本感知奖励。奖励由格式合规、准确度和工具调用成本三部分构成。准确度奖励设计为：若预测误差在容忍阈值内，奖励 = 1 - 绝对误差；若超过阈值且未调用工具，惩罚 -1.0；若超过阈值但调用了工具，奖励 0。这驱动模型只在必要时调用工具以避免灾难性惩罚。
- 推理时，系统通过拦截 `<tool_call>` token 暂停解码，执行搜索 API（Perplexity），将结果拼入上下文后恢复生成，详见 Algorithm 1。

**关键结果**
- 在 BEIR 9 个数据集上，TALRanker-8B 平均 NDCG@10 达 46.3，超越 Rank-R1-14B 等大尺寸模型；在推理密集型 BRIGHT 基准上平均 NDCG@10 为 29.7，尤其知识密集子集（如 TheoT.、TheoQ.）提升显著。
- 吞吐量极高：4B/8B 模型在 BRIGHT 上分别达到 977/778 queries/hour，与纯点式直接评分模型相当，而推理型基线（如 Rank-R1-14B）仅 30 queries/hour。
- 工具调用率随模型规模和数据难度自适应：8B 模型在 TREC-DL19 上完全不调用工具，在 BRIGHT 心理学子集上调用率仅 0.28%，而 0.6B 模型则因参数知识不足始终尝试调用（但格式失败）。
- 消融表明，去掉 KL 正则化会导致 QA 能力完全崩溃；成本奖励中的超参数 λ=0.02、γ∈[0.2,0.3] 能平衡精准度与工具调用率。
