---
title: Modality-Aware Expert Pruning for MoE-Based Multimodal Large Language Models
title_zh: 面向 MoE 多模态大模型的模态感知专家剪枝
authors:
- Donggeun Kim
affiliations:
- Nota Inc.
arxiv_id: '2611.05927'
url: https://arxiv.org/abs/2611.05927
pdf_url: https://arxiv.org/pdf/2611.05927
published: '2026-11-03'
collected: '2026-11-12'
category: Multimodal
direction: MoE 专家剪枝 · 多模态 LLM 压缩
tags:
- MoE
- expert pruning
- multimodal LLM
- model compression
- modality-aware
one_liner: 提出训练免费的 MAEP，按视觉/文本模态分解专家重要性，用 ΔH 与低注意力视觉 token 剪枝 MoE 专家
practical_value: '- 如果业务里部署多模态 MoE LLM（如视觉商品理解 + 文本对话），可直接采用训练免费的 MAEP 思路：单次前向按模态统计专家重要性，省去额外训练成本，压缩后能把
  58GB 模型放进 40GB GPU，显存降约 47%。

  - 视觉侧用低注意力视觉 token 计算重要性作为剪枝信号，文本侧重要性作为保留信号；该视觉信号在不同数据集上排名稳定，适合线上数据分布变化频繁的电商场景，不必频繁重剪。

  - ΔH 指标度量删除某专家后 MoE 输出的重分配变化，比单纯按激活频次或权重范数更贴近期望输出，工程实现时可以在 router 输出后重归一化剩余专家权重来近似计算。

  - 全局跨层排序专家重要性再剪枝，能避免逐层等比例剪枝导致某些关键层性能崩塌；在推荐/Agent 使用 MoE LLM 做 reasoning 或多模态特征提取时，可复用这种全局排序策略。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现代 MoE 多模态 LLM（如 InternVL3.5-30B-A3B、Qwen3-VL-30B-A3B）的专家参数约占模型总大小 90% 以上（约 58GB 中 54GB），但推理时每 token 只激活少数专家。现有专家剪枝方法对所有 token 统一聚合重要性，忽略同一专家在视觉与文本处理中可能扮演不同角色，导致压缩后多模态性能明显下降。

方法关键点：提出 MAEP，训练免费，只需要一次前向传播。核心是模态感知的专家重要性分解：文本侧重要性作为保留信号，视觉侧重要性作为剪枝信号。引入两个机制：1）ΔH 输出指标，度量移除某专家后 MoE 层输出因重分配产生的变化，避免仅看静态权重或激活频次；2）低注意力视觉 token 作为视觉剪枝信号，其在多个数据集上的专家重要性排名保持稳定，不依赖具体数据集分布。专家按全局跨层排序，统一决定剪枝比例。

关键结果：在三个 MoE 多模态 LLM 上，跨多模态与纯文本 benchmark 评估，MAEP 在多数多模态 benchmark 上优于模态无关剪枝基线，纯文本任务保持竞争力；BF16 专家权重显存减少约 27GB（约总内存 47%），使约 58GB 模型可放入单张 40GB GPU。
