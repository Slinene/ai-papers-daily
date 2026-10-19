---
title: 'MARS: Memory-Aware Routing for Session-Level LLM Assistants'
title_zh: 记忆感知路由：会话级LLM助手的记忆构造与模型选择协同框架
authors:
- Minghan Wang
- Jinhang Zuo
- Zhongxiang Dai
- Zhiyong Wang
- Fang Kong
affiliations:
- Southern University of Science and Technology
- City University of Hong Kong
- The Chinese University of Hong Kong, Shenzhen
- Harbin Institute of Technology (Shenzhen)
arxiv_id: '2610.23583'
url: https://arxiv.org/abs/2610.23583
pdf_url: https://arxiv.org/pdf/2610.23583
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: Agent 会话记忆与路由协同优化
tags:
- Memory-Aware Routing
- Session-Level LLM
- Contextual Bandit
- Long-Term Memory
- Cost-Quality Trade-off
- LLM Router
one_liner: 通过共享会话状态协调记忆暴露与模型选择，在长历史交互中实现质量-成本平衡
practical_value: '- 在电商客服/导购 Agent 中，将记忆构造与模型路由解耦会导致强模型被错误上下文拖累，建议引入轻量级控制器（QTM）输出结构化会话状态，同时指导召回/上下文组装和模型选择，降低过期信息与干扰。

  - 使用 LinUCB 在线学习路由策略，以 turn-level rubric 评分减生成成本作为奖励，冷启动即可用，无需重训底层 LLM，适合线上多模型池的动态成本控制。

  - 区分「记忆访问」与「记忆暴露」：维护大记忆池但只给生成模型打包决策相关证据，并通过预算感知 pack 适配不同模型的上下文窗口，能有效避免 context
  overflow 和多余 distractors。

  - 借鉴 QTM 的 schema 字段（action/query_type/phase/retrieval_scope/top_k_hint/lens_recommendation），避免把原始
  topic 标签直接喂给路由器，有助于跨任务泛化和可解释性。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
长期 LLM 助手需要反复决定暴露哪些历史上下文以及选择哪个模型。现有 memory 系统和 model router 通常独立决策，但记忆构造会改变证据、干扰项和上下文难度，模型选择又决定这些上下文能否被可靠利用。质量-记忆-成本之间存在耦合权衡：记忆不足会导致约束丢失或使用过期信息，记忆过全增加 distractors，模型过强造成成本浪费。需要协调记忆暴露与模型选择。

## 方法关键点
- 将问题形式化为序列决策：在每个 turn 估计会话状态，构造候选记忆视图，选择模型，按模型预算打包，生成后通过 turn-level 反馈更新路由策略。
- 引入 Query and Topic Manager (QTM)，用较小指令模型输出结构化会话状态 z_t：action（MATCH/NEW_TOPIC）、query_type、phase、retrieval_scope、top_k_hint、prefer_recent、lens_recommendation 等；同一状态作为 memory policy 和 router 的共享接口。
- memory policy 根据 z_t 生成 memory controls，从 active state、recent turns、historical retrieval 组装候选视图；router 用 z_t 和预打包视图统计（token 负载、相似度等）选择模型；最后按模型 context budget 裁剪打包。
- Router 采用 LinUCB 在线学习，turn-level 反馈由 rubric 评测（六维 0-5 分 + 硬失败 flag）加权后减去生成成本得到 reward，只更新所选臂，不重训底层 LLM。

## 关键结果
- REALMEM（10 personas，1415 queries）：MARS QA 0.7406，达到 full-context GPT-4o 0.7540 的 98.2%；生成+控制器 API 成本 $26.65，仅为 GPT-4o $184.40 的 14.5%；同时 Memory Recall 和检索指标最强。含反馈成本约 $32.53，占 17.6%。
- MULTICHALLENGE 全量：MARS 58/245，低于 full Qwen2.5 72B 的 67/245 和 GPT-4o 的 64/245；在机制聚焦子集 44/137 接近 Qwen 45/137，成本更低。
- 消融显示 QTM 引导上下文比纯 embedding 语义检索和 recent-only 记忆更好；冻结路由器（no-update）会使 QA 从 0.7444 降至 0.4221，说明在线更新对质量关键。

## 最值得记住的一句话
记忆构造与模型路由应当共享同一个结构化会话状态接口，而不是把检索当预处理、把路由当独立决策。
