---
title: 'NarrowSpec: Draft Hidden Width Need Not Match the Target in Speculative Decoding'
title_zh: NarrowSpec：投机解码中草稿隐藏宽度无需与目标一致
authors:
- Alagappan Valliappan
- Ankit More
- Dheevatsa Mudigere
- Jatin Mitra
affiliations:
- NVIDIA
arxiv_id: '2611.23835'
url: https://arxiv.org/abs/2611.23835
pdf_url: https://arxiv.org/pdf/2611.23835
published: '2026-11-17'
collected: '2026-11-20'
category: LLM
direction: 投机解码草稿宽度压缩
tags:
- Speculative Decoding
- Draft Model
- Hidden Width
- LLM Inference
- Latency Optimization
- SGLang
one_liner: 草稿残差宽度可缩至目标一半或四分之一，端到端解码提速且接受率损失很小
practical_value: '- 自研或微调 speculative decoding drafter 时，不要默认继承 target hidden_size：DFlash/EAGLE-3
  可训练为 1/2 或 1/4 宽度，Qwen3-8B、GPT-OSS-20B 上 acceptance 损失约 ≤3%/5.4%，B200 端到端 1.06–1.12×，低带宽
  GB10 上 1.13–1.44×。

  - 部署 DFlash 时把 output adapter 与 target LM head 合并为 W_fold = W_lm W_out，直接从小宽度投到
  vocab，省掉全宽 head GEMM；logits 等价到浮点舍入。EAGLE-3 的 input adapter 可折叠进 embedding。

  - 选择宽度取决于 GPU 带宽和 batch：B200 优先 half，低带宽边缘卡优先 quarter；batch 32–512 仍可获得 1.02–1.23×
  iteration 加速，narrow draft 在吞吐-延迟 Pareto 上不劣于 full width。

  - 训练窄 draft 时 learning rate 和 init scale 要按新宽度重调，不要复用全宽配置；宽度压缩与 vocab pruning 正交，可组合使用。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机

Speculative decoding 的时间公式为 TPOT = Titer / AL，已有工作大多通过提高接受率 AL 来加速。但草稿模型的残差 hidden width 通常直接继承 target，这在线路上是过度配置：draft 的每个 block 都读写残差流，缩小宽度可以同时压缩所有投影，显著降低单次迭代成本 Titer。

## 方法关键点

- 研究对象为两类 feature-conditioned drafter：DFlash（block-parallel，借用 target LM head）和 EAGLE-3（单层 autoregressive，自训 head），在两个 target 上分别训练 full / half / quarter 宽度。
- 窄 draft 从零训练，只在与 target 宽度交界处加 adapter：输入 adapter 把 target embedding/feature 投影到 dd，DFlash 的输出 adapter 在推理加载时与 target LM head 折叠成一个 W_fold = W_lm W_out，从 dd 直接到 vocab，logits 仅因浮点舍入有差异。
- head count、head_dim、层数、vocab、训练数据和 seed 保持不变，learning rate 与初始化按宽度单独选择。
- EAGLE-3 将 input adapter 折叠进 embedding table，避免每个 step 重复运行 adapter。

## 关键实验

在 SPEED-Bench 880 条 prompt、batch 1、temperature 0 下：B200 上 half/quarter 宽度端到端加速 1.06–1.12×；half 的 AL 损失最多 3.0%，quarter 为 2.1–5.4%。GB10 上加速达 1.13–1.44×，quarter 是每个 cell 中最快。batch 32–512 上最高可达 1.21×，所有窄 draft 都不慢于 full width。延迟拆解显示 quarter 宽度 draft 在 B200 上比全宽快 1.43–1.75×，GB10 上快 3.44–3.87×；DFlash 的 head 折叠贡献了约 38–44% 的 draft-body 节省。

最值得记住的一句话：draft hidden width 是训练前应独立选择的设计超参，数据中心 GPU 优先 half，低带宽 GPU 优先 quarter，而不是从 target 继承。
