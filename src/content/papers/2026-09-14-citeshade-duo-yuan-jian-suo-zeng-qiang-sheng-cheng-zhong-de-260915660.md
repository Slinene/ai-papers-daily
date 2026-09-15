---
title: 'CiteShade: Citation Laundering in Multi-Source Retrieval-Augmented Generation
  and Its Counterfactual Defense'
title_zh: CiteShade：多源检索增强生成中的引用洗钱攻击及其反事实防御
authors:
- Guo Fuzheng
affiliations:
- City University of Hong Kong
arxiv_id: '2609.15660'
url: https://arxiv.org/abs/2609.15660
pdf_url: https://arxiv.org/pdf/2609.15660
published: '2026-09-14'
collected: '2026-09-15'
category: RAG
direction: RAG 引用安全与防御
tags:
- RAG
- Citation Laundering
- Adversarial Attack
- LLM Security
- Counterfactual Defense
one_liner: 提出首个 RAG 引用洗钱攻击，展示如何让模型把错误答案归因于可信源，并给出反事实防御。
practical_value: '- 在构建基于 RAG 的搜索/问答/推荐解释系统时，不能默认引用真实可靠：攻击者可通过单一恶意源污染多源上下文，需引入引用链路验证机制，单纯检查答案困惑度或引用支持度不够（本文已证明可被绕过）。

  - 借鉴反事实防御思路：在线生成后执行“源删除”或干预测试，观察答案是否改变，以检测哪个来源真正驱动了答案，可作为校验模块部署在生成链路末端。

  - 漏洞与模型的引用倾向相关而非模型规模，选型时应实测模型在引用指令下的“易受骗程度”，优先选择引用倾向低或约束引用格式的模型，而不是只看参数规模。

  - 在多源外部数据接入（商品描述、用户评论、广告文案）时，建议对来源可信度分级，并对引用来源做隔离或加权，防止低可信来源劫持高可信来源的引用。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：RAG 系统返回答案与引用，用户把引用当作审计线索。现有 RAG 安全研究只关注答案被篡改，引用渠道完全未设防，构成新的攻击面。

**方法关键点**：提出 CiteShade 攻击——攻击者控制单一恶意源，诱导 LLM 生成攻击者指定的错误答案，并将其归因于不支持该答案的受信任源，同时正确答案的证据仍保留在上下文中。攻击被形式化为优化问题，推导出检索、生成、引用三个必要条件，并构造满足条件的来源，全程无需显式指令。防御上，提出反事实防御：通过验证哪个来源实际驱动了答案来识别操纵。

**关键结果**：在多源多跳问答上，攻击将错误答案率从 0.01 提升至 0.68；源删除实验在所有测量案例中确认恶意源是因果驱动。漏洞与模型引用倾向高度相关而非模型规模，引用倾向最高的模型上 CLR 达 0.84（显式指令）和 0.64（无指令）。困惑度过滤与引用支持检查均不足以防御。
