---
title: 'DataComp-VLM: Improved Open Datasets for Vision-Language Models'
title_zh: DataComp-VLM：改进视觉语言模型的开放数据集基准
authors:
- Matteo Farina
- Vishaal Udandarao
- Thao Nguyen
- Selim Kuzucu
- Maximilian Böther
- Andreas Hochlehnert
- Adhiraj Ghosh
- Marianna Nezhurina
- Karsten Roth
- Joschka Struber
arxiv_id: '2606.28551'
url: https://arxiv.org/abs/2606.28551
pdf_url: https://arxiv.org/pdf/2606.28551
published: '2026-06-25'
collected: '2026-07-07'
category: Multimodal
direction: 多模态数据筛选与混合策略基准
tags:
- VLM
- data curation
- multimodal pretraining
- benchmark
- scaling laws
one_liner: 数据混合而非过滤是提升VLM训练质量的关键，指令丰富混合可扩展性更优
practical_value: '- **数据混合优于过滤**：在构建电商多模态模型（如商品图文理解）时，应优先投入人力设计数据配比（例如指令数据 vs. 简单图文对），而非单纯用质量过滤丢弃数据。

  - **增加指令微调数据占比**：对于需要遵循指令的产品（如商品描述生成、多模态对话搜索），在预算内大幅提升指令格式样本的比例，能带来更好的下游任务扩展性，且收益随模型规模扩大而放大。

  - **复用 DCVLM 基准框架**：可将内部多源数据（用户评价图、商品主图、商品标题、问答对）组织成类似四类数据类型（图像-文本对、交错文档、纯文本、指令数据），利用其可插拔过滤/混合/采样接口做快速消融实验，找到最优数据配方。

  - **小预算探索大模型效果**：DCVLM 的低 token 预算轨道（如 6.25B）可用来预估不同数据策略在更大规模下的表现，适合资源有限的业务团队在迭代中提前淘汰劣化配方。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：当前社区缺乏系统性评估 VLM 训练数据管理策略的基准，导致难以量化不同筛选、混合、格式选择对下游性能的影响。

**方法**：构建 DataComp for VLMs (DCVLM) 基准，包含 160 个数据集、6T 多模态 token，覆盖图文对、交错文档、纯文本、指令数据四类。提供 1B-8B 模型规模与 6.25B-200B token 预算的受控实验赛道，下游评估涵盖 9 个领域 52 个基准。支持参与者对比过滤、混合、格式化、采样等策略。

**关键结果**：大规模实验揭示数据混合（而非过滤）是决定训练数据集质量的核心因素；富含指令的混合（instruction-heavy）相比富含简单图文的混合（caption-heavy）具有更好的可扩展性，随模型与数据规模增大，性能差距持续扩大。基于此设计的 DCVLM-Baseline 数据集，在 200B token 预算下将 8B VLM 在 33 个核心任务上的平均准确率提升至 63.6%，较之前最佳开放数据集 FineVision 提高 5.4 个百分点。
