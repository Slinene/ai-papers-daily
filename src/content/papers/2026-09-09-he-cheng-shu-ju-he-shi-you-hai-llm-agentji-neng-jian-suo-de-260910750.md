---
title: 'When Synthetic Data Hurts: On Catastrophic Forgetting in Skill Retrieval for
  LLM Agents'
title_zh: 合成数据何时有害：LLM Agent技能检索中的灾难性遗忘
authors:
- Syed Shariyar Murtaza
- Yifan Nie
- Utkarsh Soni
- Eugene Wen
- Arvid Frydenlund
affiliations:
- Manulife
arxiv_id: '2609.10750'
url: https://arxiv.org/abs/2609.10750
pdf_url: https://arxiv.org/pdf/2609.10750
published: '2026-09-09'
collected: '2026-09-11'
category: RAG
direction: LLM Agent 技能检索 · LoRA 遗忘缓解
tags:
- Catastrophic Forgetting
- Synthetic Data
- Skill Retrieval
- LoRA
- Bi-Encoder
- Reranker
one_liner: 在34,396技能规模上，朴素LoRA合成数据微调会遗忘真实/OOD任务；保守正则可保持OOD并提升分布内召回13.98%。
practical_value: '- 在电商/广告召回或相关性模型微调中，真实点击/转化标注通常远少于曝光；若用LLM合成训练样本，优先选择低秩保守LoRA（如r=8、attn-only、lr=5e-6）并加LwF/EWC/anchor/L2-init正则，可降低真实流量OOD掉点风险。

  - 上线评估必须拆OOD真实query：不能只看合成集指标。论文中激进LoRA在合成Ring提升，但真实Ring 3 Recall@10从0.850跌至0.650；因此要单独监控自然流量、长尾类目、未参与训练的场景。

  - 轻量0.6B bi-encoder在技能检索上可匹配4B+BM25 hybrid（HIT@10=0.907），搜索/推荐召回侧可用小模型+FAISS降低成本；微调稳定性主要由LoRA
  rank控制，anchor weight影响较小，优先调rank。

  - retriever与reranker分数融合可采用per-query min-max归一化后线性加权α；BM25等稀疏召回用RRF融合，避免不同分数尺度校准问题。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：LLM Agent 在运行时依赖外部技能检索，技能库规模达34,396；真实标注稀缺，业界常用LLM合成数据微调检索模型。问题是合成数据微调可能带来灾难性遗忘，真实/OOD场景召回显著退化。

方法关键点：
- 数据：Track A 由1,669个anchor-skill合成任务与候选技能组成，单正样本；Track B 混合157条真实、4,256条paraphrase、8,858条skill-first合成，正样本加权并经过LLM质量门。
- 模型：Qwen3-Embedding-0.6B bi-encoder + Qwen3-Reranker-0.6B，LoRA微调；对比frozen 0.6B、4B+BM25 hybrid。
- 遗忘缓解：embedding anchor、L2-init、EWC、LwF；reranker用listwise LwF正则。
- 评估：75任务真实pool、Ring1/2/3、BEIR 6个OOD数据集。

关键结果：
- 激进LoRA在真实Ring 3 Recall@10从0.850跌至0.650；Track A中real-only Recall@10=0.607，加合成后降到0.586。
- 四种正则方法均保持OOD表现（Ring 3=0.850），同时Ring 2从frozen 0.534提升到0.608，相对+13.98%。
- 最终正则化retriever + LwF reranker融合在75真实任务达h@5=0.893、MRR=0.780。

最值得记住：真实/OOD评估必须与合成分布指标并列，低秩保守正则是让合成数据微调可上线的关键。
