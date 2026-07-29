---
title: 'TRACE: Business Rule-Grounded Reasoning Curriculum for Knowledge-Preserving
  Parametric Tool Retrieval in Enterprise LLMs'
title_zh: TRACE：基于业务规则的推理课程实现知识保留的参数化工具检索
authors:
- Sai Shruthi Sistla
- Ashutosh Hathidara
- Christopher Toukmaji
- Mayank Shrivastava
- Karthikeyan Asokkumar
affiliations:
- SAP Labs
arxiv_id: '2607.22639'
url: https://arxiv.org/abs/2607.22639
pdf_url: https://arxiv.org/pdf/2607.22639
published: '2026-06-21'
collected: '2026-07-29'
category: Agent
direction: 工具检索 · 业务规则推理 · 知识保存
tags:
- Parametric Tool Retrieval
- Business Rule Grounding
- Reasoning Traces
- Knowledge Preservation
- LoRA
- Enterprise LLM
one_liner: 通过两阶段课程与业务规则推理轨迹，在保持工具知识的同时实现单束解码的高召回工具检索
practical_value: '- **业务规则注入推理轨迹的方法可迁移至电商推荐/搜索**：将促销规则、禁售约束、新品权重等转化为“规则-推理-答案”训练数据，让模型在生成推荐或查询改写时显式引用规则，提升准确率和可解释性。

  - **两阶段课程设计可缓解微调遗忘**：先通过多格式记忆（LoRA）保持原始知识，再叠加推理增强任务，适合在推荐模型持续学习新业务规则时防止商品属性知识退化，确保工具/商品
  ID 的语义锚定。

  - **单束贪婪解码替代约束束搜索**：将推理过程融入生成，避免推理时前缀 trie 约束，大幅降低延迟（~200× 吞吐提升），可直接部署于实时搜索推荐系统。

  - **合成数据管道生成规则覆盖**：通过 LLM 将领域专家编写的业务规则转化为多样化查询-推理对（显式、隐式、异常三种风格），可在规则较少时快速扩充训练数据，适用于电商意图识别、多意图查询路由等场景。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
企业 AI 助手需将用户查询路由到数千个专用 API，传统嵌入检索在工具描述重叠、受业务规则约束的场景下召回率极低（~27%），且无法内化工具知识。参数化检索虽能提升召回，但会灾难性地破坏模型对工具的已学知识（MCQ、QA 探测准确率降至随机基线）。亟需一种既能保持工具知识、又能适应业务规则推理的检索方案。

**方法关键点**  
- **两阶段课程**：Stage 1 沿用 ToolSense 的多格式记忆 SFT（LoRA）将工具描述与虚拟 token 锚定，内化工具知识；Stage 2（核心贡献）让模型先推理后检索，生成思考轨迹（thinking trace）再输出 JSON 工具令牌列表。  
- **业务规则数据增强**：从 123 条领域专家规则生成显式、隐式、异常三种风格的用户查询，覆盖语义重叠工具集，强制模型在推理中引用规则。  
- **名字-令牌耦合**：训练时将轨迹中的工具名替换为虚拟 token，防止 token 与知识脱钩。  
- **合成数据流水线**：先由 RRB 管道生成多难度查询，再针对每条规则生成查询-推理对，最后通过程序化校验和 LLM 评判过滤低质量样本。  
- **推理时单束贪婪解码**：无需约束束搜索，直接生成轨迹和工具列表，大幅降低延迟。

**关键结果**  
在 HR 和 Finance 两个域共 8,283 个工具上，TRACE 相比嵌入基线（text-embedding-3-large）召回率从 27.5% 提升至 86.3%（Domain A，单束解码），Domain B 达 60.2%。较非推理参数化检索基线，推理训练使工具知识完整保持：MCQ 提升 3.2 pp，QA 提升 9 pp；业务规则数据进一步提升召回最多 23 pp。单用户延迟从 19.1 s 降至 1.9 s，吞吐量提升约 200×。**核心启示：在工具检索中引入业务规则推理轨迹，是兼顾高召回、知识保留与低延迟的有效路径。**
