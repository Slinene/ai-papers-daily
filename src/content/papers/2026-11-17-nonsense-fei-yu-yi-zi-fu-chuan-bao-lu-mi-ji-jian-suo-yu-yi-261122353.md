---
title: 'NONSENSE: Non-Semantic Strings Expose Semanticity Gaps in Dense Retrieval'
title_zh: NONSENSE：非语义字符串暴露密集检索语义性差距
authors:
- Ankit Gupta
affiliations:
- Michigan State University
arxiv_id: '2611.22353'
url: https://arxiv.org/abs/2611.22353
pdf_url: https://arxiv.org/pdf/2611.22353
published: '2026-11-17'
collected: '2026-11-19'
category: Eval
direction: 密集检索语义性评估与对抗探针
tags:
- Dense Retrieval
- Semanticity
- Adversarial Probe
- Evaluation
- Single-vector Retriever
one_liner: 构造非语义字符串仅优化相似度即可在密集检索中排名第一，揭示相似度与语义证据的可分离性
practical_value: '- 在商品/内容/广告的向量召回链路中，不能直接信任 top-K 相似度分数；建议引入二次语义校验（如交叉编码器重排、BM25
  混合、规则过滤），防止非语义垃圾文本或 SEO 作弊内容被召回。

  - 可将 NONSENSE 思路改造为离线回归测试：定期生成非语义探针，检查线上检索模型是否对无意义文本赋高分，监控语义性漂移，作为模型鲁棒性指标。

  - 在 RAG / Agent 链路中，检索到的“高相似度”片段不一定是可靠上下文，关键决策环节应增加证据有效性验证，避免 Agent 基于非语义片段推理。

  - 对生成式推荐（如 Semantic ID、token 生成）同样需警惕嵌入空间被无意义 token 序列“攻破”，可借鉴探针方法评估生成空间的语义一致性。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

密集检索中，高相似度得分通常被当作语义相关性的证据。该研究针对这一假设进行压力测试，提出 NONSENSE 探针：给定查询和单向量检索器，初始化固定长度的可见填充字符串，通过单字符替换进行稀疏编辑，仅接受能提升密集相似度的替换，并明确禁止任何查询词复制，最终将优化后的字符串插入完整语料库参与排序。在五个 BEIR 风格数据集和三种流行的单向量检索器上，这些明显非语义的字符串经常在相似度上超过检索器自身的最佳判断相关段落（QRP），甚至常排名全语料第一。结果表明，检索器的最近邻地位与段落式意义可以分离，存在语义性鸿沟。作者强调，评估密集检索器不能只关注是否检索到相关文档，还须检验相似度分数是否可靠反映语义证据。
