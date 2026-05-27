---
title: 'MuChator: Enabling Active Music Discovery via Conversational Music LLMs in
  Douyin Music'
title_zh: MuChator：基于对话式音乐LLM的抖音音乐主动发现框架
authors:
- Jiahao Liang
- Linzhi Huang
- Xuannan Liu
- Xukai Wang
- Xuanpu Luo
- Yongchun Zhu
- Jingwu Chen
- Feng Zhang
- Xiao Yang
affiliations:
- ByteDance
arxiv_id: '2605.27103'
url: https://arxiv.org/abs/2605.27103
pdf_url: https://arxiv.org/pdf/2605.27103
published: '2026-05-26'
collected: '2026-05-27'
category: RecSys
direction: 生成式推荐 · 对话推荐 · MusicLLM
tags:
- MusicLLM
- Conversational Recommendation
- Multi-stage Pre-training
- GRPO
- Preference Alignment
- Next-behavior Prediction
one_liner: 提出端到端对话音乐LLM框架MuChator，通过三阶段预训练注入知识/偏好、自动合成指令微调及混合奖励GRPO对齐，线上活跃天数提升46.49%
practical_value: '- **多阶段课程注入领域知识**：分阶段预训练（客观元数据→主观评论/播放列表→个性化行为序列）逐步提升LLM对垂直领域的理解，可迁移到电商中渐进融入商品知识、用户评论和购买偏好。

  - **下一行为预测统一序列建模**：将物品推荐和用户反馈（点赞、跳过）交织成自回归序列，提供更稠密的监督信号，提升训练效率，适合电商的点击/加购/转化序列联合建模。

  - **自动化指令数据合成pipeline**：通过语义聚类、候选检索和个性化模型打分过滤，低成本构建高质量用户-查询-物品指令对，可用于快速搭建对话推荐或Agent的任务数据。

  - **混合奖励与GRPO对齐**：结合模型奖励（相关性/个性化）与规则奖励（格式、事实性、多样性、去重），并以二值门控强制查询-物品相关性，可复用到电商对话推荐，确保推荐既符合意图又满足业务约束。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：抖音音乐沉浸式Feed流推荐无法满足用户主动、情境化且模糊的音乐发现需求（如“刚升职加薪，推荐什么歌？”）。直接应用LLM存在缺乏音乐领域知识、难以协同推理音乐-查询相关性、不理解个性化偏好三大难题，导致在线收益不及传统检索系统。

**方法关键点**：
1. **三阶段音乐知识预训练**：课程学习策略逐步注入客观音乐知识（元数据、百科、歌词描述）、主观知识（评论、播放列表、关系）和个性化偏好（用户画像、行为序列），并提出**下一行为预测**将物品推荐与反馈预测统一为自回归序列，提升训练效率与密度。
2. **上下文感知指令微调**：通过自动化pipeline合成用户-查询-音乐三元组：先语义聚类查询，再按用户收藏检索候选，最后用个性化奖励模型过滤出top10歌曲，构造UQ2I监督数据。
3. **混合奖励偏好对齐**：设计模型奖励（二元相关性门控×个性化分数）与规则奖励（格式、事实性、多样性、去重），采用GRPO强化学习优化，强制优先查询相关性，再精确匹配个人偏好。

**关键结果**：
- 离线评测：MuChator个性化8.4、相关性89.1%、多样性51.1%、事实性99.3%，全面超越GPT-5.2、Gemini-3-Pro及Qwen3-8B SFT/RAG。
- 在线A/B：对比内部音乐搜索系统，活跃天数**+46.49%**，播放时长**+77.36%**，CTR**+11.26%**。
- 消融实验：三阶段课程预训练优于混合预训练，逐步加入用户上下文各组件（画像、状态、反馈）持续降低个性化PPL，取消相关性门控或个性化奖励均导致对应指标下降。

**一句话核心**：在LLM中按课程顺序注入领域知识并统一物品与反馈预测，再通过混合奖励GRPO对齐，是让生成式模型胜任复杂、个性化对话推荐的实用路线。
