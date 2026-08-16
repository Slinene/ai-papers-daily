---
title: 'HybridRAG-BN: A Retrieval-Augmented Framework with Fine-Tuned Verification
  for Bangla KBQA'
title_zh: HybridRAG-BN：面向孟加拉语KBQA的检索增强与微调验证框架
authors:
- Rathijit Aich
- Nirjhar Das
- Mahfuzulhoq Chowdhury
affiliations:
- Chittagong University of Engineering & Technology
arxiv_id: '2608.13004'
url: https://arxiv.org/abs/2608.13004
pdf_url: https://arxiv.org/pdf/2608.13004
published: '2026-08-13'
collected: '2026-08-16'
category: RAG
direction: 低资源语言KBQA · 混合检索+验证精炼
tags:
- RAG
- KBQA
- Bangla
- LoRA
- Hybrid Retrieval
- Verification
one_liner: 混合稀疏/稠密检索与LoRA验证、后处理兜底的Bangla KBQA方案，竞赛双榜F1最高0.729
practical_value: '- 在跨境电商/多语言客服KBQA中可复用“BM25+BGE-M3”混合召回：BM25卡精确词，BGE-M3补跨语言语义，减轻低资源语言形态变化对召回的冲击；工程上可离线建倒排+向量双索引。

  - 生成器+LoRA验证器双模型范式：先用大模型生成候选答案，再用同一底座LoRA微调做验证与精炼，可嵌入客服回复、商品问答、Agent工具调用结果的质量把关环节，降低不可靠输出。

  - 兜底后处理：对低置信度或未解析case，用fallback规则+外部搜索（如DuckDuckGo）二次检索，适合商品知识库覆盖不全时的实时兜底，避免Agent空答或乱答。

  - GGUF量化部署Gemma-4-31B，在有限GPU下也能跑生成+验证两个模型；低资源业务可借鉴量化+LoRA节省成本。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：孟加拉语KBQA面临低资源、检索研究少、生成难以对齐外部知识等挑战，现有RAG在高资源语言上的成功难以直接迁移。

**方法关键点**：提出HybridRAG-BN框架，检索端采用BM25稀疏检索与BGE-M3稠密向量检索的混合召回，兼顾词法匹配与跨语言语义泛化；生成端使用GGUF量化的Gemma-4-31B-Instruct产生候选答案；随后引入LoRA微调的同底座Gemma-4-31B-Instruct作为验证器，对候选答案进行验证与精炼，降低幻觉风险。后处理阶段对未解决样本进行fallback答案替换，并利用DuckDuckGo辅助检索，提升鲁棒性。

**关键结果**：在基于Indic-RAG-Suite、约3000条数据的竞赛中，token级F1公开/私有榜分别达到0.71654和0.72912，取得第一名。
