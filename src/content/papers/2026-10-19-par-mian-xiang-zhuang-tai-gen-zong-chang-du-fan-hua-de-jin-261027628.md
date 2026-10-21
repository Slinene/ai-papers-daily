---
title: 'PAR: Progress-Aligned Recurrence for Length Generalization in State Tracking'
title_zh: PAR：面向状态跟踪长度泛化的进度对齐循环方法
authors:
- Pan Wang
- Yihao Hu
- Guangyuan Dong
- Yitong Lin
- Hang Wang
- Zimi Liu
- Zhihao Wen
- Jianshe Li
- Jiang-Ming Yang
- Wei Wu
affiliations:
- Ant International
- National University of Singapore
arxiv_id: '2610.27628'
url: https://arxiv.org/abs/2610.27628
pdf_url: https://arxiv.org/pdf/2610.27628
published: '2026-10-19'
collected: '2026-10-21'
category: Training
direction: 循环语言模型长度外推训练
tags:
- looped language models
- length generalization
- state tracking
- recurrent depth
- norm anchoring
one_liner: 训练迭代 k 预测前 k 步状态并锚定范数，使 0.5B 模型在状态跟踪上将外推因子提升至 16 倍
practical_value: '- 在 Agent 多步任务或长会话状态跟踪中，可引入进度对齐中间监督：让模型在每一步/迭代预测已执行操作后的状态，而非只给最终答案，能显著提升长序列上的准确率。可结合
  prefix self-distillation 用仅有最终结果的数据构造中间标签。

  - 对循环状态（如 RNN 隐状态、KV cache 或累加器）做范数归一化：将每次更新后的状态缩放到与首次迭代相同的范数尺度，防止数值漂移，这是长度外推的关键
  trick，可在长上下文或多轮对话状态缓存中尝试。

  - 学习一个 completion readout 或 early exit 模块，让模型自行判断何时输出答案，避免固定深度或人工设定停止条件，适合在线推荐/对话中动态控制计算量。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：循环语言模型测试时可增加迭代，但额外迭代不保证解决更长问题；顺序状态跟踪中最终答案监督未指定每步迭代前进距离，且重复更新改变循环状态尺度，导致长度泛化差。

**方法关键点**：PAR 训练迭代 k 的预测匹配前 k 个操作后的状态（进度对齐），并将循环状态重新缩放到首次迭代范数（范数锚定）。学习完成读出器决定何时停止回答，无需提供停止深度；当中间标签缺失时，前缀自蒸馏仅用最终答案从较短前缀诱导对应关系。

**结果**：在 swap-S5 上，Qwen2.5-0.5B 训练最多 32 步，512 步测试达 95.5% 平均全状态准确率，即 16 倍训练长度，远超 RLT 的 55.7% 和显式 CoT 的 0.8%。消融显示移除范数锚定使外推因子从 16 倍降至 2.2 倍以下；替换为最终答案监督则最多 8 倍。方法在多个顺序状态跟踪任务上有效，确立了深度外推所需任务结构。
