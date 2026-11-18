---
title: Runtime Verification of Multiple Natural Language Criteria for Agent Governance
title_zh: Agent 治理中多自然语言准则的运行时验证
authors:
- Silviu Pitis
- Parand A. Alamdari
- Jessica Tang
- Toryn Q. Klassen
- Sheila A. McIlraith
affiliations:
- University of Toronto
- Vector Institute
arxiv_id: '2611.23074'
url: https://arxiv.org/abs/2611.23074
pdf_url: https://arxiv.org/pdf/2611.23074
published: '2026-11-17'
collected: '2026-11-18'
category: Agent
direction: Agent 运行时准则并行验证
tags:
- Runtime Verification
- Tree Attention
- Agent Governance
- Natural Language Criteria
- CriteriaBank
- Ternary Verdicts
one_liner: VFM 树注意力验证器并行评估上千条自然语言准则，逐条返回满足/违反/不适用三元判定
practical_value: '- 在电商/广告 Agent 链路上部署轻量级准则验证器（如 VFM-4B），线上实时检查生成内容是否违反业务规则（广告合规、价格约束、敏感词、平台政策等），单卡
  H100 可在 2 秒内评估 1000 条准则、显存 <11 GB，适合作为中间件集成到推荐/搜索 Agent 工作流。

  - 将大量分散的业务准则、审查规则统一编码为自然语言，利用树注意力共享上下文并行打分，替代逐条串行调用 LLM 验证，降低延迟和成本。

  - 当检测到某条准则被违反时，只把该准则、相关上下文和目标文本交给更大规模的 CoT 法官做聚焦升级，避免全量二次审查，平衡准确率与算力。

  - 借鉴 CriteriaBank 预训练思路：自动构造或采集 (context, target, criterion, verdict) 四元组对验证器做领域预训练，可显著提升低数据
  regime 下的跨域迁移能力，适合冷启动业务规则验证。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：AI agent 需同时遵守数百条来自系统提示、监管、用户和运行时上下文的自然语言准则，但现有验证器无法高效评估大量准则并逐条报告是否满足、违反或不适用，导致线上失败频发。

方法关键点：提出 VFM 树注意力验证器，编码共享上下文和目标文本，并行对 N 条自然语言准则打分，返回每个准则独立的三元判定。模型预训练于新语料 CriteriaBank，包含 394K 条 (context, target, criterion, verdict) 四元组，覆盖超 321K 条不同准则文本。

关键结果：微调后的 VFM-4B 在合成治理基准上超过 GPT-5.4；在 DynaBench 多准则基准上，轨迹级失败检测优于 DynaGuard-4B，其逐准则判定能定位违规规则并支持聚焦升级至更大的 CoT 法官。CriteriaBank 预训练改善跨域迁移，尤其在低数据 regime 效果显著，全数据下与强直接微调对照持平。工程上单张 H100 对 4K token 上下文评估 1000 条准则耗时 <2 秒、显存 <11 GB，适合运行时验证。
