---
title: Invariant Gradient Alignment for Robust Reasoning Distillation
title_zh: 不变梯度对齐的鲁棒推理蒸馏
authors:
- Zehua Cheng
- Wei Dai
- Jiahao Sun
affiliations:
- University of Oxford
- FLock.io
arxiv_id: '2606.05025'
url: https://arxiv.org/abs/2606.05025
pdf_url: https://arxiv.org/pdf/2606.05025
published: '2026-06-03'
collected: '2026-06-04'
category: Training
direction: 鲁棒知识蒸馏 · 不变学习
tags:
- Knowledge Distillation
- Invariant Learning
- Gradient Masking
- OOD Generalization
- Chain-of-Thought
- LoRA
one_liner: 通过逻辑同构集和连续梯度冲突掩码对齐梯度，提升小模型链式推理的 OOD 泛化性
practical_value: '- 蒸馏推理模型时，构造跨域逻辑同构数据可显著减少表面捷径学习，对需要跨品类解释的推荐系统 CoT 蒸馏有直接借鉴。

  - 连续梯度冲突掩码（M=exp(-τ·V)）可抑制任务特定维度，保留跨任务不变梯度，适用于多任务推荐模型（如同时优化点击、转化、停留）中避免负迁移。

  - 将掩码梯度通过截断 SVD 投影回 LoRA 子空间，不引入额外推理参数，适合在参数高效的推荐召回或排序模型微调中部署。

  - 逻辑一致性得分可作为评估指标，用于检测推荐解释或 Agent 推理的 OOD 稳定性，促进生产级可靠性。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLMs 在分布外输入上易受捷径学习影响，表面上语义变化而逻辑相同的题目会导致蒸馏出的学生模型推理失败，现有知识蒸馏流程欠缺对逻辑不变性的显式建模。

**方法**：提出 IGA 框架，包含三个组成部分：① **逻辑同构集**（Logical Isomer Sets）—— 按相同逻辑结构将数学、医学、法律、科学等不同语义域的问题分组，强制模型学习跨域不变推理；② **可微连续梯度冲突掩码** $M = \exp(-\tau \cdot V)$，其中 $V$ 为跨域梯度方差，掩码压制高冲突参数维度，保留梯度方向一致的维度；③ **截断 SVD 投影**将掩码后的梯度重新映射到 LoRA 低秩流形上，兼顾参数效率与不变性约束。理论上，IGA 的 OOD 泛化界随同构域数量扩展而收紧，并保有标准 SGD 收敛速率。

**结果**：在四个推理基准上超越八种基线方法，准确率最高提升 14.3 个百分点（相比 ERM-SFT），逻辑一致性得分从 0.142 降至 0.031，代表不变性提升四倍，有效缓解了跨域推理退化。
