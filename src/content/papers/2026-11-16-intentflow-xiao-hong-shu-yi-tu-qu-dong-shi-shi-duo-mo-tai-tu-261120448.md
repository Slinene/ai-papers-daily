---
title: 'IntentFlow: An Intent-Driven Real-Time Multimodal Search System with Image-Text
  Queries at Xiaohongshu'
title_zh: IntentFlow：小红书意图驱动实时多模态图像-文本搜索系统
authors:
- Dongjia Zhao
- Yuchen Ma
- Chunsheng Shi
- Ziqiu Gui
- Chao Yuan
- Jianing Zhu
- Zhaoxing Zhang
- Yahui Liu
- Daoxin Zhang
- Yi Wu
affiliations:
- Xiaohongshu Inc
arxiv_id: '2611.20448'
url: https://arxiv.org/abs/2611.20448
pdf_url: https://arxiv.org/pdf/2611.20448
published: '2026-11-16'
collected: '2026-11-17'
category: Multimodal
direction: 意图驱动的多模态搜索 · 工业部署
tags:
- intent modeling
- multimodal retrieval
- reranking
- agentic data construction
- image-text query
- industrial search
one_liner: 构建分层意图体系统一数据标注、召回与重排，在小红书十亿级索引上实现意图驱动的多模态搜索
practical_value: '- 将检索意图做成层级 taxonomy，并用 intent-specific relevance criteria 统一数据标注、召回和重排；在电商搜索中可把“找同款/搭配/属性变体/信息问答”分开定义正样本，避免视觉相似但意图不符的候选污染。

  - Agentic 数据构造：用 agent 验证候选是否满足意图条件，unknown 不直接当负样本、模糊样本送人审；对电商多模态标注有参考价值。

  - 固定 doc index + query-side LoRA/残差投影更新，避免全量 re-embedding 成本；适合千万/亿级商品库频繁迭代 embedding
  模型。

  - 重排用 compact 0.8B 多模态生成模型预测 0/1/2 分级标签，按 grade 排序，同 grade 内走原有策略；比精细分数更易控且工程友好。

  - 图像 cache + 离线处理降低 tail latency；CSLS 校正 embedding hubness。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
多模态 image-text query 搜索中，同一参考图不同问法需要不同证据，视觉相似不等于满足意图；仅重排视觉召回会漏掉真正相关笔记。需要显式意图建模统一召回和重排。

**方法关键点**
- 定义层次意图 taxonomy：第一层 Visual Search / Information Seeking / Unclear，第二层七类（Item Search, Image Search, Attribute Variant Search, Outfit Styling, Target-Specific Info, Transferable Info）。同一 query-candidate 在不同意图下给不同 0/1/2 分级标签。
- Agentic 数据构造：用 agent 验证意图、构造正负样本、收集证据，unknown 不直接当负，模糊样本人审。产生 graded labels 和 hard negatives。
- 嵌入模型：意图感知对比学习 + hard-negative margin + graded ranking（NDCG 加权的 pairwise loss）+ 从 2B teacher 蒸馏到 0.8B student。doc index 固定，query 侧用 LoRA + residual projection（6 experts, bottleneck 8/64）适配，避免重索引；CSLS 校正。
- 重排器：0.8B 多模态生成模型，输入 query-candidate 证据 + 预测意图，输出 relevance grade 0/1/2；两个 teacher 标注，不一致时第三个裁决。在线按 grade 降序，同 grade 内用原有策略。

**关键实验**
- 在线 A/B：相比 visual search + rerank 控制组，增加意图识别+重排后 Top-4 QCTR +21.65%，QCTR +15.12%，时长 +9.66%；再加多模态检索后 Top-4 QCTR +28.17%，QCTR +18.96%，时长 +12.56%。P50 latency 1.07s，P90 1.34s。
- 意图识别 0.8B 学生：一/二级准确率 95.90/91.54，macro-F1 91.63，接近 teacher。
- 检索评估：20k queries，在 0.5M/1.9M 两个 gallery 上，以 grade 2 为 positives，衡量 Hit@1/10/100, Recall@100, NDCG@10。

**最值得记住的一句话**：把“用户想要什么结果”先定义成层级意图和检索证据，再用同一套 graded relevance 标准驱动数据、召回和重排，才能让多模态搜索从“像不像”升级到“满不满足”。
