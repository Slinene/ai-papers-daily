---
title: Position Bias Correction is Insufficient for One-Pass Attention Sorting
title_zh: 位置偏见修正不足以替代迭代注意力排序
authors:
- Qiong Tang
- Xiangkun Hu
- Xiangyang Liu
- Yiran Chen
- Yunfan Shao
affiliations:
- Analemma
arxiv_id: '2606.27793'
url: https://arxiv.org/abs/2606.27793
pdf_url: https://arxiv.org/pdf/2606.27793
published: '2026-06-26'
collected: '2026-06-29'
category: RAG
direction: RAG 上下文重排中的位置偏失去偏
tags:
- position bias
- attention sorting
- debiasing
- long-context LLM
- RAG
- lost-in-the-middle
one_liner: 去偏单次注意力排序在高偏置模型上可小幅提升，但仍远不及迭代排序，仅弥补 37% 的精度差距
practical_value: '- **轻量级文档重排 trick**：在长上下文 RAG（如多文档问答）中，仅用一次 decode 的注意力权重即可对文档排序，计算代价极小，可作为生成前的轻量重排模块，且效果接近单次注意力排序基线。

  - **提示级位置偏曲线估计**：利用同一 prompt 中低注意力文档（剔除 top-α）分箱聚合（中位数或均值）来估计位置偏置曲线，再用减法或除法校正原始注意力分数。这一思路可直接迁移到需要对抗位置偏见的生成式推荐或搜索摘要场景，无需额外训练或外部数据。

  - **迭代 vs 单次的取舍**：结果表明，对于位置偏置不严重的模型（如 LLaMA‑2‑32K‑Instruct），单次注意力排序已足够，迭代排序带来的增益极小（0.6pp
  以内），可节省多轮生成的计算开销；对偏置严重的模型（如 YaRN），仍需要迭代排序才能获得较大收益，但可先尝试去偏一次排序，若效果不足再增加迭代。

  - **注意力排序的部署成本控制**：若业务对延迟敏感（如实时推荐搜索）且使用偏置较弱的模型，可直接用单次排序（1 sort+1 gen），仅需一次前向和一次生成，大幅降低延迟，避免
  5 次 sort‑and‑generate 的代价。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
长上下文 LLM 存在“lost‑in‑the‑middle”现象：位置偏置导致中段信息被忽视。迭代注意力排序通过多次文档重排提升 QA 精度，但每次迭代都需重新生成答案，计算成本高昂。作者假设位置偏置是主要瓶颈，若能预先校正注意力分数中的位置偏置，单次排序即可匹敌迭代排序。

**方法**
提出 Debiased One‑Pass Attention Sorting，仅需一次排序+一次生成：
- 在 prompt 中为每个文档计算原始注意力质量（汇总首生成 token 对各文档 tokens 的注意力权重）。
- 从同一 prompt 内部估计位置偏置曲线：剔除 top-α 高注意力文档（视为可能相关），剩余文档按位置分箱计算中位数或均值，线性插值得到连续偏置曲线 ˆb(p)。
- 用减法（s_i = a_i − ˆb(p_i)）或除法（s_i = a_i / max(ˆb(p_i), ε)）校正原始注意力分数。
- 按校正后分数重排文档，末尾放高注意力文档，最后生成答案。

**关键实验**
在 SynthWiki@28K 基准上测试两个模型：LLaMA‑2‑7B‑32K‑Instruct（偏置中等）和 YaRN‑Llama‑2‑7b‑64k（严重近因偏置），对比无排序、k=1 原始注意力排序、去偏 k=1 以及 k=5 迭代排序。
- LLaMA‑2‑7B‑32K‑Instruct：去偏 k=1 与未校准 k=1 均为 94.83%，零改进；k=5 仅略高 0.67pp。
- YaRN‑Llama‑2‑7b‑64k：去偏 k=1 达 55.83%（+8.67pp），但仍比 k=5 的 70.67% 低 14.84pp，仅弥补 37% 的差距。

**核心结论**
位置偏失去偏无法等价迭代排序的重排收益。迭代排序带来的额外提升（尤其在 YaRN 上）可能源于注意力上下文的迭代精炼或噪声减少，未来需进一步探究其机制。去偏方法应针对高偏置模型选择性使用。
