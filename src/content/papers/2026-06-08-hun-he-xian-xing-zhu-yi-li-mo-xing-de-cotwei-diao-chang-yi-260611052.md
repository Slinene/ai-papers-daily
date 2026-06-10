---
title: 'Attention Amnesia in Hybrid LLMs: When CoT Fine-Tuning Breaks Long-Range Recall,
  and How to Fix It'
title_zh: 混合线性注意力模型的CoT微调长程遗忘及修复方法
authors:
- Xinyu Zhou
- Boyu Zhu
- Yi Xu
- Zhiwei Li
- Yingfa Chen
- Huiming Wang
- Zhijiang Guo
affiliations:
- LARK, HKUST(GZ)
- University College London (UCL)
- Mistral AI
- Tsinghua University
- Singapore University of Technology and Design (SUTD)
arxiv_id: '2606.11052'
url: https://arxiv.org/abs/2606.11052
pdf_url: https://arxiv.org/pdf/2606.11052
published: '2026-06-08'
collected: '2026-06-10'
category: Training
direction: 混合注意力模型的CoT微调退化分析与训练免费修复
tags:
- QK-Restore
- CoT-SFT
- hybrid linear attention
- long-context recall
- gradient locality
one_liner: CoT微调破坏混合模型的长距离召回，提出仅恢复 Q/K 投影的训练免方法QK-Restore，高效修复
practical_value: '- 若使用混合线性注意力模型（如 HypeNet、Jet-Nemotron）处理长上下文（例如多轮对话、长文档），在 CoT 推理微调后应监控检索退化，可直接用
  QK-Restore 方法恢复基座模型的 Q/K 投影权重，几乎零成本复原长程召回。

  - 观察到 CoT 序列的局部梯度偏向现象具有通用性，做 CoT SFT 时可通过冻结 Q/K 投影或使用 QK-Restore 修复，避免长上下文能力丢失，适用于将推理能力注入长上下文应用（如多步检索增强生成）。

  - 该修复手法仅替换 Q、K 矩阵，保留 V 和输出投影的微调增益，表明可以将“路由”与“内容提取”解耦，对混合模型架构设计有指导意义：部署时可分别管理路由和提取参数，进行差异化更新。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：混合线性注意力模型通过保留少数 softmax 注意力层实现高效长文本处理，常被蒸馏得到，随后需 CoT SFT 增强推理。本文发现 CoT SFT 会系统性地破坏模型的长距离召回能力（NIAH 测试），尤其在困难检索和更长上下文下退化显著（如 HypeNet-9B 在 NIAH-S2@256K 从 67.2% 跌至 9.4%）。这种退化具有结构化，主要影响负责长程路由的 Q/K 投影，而局部推理能力保留。

**方法关键点**：
- 将 CoT 推理序列建模为隐马尔可夫链，理论推导出梯度信号随 token 距离指数衰减，导致 Q/K 投影偏向短距交互。
- 提出训练免费的 **QK-Restore**：将微调后模型的 Q、K 投影矩阵替换回预训练（SFT 前）的对应矩阵，V 和其余参数保留微调后版本，从而恢复长程路由，保留推理增益。
- 进一步提出 **QK-Procrustes** 变体，在保证路由结构的前提下微调 Q/K，平衡路由保留和推理适应。

**关键实验与结果**：
- 模型：HypeNet 2B/5B/9B、Jet-Nemotron-2B。
- 数据：数学 CoT SFT（Miromind）和通用 CoT SFT（OpenThoughts-3）。评估：NIAH 单针/二针/三针，GSM8K、MATH500、LiveCodeBench。
- 退化后，QK-Restore 大幅恢复长文本检索（如 HypeNet-2B NIAH-S3@256K +19.6 pp，HypeNet-9B +19.8 pp），且数学/编码性能与 SFT 后模型相近，少数场景甚至超越预训练基线。
- 普通指令微调（非 CoT）不会引起类似退化，确认问题与 CoT 序列的局部依赖性相关。

**核心洞见**：CoT SFT 将 Q/K 投影的梯度信号局限在短距离，而 V 投影不受影响；只需替换 Q/K 权重即可解耦修复，无需重训练。
