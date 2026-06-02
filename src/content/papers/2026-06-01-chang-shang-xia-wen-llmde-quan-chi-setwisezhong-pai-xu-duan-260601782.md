---
title: Whole-Pool Setwise Reranking with Long-Context Language Models
title_zh: 长上下文LLM的全池Setwise重排序：双端选择加速排名构造
authors:
- Hang Li
- Chuting Yu
- Teerapong Leelanupab
- Bevan Koopman
- Guido Zuccon
affiliations:
- The University of Queensland
arxiv_id: '2606.01782'
url: https://arxiv.org/abs/2606.01782
pdf_url: https://arxiv.org/pdf/2606.01782
published: '2026-06-01'
collected: '2026-06-02'
category: RecSys
direction: LLM重排序 · 全池Setwise · 双端填充
tags:
- LLM Reranking
- Setwise
- Long-context
- DualEnd
- Efficiency
one_liner: 在长上下文LLM中一次调用同时选出最相关和最不相关的段落，将排名构造的串行调用数减半。
practical_value: '- 当候选池可完整放入长上下文时，采用 **双端选择（DualEnd）** 策略：每次 LLM 调用要求模型同时给出最相关和最不相关的物品，将排序构造所需调用数从
  N−1 降至 N/2，显著降低延迟与成本。

  - 电商推荐重排可参考**全池（Whole-Pool）思想**：不再用滑动窗口拼凑全局序，直接一次看到全部候选，避免窗口间不一致，提升排序质量，尤其适合召回池在
  100 以内的场景。

  - 注意长上下文中的位置偏差，DualEnd 对输入顺序敏感；工程落地时可结合随机打乱或自一致性技巧来减弱偏差，或保留原始 BM25 序作为暖启动。

  - 该方法的代价有效性曲线表明：用极少的 nDCG@10 损失（-0.018）换取近 50% 的调用量下降，对实时性要求高、预算受限的业务（如在线重排）很有吸引力。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：LLM 重排序通常受限于短上下文，需要把候选池切成小窗口进行多次比较（如 Setwise-Windowed），导致大量串行调用，延迟高且成本昂贵。随着长上下文 LLM（如 Qwen3.5、Llama3.1）出现，整个候选池可一次性放入，如何在单次调用中获取更多排序信息成为关键问题。

**方法**：提出 **Whole-Pool Setwise 重排序**，每次 LLM 调用都考虑当前所有未排名的候选段落。在基础版本 **WP-T（Top）** 只选最相关的基础上，进一步提出 **WP-DualEnd**：一次调用同时选出最相关和最不相关的段落，分别填入输出排名的头部和尾部，两者均从待排池中移除。这样对于 N 个候选，轮数从 N−1 降至 N/2，算法级提速。

**实验**：在 TREC DL2019/2020 的段落重排序任务上，使用 BM25 召回 top-100 候选，比较 9 个开源指令微调模型（Qwen3.5 0.8B–27B、Llama3.1-8B、Ministral3 3B–14B）。对比基准包括原始的 Setwise-Windowed 变体（SW-TB/TH/BB/BH）和单端全池方法 WP-T、WP-B。

**关键结果**：
- **调用量**：pool-100 时，WP-DE 仅需 50 次串行 LLM 调用，WP-T/WP-B 需 99 次，SW-TB 需 448 次，SW-BB 需 2500 次；相对 WP-T 节省 49.5%。
- **效果**：WP-DE 的平均 nDCG@N 为 0.528，与 WP-T（0.535）和最强 SW 变体（0.534）接近；nDCG@10 为 0.627，仅比 WP-T 低 0.018，比 SW-TB 低 0.046，统计非劣效检验显示多数模型差异不显著。
- **成本**：WP-DE 总 token 消耗约 255K/query，时间为 42s/query，约为 WP-T 的一半；解析失败率更低（0.066 vs 0.854）。

**核心观点**：长上下文不仅在空间上容纳更多文本，更改变了每步调用能完成的任务量。DualEnd 是一次调用做两个排序判定的最小化示例，展示了 LLM 重排序器在质量与效率间的新权衡可能。
