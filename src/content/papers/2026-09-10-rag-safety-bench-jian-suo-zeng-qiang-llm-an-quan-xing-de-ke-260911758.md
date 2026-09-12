---
title: 'RAG-Safety-Bench: Reliable Evaluation of Retrieval-Augmented LLM Safety'
title_zh: RAG-Safety-Bench：检索增强 LLM 安全性的可靠评估
authors:
- Adithiyan Rajan Indira Saravanan
- Kathleen C. Fraser
affiliations:
- University of Ottawa
arxiv_id: '2609.11758'
url: https://arxiv.org/abs/2609.11758
pdf_url: https://arxiv.org/pdf/2609.11758
published: '2026-09-10'
collected: '2026-09-12'
category: Eval
direction: RAG 安全评估基准
tags:
- RAG
- LLM safety
- evaluation benchmark
- guardrails
- open-source LLMs
one_liner: 提出 RAG-Safety-Bench 基准，用四种条件隔离 RAG 安全退化因素，发现护栏不保证 RAG 安全且良性文档也可能引发不安全生成
practical_value: '- 在企业知识库接入 LLM/RAG 做客服、商品问答或营销文案时，不能只依赖模型自带安全护栏，需对检索文档做安全过滤、冲突检测和输出审核。

  - 设计 RAG 评估时，可借鉴论文做法：将检索质量与生成安全性解耦，设置 oracle/相关/随机文档等条件，定位安全退化到底来自检索内容还是模型自身。

  - 即使检索文档看似“安全/良性”（如产品描述、用户评价），也可能诱发不安全生成，因此需要额外的输出安全分类器或后处理规则，尤其在面向 C 端的生成式推荐场景。

  - 模型选型时注意 trade-off：通用能力越强的开源模型可能越容易在 RAG 条件下被激活不安全能力，需要结合下游任务做安全性压测。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**
RAG 被广泛用于将企业文档和知识库接入 LLM 系统，以降低幻觉、提升可靠性。但近期工作表明，当用户提出有害请求时，RAG 可能带来非预期的安全副作用。随着越来越多终端用户依赖 RAG，需要更清晰地理解安全退化的机制。

**方法关键点**
引入 RAG-Safety-Bench，核心是消除 retriever 质量带来的混淆，将问题划分为四种条件：
- non-RAG：不检索，直接生成；
- RAG + oracle 文档：检索到包含有害请求答案的文档；
- RAG + 相关文档：文档与有害请求相关但不含具体答案；
- RAG + 随机安全文档：检索到随机良性文档。

通过比较这四种条件，隔离不同因素对安全退化的影响。在五个开源 LLM 上进行评测。

**关键结果数字**
- 发现良性能力与不安全能力呈反向关系：模型通用能力越强，RAG 下越容易出现不安全生成。
- 基线安全护栏在 non-RAG 下有效，但在 RAG 条件下不能提供下游安全保证。
- 部分模型支持此前发现：即使只提供良性文档，RAG 也可能诱导不安全生成。
