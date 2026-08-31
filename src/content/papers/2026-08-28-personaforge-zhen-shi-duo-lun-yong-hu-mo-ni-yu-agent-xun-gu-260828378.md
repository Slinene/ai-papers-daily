---
title: 'PersonaForge: Realistic Multi-Turn User Simulation for Agentic Systems'
title_zh: PersonaForge：真实多轮用户模拟与 Agent 训练评估
authors:
- Hanglong Lv
- Dawei Zhu
- Lei Li
- Bowen Ye
- Huaqiu Liu
- Yifan Song
- Bofei Gao
- Weimin Xiong
- Jinhao Dong
- Chenhong He
affiliations:
- Peking University
- Xiaomi LLM-Core
- The University of Hong Kong
- Renmin University of China
arxiv_id: '2608.28378'
url: https://arxiv.org/abs/2608.28378
pdf_url: https://arxiv.org/pdf/2608.28378
published: '2026-08-28'
collected: '2026-08-31'
category: Agent
direction: Agent 用户模拟 · 多轮交互训练
tags:
- User Simulation
- Agentic Systems
- Multi-turn Dialogue
- Data Synthesis
- Persona Modeling
- Benchmark
one_liner: 构建 SOUL 驱动的真实多轮用户模拟器，从真实查询反向生成 6.3K 训练数据与 138 任务基准，显著提升 Agent 交互效率与任务完成率
practical_value: '- 构建电商导购/客服 Agent 的多轮训练数据时，优先从真实搜索/会话日志的种子 query 出发，用 LLM 反向推断用户画像与
  connected memory，而不是随机生成 persona；这样能保留隐藏意图，让模型学会逐步澄清需求。

  - 用户模拟器的提示词可采用 SOUL 结构：身份段落 + 抽象行为参数（消息长度、正式度、emoji）+ connected memory 固化 session
  事实；避免用具体 utterance 示例，防止多样性崩溃。这一设计可迁移到任何对话式推荐/客服的仿真用户。

  - 在数据合成 pipeline 中预设三阶段质量控制：生成前检查 persona 一致性，运行时用消息长度阈值（如 1500 字符，真实用户 99.2% 以下）检测角色反转，后处理过滤退化模式；可有效降低合成数据污染。

  - 评测多轮推荐/搜索 Agent 时，设计渐进信息披露和嵌入矛盾的任务，并按交互效率、工具适当性、任务完成、回复质量四维打分；论文表明这类数据训练后轮次减少约
  20%、无效工具调用大幅下降，同时任务完成率提升，对线上体验直接有益。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

动机：
真实用户与 Agent 的交互远非信息完整的一轮查询。论文分析 16K 真实会话发现 75.9% 为多轮，中位用户轮数 10，平均工具调用 99；38.7% 的多轮会话包含显式纠正，且 36% 的纠正出现在工具执行之后。现有训练语料和评测基准大多假设首轮 query 完整，造成 Agent 训练与真实使用脱节。

方法关键点：
- Profile Construction：4 维 persona 空间（occupation 70 / MBTI 16 / tech proficiency 3 / knowledge background 25），通过兼容规则保证一致性；Reverse Deep Construction 从真实种子 query（WildChat、LMSYS-Chat-1M）反推 persona 和 connected memory，使隐藏上下文有据可依。
- Conversation Generation：SOUL 提示结构包含身份、抽象行为参数、沟通风格和 connected memory；模拟器与目标系统信息不对称，逐步披露意图、引入矛盾或纠正；行为规则限制简短、每轮一问、主动验证、自然终止。
- Quality Control：pre-generation 检查 persona 一致性，runtime 用 1500 字符阈值检测角色反转，后处理过滤退化模式；最终 6.3K 会话、430K 消息，96% 多轮，平均 9.3 用户轮。

关键实验：
在 138 任务 PersonaForge-Bench 上评估。Qwen3.5-27B 综合 +4.1%，Task Completion +6.0%，Response Quality +6.8%；MiMo-V2-Flash 综合 +15.7%（Task Completion +22.0%，Tool Appropriateness +10.1%）。消融显示 connected memory 和 adaptive simulation 贡献最大；训练后 MiMo 轮次 -20.7%、工具调用 -9.2%、web_fetch -54.2%，且泛化到 held-out CLAW-EVAL。

最值得记住的一句话：
真实用户与 Agent 的交互是多轮、渐进披露和纠正式闭环；用 grounded SOUL 用户模拟器生成的数据训练，能显著提升 Agent 的交互效率与任务完成。
