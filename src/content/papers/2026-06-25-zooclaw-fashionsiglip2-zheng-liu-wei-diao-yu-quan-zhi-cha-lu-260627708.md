---
title: 'ZooClaw-FashionSigLIP2: Distilled Fine-tuning for Robust Fashion Retrieval'
title_zh: ZooClaw-FashionSigLIP2：蒸馏微调与权值插值实现鲁棒时装检索
authors:
- Siqiao Xue
- Chunxue Xu
affiliations:
- ZooClaw.ai
arxiv_id: '2606.27708'
url: https://arxiv.org/abs/2606.27708
pdf_url: https://arxiv.org/pdf/2606.27708
published: '2026-06-25'
collected: '2026-07-01'
category: RecSys
direction: 视觉-语言模型蒸馏微调 · 时装检索
tags:
- VLE fine-tuning
- knowledge distillation
- WiSE-FT
- fashion retrieval
- multi-task contrastive
- benchmark quality
one_liner: Full fine-tuning + LwF 蒸馏 + WISE-FT 权值插值，在时尚图文检索中同时击败 LoRA、更大骨干和外部数据
practical_value: '- **Full FT + LwF + WiSE-FT 是比 LoRA 更稳的域适配方案**：对在电商搜索中微调 VLE 时，直接全量微调图像/文本编码器并配合知识蒸馏（冻结基座做
  teacher），再用 WiSE-FT 与 base 做权值插值，能在保住零样本泛化的同时大幅提升域内指标。LoRA 的低秩约束会迫使更新集中在少数方向，OOD
  下降明显。

  - **双查询多任务训练可覆盖真实搜索场景**：训练时同时构造短关键词（≤8 词，模拟用户搜索）和长描述（30–60 词，模拟详情页/QA），并用不同权重组合损失。对搜索推荐场景，可类似设计“短实时
  query”与“长上下文 query”双路训练，提升多意图覆盖。

  - **GCL 损失利用软标签缓解 batch 内假负例**：用 VLM 为图文对打分作为 graded relevance，通过 GCL 中权重项对高相关负样本降权，避免把相近款当严格负例推远。电商推荐中若有人工/半自动的款型相似度标签，可直接复用该思路。

  - **对 OOD 评估基准的偏差需主动审计**：论文发现 Fashion200k 的 ground truth 由 caption 来源图像构建，存在系统性偏向模型训练分布。工作中应警惕沿用公开基准的原始
  qrels，必要时可采用多模型池化 + LLM 重打分做无偏评估，避免指标虚高。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**
将基础视觉-语言编码器（如 SigLIP2）适配到时尚图文检索时，会面临域内性能与 OOD 泛化的根本权衡：生产环境不仅要服务训练集类目，还需应对不同查询风格的外部目录。同时，实际搜索流量中的查询多为短关键词，而多数 VLE 训练与评测依赖长自然语言描述，两者存在鸿沟。

**方法关键点**
- **全量微调 + 知识蒸馏**：放弃 LoRA，直接对图像/文本编码器做 full fine-tuning，用冻结的基座模型作为 teacher，在图像侧施加 LwF 损失（余弦距离），抑制灾难性遗忘。
- **多任务 contrastive 训练**：同时训练短查询（≤8 词）与长查询（30–60 词）两种检索任务，短查询通过随机丢弃属性并用 Gemma-4-31B 改写生成，长查询由完整属性集生成描述。损失使用 GCL，以 VLM 评分的分级相关性软标签下降低相关负样本权重。
- **WiSE-FT 权值插值**：微调后与基座模型的参数做线性插值（搜索 α∈[0,1]），选取同时在域内和 OOD 上高于最强基线的 α（本文选 α=0.4），以极小的工程代价获得“超越所有 baseline”的 sweet spot。
- **训练数据策划**：从商业目录构建 20 万–80 万对训练数据，利用 1355 个细粒度类目做 hard negative mining，避免引入外部数据带来的分布干扰（添加 Marqo-Fashion 数据反而下降）。

**关键结果**
在 ZooClaw-Fashion、H&M 和 Fashion200k 三个 benchmark 上，ZooClaw-FashionSigLIP2 在全部指标上领先或持平所有对比方法（Marqo-fashionCLIP、Marqo-fashionSigLIP、零样本 SigLIP2-base、LLM2CLIP）。特别在 Fashion200k 采用池化重评后（102K 标注），模型在 MRR@10 和 nDCG@10 上反超 Marqo-fashionSigLIP（原 benchmark 下曾落后 2.7pp R@10），揭示原 qrels 的 caption 来源偏差。LoRA 配置无一能在 Fashion200k 上达到基座水平，而增大骨干（最高 1B）也未提升 OOD。WiSE-FT 插值在 α∈[0.3,0.6] 内均能击败最强 baseline，方法鲁棒。
