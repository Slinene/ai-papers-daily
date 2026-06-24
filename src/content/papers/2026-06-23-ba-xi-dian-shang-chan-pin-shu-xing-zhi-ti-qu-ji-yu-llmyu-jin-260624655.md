---
title: 'AI-PAVE-Br: Leveraging Large Language Models for Enhanced Product Attribute
  Value Extraction through a Golden Set Approach'
title_zh: 巴西电商产品属性值提取：基于LLM与黄金标注集的方法
authors:
- Murilo Gazzola
- Hugo Gobato Souto
- Samuel Silva
- Júlia Schubert Peixoto
- Felipe Siqueira
- André Luis Pedroso de Morais
- Caio Gomes
affiliations:
- LuizaLabs
- Mackenzie Presbyterian University
- University of São Paulo
arxiv_id: '2606.24655'
url: https://arxiv.org/abs/2606.24655
pdf_url: https://arxiv.org/pdf/2606.24655
published: '2026-06-23'
collected: '2026-06-24'
category: RecSys
direction: LLM赋能属性提取 · 巴西电商
tags:
- PAVE
- LLM
- Prompt Engineering
- Golden Set
- Brazilian Portuguese
- E-commerce
one_liner: 用精心设计提示词的LLM代替传统NER，在巴西葡语商品属性提取上F1提升约15个百分点
practical_value: '- **用LLM+提示工程直接做商品属性提取**：无需微调，为每个品类定制提示词（任务说明、上下文、输出JSON格式、few-shot示例），可快速替换传统NER，特别适合多品类、多语种电商快速迭代。

  - **构建黄金标注集的方法论**：使用Cochran公式确定每类产品的样本量（95%置信度、5%误差，约385条），20个品类共覆盖数十万产品，可作为评估模型质量的无偏基准，也适合作为业务内部模型评测的固定验证集。

  - **结构化输出设计**：提示词中明确要求JSON输出，下游可直接解析入属性库、供搜索/推荐使用；对电压、尺寸等多值或歧义属性，提示词中需提供具体格式和示例，可大幅减少后处理。

  - **工程部署考量**：文中对比了自托管开源模型（VM部署，可预见延迟和成本）与闭源API（Gemini 2.5 Flash-Lite，1000并发请求平均1.3s但偶发30s）。推荐高吞吐场景优先自托管，避免API延迟波动和rate
  limit。

  - **属性标准化仍是痛点**：同一属性存在多种写法（“bivolt”“110/220V”），LLM虽能提取但一致性不足，建议后续增加规则或正则规范化层，或对LLM施加更严格的输出格式约束。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：巴西电商产品描述语言多样、不规范，传统NER或规则系统难以应对新品类和口语化表达，导致搜索、推荐、分类等下游任务数据质量差。急需一种可泛化、高精度的属性值提取方案，同时需要可复用的评测基准。

**方法关键点**：
- **Golden Set构建**：12人团队手动标注20个品类，每个品类按Cochran公式计算样本量（约385条），形成高置信度、低偏差的标注数据集，公开在GitHub。
- **LLM方案**：选用Gemini 1.5 Flash，为每个实体设计定制提示词，包含任务指令、输入字段（标题、描述、规格等）、期望输出（JSON形式）和few-shot示例，直接完成属性key-value抽取。
- **对比基线**：传统内部NER系统，在同一Golden Set上评估。

**关键结果**：
- 平均F1：传统基线59.79% → LLM方案74.68%，提升约15个百分点。
- 平均覆盖率：传统基线46.71% → LLM方案71.96%，表明LLM更少出现空预测。
- 仍低于理想覆盖率83.96%，主要因属性格式不统一（电压、尺寸等）和歧义导致提取困难。

**核心结论**：针对巴西葡语电商，用LLM加精心设计的提示词可大幅超越传统NER方法，但属性值标准化仍是实用化关键瓶颈。
