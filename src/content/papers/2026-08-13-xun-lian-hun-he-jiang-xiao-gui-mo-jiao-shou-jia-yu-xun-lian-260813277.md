---
title: 'Mixture of Training: Recombining Small-Scale Scaffolded Pretraining Runs into
  a Larger Language Model'
title_zh: 训练混合：将小规模脚手架预训练运行重组为更大语言模型
authors:
- Mohammed Sabry
- Sean Augenstein
- Keith Rush
- Lucio Dery
affiliations:
- Google, Mountain View, CA, USA
- School of Computing, Dublin City University, Dublin, Ireland
arxiv_id: '2608.13277'
url: https://arxiv.org/abs/2608.13277
pdf_url: https://arxiv.org/pdf/2608.13277
published: '2026-08-13'
collected: '2026-08-14'
category: Training
direction: 模块化 LLM 预训练 · 脚手架重组
tags:
- Mixture of Training
- Scaffolded Pretraining
- Modular Training
- LLM Pretraining
- Compute Efficiency
- Critical Path
one_liner: 提出 MoT：在冻结对齐器脚手架中独立训练 Transformer 深度块并重组，验证模块化预训练可行性
practical_value: '- **模块化底座与多域迁移**：若做电商/广告/搜索的多域 LLM 底座，可把不同领域的深度 block 独立训练再重组，避免每次全量重训；复用
  off-the-shelf aligner 作为稳定表示接口，重组后加少量 end-to-end adaptation 回补接口错配。但要把 aligner 成本按复用次数摊销，R≥3
  才有净收益。

  - **数据流设计 trick**：aligner 存在时，给各子模型上 disjoint data streams 能改善冷组合 PPL（19.3 vs 20.3），没有
  aligner 反而恶化；说明在表示接口稳定后，更广 token 覆盖对模块化重组有帮助，可直接用于多 worker 独立训练的数据划分策略。

  - **工程核算与调度**：把训练成本拆成 train EF / full-charge EF / amortized EF，并估算 layer-equivalent
  critical path，有助于在做出“模块化训练更省”的结论前避免被 aligner 一次性成本误导；Stage 1 各 scaffold 可并行、故障可局部恢复，适合小规模科研迭代或需要隔离故障的长训练任务。

  - **风险与局限**：当前仅验证 PPL，未测 downstream reasoning/校准/鲁棒性；在竞价广告/推荐排序这类对业务指标敏感的场景，不能假设模块化预训练模型可直接替换
  monolithic，需要补做 SFT/RLHF 或在线 A/B 评估。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：LLM 训练通常是单个端到端整体优化，所有层耦合导致故障影响整个运行、每次改进都要重启大系统。MoT 试图把预训练分解为可独立训练的小任务，再重组为更大的可用模型，特别适合小规模训练研究。

**方法关键点**：
- 目标 Transformer 切成 K 个连续层块 f_i；引入形状兼容的冻结预训练 aligner A，切成相同块。
- 每个 scaffold S_i = 顶部 aligner 块 + f_i + 底部 aligner 块，只训练 f_i，损失为 next-token prediction；无需跨块梯度交换。
- Stage 0 准备 aligner；Stage 1 并行训练所有 scaffolds；Stage 2 丢弃 aligner，重组 F=f_K∘...∘f_1，可选短时端到端 adapt。
- 实验：12 层、1.3B Gemma-style target，C4；baseline 128k updates，33.6B tokens，PPL 15.0，268.4 EFLOPs；MoT 默认 K=2、4 层 aligner、disjoint data streams。

**关键结果**：
- 冷组合 PPL 19.3（train 128.2 EF / full-charge 157.9）；+15k 适应后 PPL 15.9（full 189.4，比 baseline 低 29%）；quality parity 达 PPL 15.0，但 full-charge 285.0 高于 baseline，需 amortize aligner（R≥3）才低于 baseline。
- 消融：无 aligner 冷组合 PPL 38.9；有 aligner 且 disjoint data 为 19.3，优于 shared 20.3；K=4 降至 24.8，更便宜但差。

**最值得记住**：独立训练的深度切片在共享 aligner 表示接口下可重组为可用大模型，质量差距主要靠短时 end-to-end adapt 弥补；当前只是小规模机制验证，不等同于同等算力或硬件加速收益。
