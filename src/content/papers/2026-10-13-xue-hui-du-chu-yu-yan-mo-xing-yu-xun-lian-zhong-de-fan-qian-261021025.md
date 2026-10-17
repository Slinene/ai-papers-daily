---
title: 'Learning to Read Out: Unembedding Dynamics in Language Model Pretraining'
title_zh: 学会读出：语言模型预训练中的反嵌入动态
authors:
- Matteo He
- William F. Shen
- Alex Iacob
- Andrej Jovanovic
- Xinchi Qiu
- Nicholas D. Lane
arxiv_id: '2610.21025'
url: https://arxiv.org/abs/2610.21025
pdf_url: https://arxiv.org/pdf/2610.21025
published: '2026-10-13'
collected: '2026-10-17'
category: Training
direction: 预训练中读出矩阵与能力涌现解耦
tags:
- unembedding
- pretraining dynamics
- interpretability
- crosscoding
- emergence
- readout
one_liner: 提出参数轨迹交叉编码，发现模型隐藏态编码任务信息早于其输出读出表达，能力时间线混淆了编码与读出
practical_value: '- 评估 LLM 能力或上线时机时，不要只看行为输出（如生成准确率）。模型内部可能已具备任务信息，但 readout 尚未表达，可结合
  hidden state 线性探针或干预 readout 来更早识别可用能力。

  - 对生成式推荐/搜索模型（如 Semantic ID 生成）做微调或适配时，readout 作为最后映射层可能滞后于内部表征，可尝试单独调高 readout
  学习率或冻结其他层，加速输出表达能力对齐，减少训练早期的“假阴性”。

  - 离线分析历史 checkpoints 时，parameter-trajectory crosscoding 只依赖权重、不需要保存 activations，适合在训练迭代中审计能力变化，定位窄窗口，判断某个能力是内部已学到还是读出层尚未跟上。

  - 论文偏基础科学，但“hidden state 与输出 gap”的视角可迁移到 LLM-based 推荐/Agent 系统的能力诊断：当输出质量不佳时，先排查是表征没学到还是读出层没表达，避免盲目增大数据或模型规模。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：现有研究常以模型开始输出正确 token 的时间来判定能力获得，但输出经过 unembedding（readout）矩阵，该矩阵本身也在预训练中学习。这导致行为时间线混淆了“模型学到任务信息”与“readout 表达任务信息”。

方法关键点：提出 parameter-trajectory crosscoding，直接跟踪每个 checkpoint 每个 token 的 readout 行向量，拟合稀疏字典以观察 readout 组织变化。该方法仅需 checkpoint 权重，不需要存储或复现 activations，适合大规模离线分析。用 WordNet 词类解码作为任务，对比 readout 行解码能力与 hidden state 线性探针解码能力的出现时间。

关键结果：在 Pythia 预训练 0.4–1.1% 处发现一个窄窗口，readout 发生重组，WordNet 词类首次可从 readout rows 解码；但此时 hidden state 线性探针早已能解码该信息，而模型自身输出尚未显示。小模型对照实验表明，提高 readout 学习率使 readout 发展更早、hidden state 与输出的 gap 更快闭合，对最终 loss 影响很小。结论：早期训练中许多发展转变的“行为日期”可能主要反映 readout 何时学会表达，而不是模型何时学到该能力。
