---
title: Leveraging Low-Level Symbolic Competences for Unsupervised Grounding in Hallucination
  Detection
title_zh: 利用低层符号能力进行无监督扎根的幻觉检测
authors:
- Renato Vukovic
- Hsien-chin Lin
- Carel van Niekerk
- Benjamin Ruppik
- Michael Heck
- Shutong Feng
- Nurul Lubis
- Milica Gasic
affiliations:
- Heinrich Heine University Düsseldorf, Germany
arxiv_id: '2609.05025'
url: https://arxiv.org/abs/2609.05025
pdf_url: https://arxiv.org/pdf/2609.05025
published: '2026-09-04'
collected: '2026-09-08'
category: RAG
direction: 神经符号方法，SQL 落地检测幻觉
tags:
- hallucination detection
- neurosymbolic
- SQL grounding
- unsupervised
- RAG
- LLM
one_liner: 让 LLM 用 SQL 构建参考文档数据库，以神经符号方式无监督检测生成响应中的幻觉，无需领域微调
practical_value: '- 在电商/广告生成式推荐中，可将商品知识库、广告素材或用户评价等参考文档预先转换为 SQL 表，然后用 SQL 查询校验 LLM
  生成的推荐理由、商品描述或客服回答是否忠于原文，低成本的线上幻觉检测无需标注数据。

  - 利用 LLM 的低层符号能力（SQL/JSON 查询）作为 grounding 工具，比直接让 LLM 判断幻觉更可解释、稳定，且不依赖领域微调，适合快速迁移到不同商品类目。

  - 神经符号 pipeline 可拆分为「文档→SQL 数据库构建」和「基于 SQL 的声明验证」两步，工程上可以并行或缓存数据库，适用于实时校验。

  - 适合对事实一致性要求高的场景，如生成商品参数、价格、促销信息等，可避免编造属性导致的客诉或合规风险。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM 幻觉检测困难，因为其推理过程不透明，难以判断输出是否由参考文档支持；现有方法常需领域微调或大量标注，难以泛化。

**方法**：利用 LLM 已有的低层符号能力——SQL——构建无监督幻觉检测 pipeline。具体地，让 LLM 从参考文档中提取事实并构建 SQL 数据库；然后基于该数据库对参考文档和生成的响应进行 SQL 推理，执行“神经符号检查”（neurosymbolic checkup）：若响应中的陈述无法在数据库中找到支持，则标记为幻觉。整个过程无需领域特定微调，只依赖 LLM 的一般 SQL 能力。

**结果**：在 RAGTruth 和 DiaHalu 幻觉检测数据集上，该方法优于直接让 LLM 预测幻觉的 baseline，并与现有 SOTA 方法竞争，同时不需要领域微调。作者认为这证明了 LLM 低层符号能力在神经符号方法中的价值，值得进一步探索。
