---
title: 'jina-reranker-v3.5: An Efficient Listwise Reranker with Hybrid Attention and
  Self-Distillation'
title_zh: jina-reranker-v3.5：基于混合注意力与自蒸馏的高效列表重排器
authors:
- Christina Nasika
- Feng Wang
- Antonis Krasakis
- Han Xiao
affiliations:
- Jina AI by Elastic
arxiv_id: '2607.18152'
url: https://arxiv.org/abs/2607.18152
pdf_url: https://arxiv.org/pdf/2607.18152
published: '2026-07-20'
collected: '2026-07-21'
category: RecSys
direction: 列表重排·混合注意力·自蒸馏
tags:
- listwise reranker
- self-distillation
- hybrid attention
- efficiency
- structured retrieval
- multilingual
one_liner: 0.6B列表重排器通过混合窗口/全局注意力与三阶段自蒸馏，在保持重排质量的同时大幅降低延迟并提升结构化数据理解
practical_value: '- **混合注意力用于重排器降延迟**：将全注意力改为 3L2G 滑动窗口+全局层交错，终端层保持全局，可显著降低 listwise
  重排的预填充延迟（最长序列下 1.56× 提速），适合电商搜索候选列表较长的场景。

  - **三阶段自蒸馏解决注意力模式不匹配**：先用全注意力训练教师，再用稀疏注意力适应学生，最后用排名/分数/状态/嵌入多层蒸馏回收性能。该范式可迁移到将大模型重排能力蒸馏进小模型或不同架构的部署模型。

  - **以失败模式驱动训练数据构建**：针对法律、金融、结构化等重排易失败领域，用 LLM 合成约束型查询与近重复硬负例，高频采样困难切片，有效提升 domain‑specific
  零样本性能（法律任务提升 14 点 nDCG@10），电商商品目录或知识图谱场景可直接复用此数据策略。

  - **结构化字段重排的增强方式**：对 JSON/表格数据生成约束条件→查询→字段扰动硬负例→LLM 打标，让模型学习字段级别的匹配而非表面词重叠，适用于电商属性筛选、表格数据的重排任务。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
列表重排器是智能体检索流水线的核心判别组件，但在生产环境中面临效率、领域鲁棒性与半结构化数据理解的综合挑战。jina‑reranker‑v3 虽以 LBNL（last‑but‑not‑late）交互实现交叉文档比较，但其全注意力机制导致长候选列表时计算成本高昂，且训练数据偏通用领域，在法律、医疗、结构化等垂直场景表现不足。

### 方法关键点
- **3L2G 混合注意力**：将 28 层 Transformer 的注意力模式改为 3 层滑动窗口（window=1024）后接 2 层全局层，并固定最后一层为全局层以满足 LBNL 的跨文档读出头，将局部层复杂度从 O(L²) 降至 O(L·w)。
- **失败模式驱动的多域训练数据**：针对法律、金融、医学、多语言及结构化检索的短板，合成约束型查询与近重复硬负例；结构化数据通过“采样约束→扰动字段→挖掘难负例→LLM 判定”循环生成训练样本。
- **三阶段自蒸馏**：Ⅰ）全注意力教师完全微调；Ⅱ）学生启用 3L2G 模式，先冻结非注意力层仅重训注意力投影，再全参微调适应稀疏信息路由；Ⅲ）冻结教师，用排名 KL、分数 MSE、隐藏状态 MSE、嵌入余弦距离以及辅助自监督损失（λ 均在 0.65 左右）等多层目标蒸馏，填补教师-学生性能差。

### 关键结果
- BEIR 零样本：nDCG@10 达 63.20，超过 v3 的 62.10 和 4B Qwen3‑Reranker‑4B（62.28），参数仅为后者的 1/7。
- Struct‑IR 控制池重排：相比 v3 提升 9.6 个绝对点（48.3 vs 38.7），在大部分子领域领先同体量模型。
- 法律域 RTEB：AILA‑Statute 提升 14.0 点，AILA‑Case 提升 11.7 点。
- 延迟：短序列（NQ）提速 1.22×，长序列（AILACasedocs）提速 1.56×。
