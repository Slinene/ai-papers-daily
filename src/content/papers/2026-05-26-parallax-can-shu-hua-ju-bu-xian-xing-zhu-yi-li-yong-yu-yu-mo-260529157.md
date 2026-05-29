---
title: 'Parallax: Parameterized Local Linear Attention for Language Modeling'
title_zh: Parallax：参数化局部线性注意力用于语言建模
authors:
- Yifei Zuo
- Dhruv Pai
- Zhichen Zeng
- Alec Dewulf
- Shuming Hu
- Zhaoran Wang
affiliations:
- Northwestern University
- Tilde Research
- University of Washington
arxiv_id: '2605.29157'
url: https://arxiv.org/abs/2605.29157
pdf_url: https://arxiv.org/pdf/2605.29157
published: '2026-05-26'
collected: '2026-05-29'
category: LLM
direction: 参数化局部线性注意力 · 架构优化器协同
tags:
- Efficient Attention
- Local Linear Attention
- LLM Pretraining
- Architecture-Optimizer Codesign
- Hardware-Aware
one_liner: 提出可扩展的参数化局部线性注意力 Parallax，通过硬件感知优化和架构-优化器协同，在 LLM 预训练上实现帕累托改进
practical_value: '- 若自研 LLM 或注意力模块用于召回/排序，可尝试 Parallax 的参数化局部线性注意力替代 softmax，预训练困惑度和下游迁移均有提升，且数值稳定。

  - 硬件感知优化：Parallax 的解码核设计提高了算术强度，在批次和上下文变化时稳定匹配 FlashAttention 2/3，可参考其融合策略降低推理延迟。

  - 架构与优化器协同：发现 Muon 优化器对 Parallax 至关重要，提示探索新架构时需配对特定优化器，否则可能无法释放潜力。

  - 局部线性估计在记忆检索任务上偏差-方差更优，对于需要强联想记忆的场景（如长序列用户行为建模）提供理论基础。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Softmax 注意力在联想记忆上使用局部常数估计，而局部线性注意力 (LLA) 可提供更优的偏差-方差权衡，但之前因计算和数值稳定性难以扩展至 LLM 预训练。

**方法**：提出 Parallax，参数化 LLA：移除数值求解器，学习额外的 query-like 投影器来探测 KV 协方差，统一带宽、探测和仿射结构。设计硬件感知算法提高算术强度，使解码核在多样条件下匹配或超越 FlashAttention 2/3。在 0.6B 和 1.7B 规模预训练，并发现 Muon 优化器是释放 Parallax 能力的关键。

**结果**：解码核性能与 FlashAttention 2/3 相当或更优；预训练困惑度持续改善（0.6B 和 1.7B），下游基准任务迁移增益明显；在参数匹配和计算匹配对比中均实现帕累托改进；首次实证注意力机制的架构-优化器协同设计。
