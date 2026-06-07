---
title: 'Code2LoRA: Hypernetwork-Generated Adapters for Code Language Models under
  Software Evolution'
title_zh: Code2LoRA：面向软件演化的超网络生成代码适配器
authors:
- Liliana Hotsko
- Yinxi Li
- Yuntian Deng
- Pengyu Nie
affiliations:
- University of Waterloo
arxiv_id: '2606.06492'
url: https://arxiv.org/abs/2606.06492
pdf_url: https://arxiv.org/pdf/2606.06492
published: '2026-06-03'
collected: '2026-06-07'
category: Training
direction: 参数高效微调 · 超网络生成 LoRA
tags:
- Hypernetwork
- LoRA
- Code Language Model
- Software Evolution
- PEFT
one_liner: 用超网络为代码仓库动态生成 LoRA 适配器，零推理 token 开销注入库级知识，支持静态与演化场景。
practical_value: '- **为不同场景动态生成 LoRA**：超网络可推广到电商推荐中，为不同用户群、商家或商品类目生成专属 LoRA，避免为每个实体独立微调，节省存储与训练成本。

  - **零推理 token 开销注入知识**：生成的适配器直接融合到基座模型，推理时无额外上下文拼接，适合延迟敏感的推荐重排或 Agent 调用。

  - **进化机制应对分布漂移**：GRU 隐藏状态按 commit 更新适配器，类似可用于在线学习场景，持续跟踪用户兴趣变化或商品趋势，低成本保持模型新鲜度。

  - **基准与评估框架**：RepoPeftBench 的构建思路可借鉴到电商领域，构建包含不同商家、不同时期的 PEFT 评估基准，量化个性化与迁移能力。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：代码语言模型需要仓库级上下文解析导入、API 和项目约定。现有方法要么通过 RAG 注入长文本，推理 token 消耗大；要么为每个仓库微调 LoRA，成本高且无法应对代码持续演化。

**方法**：提出 Code2LoRA，用超网络将仓库内容编码为 LoRA 权重，实现零推理 token 开销注入仓库知识。支持两种模式：静态（Code2LoRA-Static）将仓库快照生成适配器，适合稳态代码理解；演化（Code2LoRA-Evo）使用 GRU 隐藏状态按代码 diff 更新适配器，适合活跃开发场景。构建 RepoPeftBench 基准，含 604 个 Python 仓库，静态任务 40K 训练 / 12K 测试，演化任务 215K 训练 / 87K 测试。

**关键结果**：静态轨道，Code2LoRA-Static 跨仓库 exact match 达 63.8%、仓库内 66.2%，与独立 LoRA 上限持平；演化轨道，Code2LoRA-Evo 跨仓库 exact match 60.3%，超越单一共享 LoRA 5.2 个百分点。
