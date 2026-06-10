---
title: 'SkillResolve-Bench: Measuring and Resolving Same-Capability Ambiguity in Agent
  Skill Retrieval'
title_zh: 'SkillResolve-Bench: 衡量与解决 Agent 技能检索中的同类能力歧义'
authors:
- Jiandong Ding
affiliations:
- Huawei Technologies Ltd.
arxiv_id: '2606.10388'
url: https://arxiv.org/abs/2606.10388
pdf_url: https://arxiv.org/pdf/2606.10388
published: '2026-06-09'
collected: '2026-06-10'
category: Agent
direction: Agent 技能代表性选择与检索安全
tags:
- skill retrieval
- same-capability ambiguity
- benchmark
- agent
- utility learning
- representative selection
one_liner: 提出基准 SkillResolve-Bench 及 SkillResolve 方法，通过同类簇解析与效用学习，消除能力相似但执行有害的技能暴露同时提升有用技能排序
practical_value: '- **同类候选的代表性选择机制可直接迁移**：在电商搜索与推荐中，同一品类下常有多个外观相似但适配性不同的商品（如不同型号、版本），可借鉴本文的同类簇解析（Capability
  Resolver）+ 查询条件化效用评分 + 单代表输出的框架，避免将功能对等但配置过时的物品推给用户，降低体验风险。

  - **合同特征(contract profile)增强检索信号**：从资源绑定、前置条件、时效范围、输出模式等维度构造确定性对比特征，可嵌入排序模型的特征工程中，提升对版本差异、接口兼容性等执行面差异的区分度，适用于需要精准匹配上下文（如
  API 推荐、方案选型）的场景。

  - **以“有害暴露率”作为安全补充指标**：在 Agent 多智体或生成式推荐中，可增设类似 HSR@K 的指标，监控系统输出的“低风险但错误执行”推荐比例，而不仅看点击/满意度；结合簇内效用竞争，可在不伤害核心召回的代价下大幅抑制风险项曝光。

  - **利用易混淆库内负例训练效用模型**：使用同一查询下与有用技能相似的但未被采纳的库内候选作为负例进行配对学习，比随机负采样更能让模型学习到细微的上下文区分，对具有丰富标签的电商场景（如真实成交
  vs. 高相似度但未转化商品）有直接借鉴意义。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：Agent 技能库日益庞大，同一能力族下常存在多个相似技能，它们共享任务词汇和形式，但在资源绑定、前置条件或执行程序上不同。现有检索系统能匹配到正确的能力族，却可能暴露族内错误代表，导致 agent 使用过期资源、跳过必要前置或执行错误程序。这种“同类能力歧义”所造成的执行风险，在标准相关性检索中被忽略，需要新的评估基准和解决方法。

**方法关键点**：
- 构建 SkillResolve-Bench 1.0 基准，包含 661 个查询，每个查询配对一个有用技能和一个同族但执行有害的“风险兄弟”技能，并加入 7,982 个候选技能以施加库压力，同时记录风险类型、证据和审计检查。
- 提出 SkillResolve 方法：1) Capability Resolver 将候选技能按能力族分组；2) Utility Scorer 用易混淆库内负例训练查询条件化效用模型，融合词法、路由分、以及专门设计的“合同特征”（资源绑定、前置条件、API/时间范围、输出模式等）；3) Representative Selector 在每个族内选择效用最高的代表，最终 Top-K 只包含各族的胜者。
- 通过逻辑回归学习效用得分，训练负例为同一查询下除有用/风险兄弟外排名靠前的相似但未入选技能，不使用风险兄弟参与损失计算。

**关键结果**：在 661 对及 7,982 候选池上，SkillResolve 取得 Recall@3 0.766、NDCG@3 0.699，且 HSR@3 保持 0。相比 SkillRouter，召回提升 0.112、NDCG 提升 0.165，同时将有害暴露率从 0.693 降至 0。去除代表选择步骤后，HSR@3 反弹至 0.236，证实代表选择是风险控制的关键。公开元数据或文本簇代替基准族关系也能维持 HSR@3=0，但分组更粗糙。组件消融和改写压力测试进一步验证方法稳健性。
