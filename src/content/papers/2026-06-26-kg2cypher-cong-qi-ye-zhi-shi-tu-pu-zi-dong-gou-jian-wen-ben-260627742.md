---
title: 'KG2Cypher: Data-Centric Pipeline for Building Enterprise Text-to-Cypher Systems'
title_zh: 'KG2Cypher: 从企业知识图谱自动构建文本到Cypher系统的数据驱动流水线'
authors:
- Minjun Choi
- Yerin Kim
- Junghyuk Seo
- Sujin Mo
- Hyemin Lee
- Youngjoong Ko
affiliations:
- Sungkyunkwan University
- NAVER
arxiv_id: '2606.27742'
url: https://arxiv.org/abs/2606.27742
pdf_url: https://arxiv.org/pdf/2606.27742
published: '2026-06-26'
collected: '2026-06-29'
category: Other
direction: Text-to-Cypher数据合成与模型微调
tags:
- Text-to-Cypher
- Data-Centric
- LoRA
- SFT
- Knowledge Graph
- Enterprise
one_liner: 利用图谱事实反向生成训练数据，结合候选感知SFT与LoRA高效微调，大幅提升企业级Text-to-Cypher执行准确率
practical_value: '- **合成训练数据**：从结构化知识图谱反向生成自然语言查询，可用于商品知识图谱的NL2Query数据增强，低成本构建搜索意图理解训练集。

  - **候选感知SFT格式**：在输入中加入召回实体列表，提高实体链接准确率，适合需要实体链接的对话式推荐或结构化查询场景。

  - **类条件schema提示**：按查询类别动态选择相关schema片段，减少prompt长度和噪声，提升多任务查询生成的推理效率和准确率。

  - **LoRA微调**：低成本适配领域专用模型，可在有限标注下快速提升Text-to-SQL/Cypher能力，适用于电商内部分析工具或Agent的图查询模块。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：企业内部知识图谱广泛用于搜索和分析，但构建自然语言转Cypher的接口成本高、缺乏训练数据。  
**方法**：提出KG2Cypher流水线，从现有KG自动合成训练数据。首先基于图事实构建可执行Cypher查询，再用LLM生成对应的自然语言问题；生成的Text-Cypher对经LLM评判和人工验证，并转化为候选感知的SFT格式（输入中包含候选实体）。服务时采用类条件schema提示、实体检索和LoRA推理。  
**结果**：在韩语企业场景（包含短搜索式查询和schema改写）中，LoRA SFT将执行结果F1在广播节目查询上从0.806提升至0.950，在公司查询上从0.70提升至0.92；在11类任务上，精确匹配率95.2%，执行率99.9%，执行结果F1达到0.964。
