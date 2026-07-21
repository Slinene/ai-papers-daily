---
title: Adapting Embedding Models for Agent Capability Retrieval
title_zh: 适配嵌入模型用于智能体能力检索
authors:
- Tingwei Chen
- Yunxiao Shi
- Zhengdong Chu
- Qingsong Wen
- Min Xu
affiliations:
- University of Technology Sydney
- Squirrel AI Learning
arxiv_id: '2607.17347'
url: https://arxiv.org/abs/2607.17347
pdf_url: https://arxiv.org/pdf/2607.17347
published: '2026-07-19'
collected: '2026-07-21'
category: Agent
direction: Agent 能力检索 · 嵌入模型微调
tags:
- agent retrieval
- embedding adaptation
- transfer learning
- capability profiles
- text embedding
- model fine-tuning
one_liner: 微调通用文本嵌入模型实现跨目录的 Agent 能力检索，并在未见数据集上验证迁移有效性
practical_value: '- **电商功能/服务统一检索**：将商品、工具、服务包装成“能力 profiles”，可用相同范式构建搜索引擎，统一索引异构货架。

  - **元数据驱动的 embedding 微调**：利用公开元数据自动生成能力描述，无需人工标注大量 query-item 对，可快速搭建新业务的检索基线。

  - **跨域迁移的思路**：先在一个可获取的源域（如开源 Agent 目录）微调，再部署到目标域（如内部工具/技能库），无需冷启动大量数据，验证了跨目录泛化可行性。

  - **模型选择**：BGE-base、KaLM-v1.5、EasyRec 等通用检索模型经微调后可用于垂直 Agent 搜索，为工业上选型提供参考。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：开放 Agent 市场将原生智能体、工具包、技能包混合展示在同一搜索界面，但如何有效检索可执行的 Agent 能力仍然缺乏指导。现有检索模型面向通用文本，需验证其能否适配这种混合目录的 query-to-agent 匹配，以及能否迁移到新场景。

**方法**：将市场可见单元表示为“能力 profiles”（基于公开元数据构建），微调三个开源检索骨干（BGE-base、KaLM-v1.5、EasyRec）在 AgentSelect 数据集上，学习将用户查询映射到能力 profiles。随后在未参与训练的 MuleRun 原生 Agent 目录和 ClawHub 技能基准（50 技能、1000 查询）上测试跨目录迁移效果。

**关键结果**：微调后模型在两个新目录上均展现出检索性能提升，表明通用嵌入模型经适性训练可有效泛化到新的 Agent 能力检索场景。具体指标未在摘要公布，但证实了方法跨目录有效。
