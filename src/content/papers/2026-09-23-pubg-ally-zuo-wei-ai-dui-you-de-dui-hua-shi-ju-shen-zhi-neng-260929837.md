---
title: 'PUBG Ally: A Conversational Embodied Agent as an AI Teammate'
title_zh: PUBG Ally：作为 AI 队友的对话式具身智能体
authors:
- Beomsoo Kim
- Byeongju Kim
- Dohyun Kim
- Dongwon Kim
- Eunchong Kim
- Hongmin Kim
- Hyeojung Im
- Hyeonbin Hwang
- Hyeonghwan Kim
- Hyoseok Seol
affiliations:
- PUBG
arxiv_id: '2609.29837'
url: https://arxiv.org/abs/2609.29837
pdf_url: https://arxiv.org/pdf/2609.29837
published: '2026-09-23'
collected: '2026-09-25'
category: Agent
direction: 具身智能体实时协作与语音交互
tags:
- Embodied Agent
- LLM Agent
- Real-time Control
- Human-AI Teaming
- Game AI
one_liner: 提出 PUBG 语音队友 Ally，结合 LLM 智能体与实时控制层，基于 39k 真实对局数据训练并在 141 国上线，正面评价超负面 25.1
  个百分点
practical_value: '- 分层控制架构：LLM 负责高层意图和决策，将实时敏感的执行下放到低延迟控制层。电商导购/客服 Agent 可借鉴：让 LLM
  做意图识别、策略选择、话术生成，而将库存查询、推荐排序等高频操作交给轻量服务，以降低端到端延迟并保证一致性。

  - 真实交互数据闭环与偏好校准：利用近 39k 真实用户会话收集“上下文-决策-反馈”数据，并发现离线评测与玩家偏好存在差距后迭代评估标准。推荐/搜索系统可引入类似机制，通过真实用户偏好比较（如
  pairwise 反馈）校准离线指标，定期挖掘“离线高、线上差”的 case。

  - 模型压缩与上下文压缩：针对实时服务，采用模型压缩、上下文压缩、记忆脱敏和运行时护栏。移动端或边端部署的推荐 Agent、语音导购可借鉴，对用户历史上下文做摘要压缩，同时脱敏敏感信息，并设置安全
  guardrails 防止不当输出。

  - 语音/动作同步：保持语言输出与系统行为一致（Ally 说什么就做什么），避免用户信任崩坏。电商 Agent 在生成推荐理由或承诺时，需确保底层系统能实际执行（如优惠、到货通知），否则会严重损害体验。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：要构建一个能在 PUBG 中与玩家语音协作、自主行动的 AI 队友，需要同时满足实时游戏感知/行动和自然语言交互，且语言与行为必须保持同步。  
**方法**：Ally 采用分层架构：上层 LLM 智能体通过受控接口检查游戏信息、解释玩家语音、维持上下文、生成发言并做出高层行动选择；下层快速控制层执行移动、战斗和恢复等实时操作。训练数据来自近 39k 场真实玩家与 Ally 的对局，记录游戏过程、玩家语音、智能体决策、工具调用、动作和玩家反馈，以此迭代训练。部署时通过模型压缩、上下文压缩、安全训练、运行时护栏和记忆脱敏满足低延迟和安全要求。  
**结果**：Ally 在 141 个国家和地区上线服务，在确认游戏记录的受访玩家中，推荐意愿的正面评价高出负面评价 25.1 个百分点，玩家称其为队友或伙伴而非工具。
