---
title: 'ETAMem: Decoupling and Aligning Heterogeneous Memory for Long-Term Conversational
  Agents'
title_zh: ETAMem：面向长期对话智能体的异构记忆解耦与多视图对齐框架
authors:
- Xinying Qian
- Ying Zhang
- Yu Zhao
- Xubo Liu
- Baohang Zhou
- Jeff Z. Pan
affiliations:
- Nankai University
- Tiangong University
- University of Edinburgh
arxiv_id: '2610.37443'
url: https://arxiv.org/abs/2610.37443
pdf_url: https://arxiv.org/pdf/2610.37443
published: '2026-10-27'
collected: '2026-10-28'
category: Agent
direction: Agent 长期记忆 · 多视图解耦
tags:
- Long-term Memory
- LLM Agent
- Multi-view Retrieval
- Affect-aware Memory
- Hierarchical Memory
- Entropy Routing
one_liner: 将对话记忆拆分为事件、情感、时间三视图并自适应路由检索，显著提升长期记忆中的多跳与时间推理。
practical_value: '- 在构建用户长期记忆画像时，不要只按语义或时间组织；可拆成「事件 / 偏好情感 / 时间」三个视图：事实类用 semantic
  embedding，偏好类用 affect embedding，时间类强制按 Session→Day→Week→Month 建索引，避免偏好信息混在事件里导致检索错配。

  - Entropy-based routing 可作为低成本的 query 级记忆路由：对 query 和各视图 leaf summary 算相似度分布，用归一化熵判断信号集中程度，再分配检索预算。相比
  LLM routing 更稳定、开销更低。

  - 工程实现上值得复用：内部节点摘要用 pending-change counter + lazy update，减少 LLM 调用；维护阈值用 Otsu +
  EMA 根据相似度分布自适应校准，避免长期运行后树结构退化；leaf split/merge 是必要维护操作。

  - 层级 beam search 中混合 semantic embedding 与 BM25 打分，对品牌名、商品名等 exact term 查询尤其有效，可迁移到电商客服/推荐解释的记忆召回场景。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机

现有 LLM 长期记忆系统面临两大问题：一是信息纠缠，对话轮次中事实、偏好、时间被混在粗粒度记忆条目里，检索时难以隔离相关证据；二是组织错配，单纯按语义或时间组织记忆，无法对齐不同信息类型的特性。例如「我喜欢什么活动」需要跨场景聚合偏好，「我这周做了什么」需要时间聚合，两者要求不同的记忆组织方式。

### 方法关键点

- **异构解析**：每轮对话用 LLM 抽取原子记忆单元 AMU，并用 RoBERTa 情感分类器标记 neutral / positive / negative。
- **三视图记忆组织**：neutral AMU 进入 Event 语义树，affective AMU 进入 Affect 情感树，全部 AMU 进入 Time 时间树（Session→Day→Week→Month）。Event 用 text encoder，Affect 用 affect encoder，Time 按预定义时间粒度组织。
- **动态维护**：插入分 Attach / NewLeaf / NewRoot 三档，依相似度阈值选择；叶子过大或低凝聚时 split，相似节点 merge；内部节点摘要 lazy update，用 pending-change counter 减少 LLM 调用。
- **自适应校准**：最大叶子容量、分支数、深度按历史数据重新计算；维护阈值用 Otsu 分割相似度分布并通过 EMA 更新。
- **熵路由检索**：对 query 与各视图 leaf summary 计算相似度分布，用归一化熵衡量视图检索信号强度，分配每视图检索预算；视图内做层级 beam search，融合 semantic + BM25 打分；证据不足时 fallback 原始对话。

### 关键实验

在 LoCoMo 上 overall accuracy 84.68%，比最强 baseline TiMem 相对提升 12.46%；在 LongMemEval-S 上 83.00%，相对提升 7.96%。多跳和开放域问题提升尤其显著，且构建 token 比 TiMem 低 67.92%。消融显示 AMU、树结构、fallback 均有效；统一单视图（semantic / affective / temporal）均弱于三视图解耦；CloneMem 上 Affect 视图对 Emotion 类问题贡献更高。

**最值得记住的一句话**：异构记忆必须按信息类型解耦到不同视图并匹配对应表征与组织结构，否则单视图检索会互相干扰。
