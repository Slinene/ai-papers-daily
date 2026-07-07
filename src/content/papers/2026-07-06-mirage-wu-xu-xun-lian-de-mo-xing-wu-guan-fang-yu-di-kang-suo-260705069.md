---
title: 'MIRAGE: Defending Long-Form RAG Against Misinformation Pollution'
title_zh: MIRAGE：无需训练的模型无关防御，抵抗检索增强生成中的错误信息污染
authors:
- Saadeldine Eletter
- Ruihong Zeng
- Yuxia Wang
- Maxim Panov
- Aleksandr Rubashevskii
- Preslav Nakov
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence (MBZUAI)
- INSAIT, Sofia University “St. Kliment Ohridski”
arxiv_id: '2607.05069'
url: https://arxiv.org/abs/2607.05069
pdf_url: https://arxiv.org/pdf/2607.05069
published: '2026-07-06'
collected: '2026-07-07'
category: RAG
direction: RAG 错误信息防御与事实性恢复
tags:
- RAG
- misinformation
- defense
- NLI
- claim graph
- long-form QA
one_liner: 提出一种训练无关、模型无关的防御方法，通过跨文档声明图和多源一致性门控恢复RAG事实性
practical_value: '- 在电商搜索/推荐系统里，若用 RAG 增强物品描述或评论摘要，可借鉴 MIRAGE 的多源一致性验证：对多路召回（不同数据库、不同站点）抽取原子声明，用
  NLI 构建声明图，仅保留多文档支持的声明，减少单品描述中的虚假信息。

  - 面向 Agent 系统中检索知识冲突的应对：当检索到的证据相互矛盾时，可以设置“防御门”退回参数化回答或拒答，避免 Agent 被污染信息误导，提升决策可靠性。

  - 污染检测的工程化思路：定义最小编辑的污染类型（如明确错误、矛盾、误导、捏造），可用于线上 A/B 测试或离线评测，量化检索或生成环节对输入噪声的鲁棒性。

  - 无需训练、模型无关的设计使其能即插即用到现有 RAG pipeline，适合快速迭代的工业场景，无需重训练或更换生成模型。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：长文本问答依赖 RAG，但真实检索常混入看似相关实则含微妙错误的污染条目，现有 LLM 易盲从检索上下文，导致生成错误答案。亟需一种训练无关、模型无关的防御机制。

**方法**：提出 MIRAGE，分两步：① 基于 NLI 构建跨文档声明图，将各检索段落分解为原子声明，通过蕴含关系检测声明的多源一致性；② Defended-Claims Gate 根据一致性决定生成策略——存在足够多源支持的声明子集时，仅用该子集增强生成；否则阻断检索，完全依赖模型参数回答。同时发布了一套最小编辑污染协议，涵盖无歧义错误、冲突、误导、捏造四种扰动，可构建洁净/混合/全污染的对比评测环境。

**结果**：在四个长文本 QA 基准及多款商用/开源 LLM 上，污染严重损害普通 RAG 的事实性，而 MIRAGE 在混合和全污染条件下一致恢复事实性且显著优于之前鲁棒 RAG 方法。
