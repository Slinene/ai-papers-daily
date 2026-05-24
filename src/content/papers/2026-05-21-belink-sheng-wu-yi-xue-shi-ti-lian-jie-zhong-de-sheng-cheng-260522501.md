---
title: 'BeLink: Biomedical Entity Linking Meets Generative Re-Ranking'
title_zh: BeLink：生物医学实体链接中的生成式重排序
authors:
- Darya Shlyk
- Stefano Montanelli
- Lawrence Hunter
affiliations:
- University of Milan
- University of Chicago
arxiv_id: '2605.22501'
url: https://arxiv.org/abs/2605.22501
pdf_url: https://arxiv.org/pdf/2605.22501
published: '2026-05-21'
collected: '2026-05-24'
category: RAG
direction: 生成式重排序 · 生物医学实体链接
tags:
- Entity Linking
- Generative Re-Ranking
- Instruction-Tuning
- RAG
- Biomedical NLP
- Open-source LLM
one_liner: 用指令微调的开源生成模型在重排序阶段实现集合式候选选择，准确率提升3-24%，推理更快。
practical_value: '- 电商商品实体链接（如商品名→标准SPU）可直接复用该方法：用指令微调的开源LLM替代传统BERT交叉编码器做候选重排序，尤其适合冷门实体。

  - 集合式指令格式：一次性输入多个候选，要求模型输出最佳匹配，减少推理轮次，降低在线延迟，适合高QPS场景。

  - 模块化检索-重排序架构：可灵活插拔不同检索器（稀疏/稠密），业务侧能快速验证不同召回策略与重排序器的组合。

  - 低成本部署：微调7B级模型即可达到甚至超越大模型效果，平衡准确率与推理成本，便于在资源受限的工业环境中落地。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：生物医学实体链接（BEL）虽引入大语言模型（LLM）取得进展，但计算效率低，难以实际部署。本工作关注重排序阶段，探索用开源生成模型替代常规判别式重排序器，以兼顾效果与速度。

**方法**：提出集合式指令微调（set-wise instruction-tuning）策略：将候选实体列表与提及上下文一同输入指令微调后的生成模型，要求模型直接生成正确概念ID。该方法一次处理多个候选，避免逐对打分的高开销。模型选用Flan-T5等开源架构，在多个BEL数据集上微调。此外，将生成式重排序器集成到模块化、端到端的BeLink系统中，支持灵活的检索与重排序配置。

**结果**：在多个生物医学实体链接基准（如MedMentions、NCBIDisease）上，准确率相对提升3%–24%，同时推理耗时比现有最佳系统显著缩短。消融实验证实集合式处理相比逐对排序在速度与效果上的优势。
