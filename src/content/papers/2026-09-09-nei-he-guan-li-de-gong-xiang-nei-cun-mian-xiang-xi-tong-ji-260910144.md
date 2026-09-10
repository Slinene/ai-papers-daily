---
title: Kernel-Managed Shared Memory for System-Wide Personalization
title_zh: 内核管理的共享内存：面向系统级个性化的多智能体基础设施
authors:
- Ryan Lum
- Yongfeng Zhang
affiliations:
- Rutgers University
arxiv_id: '2609.10144'
url: https://arxiv.org/abs/2609.10144
pdf_url: https://arxiv.org/pdf/2609.10144
published: '2026-09-09'
collected: '2026-09-10'
category: MultiAgent
direction: 多智能体共享记忆与个性化基础设施
tags:
- Multi-Agent
- Shared Memory
- Personalization
- LLM
- Agent Infrastructure
- RAG
one_liner: 将多智能体个性化记忆的检索、隐私与注入集中到系统内核，以更低延迟和 token 成本获得与全量上下文接近的效果
practical_value: '- **统一记忆管理层**：在电商/广告多 Agent 系统（如商品推荐 Agent、用户助手、客服 Agent）中，将用户画像/会话记忆的检索、隐私过滤、格式化与注入上移到中心服务，避免每个
  Agent 各自实现导致逻辑重复与隐私漏洞。

  - **写屏障保证一致性**：当多个 Agent 异步写入用户偏好或任务状态时，用 per-user 序列号 + 等待写确认的机制确保读后写一致，防止推荐/对话中因竞态缺失最新画像。

  - **格式化记忆为自然语言**：对 7B/8B 小模型，将结构化 JSON 画像转成自然语言语句再注入 prompt，可明显提升利用效果；结构化存储仅用于检索和审计。

  - **成本-效果权衡**：不要默认拼接全量上下文，而是用检索截断后的精选记忆（top-k + token 预算），在效果接近的情况下延迟可降低 15–61%，适合线上高并发推荐/对话场景。

  - **显式身份解析优先级链**：多用户并发时按“请求标识 → 最近会话 → 历史注册 → Agent 自身”的顺序解析用户 ID，可有效避免交叉污染，值得在用户画像服务中复用。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
多智能体系统中，不同 Agent 学到的用户上下文彼此隔离，导致系统级个性化不一致；各 Agent 自行管理记忆又会重复实现检索、隐私过滤与注入逻辑，且容易产生隐私泄漏和竞态问题。标准 RAG 检索时常忽略稳定画像（profile）信息，而全量上下文拼接成本过高。

## 方法关键点
- 提出内核管理的共享内存：Agent 只负责写结构化带标签记忆，系统内核统一负责身份解析、写排序、隐私过滤、检索、排序、格式化与 prompt 注入。
- 实现于 AIOS，实例化三个 Agent：ProfileAgent 提取稳定偏好，TaskAgent 提取短期任务上下文，AssistantAgent 无检索直接消费内核注入的上下文。
- 记忆元数据包含 owner_agent、user_id、memory_type、sharing_policy；可见性规则由内核静态强制，私有记忆对非拥有 Agent 恒不可见，实现隐私不变量。
- 写屏障：每个用户维护单调递增序列号，检索前等待该用户所有已分配写操作确认，保证读后写一致性，避免异步写导致的上下缺失。
- 注入前将结构化 JSON 格式化为自然语言语句，提升小模型利用效果；按语义相关性排序并截断到 token 预算。

## 关键实验
在 GPT-4o、Llama-3.1:8B、Qwen-2.5:7B 三个模型上进行 1,800 次合成个性化试验，用 GPT-5.4 按 Profile Usage、Task Usage、Integration 三维度评分（1–5）。

主要结果：
- 对比未管理的外部记忆后端 Mem0（相同底层存储），内核管理使个性化分数提升 2.4–4.0 分，所有比较 p<10⁻¹⁸；例如 GPT-4o Profile 从 1.05 升至 4.69。
- 对比标准 RAG，内核方法同样大幅显著领先，因为 vanilla_rag 的 profile 分数始终停滞在 ~1.84，而 task 分数较高，说明检索系统会丢弃稳定画像。
- 对比全量上下文拼接（naive_concat），内核管理在 GPT-4o 和 Qwen 上统计持平，在 Llama-3.1 上部分维度略低，但端到端延迟降低 15–61%（GPT-4o 7.5s vs 19.2s；Qwen 26.3s vs 36.3s）。
- 人类验证（30 条盲评）确认 kernel_shared 与 naive_concat 平均分均为 4.17，远高于 mem0_default 的 1.00；私有记忆泄漏为 0/450。

## 最值得记住的一句话
把记忆管理上移到系统内核，将检索、隐私、注入变成基础设施能力，可以在大幅降低延迟和 token 成本的同时，获得与全量上下文相当的个性化质量。
