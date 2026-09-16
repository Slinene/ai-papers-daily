---
title: 'Drift-Constrained Optimization: Only Direction Matters in Fine-Tuning Instruct
  Models'
title_zh: 漂移约束优化：微调指令模型时方向比距离更重要
authors:
- Fei Yuan
- Changjiang Gao
- Yilei Tu
- Yifeng Liu
- Shujian Huang
- Yu Qiao
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Nanjing University
- University of British Columbia
arxiv_id: '2609.13680'
url: https://arxiv.org/abs/2609.13680
pdf_url: https://arxiv.org/pdf/2609.13680
published: '2026-09-11'
collected: '2026-09-16'
category: Training
direction: LLM 微调 · 漂移约束 · 方向选择
tags:
- drift-constrained optimization
- layer-selective tuning
- Fisher information
- QA-only fine-tuning
- multilingual translation
- LLM
one_liner: 将微调重构为固定行为漂移预算下的方向选择，用层选择调优逆转 QA-only 失效
practical_value: '- 把「允许的行为漂移」显式作为预算，而不是事后加 KL 惩罚或观察遗忘；在微调电商/搜索/推荐 instruct LLM 时，可先冻结
  embedding 与 lm_head，用 anchored KL 评估漂移，避免输出层带来无效分布偏移（论文图6a：训练 lm_head 只增 KL 不提升精度）。

  - 层选择方向搜索可采用两段式配置（如 bottom 4 + top 16，冻结中间层）；连续底部长块 b16 效果差。低漂移预算下 split 配置效率更高，高漂移预算下
  contiguous 更优。业务上可先跑少量 layer-subset 探针，按 ΔTask/√KL 选方向。

  - QA-only/弱监督（如点击、成交标签、无推理过程）微调强 instruct 模型，不要默认全参 SFT；优先试 LoRA 或层选择，可保留通用能力。

  - 选出的有效方向（如 b4t16）可作为后续 RL 初始化，RL 增益更大；在排序/Agent 模型做 SFT+RL 时，可固定该层选择策略再进入 RL。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
标准 SFT 只优化目标任务，不显式控制与参考模型的行为漂移，常导致灾难性遗忘。论文将漂移当作约束预算：固定 D_ref(θ)≤δ，问如何在预算内最大化任务提升。局部看，anchored KL 诱导 Fisher 几何，更新可分解为径向坐标 ρ 和方向 v，于是微调变成方向选择问题。

## 方法关键点
- 优化问题：min T(θ) s.t. D_ref(θ)≤δ；局部二次近似下，最优方向 ∝ -F^{-1}g（自然梯度）。
- 方向效率：η(u) = -g^Tu / sqrt(u^TFu)，等价于任务提升 / 行为漂移，用于跨方法比较。
- FFT、LoRA、参数子集调优被统一为不同可行方向族；LoRA 限低秩，PST 仅更新子集。
- 实践探针：Layer-Selective Tuning (LST)，采用两段式层子集 M(l1,l2)={1..l1}∪{l2..L}，冻结 embedding 和 lm_head 以估计 anchored drift。
- 弱监督设置：仅用 QA 对训练，推理仍要求生成 reasoning trajectory。

## 关键实验
- Qwen3-8B/14B 上，QA-only 全参微调造成推理与通用能力下降；split LST（b4t8/b4t12/b4t16）能同时提升目标并保留通用能力。
- 多语翻译：约 2.8M Lego-MT 语料、100+ 语言，Qwen3-8B b4t16 将 xCOMET lg→x/x→lg 从 47.07/51.40 提升到 52.66/55.60，超过 Seed-X-PPO-7B、Tower-Plus-9B、Aya-Expanse-8B；且优于 Qwen3-8B+RL 所有方向。
- 分析：匹配 drift 时不同方向差异大；低 drift 预算下 split 效率高，高预算 contiguous 更优；增大中间冻结层 gap 会降精度但提升效率；冻结 lm_head 更高效；b4t16 初始化使后续 RL 增益更大。

## 值得记住
微调不只是模型改了多少，而是这些改变被花在了哪个方向。
