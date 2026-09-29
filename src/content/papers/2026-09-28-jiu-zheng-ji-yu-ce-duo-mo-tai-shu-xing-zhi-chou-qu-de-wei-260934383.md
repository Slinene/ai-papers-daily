---
title: 'Correcting to Predict: Pseudo-Value Correction for Multimodal Attribute Value
  Extraction'
title_zh: 纠正即预测：多模态属性值抽取的伪值校正
authors:
- Junhao Zhang
- Feiran Hu
- Xiao Hu
- Baoliang Cui
- Xiaoyi Zeng
affiliations:
- Alibaba International Digital Commerce Group
arxiv_id: '2609.34383'
url: https://arxiv.org/abs/2609.34383
pdf_url: https://arxiv.org/pdf/2609.34383
published: '2026-09-28'
collected: '2026-09-29'
category: Multimodal
direction: 多模态商品属性抽取 · 伪值校正
tags:
- Attribute Value Extraction
- MLLM
- Pseudo-Value Correction
- Self-Consistency Refinement
- E-commerce
- LoRA
one_liner: 将多模态属性值抽取重构为伪值纠正任务，训练时混合检索伪值与占位符，推理用固定占位符实现免检索单次预测
practical_value: '- 把分类/抽取任务改造成“伪值纠正”范式：训练时给模型一个可纠正的初始假设（检索候选或占位符），让模型依据多模态证据决定保留还是纠正，而不是直接生成。这比直接生成更能逼出细粒度证据校验，适合属性补全、商品理解、意图分类等电商任务。

  - 检索增强避坑：不要将检索候选当 RAG 上下文拼接，而是作为待验证的 pseudo-value 放进 prompt 让模型纠正。这样可以减少输入 token（本文
  233 vs 585），提升 QPS（4.77 vs 1.45），并对检索错误更鲁棒；在搜索推荐场景中，对 query 分类、类目预测也可以借鉴。

  - 用 Self-Consistency Refinement 做扰动样本挖掘：对同一输入换多个伪值看预测是否变化，不一致样本加入第二阶段微调。这种针对“输入扰动不稳定”的信号比通用困难样本更有效，可以迁移到
  prompt/上下文敏感任务的稳健性训练。

  - 部署设计采用“训练复杂、推理简单”：训练时用检索伪值学到修正行为，推理只需固定占位符触发，免在线检索和迭代 refine，保持接近直接生成的吞吐，适合大流量生产系统。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：电商商品属性值抽取（AVE）是搜索、推荐、过滤和运营的基础，但隐式属性需要联合图文推理，MLLM 直接生成时初始预测常证据不足，后处理自校正或多智能体辩论难以推翻早期错误。本文把预测重构为“纠正伪值”，让模型先接收一个待验证的初始假设，再根据多模态证据修正。

**方法关键点**：
- 输入包含图片、标题、描述、类别、属性，Prompt 中显式提供 [Pseudo-Value] 和最多 20 个高频 canonical 候选值，规则要求模型根据图文证据保留或纠正伪值。
- 训练伪值来源：占位符 `invalid` 和 GME 检索 top-3 同属性相似商品真实值。检索 top1 匹配率仅 65.9%/55.1%，但“可信但不完美”的假设提供更强监督。
- Self-Consistency Refinement：用 leastV、invalid、候选集等多种伪值评估训练样本，预测不一致者标记为不稳定样本；用该子集 + 50% 重放原始数据继续训练 2 轮。不稳定子集 hard 属性占比从 28.29% 升至 68.14%。
- 推理：固定占位符 leastV，单次前向，免在线检索和迭代。

**关键结果**：
- ImplicitAVE 上 C2P-SCR Micro-F1 88.87，超过 MICE 87.95、直接 SFT 87.19、GPT-4V 86.77。
- AE-Product 上 91.39，较直接 SFT 88.12 提升 3.27；hard 属性子集从 66.87 到 76.79（+9.92）。
- 对比 RAG-top3，C2P 提升 1.21 点，平均输入 token 从 585 降至 233，QPS 从 1.45 升至 4.77。
- 线上 7 天 A/B：可部署类-属性对 +22.6%，核心属性完整商品 GMV share +9.8%，seller adoption 83%→85%，搜索相关 filter options +37.2%、filter usage +15.6%、filtered sessions CTR +3.3%。

**最值得记住的一句话**：需要依据证据判定的分类/抽取任务，不要直接生成答案，而是给模型一个可纠正的初始假设——训练时用检索出的“可信但不完美”伪值强制证据校验，推理时用固定占位符触发修正行为，实现高精度与低延迟。
