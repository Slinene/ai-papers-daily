---
title: 'SignRAG: Unified Retrieval-Augmented Gloss-Free Sign Language Translation'
title_zh: SignRAG：面向无标注手语翻译的统一检索增强框架
authors:
- Zhi Rao
- Yucheng Zhou
- Qianran Sun
- Yiqing Huang
- Longcan Yuan
- Jiayi Hou
- Chengwen Yao
- Lin Cheng
- Donghui Sun
- Xiaoxin Chen
affiliations:
- Macau University of Science and Technology
- University of Macau
- Institute of Automation, Chinese Academy of Sciences
- Yale University
- VIVO AI Lab
arxiv_id: '2610.11371'
url: https://arxiv.org/abs/2610.11371
pdf_url: https://arxiv.org/pdf/2610.11371
published: '2026-10-08'
collected: '2026-10-11'
category: Multimodal
direction: 手语多模态翻译 · RAG 与强化微调
tags:
- Sign Language Translation
- Retrieval-Augmented Generation
- Decoder-only LLM
- Reinforcement Fine-Tuning
- Multimodal Alignment
- Gloss-free
one_liner: 提出SignRAG，结合分层预训练、目标域检索增强与检索效用强化微调，首次在CSL-Daily全指标超越基于标注的手语翻译方法
practical_value: '- 将“目标域检索库”视为业务内高质量少样本池：为特定商品类目或活动页建立小型 retrieval gallery，推理时注入
  top-k 实例，可减少全量参数微调成本。

  - RUG-RFT 的“检索效用奖励”值得迁移：用质量+效用双 reward 训练模型分辨哪些检索结果是正/负干扰，可用于推荐解释生成、Agent 工具调用路径选择等场景。

  - 分层对齐思路可复用：先学习视觉/文本模态对齐，再与 LLM 联合训练，能缓解跨模态优化不平衡；在多模态商品表示接 LLM 时可参考。

  - 无 gloss 超越有监督结果说明：检索增强+弱监督可能替代昂贵结构化标注，在商品属性补全、Query 改写等任务中可尝试。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：Decoder-only LLM 在通用领域表现出色，但 gloss-free 手语翻译的预训练范式仍围绕 encoder-decoder 模型，无法直接迁移到 decoder-only LLM。

**方法关键点**：提出 SignRAG，包含三层设计：① 分层预训练——先学习语言学对齐的手语表示，再与 LLM 联合对齐，缓解跨模态优化不平衡；② 下游适配时，构建目标域检索库，为每个样本提供实例级翻译线索；③ 提出 Retrieval Utility-Guided Reinforcement Fine-Tuning (RUG-RFT)，用翻译质量与检索效用双 reward，鼓励模型利用有益检索、抑制有害依赖。

**关键结果**：在多个 SLT 基准上取得新 SOTA；尤其在 CSL-Daily 上，首次在所有报告指标上超越 gloss-supervised 方法。代码已开源。
