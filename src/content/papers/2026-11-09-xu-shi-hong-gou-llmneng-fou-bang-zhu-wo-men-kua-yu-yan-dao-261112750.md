---
title: 'The Narrative Gap: Can LLMs Help Us Navigate Diverse Narratives Across Languages?'
title_zh: 叙事鸿沟：LLM能否帮助我们跨语言导航多元叙事？
authors:
- Nikhil Sharma
- Kelly Marchisio
- Kenton Murray
- Ziang Xiao
affiliations:
- Johns Hopkins University
- Cohere
- George Mason University
arxiv_id: '2611.12750'
url: https://arxiv.org/abs/2611.12750
pdf_url: https://arxiv.org/pdf/2611.12750
published: '2026-11-09'
collected: '2026-11-12'
category: Eval
direction: LLM 多语言信息获取评测
tags:
- NarrativeBench
- Multilingual
- Diverse Information Seeking
- LLM Evaluation
- Narrative Diversity
- Query Framing
one_liner: 提出NarrativeBench基准，评测14个LLM在24种查询语言下导航多语言竞争叙事的能力，发现模型在多样性覆盖与跨语言信息平等方面存在明显差距
practical_value: '- 借鉴其分层能力定义：将推荐/搜索中的内容多样性拆解为“包含、排除、缺失识别”等可评测指标，尤其适用于敏感或争议话题场景的内容供给监控。

  - 重视查询框架与确认偏差：评测显示确认性查询会进一步压缩叙事覆盖，提示在电商搜索和推荐中不能只做个性化匹配，需主动注入多样性以对抗用户query偏向。

  - 跨语言信息对等性可迁移到多语言电商平台：定期检测同一query在不同语言下的结果分布偏差，防止某些语言市场产生信息茧房或商品曝光失衡。

  - 使用社区真实讨论生成query的方法值得参考，能提升评测生态效度；但该工作聚焦新闻争议话题，离电商/广告业务直接价值有限。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM日益成为信息获取的中介，尤其在争议话题上，不同语言和地区存在竞争性叙事。用户需要跨语言、跨信息流导航多元叙事，但现有模型缺乏可靠支持。

**方法关键点**：定义六项必要能力——三项基础能力：叙事包含、叙事排除、缺失叙事识别；三项高级能力：呈现多元叙事、确认性查询下保持叙事覆盖、跨语言信息对等。构建NarrativeBench基准，包含1,333篇新闻文章、23种发布语言、23个争议话题和460个Reddit衍生查询。在24种查询语言上评估14个LLM。

**关键结果数字**：当前模型无法稳定导航多元叙事；即使明确要求多样性，竞争性叙事的曝光仍存在重大空白；查询措辞和语言不同导致信息获取显著差异，增加了回音室、语言过滤气泡和信息不平等的风险。14个LLM在六项能力上均未达标，用户对接收视角的控制十分有限。基准为跨语言、跨地区赋予用户信息自主权的系统开发提供了评测基础。
