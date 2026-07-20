---
title: Loop the Loopies!
title_zh: Loopie：循环MoE Transformer超越普通模型的计算匹配扩展法
authors:
- Zitian Gao
- Yilong Chen
- Yihao Xiao
- Xinyu Yang
- Ran Tao
- Joey Zhou
- Bryan Dai
affiliations:
- IQuest Research
arxiv_id: '2607.16051'
url: https://arxiv.org/abs/2607.16051
pdf_url: https://arxiv.org/pdf/2607.16051
published: '2026-07-16'
collected: '2026-07-20'
category: LLM
direction: 层循环MoE架构 · 计算匹配预训练扩展
tags:
- Looped Transformer
- MoE
- Layer-loop
- Compute-matched scaling
- SPT
- RL Reasoning
one_liner: 提出层循环MoE架构与计算匹配扩展方案，在相同预训练计算量下首次超越非循环大模型。
practical_value: '- **层循环(layer-loop)设计**：逐层迭代再传递，降低激活内存，允许更大micro batch。可迁移到推荐系统中特征交互或序列建模的深层Transformer，在内存受限时用循环换取有效深度。

  - **计算匹配扩展方法**：从参考模型先减层加循环，内存节省后增大batch size，再投资到宽度上。在业务中可按此思路在给定推理预算下最大化模型容量，尤其适合电商搜索粗排/精排模型的轻量化设计。

  - **监督预训练(SPT)**：用预训练尺度（大批量、长序列、多轮次）做有监督微调，同时提升通用知识和推理能力，避免灾难性遗忘。可借鉴到业务LLM适配，用大规模业务数据做SPT保持基座能力。

  - **循环推理与RL结合**：多步循环为推理提供了迭代优化空间，配合分组序列策略优化(GSPO)提升复杂任务规划。可启发Agent在多步决策中引入内循环推理，增强长期规划能力。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
循环Transformer因可复用深度而受到关注，但此前研究未解决核心挑战：在相同预训练计算量下，循环模型通常不如直接增加参数的非循环模型。同时，现代大模型普遍采用MoE，如何将循环与MoE结合并实现计算匹配的扩展是尚未探索的关键问题。

## 方法关键点
- **层循环（layer-loop）**：与传统模型循环不同，Loopie在每个层内执行多次循环再传入下一层，提高了执行局部性，形成更自然的参数共享模式，且实测性能在训练后期超越模型循环。
- **Loopie 扩展方案**：以Qwen3-MoE为参考，将存储层数减半并设置循环次数=2，利用激活内存减半带来的micro batch加倍，将效率增益再投资到扩大宽度上（如hidden dim增大），最终匹配参考模型的每步训练时间。
- **预训练与后训练**：预训练分两阶段，第一阶段多轮训练于高质量数据(Nemotron-CC-v2-HQ)，第二阶段使用1.26T token的高质量退火数据（含SFT、STEM、代码等）。后训练引入**监督预训练(SPT)**，用2T token的SFT数据进行大规模批训练，克服灾难性遗忘；随后用**GSPO+动态过滤**的强化学习在数学和代码任务上提升推理能力。

## 关键结果
- 在相同预训练计算预算下，Loopie-20B-A2B（2B活跃）在8项基准上平均超过Qwen3-30B-A3B（3B活跃)基线，训练吞吐量提升约38%（261.5 vs 189.6 TFLOPS/s）。
- 在AIME、AMC、OlympiadBench等推理基准上，Loopie-20B-A2B达到90%以上的准确率，并在2025 IMO和IPhO上取得金牌水平（无工具）。
- 消融实验显示，层循环相比单纯增加计算量的无循环变体有显著提升（例如Loopie-6B-A0.6B相对无循环版本提升明显）。
- SPT阶段在2T token上持续提升MMLU、ARC等通用指标，同时大幅增强推理能力，证明大规模监督微调可同时避免遗忘。

一句话：**通过层循环和计算匹配扩展，Loopie首次证明循环MoE模型可在相同预训练计算量下超越非循环大模型，并达到竞赛级推理性能。**
