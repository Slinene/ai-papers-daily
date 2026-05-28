---
title: 'STREAM: A Data-Centric Framework for Mining High-Value Task-Oriented Dialogues
  from Streaming Media'
title_zh: STREAM：基于流媒体挖掘高价值任务型对话的数据中心框架
authors:
- Liang Xue
- Haoyu Liu
- Cheng Wang
- Pengyu Chen
- Haozhuo Zheng
- Yang Liu
affiliations:
- Harbin Institute of Technology
- Byering Technology
arxiv_id: '2605.25162'
url: https://arxiv.org/abs/2605.25162
pdf_url: https://arxiv.org/pdf/2605.25162
published: '2026-05-23'
collected: '2026-05-28'
category: RecSys
direction: 任务型对话数据合成 · 流媒体挖掘
tags:
- task-oriented dialogue
- data synthesis
- streaming media
- RAG
- dialogue state tracking
- persona-driven generation
one_liner: 从公开直播/短视频中提取真实交互信号，合成大规模富含策略的任务型对话数据StreamDial
practical_value: '- **利用公开流媒体替代人工标注**：直播、短视频中的客服咨询与用户弹幕可提取为（问、答、策略）三元组，低成本构建垂直领域对话语料。

  - **对话蓝图（Conversational Blueprint）显式规划对话节奏**：将对话阶段、关键节点、应对策略结构化，可借鉴到电商售前咨询场景，提升多轮谈判、需求挖掘的连贯性。

  - **RAG增强的对话生成模式**：结合知识库与历史对话样本检索，生成知识密集型回复，适用于商品推荐、库存查询等需实时信息注入的对话。

  - **四元组数据格式提供丰富监督信号**：<用户人设，客服人设，对话蓝图，历史>的结构可同时训练角色扮演和策略跟随能力，有利于构建可控的对话推荐Agent。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：垂直领域的高价值任务型对话数据面临三难困境——专家标注昂贵、真实客服对话受隐私限制、静态语料时效性差。过往仿真方法缺乏真实用户意图分布和策略深度，而流媒体（直播、短视频）中沉淀了大量真实的客服-用户交互，包含长尾意图、决策模式和领域知识，却未被系统利用。

**方法关键点**：本文提出STREAM四阶段合成框架。
- **SSI（流信号摄取）**：从网页、直播、短视频中提取原子交互信号，包括用户问题、客服回复、问答对、对话策略标签和账号元数据，并通过ASR校正、语义对齐、证据检查进行清洗。
- **APS（自适应人设合成）**：基于上述信号分别构建用户人设（目标、约束、表达风格）和客服人设（角色、话术、知识边界），实现角色级真实感。
- **CB（对话蓝图构建）**：生成包含阶段节奏、关键节点、典型场景应对和路径图谱的结构化蓝图，为多轮对话提供战略级规划。
- **IDG（交互式对话生成）**：采用RAG机制，从种子对话中检索相似上下文作为行为参考，用户模拟和客服生成的循环使用双向检索增强，并通过图聚类过滤冗余，输出四元组<用户人设，客服人设，蓝图，历史>。

**关键实验**：基于该框架发布**StreamDial**数据集，覆盖汽车、餐厅、酒店三领域，共87,498个会话、1,497,320轮，平均17.11轮/会话。内在质量评估中，三款LLM裁判（Qwen3-Max、GPT-5.2、Gemini3-Pro）一致给出更高的信息量、多样性和灵活性评分；人类评估也确认了信息密度和灵活性的优势。下游DST任务上，在固定2k训练数据规模下，用 **1k公开数据 + 1k StreamDial混合训练**，相比纯公开数据，Qwen3-1.7B、8B、Gemma3-4B的JGA分别提升至96.97%、96.72%、97.98%，且跨领域和多语言迁移（英、法、韩）均有正向增益。

**一句话记住**：公开流媒体是高质量、富含策略的任务型对话数据矿山，通过信号提取-人设-蓝图-RAG的流水线，可系统性合成比人工标注更丰富、更灵活的垂直领域对话，显著提升对话状态追踪的监督效果。
