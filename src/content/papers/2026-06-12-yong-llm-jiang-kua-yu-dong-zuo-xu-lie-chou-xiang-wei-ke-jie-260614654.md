---
title: Abstracting Cross-Domain Action Sequences into Interpretable Workflows
title_zh: 用 LLM 将跨域动作序列抽象为可解释的工作流
authors:
- Gaurav Verma
- Scott Counts
affiliations:
- Microsoft Corporation
arxiv_id: '2606.14654'
url: https://arxiv.org/abs/2606.14654
pdf_url: https://arxiv.org/pdf/2606.14654
published: '2026-06-12'
collected: '2026-06-15'
category: LLM
direction: 基于LLM的跨域行为序列抽象与用户意图理解
tags:
- action sequence abstraction
- LLM
- hierarchical prompting
- intent understanding
- zero-shot
- few-shot
one_liner: 提出 WorkflowView，通过 LLM 层次化提示将低级操作日志转为高级活动描述，零/少样本实现跨域意图理解和分类。
practical_value: '- **用户行为理解与意图推断**：电商中用户点击、浏览等动作序列可用 WorkflowView 分层生成自然语言描述，直接推断购物意图（如比价、找风格），替代传统规则或监督分类，提升实时推荐的上下文感知能力。

  - **冷启动场景的少样本分类**：仅需每个类别 5 个示例即可达到与全量训练模型竞争的退课预测（F1=0.90），可快速迁移到电商评论意图分类、用户流失预警等任务，大幅降低标注成本。

  - **可解释的中间表示**：Layer1 的自然语言描述可作为可解释的行为表示，直接用于生成推荐解释或输入下游排序模型，增强推荐理由的透明度和可信度。

  - **多模态扩展启示**：文中提出结合 UI 截图进行行为理解，电商场景下可融合商品图片、页面布局等视觉信息，构建更丰富的用户状态建模，为 Agent 主动服务提供实时上下文。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**

用户数字应用交互日志以海量、细粒度、高噪声的动作序列形式存在，难以直接从中提取高级任务信息。传统模式挖掘或序列建模方法依赖大量标注数据，跨领域泛化能力弱。为高效、通用地将底层操作日志转化为可解释的高级活动，论文提出利用大语言模型（LLM）的零/少样本推理能力进行层次化抽象。

**方法关键点**

- **WorkflowView 框架**：设计三层 LLM 提示链，Layer1 将时间戳动作序列转为自然语言描述（去噪），Layer2 从描述中推断简洁的高级活动摘要，Layer3 可选地将活动分类到发现或预定义的类别（支持二分类、多分类）。
- **模块化与渐进去噪**：分层设计实现输出复用和逐步降噪，使高层分类仅需适配最后一层。
- **零/少样本泛化**：无需微调，通过提示中插入少量示例即可适应新领域和新任务。

**关键实验与结果**

- **浏览器任务推断**（Mind2Web 数据集，2,022 个任务）：零样本生成的任务描述与真值语义相似度均值 0.91，全局检索 MRR=0.90，Recall@1=0.86，效果显著超越 LSTM/BERT seq2seq 微调基准。
- **MOOC 退课预测**（Feng et al. 数据集，67,699 条注册记录）：仅用每类 5 个示例（共 10 个）时，加权 F1 达到 0.90（精准率 0.83，召回率 0.98），与使用数十万训练样本的基线方法（CFIN F1=0.91，LSTM-based F1=0.87）持平。
- **Microsoft Word AI 工具使用分析**（50k 用户随机样本）：基于行动日志发现“主动内容编辑”为使用 AI 前后的最高频活动，且 AI 接受后格式化活动比例上升，为产品改进提供可操作洞察，同时保障用户隐私。

**最值得记住的一句话**：LLM 通过层次化提示可将低层动作序列转化为可解释的高级活动，在零/少样本、跨域场景下与监督模型性能相当，且兼具模块化部署和隐私保护的优点。
