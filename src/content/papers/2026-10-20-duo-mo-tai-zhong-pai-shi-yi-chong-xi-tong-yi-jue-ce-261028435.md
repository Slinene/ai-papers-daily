---
title: Multimodal Reranking Is a System One Decision
title_zh: 多模态重排是一种系统一决策
authors:
- Zhuchenyang Liu
- Yao Zhang
- Yu Xiao
affiliations:
- Aalto University
arxiv_id: '2610.28435'
url: https://arxiv.org/abs/2610.28435
pdf_url: https://arxiv.org/pdf/2610.28435
published: '2026-10-20'
collected: '2026-10-21'
category: RecSys
direction: 多模态检索重排 · System One 决策
tags:
- Multimodal Reranking
- System One Decision
- VLM
- Zero-shot Reranking
- Decision Tuning
one_liner: 将多模态重排转化为System One选择题，通用VLM一次前向读logits排序，零样本超越专用小模型，文本决策微调有增益
practical_value: '- 在电商多模态商品重排中，可用选择题范式替代逐候选打分：将 query 与 top-k 候选图/描述组成一个多选项 prompt，让通用
  VLM（如 Qwen3-VL）一次前向输出每个选项 token 的 logits 作为排序分数，比逐对 yes/no 更快且 hit@1 更高。

  - 零样本通用大模型可替代专用重排小模型：若业务数据覆盖较广，直接使用通用 VLM 零样本重排，通常能超过有监督小 reranker，减少标注和训练成本；工程上可放在第二级重排或高价值流量。

  - 用纯文本决策数据微调决策能力：即使没有多模态重排标注，也可构造纯文本选择题数据对 VLM 做 decision tuning（如 JEV），提升页面重排等任务，自然图像任务保持稳定，适合快速冷启动。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：传统多模态重排依赖专用模型逐候选打分或列表式重排，训练成本高。System One 决策模型（如 JEV）将状态和问题映射为选项概率，无需生成文本，通用 VLM 具备此能力，可零样本用于重排。

**方法**：将重排转化为选择题：query 与 top-16 候选组成一个多选项 prompt，VLM 单次前向取每个候选标签的 logits 作为排序分数；另探索文本决策微调（decision tuning）提升效果。

**结果**：在 MMEB-V2 图像检索上，选择题比逐候选 yes/no 高 5.4-7.3 hit@1，yes/no 甚至低于第一阶段。零样本 Qwen3.8-27B 在三个基准上均超过有监督 Qwen3-VL-Reranker-2B，与 Reranker-8B 差距≤1.6 点；在视觉文档任务上追平 Reranker-8B（84.79 vs 84.78 nDCG@5），延迟为其 1.1-1.5 倍。JEV-27B-VL 经纯文本决策微调后，页面重排提升 0.6-1.1 点（符号检验 p≤0.017），自然图像无显著变化。作者指出模型大小和代际差异可能混淆比较，需进一步实验验证。
