---
title: The Answer Path and the Grounding Instruction in LLM Question Answering over
  Knowledge Graphs
title_zh: LLM 知识图谱问答中的答案路径与 grounding 指令
authors:
- Arquimedes Canedo
affiliations:
- Siemens Digital Industries Software
arxiv_id: '2609.10237'
url: https://arxiv.org/abs/2609.10237
pdf_url: https://arxiv.org/pdf/2609.10237
published: '2026-09-09'
collected: '2026-09-11'
category: RAG
direction: GraphRAG · 上下文构建与评估
tags:
- GraphRAG
- Knowledge Graph QA
- Grounding Instruction
- Retrieval Recall
- Evaluation Methodology
one_liner: GraphRAG 中答案路径是否出现决定性能，grounding 指令在无事实时使 F1 降 8.63 倍；语法/顺序/大小无影响
practical_value: '- GraphRAG 工程优先保证答案路径/关键事实的召回，而非上下文中全部三元组的精度：在固定三元组数量下替换非路径三元组为无关实体，F1
  仅 +0.003，但缺失答案路径损失大部分图谱价值；检索预算应投高召回、允许低精度。

  - 避免在 prompt 中加入“只使用提供的事实”这类 grounding 指令，除非确认所有必要事实都在上下文中：无事实时该指令使 F1 从 0.299 降到
  0.035（8.63 倍）。在检索不完整的 RAG 场景中，此类严格限定会严重损害回答质量。

  - 评估 GraphRAG 时注意实验公平性：若只对图谱上下文分支加 grounding 指令、不对无上下文基线加，会虚假得出“图谱上下文有害”结论；作者在自己的结果中发现并撤回。业务评估应统一指令设置。

  - 错误子图不易被 LLM 察觉，知识库写入路径是提示注入攻击面；电商知识图谱（商品属性、活动规则）更新时需要校验来源，防止恶意或错误三元组污染回答。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：GraphRAG pipeline 的上下文构建涉及多个选择——哪些三元组、用什么语法、顺序、给模型的指令，但各因素对最终 QA 的影响未被单独测量。

**方法**：用 6 个 LLM 和 2 个 KGQA 基准，子图来自 gold SPARQL（无检索器），分别变化：是否包含答案路径、grounding 指令、三元组语法、三元组顺序、子图大小。

**关键结果**：①答案路径是否出现在 prompt 中是最大因素。保持三元组数量不变、把非路径三元组替换为无关实体，F1 仅 +0.003；但移除答案路径损失大部分图谱价值——检索预算应投给召回，精度在测试范围内无收益。②grounding 指令在无事实时：要求模型只使用提供的事实，F1 从 0.299 降到 0.035（8.63 倍），该数字来自空上下文臂；若只对上下文臂加指令、不对无上下文基线加，会虚假得出图谱上下文有害的结论，作者发现并撤回。③语法、三元组顺序、子图大小在多跳深度无显著影响。④错误子图不易被模型检测，知识库写入路径具有提示注入攻击面。
