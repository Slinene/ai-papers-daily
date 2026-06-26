---
title: 'ConvMemory v3: A Validity Context Layer for Conversational Memory via Target-Conditioned
  Relation Verification'
title_zh: ConvMemory v3：对话记忆的目标条件有效性验证层
authors:
- Taiheng Pan
affiliations:
- University of Melbourne
arxiv_id: '2606.26753'
url: https://arxiv.org/abs/2606.26753
pdf_url: https://arxiv.org/pdf/2606.26753
published: '2026-06-25'
collected: '2026-06-26'
category: Agent
direction: Agent 记忆管理 · 有效性验证与更新检测
tags:
- conversational memory
- validity detection
- target-conditioned verification
- dual-evidence gate
- memory update
- non-destructive deployment
one_liner: 在对话记忆检索后增加目标条件双证据门控，检测记忆更新/失效，将当前状态查询命中率升至95.7%
practical_value: '- **对话推荐中的意图更新检测**：当用户在对话中修改/撤销需求时（如“换成红色”），可利用目标条件关系验证判断历史记忆的有效性，避免基于过时偏好推荐商品。

  - **双证据门控泛化**：将 MiniLM + DeBERTa-v3 双头评分与保守证据门控结合的方法，可迁移至商品信息变更、促销状态更新等时效敏感场景，提升系统对信息新鲜度的感知。

  - **合成数据 + 真实反馈的零样本迁移**：通过合成多跳数据训练验证器，再以真实失败案例反馈微调，能在无目标标签的新任务（如角色绑定）上达到高准确率，大幅降低标注成本。

  - **安全部署的双模式设计**：默认 context 模式仅附加有效性标签不改变检索结果，保护现有链路；按需开启 demote 模式提升高时效查询的命中率，同时保持非过时记忆
  99.4% 召回，适合生产环境渐进式升级。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有对话记忆检索仅优化相关性，但相关记忆可能已被后续对话更新、纠正或取代，导致基于过时信息生成错误回答。需要一种机制判别记忆的有效性状态。

**方法关键点**：在已有的 ConvMemory v1/v2 检索路径后增加有效性上下文层。核心是目标条件双证据门控：对每个（目标命题，来源语句）对，通过 MiniLM 和 DeBERTa-v3 的 slot head 分别评分，乘积后经保守的事件/操作证据门控过滤，再按 noisy-or 聚合多跳证据。训练时使用合成多跳数据，并通过真实数据反馈环路挖掘失败模式但仅用合成对训练，实现零样本迁移。部署提供两种模式：context 模式仅附加结构化有效性元数据，保持候选集与排序不变；demote 模式根据查询条件显式降级过时记忆。

**关键结果**：合成多跳基准上准确率 90.12%±1.73；零样本迁移至 Memora 角色绑定任务，组全对率 98.8%±0.9；demote 模式下当前活跃记忆 H@1 从 45.1% 提升至 95.7%±1.2，同时非取代记忆召回率保持 99.4%。验证了多跳图传播的有效性，但也指出严格前提边自动构建受限于反事实知识。
