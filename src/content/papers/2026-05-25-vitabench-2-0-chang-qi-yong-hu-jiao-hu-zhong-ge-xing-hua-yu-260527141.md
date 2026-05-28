---
title: 'VitaBench 2.0: Evaluating Personalized and Proactive Agents in Long-Term User
  Interactions'
title_zh: VitaBench 2.0：长期用户交互中个性化与主动智能体基准
authors:
- Yuxin Chen
- Yi Zhang
- Zhengzhou Cai
- Yaorui Shi
- Zhiyuan Yao
- Chenhang Cui
- Jingnan Zheng
- Yaqi Huo
- Xi Su
- Qi Gu
affiliations:
- National University of Singapore
- Meituan
- University of Science and Technology of China
- Beijing University of Posts and Telecommunications
- Zhejiang University
arxiv_id: '2605.27141'
url: https://arxiv.org/abs/2605.27141
pdf_url: https://arxiv.org/pdf/2605.27141
published: '2026-05-25'
collected: '2026-05-28'
category: Eval
direction: 大模型智能体个性化与主动性评估基准
tags:
- Personalization
- Proactive Agents
- LLM Agents
- Benchmark
- Memory
- User Preference Modeling
one_liner: 提出面向长期交互的个性化与主动性评估基准，揭示前沿LLM智能体在偏好推理、记忆利用和主动交互上严重落后于实际需求。
practical_value: '- **个性化评估维度拆解**：在推荐或对话智能体设计中，可借鉴本工作将个性化能力分解为偏好提取（从隐式行为中推理）、利用（决策时遵循偏好）和更新（应对偏好漂移）三个可量化环节，构建分层评估与诊断体系。

  - **记忆机制的现实瓶颈**：实验表明无论 Agentic Memory 还是 RAG Memory，当前模型在长期交互中都无法有效利用记忆，反而导致性能下降（Avg@4
  低于 Full Context）。在业务系统中应避免过度信任记忆，需配套主动压缩、冲突消解和多轮校验策略。

  - **主动交互是差异化能力**：主动任务得分比个性化任务低 ~40%，模型往往在信息缺失时强行决策而非发起澄清。在电商导购或售后场景，可显式训练/提示智能体识别“信息缺口”并触发追问，提升用户体验。

  - **偏好利用比提取更难**：即使提供真实偏好，Strong Model 也只有约 50% 的 Pass@4，说明模型难以在复杂工具调用中持续遵循偏好。在生成式推荐中，可考虑将用户偏好向量绑定到工具选择与参数生成的全链路，而非仅作为上下文。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有 LLM Agent 基准（如 τ-bench、SWE-bench）主要衡量推理和工具使用能力，假设任务所需信息已在上下文中显式给出。然而真实世界中，用户意图常隐含在碎片化的长期交互中，Agent 需持续提取、利用并更新偏好，同时主动识别信息缺口。这一个性化与主动性挑战缺少系统评估，VitaBench 2.0 填补该空白。

**方法关键点**  
- **用户建模**：构建 56 名用户、2000+ 条细粒度偏好，覆盖饮食、出行、购物等维度。偏好随时间演化（新增/删除/修改），嵌入对话与行为日志。  
- **任务设计**：每个用户对应一个时间序列任务集，跨越外卖配送、到店消费、在线旅行三大领域，共 66 个工具。每个任务包含查询、工具集、可执行环境和评价量规，要求 Agent 从历史交互中推断偏好并完成个性化决策。  
- **主动性评估**：引入主动任务，Agent 需识别缺少的条件信息（如用户情绪影响活动推荐），在行动前主动询问，否则任务失败。  
- **记忆接口**：提供可扩展的 Update/Retrieve 接口，实现 Agentic Memory（Agent 自主决定存什么）和 RAG Memory（向量检索）两种模式，支持控制变量对比。

**关键实验**  
- **模型**：覆盖 GPT-5、Claude-Opus-4.6、DeepSeek-R1、Gemini-2.5-Pro 等 20+ 前沿模型，分为思考/非思考模式。  
- **结果**：最强模型 Claude-Opus-4.6 在 Full Context 下 Avg@4=0.503、Passˆ4=0.337；启用思考模式未带来一致提升，主动任务得分 ~27（相比个性化 ~46）。提供真实偏好后，性能仍只有约 0.52，说明偏好利用也是瓶颈。随着任务序列推进，性能持续下降；失败分析表明偏好相关错误占比最高，强模型工具错误减少但偏好错误反而上升。

**核心结论一句话**：当基础推理与工具使用能力增强后，个性化成为制约 Agent 实用化的首要瓶颈，现有记忆机制远未解决长程偏好建模与主动交互问题。
