---
title: 'What We Keep of What We Forget: Replacement Operators and Routing Semantics
  in Training-Free MoE Expert Pruning'
title_zh: 训练无关 MoE 专家剪枝中的替换算子与路由语义
authors:
- Ezza Ali
- Sehrish Bibi
- Momina Moetesum
- Faisal Shafait
affiliations:
- School of Electrical Engineering and Computer Science (SEECS), National University
  of Sciences and Technology (NUST)
- Deep Learning Laboratory, National Center of Artificial Intelligence (NCAI), NUST
arxiv_id: '2610.41366'
url: https://arxiv.org/abs/2610.41366
pdf_url: https://arxiv.org/pdf/2610.41366
published: '2026-10-29'
collected: '2026-11-04'
category: LLM
direction: MoE 专家剪枝 · 替换算子与路由语义
tags:
- MoE
- expert pruning
- training-free
- router semantics
- replacement operator
- LLM compression
one_liner: 固定剪枝掩码，系统比较 MoE 专家替换算子与门控尺度，提出倾斜新手算子并揭示 trained-scale rule
practical_value: '- 部署 MoE 推荐/Agent 模型时，剪枝后不要默认 renormalize 幸存者 gate；先检查原模型 router
  是否在训练时做了 top-k renormalization，保留与其一致的 gate scale（trained-scale rule），否则可能掉 0.8–8.5
  个点，甚至反转 rerouting 是否优于均值常数。

  - 若要对剪掉的专家做廉价替代，可用 tilted novice：只存一个低秩输入映射（rank-32 甚至 rank-8），参数增加约 1.2–1.8%，在多项选择和生成任务上稳定优于均值常数，且对
  3/4-bit 量化鲁棒；比保留更多专家更省参数。

  - 评估剪枝模型不能只看 MCQ；务必加入 GSM8K、代码生成等推理/生成任务，因为 25% 剪枝时 MCQ 可保留 92–97%，但 GSM8K 仅 5–65%、代码
  0–17%，结论可能反转。

  - 校准数据域对剪枝 mask 影响很大（4–9 倍于重采样），推荐/Agent 场景应使用与线上分布一致的校准数据，并报告不同校准切片的结果；仅用通用文本可能掩盖领域退化。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
MoE 模型部署时专家存储成本高，training-free expert pruning 可在不训练的情况下移除专家。但过往方法同时改变两个决策：选哪些专家、以及 router 选中被删专家时如何计算，导致替换算子与路由语义的贡献混杂。本文固定 mask，专门拆解这两个维度。

### 方法关键点
- 在 OLMoE、DeepSeek-V2-Lite、Moonlight 上固定 MoNE 产生的 25/50/75% 剪枝掩码，比较 7 种替换算子：均值常数、tilted novice（低秩线性映射，rank-0 即常数）、MoRA 代理、ConMoE 槽重映射、COMPEL 权重补偿、keep-scale 与 renormalized rerouting。
- 提出 trained-scale rule：路由器训练时是否 renormalize top-k gates 决定剪枝后应保留哪种门控尺度。
- 评估覆盖 9 个 zero-shot 多选、GSM8K、HumanEval/MBPP、WikiText 等，采用配对 bootstrap + Holm 校正，并用不相交校准切片检验稳定性。

### 关键结果
- Gate scale 影响最大：在无 renorm 训练的 OLMoE/DeepSeek-V2-Lite 上，renormalize survivors 损失 0.8–8.5 点，翻转 rerouting 是否优于 MoNE 常数；在有 renorm 训练的 Moonlight/Granite 上则相反。
- Tilted novice 在 50% 剪枝时，OLMoE +3.45 点、Moonlight +1.37 点，只增加 1.2–1.8% 参数，对 3/4-bit 量化基本不减增益。
- 无算子全面获胜：DeepSeek-V2-Lite 上 trained-scale rerouting 最好；部分复制被剪专家（高能量神经元）与 tilt 在 OLMoE/DeepSeek 上统计等价。
- 评估可改变结论：25% 剪枝下常数保留 92–97% 多选准确率，但 GSM8K 只剩 5–65%、代码 0–17%；校准域移动 mask 效果是重采样的 4–9 倍。

**最值得记住的一句话：替换算子的选择固然重要，但“幸存专家的门控尺度是否与训练时一致”是与算子本身同级的、经常被忽视的决策。**
