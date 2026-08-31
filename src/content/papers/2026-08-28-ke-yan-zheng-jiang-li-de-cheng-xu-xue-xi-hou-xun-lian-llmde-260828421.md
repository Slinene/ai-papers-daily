---
title: 'Program Learning with Verifiable Rewards: Symbolic Backpropagation for Post-Training
  LLMs'
title_zh: 可验证奖励的程序学习：后训练LLM的符号反向传播
authors:
- Vishvesh Bhat
affiliations:
- CoreThink AI
arxiv_id: '2608.28421'
url: https://arxiv.org/abs/2608.28421
pdf_url: https://arxiv.org/pdf/2608.28421
published: '2026-08-28'
collected: '2026-08-31'
category: Training
direction: LLM 后训练 · 符号反向传播程序学习
tags:
- PLVR
- Symbolic Backpropagation
- Post-Training
- Program Synthesis
- RLVR
- Verifiable Rewards
one_liner: 提出PLVR，用符号反向传播从少量示例学习显式可验证程序，替代权重更新完成LLM后训练
practical_value: '- 把电商/推荐 Agent 中可验证的中间步骤（价格计算、库存校验、规则判断、SQL 生成）抽成 typed primitives，用程序搜索学习编排逻辑，而不是微调模型权重：能力外置后可审计、可逐步验证、可跨模型迁移。

  - 用 per-step contract verdict 做 dense reward 替代只校验最终结果，能显著提升多步工具调用链（query 改写→召回→过滤→排序）的学习效率，适合用于训练或引导推荐
  Agent。

  - 新任务只需约 100 条示例的程序搜索，无需新微调数据；同一原语库可服务多业务线，边际成本低，适合快速扩展不同场景的可验证逻辑。

  - 符号反向传播中的类型推断可作为可解释的 credit assignment，用于混合确定性规则与 LLM 判断的业务流程，避免黑盒 RL 的大样本需求。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

## 动机
Post-training 通常把能力写入模型权重，导致不可检查、无法逐步验证、难以迁移。对中间步骤可验证的任务，把推理置于权重之外、表示为确定性与神经原语组成的显式程序，是更可控的替代路径。

## 方法关键点
PLVR 直接从输入输出示例学习程序。核心机制是符号反向传播：每个程序层携带类型化 ontology，在输出端与 ground truth 计算损失，再通过原语签名的类型推断向回传播所需的输入 ontology；这类似链式法则，但 credit assignment 是推导而非估计。与 RLVR 仅验证最终结果不同，PLVR 的奖励是逐步 contract verdict，密集覆盖程序结构。

## 关键结果
在 LiveCodeBench v6 与 τ²-Bench 上，约 30B 基础模型使用 PLVR，在匹配预算下平均比 RL 高 27.8 分，比规模大一个数量级的前沿模型高 13.6 分。单一原语库同时服务两个基准，新任务边际成本约 100 条示例的程序搜索，无需新增微调数据。把 loss 引导搜索替换为同类型空间均匀采样后，median program 从 65.6 降到 17.5，说明优势来自反向传播而非类型系统。
