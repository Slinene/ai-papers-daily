---
title: You don't need long context
title_zh: 你不需要长上下文：频繁压缩支持短上下文智能体
authors:
- Peter Belcak
- Saurav Muralidharan
- Jindong Jiang
- Yonggan Fu
- Wonmin Byeon
- Hanrong Ye
- Ryan Angilly
- Ali Taghibakhshi
- Shih-Yang Liu
- Siru Ouyang
affiliations:
- NVIDIA
arxiv_id: '2611.05306'
url: https://arxiv.org/abs/2611.05306
pdf_url: https://arxiv.org/pdf/2611.05306
published: '2026-11-03'
collected: '2026-11-04'
category: Agent
direction: Agent 长上下文压缩与语义状态
tags:
- long context
- context compaction
- semantic state
- selective reading
- agentic LLM
- cost efficiency
one_liner: 频繁上下文压缩与选择性读取，使长程/长输入任务无需长上下文，准确率基本持平且成本大降
practical_value: '- 在电商推荐/搜索 Agent 的工作流中，将用户会话状态压缩为一段自然语言「semantic state」，每次调用大模型只携带任务描述
  + 当前状态，不保留全量对话历史；线上可显著节省 KV cache 和 decode 成本，适合需要多轮筛选/比价的购物助手。

  - 对长用户历史、商品详情、评论、规则文档等长输入，用工具化 selective reading：把长文档落在文件系统或检索索引，通过 grep/sed/head
  或向量检索按需取证据，避免全量入上下文；可结合 RAG 实现“按需读”，比直接塞 100K 文档更可控。

  - 采用 EoCC 式阈值压缩：设定上下文阈值（参考 12K–36K），触发时让模型只保留硬约束、用户偏好、未完成动作和已发现证据，重启新对话；压缩提示要约束长度并聚焦决策相关信息，防止信息丢失。

  - 在评测 Agent 时增加效率指标：不只报准确率，同时统计 peak context length、total tokens、每任务成本；可以尝试 single-action
  compaction，把长程任务建模为状态转移，验证在业务场景是否同样成立。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

动机：token 生成成本随上下文深度近似线性上升。H100 上 GLM 5.2、Kimi K2.6、Qwen 3 Coder Next 从 16K 扩到 256K，单 token 生成成本增加 3.6–7 倍，延迟和显存也翻倍。但主流模型上下文窗口已膨胀到 200K–1M；因此需要验证长上下文是否必要。

方法关键点：
- 将任务分两类：长程任务（上下文随交互增长）与长输入任务（输入本身很长）。
- 上下文管理三档：FHA 全量历史；EoCC 到达阈值后把历史压缩成任务相关状态，新对话重启；SAC 每步只带当前语义状态，执行一个动作后立即压缩。
- 长输入通过文件系统暴露为文档，用 Bash 工具按需 selective reading，将其转成长程任务。
- 评估模型为 Claude Opus 4.5、GPT 5.6 Sol，以及多个开源权重模型；基准覆盖 SWE-bench Verified、Terminal-Bench、FRAMES、τ2-bench、BFCLv3、LongBench v2、LOONG、AA-LCR、NIAH、RULER、Counting-Stars、BABILong。
- 提出 Semantic State Space Model (SSSM)：后训练模型在自然语言语义状态上更新推理结论与动作结果，而不是保留黑盒或全量历史。

关键结果：
- 长程任务：EoCC 相对于 FHA 准确率变化为 -3.7~+5.6 pp（Claude）与 -3.3~+4.4 pp（GPT），多数配置损失 ≤2 pp；成本节省 2.2–8.8x。
- 长输入任务：选择性读取+压缩几乎在所有场景匹配或超过 full-input baseline，NIAH 提升最高 +40 pp，成本节省 6.5–233.3x。
- SAC 将峰值上下文从 130–200K 降到 15–37K；Claude Opus 4.5 在 SWE-bench Verified 70.0→70.2，Terminal-Bench 47.2→51.8；GPT 5.6 Sol 分别略降 2.0/3.3 pp。

最值得记住的一句话：长上下文不是长程或长输入任务的必需品；把工程资源投向语义状态维护、按需检索和短上下文调度，比一味扩展 context window 更划算。
