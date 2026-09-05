---
title: 'SnapBench: Benchmarking Snap-and-Ask Multimodal Retrieval for Mobile Interactions'
title_zh: SnapBench：面向移动交互的拍问式多模态检索鲁棒性基准
authors:
- Zirong Chen
- Fuda Ye
- Kuan Zhang
- Enjun Du
- Junfu Pu
- Xinlei Wang
- Xinyu Zuo
- Lisheng Duan
- Jin Ma
- Yongqi Zhang
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Tencent Yuanbao
- Tsinghua University
- ARC Lab, Tencent
- The University of Hong Kong
arxiv_id: '2608.29607'
url: https://arxiv.org/abs/2608.29607
pdf_url: https://arxiv.org/pdf/2608.29607
published: '2026-08-29'
collected: '2026-09-05'
category: Eval
direction: 多模态检索鲁棒性基准与模态校准
tags:
- Multimodal Retrieval
- Robustness
- Benchmark
- Mobile AI
- Modality Fusion
one_liner: 首个配对的拍问式多模态检索鲁棒性基准，覆盖 1145 条查询、9085 个候选项和 53 种受控扰动，并提出自适应融合方法 MOOR。
practical_value: '- 在电商以图搜物/拍照问答场景，线上输入普遍存在图像模糊、短文本或拼写错误；可将 SnapBench 的 53 种受控 corruption
  方案作为离线鲁棒性评估模板，覆盖 blur/crop/low-light/typo/short query 等退化模式，用于回归测试检索模型。

  - 论文发现干净图像单独检索常优于图文联合检索，说明噪声输入下粗糙文本会拖累联合 embedding；工程上可引入输入质量信号（图像清晰度、文本长度、OCR 置信度）做
  modality gating，低质量文本时自动回退到图像检索。

  - MOOR 提供简单可复用的融合 trick：对单模态相似度分布做 outlier-aware 标准化，再按可靠性做最优加权；可直接叠加到现有多模态召回/排序的
  score fusion 层，提升 noisy 输入下的鲁棒性。

  - 图像 corruption 是主要性能瓶颈，文本 corruption 对联合检索影响有限；在资源有限时，优先投入图像质量检测与增强，而不是复杂的文本纠错。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**
移动 AI 中“拍照提问”式检索已成为高频入口，但真实用户输入中图像常模糊、文本常短小或拼写错误。现有基准只测干净输入，未系统隔离图像与文本扰动的配对鲁棒性影响。

**方法关键点**
构建 SnapBench：包含 1,145 条查询、9,085 个候选项，在 53 种受控 corruption 条件下（图像模糊/裁剪/低光等；文本短/拼写错误等）进行人工标注。评估 16 个多模态检索器，覆盖 dual-tower encoders 与 embedding-based VLMs。进一步提出 MOOR，一种 Modality-anchored, Outlier-aware, Optimal Reweighting 的自适应融合方法，基于模态可靠性对相似度得分重新加权。

**关键结果数字**
图像 corruption 显著降低检索性能；文本 corruption 主要影响纯文本检索，对联合检索影响有限。干净图像单独检索通常优于联合检索，揭示 coarse-text drag 和噪声输入下跨模态 fallback 不足。MOOR 有效提升鲁棒性，验证了可靠性感知的模态校准在 snap-and-ask 检索中的必要性。
