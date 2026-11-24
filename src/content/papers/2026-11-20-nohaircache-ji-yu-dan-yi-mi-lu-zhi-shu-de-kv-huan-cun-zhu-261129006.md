---
title: 'NoHairCache: Calibrate-Once KV Cache Eviction with One Power-Law Exponent'
title_zh: NoHairCache：基于单一幂律指数的 KV 缓存逐出校准
authors:
- Shuyang Xiang
arxiv_id: '2611.29006'
url: https://arxiv.org/abs/2611.29006
pdf_url: https://arxiv.org/pdf/2611.29006
published: '2026-11-20'
collected: '2026-11-24'
category: LLM
direction: LLM 推理优化 · KV cache 逐出
tags:
- KV cache
- eviction
- power-law
- long-context
- H2O
- StreamingLLM
one_liner: 将 H2O 与 StreamingLLM 统一为幂律族，用单指数 α 校准一次即可跨域迁移，KV 逐出 PPL 更低
practical_value: '- 在长上下文 LLM 服务（多轮 Agent 对话、长文档 RAG、长用户行为序列处理）中，可直接用 NoHairCache
  的 drop-in scorer 替换现有 KV 逐出策略；只需在通用语料上做一次 α 校准，避免按业务域反复调参，且 PPL 稳健。

  - 现有 H2O / StreamingLLM 可视为同一幂律族的两个端点，通过调整 α 在累积重要 token 和最近 token 之间平滑权衡；这为系统提供了一个单一可调旋钮，可依据延迟/内存预算快速配置，而不需切换算法。

  - 其幂律评分 s_i = A_i (t-i)^{-α} 只需维护累积注意力 A_i，计算开销低，易集成；α 校准脚本已承诺开源，可直接复用。

  - 若业务长输入场景对早期重要 token 依赖较高，可使用 α 校准后的中间值而非极端 α=0 或 α→∞，可能比 H2O/StreamingLLM 取得更好效果。'
score: 7
source: huggingface-daily
depth: abstract
---

## 动机
长上下文推理时 KV cache 内存线性增长，注意力计算二次增长，必须逐出 token。现有 H2O（累积注意力）和 StreamingLLM（滑动窗口）通常被看作无关策略，但本文发现它们是同一幂律族的两个端点。

## 方法关键点
- 统一评分公式：s_i = A_i · (t-i)^{-α}，其中 A_i 是累积注意力，α 控制年龄惩罚系数。
- H2O 对应 α=0（不惩罚年龄），StreamingLLM 对应 α→∞（仅保留最近 token，并额外硬编码 attention-sink patch）。
- no-hair 机制约束 α 的可接受范围；在单个语料（WikiText）上校准一次 α，对 Qwen2.5-1.5B-Instruct 得到 [0.556, 0.822]，且该范围在 410M–1.5B 五个模型上一致，并与 PPL 扫描的最优区间吻合。

## 关键结果
- 在三个数据集（WikiText、PG19、arXiv）上，NoHairCache 无需 per-dataset 调参取得最低 PPL，显著优于 H2O 和 StreamingLLM（p<0.05）；budget 512 时比 StreamingLLM 改善 0.06–0.10 PPL。
- 下游四选一问答上，九个 (task, budget) 组合均匹配或优于 StreamingLLM；NarrativeQA 在 25% 保留时保持全 cache 准确率的 98.2%，而 StreamingLLM 为 91.1%；但 McNemar 检验不显著，QA 仅作为旁证。
