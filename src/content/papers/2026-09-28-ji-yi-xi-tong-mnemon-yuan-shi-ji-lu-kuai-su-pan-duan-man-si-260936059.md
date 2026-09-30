---
title: 'Mnemon: Raw Records, Fast Judgments, Slow Thoughts'
title_zh: 记忆系统 Mnemon：原始记录、快速判断、慢思考
authors:
- Guangren Wang
arxiv_id: '2609.36059'
url: https://arxiv.org/abs/2609.36059
pdf_url: https://arxiv.org/pdf/2609.36059
published: '2026-09-28'
collected: '2026-09-30'
category: Agent
direction: Agent 记忆系统 · System 1/2 分工
tags:
- Agent Memory
- System 1-2
- Retrieval
- Long-term Memory
- Decision Model
- LLM
one_liner: 用 System 1 决策模型在读取时批量判断原始记录，后台只建索引，以 <4k tokens 上下文在 LoCoMo 达 91.7%
practical_value: '- 在电商推荐 Agent 中，保留用户原始行为/对话记录，不在写入时抽取事实或建图谱；后台定期构建 topic timelines（用户关注点变化）、value
  histories（偏好值变化，如价格阈值、品类偏好）、standing instructions（用户明确要求，如“不要推已购买”），并链接回原始记录。读取时用小型决策模型批量判断哪些记录与当前请求相关、是否过期、满足哪个需求，只把少量相关记录喂给
  LLM，大幅降低回答上下文和成本。

  - 将记忆读取拆成 System 1/System 2：System 1 用廉价决策模型对候选记录做独立 yes/no 判断（是否相关、是否过期、满足哪个信息需求），System
  2 仅写搜索查询、命名需求、生成回答。可以借鉴到推荐 Agent 的检索/过滤架构：用轻量模型粗筛候选池，LLM 只做高价值规划和生成，避免 LLM 逐条判断候选的延迟和成本。

  - 引入固定预算和显式规则：view 大小、pool 大小、循环轮数、判断阈值等。规则只依赖判断顺序和二分结果，不依赖校准，因此可以替换决策模型而无需重新调参。工程上可让系统在长历史上保持近似恒定成本（从
  100K 到 10M tokens 成本仅增长 1.11 倍）。

  - 评估时使用有效成本指数 ECI = (1-accuracy) + context/full_context_cost，统一衡量错误和上下文代价，适合线上 Agent
  对比模型/记忆策略，避免只优化准确率而忽略成本。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：长会话 Agent 的历史无法全部重读，现有记忆系统多写时抽取/建图，代价高、可能丢失未来问题所需信息，且绑定 schema。作者认为记忆工作像思考可分为 System 1（快速判断）和 System 2（慢速规划/回答）。

**方法关键点**：
- 存储原始带日期记录，写入时仅计算 embedding，不做任何抽取；
- LLM 作为 System 2 规划搜索（写 5 个搜索查询，含 HyDE，最多 3 个信息需求），并最终回答；
- 决策模型 Jev 作为 System 1 对池化记录批量判断：是否使用该记录、是否过期、满足哪个需求；判断独立且并行，数十个判断在 0.34 秒内完成；
- 规则用固定预算连接两系统：pool 48 条，循环最多 3 轮，View 最多 16 条记录 + 索引项，12k 字符；
- 后台 consolidation 将每条记录折叠成 topic timelines、value histories、standing instructions，链接回原始记录；索引覆盖整段会话的问题。
- 由于读取时才解释，同一 agent 可读取任何返回带日期记录的存储，无需为不同 store 写新抽取器。

**关键实验**：
- 在 OmniMemEval 重新评估的 14 个系统对比中，用 gpt-4.1-mini 回答，LoCoMo 91.7%，LongMemEval-S 83.8%，上下文 <4k tokens，LoCoMo ECI 最低（0.259）；
- 换成推理模型 DeepSeek-V4.1-Flash 后，LoCoMo 92.2%，LongMemEval-S 94.4%，与最佳已发表结果相当；
- BEAM 从 100K 到 10M tokens 历史，每问题成本只增长 1.11 倍；
- Jev 区分 gold evidence 的 AUC 0.942，高于两个 LLM 的 0.900/0.853，且快 3-11 倍。

**最值得记住**：长期记忆的大部分工作是 System 1 的批量独立判断，应在读取时由决策模型完成，而不是写时由 LLM 抽取；原始记录加后台索引，不绑定 schema，可让同一份记忆服务更强模型和更长历史。
