---
title: A Broader Look into MLLM's Retrieval Heads
title_zh: 多模态大模型检索头的拓展与优化
authors:
- Jia Wang
- Yuqing Li
- Jiangnan Li
- Zheng Lin
- Mo Yu
affiliations:
- Institute of Information Engineering, Chinese Academy of Sciences
- School of Cyber Security, University of Chinese Academy of Sciences
- Tencent
arxiv_id: '2610.32411'
url: https://arxiv.org/abs/2610.32411
pdf_url: https://arxiv.org/pdf/2610.32411
published: '2026-10-22'
collected: '2026-10-31'
category: Multimodal
direction: 多模态检索头机制与注意力优化
tags:
- Retrieval Heads
- Multimodal LLM
- Attention Optimization
- Audio-Visual Retrieval
- Document Retrieval
one_liner: 发现检索头在多模态模型中保持稀疏且跨模态共享，通过排序目标训练注意力可提升文档检索 Recall@1 6.03 点
practical_value: '- 在电商多模态商品理解中，可先定位模型的 retrieval heads（稀疏注意力头），针对性地做剪枝或稀疏推理加速，同时保留跨模态共享的不足
  2% 的关键头，避免文档理解、空间感知等能力下降。

  - 借鉴 ranking objective 训练特定注意力头的方法：构造正负证据对，只对检索头的注意力分布施加排序损失，配合文档 / 商品召回任务做轻量微调，可提升
  MMDocIR 等文档检索的 Recall@1。

  - 多模态模型中音频和视觉证据共享检索头，说明跨模态对齐可在注意力头层面实现，电商短视频、直播等音视频带货场景可复用此机制设计统一的召回模型，减少模态间冗余。

  - 消融实验显示跨模态共享的极少数头部影响多项能力，部署时可通过冻结这些头部或提高其权重稳定性，保障线上模型在多任务下的鲁棒性。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：以往研究将长上下文证据定位能力归因于检索头（retrieval heads），但分析局限于有限模态与对应模型，且如何利用检索头优化模型尚未充分探索。

**方法关键点**：
- 构造配对输入：同样答案以语音（spoken）或屏幕上显示（visual）呈现，另一轨保持不变，保证证据内容固定。
- 通过测量 question 到 needle 的注意力，减去无信息问题基线并平均，得到每头的检索分数，取 top 5% 作为检索头。
- 在 18 个语言、视觉语言、全模态 checkpoint 上验证：全模态模型基本保留其 backbone 的检索头，新模态下检索头仍稀疏且跨模态共享程度高。
- 消融这些头几乎消除音频-视觉检索；跨模态共享的不足 2% 的头还影响文档理解、空间感知和视觉数学。
- 基于发现，将检索头作为优化目标：用 ranking objective 训练其注意力分布，使问题正确关注证据 token。

**关键结果**：对 Qwen3-VL-8B 在 MMDocIR 数据集上，page Recall@1 提升 6.03 个百分点；在三个模型家族上文档检索均有改善。
