---
title: 'Beyond Polarization: The Generative Constraint of Chain-of-Thought in Pointwise
  Reranking'
title_zh: 超越极化：逐点重排序中思维链的生成式约束
authors:
- Xiaoyang Chen
- Jie Liu
- Haijin Liang
- Haibo Shi
- Jin Ma
- Ben He
- Yingfei Sun
- Dezhi Ye
affiliations:
- University of Chinese Academy of Sciences
- Chinese Information Processing Laboratory, Institute of Software, Chinese Academy
  of Sciences
- Tencent
arxiv_id: '2608.30398'
url: https://arxiv.org/abs/2608.30398
pdf_url: https://arxiv.org/pdf/2608.30398
published: '2026-08-31'
collected: '2026-09-01'
category: Reasoning
direction: CoT 推理在逐点重排序中的生成式瓶颈
tags:
- Chain-of-Thought
- Pointwise Reranking
- LLM
- Information Retrieval
- Score Polarization
- Generative Constraint
one_liner: 实证表明 CoT 在逐点重排序中的性能差距跨尺度稳定且训练干预难以消除，根因是离散文本生成限制连续相关性信号
practical_value: '- 在电商搜索/推荐排序中，若用 LLM 做 pointwise 打分（query-item 相关性），应优先选择直接输出数值的评分头，避免让模型先输出
  CoT 再打分；CoT 的离散 token 生成会降低排序信号分辨率，导致分数极化和校准偏差。

  - 论文证明即使通过 RL、细粒度监督、结构解耦等干预，相对排序 gap 依然存在，说明该瓶颈是范式层面的，不是数据或模型容量问题；业务中不要期望通过调优 CoT
  模型达到与直接打分模型相同的排序性能，更务实的方案是改用 listwise/pairwise 方法，或将 CoT 用于 query 理解、解释生成等非排序环节。

  - 如果需要可解释推荐理由，建议两阶段：先用直接打分模型完成排序，再用独立的解释生成模型基于已排序结果生成理由，避免 CoT 介入排序决策。

  - 设计生成式排序模型时，应尽量避免强制文本推理，可考虑连续表示或隐式推理机制，以减少信息损失。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：在 pointwise 文档重排序中，Chain-of-Thought (CoT) 模型通常不如直接打分模型。已有诊断归因于分类性能差、分数极化或校准崩溃，但不清楚针对性训练是否能弥补这一差距。

**方法关键点**：
- 两阶段实证研究，统一框架，使用 Qwen 系列 0.6B 到 32B 模型，并在 Llama-3.1-8B 上验证核心结论。
- 第一阶段验证性能差距的稳定性，排查模型规模和数据容量混淆因素。
- 第二阶段采用强化学习、细粒度监督、架构解耦等压力测试显式修复偏差。

**关键结果**：
- 差距在不同规模（up to 32B）和不同模型家族中稳定存在。
- 干预措施虽然提升了分类准确率和绝对分数，但相对排序 gap 依旧没有消除。
- 结论：在 pointwise 打分范式下，通过离散文本传递连续相关性语义限制了排序信号分辨率，这是一个稳定且难以用现有标准方法克服的瓶颈，而非易于解决的训练偏差。
