---
title: 'Wayfinder: Adaptive Resource Routing from Agent Citations'
title_zh: Wayfinder：基于 Agent 引用的自适应资源路由
authors:
- Miguel Romero
- George Karypis
affiliations:
- University of Minnesota
arxiv_id: '2611.16053'
url: https://arxiv.org/abs/2611.16053
pdf_url: https://arxiv.org/pdf/2611.16053
published: '2026-11-11'
collected: '2026-11-13'
category: Agent
direction: Agent 资源路由 · 引用反馈自适应
tags:
- resource routing
- agent memory
- citation feedback
- GRPO
- LoRA
- tool retrieval
one_liner: 用下游 Agent 引用的文档做反馈，在线更新资源 sketch，实现跨会话自适应路由，在语义重叠资源上明显优于静态描述
practical_value: '- 在企业 Agent 或多库检索场景中，可以把下游 LLM 实际引用/用户点击的文档作为 citation 信号，只将这些被采纳的证据写入各数据源的
  resource sketch，避免把探索性检索结果全部写进记忆，从而提升后续路由精度。

  - 用有界 LRU sketch（如每资源 M=100）+ 全局 semantic index 表示每个资源/工具，而不是全量索引；这在商品库、内容库、客服知识库、活动页等电商多来源路由中可低成本在线更新。

  - 训练 routing policy 时对 resource id 做匿名化 + session 级随机置换，防止模型记住“某库 ID = 某话题”；冷启动、跨客户/跨行业迁移时尤其有价值。

  - 评估 Agent 路由效果时，不要只看省了多少搜索调用，要同时看 citation F1 或下游证据命中，避免“省调用但答不对”的假 savings。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
Agent 需要在 chats/issues/emails/wiki 等多个资源中找 grounding，但信息位置因用户/组织而异；静态工具描述难以区分语义重叠资源，导致每次会话重复探索。现有 tool retrieval / supervised / bandit 方法不是依赖描述，就是需要目标环境标签，难以在线适应。Wayfinder 用下游 Agent 引用的文档作为弱监督，更新资源记忆，让路由随交互变好。

**方法关键点**
- Citation gating：只把被 Agent 引用、且出现在 tool output 中的文档写入 memory，过滤探索噪声和幻觉；轨迹中 citation rate 74–95%，citation accuracy 71–73%。
- Resource sketches：每个资源维护有界 LRU sketch（M=100），记录 cited doc + query + timestamp；之上建全局 semantic index，检索 top-25。
- Routing policy：Qwen3-8B + LoRA(rank 16)，GRPO RL 离线训练，ReAct 方式读取 memory；奖励用 routing F1 对 ground-truth relevant resources。
- Resource augmentation：训练时对 resource identifier 匿名化，并按 session 随机置换，迫使策略读 memory 而不是背资源名-话题关联。
- 数据集：NFCorpus/FEVER 为 intra-corpus GMM 聚类分区（18 环境）；Tech Startup 为 cross-corpus，5 个真实语料来源：Enron 邮件、Alpaca 聊天、SWE-bench issues、HotpotQA wiki、CodeSearchNet 代码。

**关键结果**
- NFCorpus/FEVER 上，Wayfinder routing F1 达 47.67/64.72，而最强 baseline 为 33.03/31.01；搜索调用节省 61.2%/73.7%，citation F1 比无路由 +2.7/+17.9。
- Tech Startup 跨语料设置中，ToolRetriever 以 98.86 F1r 领先，Wayfinder 86.60 第二；无路由 citation F1 87.44 最高，说明资源异构明显时静态描述已经足够。
- 消融：去掉 RL post-training 后，NFCorpus/FEVER F1r 从 50.69/67.94 降到 41.28/66.06；resource augmentation 在训练环境较少（NFCorpus）时更有效。
- 非平稳 drift 实验显示，Wayfinder 的 recall/precision 降幅小于静态 baseline。

**最值得记住**：路由监督不必来自目标环境标签，Agent 自己“引用了哪些文档”就是可迁移的高质量弱标签；只吸收被引用的证据，让 memory 适应目标环境，而不是依赖静态描述。
