---
title: 'Beyond Static Dialogues: Benchmarking Realistic, Heterogeneous, and Evolving
  Long-Term Memory'
title_zh: RHELM：真实、异构、演化的长期记忆评测基准
authors:
- Han Zhang
- Zihao Tang
- Xin Yu
- Xiao Liu
- Yeyun Gong
- Haizhen Huang
- Yan Lu
- Weiwei Deng
- Feng Sun
- Qi Zhang
affiliations:
- Renmin University of China
- Microsoft
arxiv_id: '2605.31086'
url: https://arxiv.org/abs/2605.31086
pdf_url: https://arxiv.org/pdf/2605.31086
published: '2026-05-29'
collected: '2026-06-01'
category: Eval
direction: LLM长期记忆评估基准
tags:
- Long-term Memory
- LLM Evaluation
- Heterogeneous Data
- Persona
- LOOP Module
- Misleading Queries
one_liner: 提出LOOP模块驱动动态多源对话，定义27项记忆特征，揭示LLM在真实场景中的严重记忆缺陷
practical_value: '- **用户画像动态演化机制**：LOOP模块的“规划-推演-演化-修剪”循环可复用于电商Agent的用户画像更新，通过概率化正面/负面结果推演，使对话长期一致且状态动态演变，避免画像僵化。

  - **异构记忆融合设计**：借鉴RHELM将对话流与外部文档（报告、邮件）在时间线上对齐的做法，在推荐或客服系统中整合多源信息（用户聊天、浏览记录、工单），提升对用户全维理解。

  - **误导查询压力测试**：引入“记忆条件误导查询”维度，主动构造与用户历史状态冲突的请求，检测模型是否盲目遵循指令。可移植到电商Agent的意图冲突检测，避免对已退货商品继续推荐或执行矛盾操作。

  - **Verifier辅助数据质检**：在合成训练或评估数据时，采用分阶段Verifier自动校验语义一致性，可降低人工成本并保障数据质量，适合大规模生成式推荐场景的数据管线。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
现有LLM记忆测评基准存在三大缺陷：对话段语义割裂，用户画像扁平静态；信息源单一，仅限纯文本会话，忽略报告、邮件等异构数据；查询往往只求显式事实，未触及记忆条件下的用户状态冲突。这导致测评脱离真实助手应用场景，难以反映模型在动态、多源、需状态推理时的记忆能力。为此，RHELM构建了一个高仿真长期记忆基准，模拟用户长达一年的生活轨迹，整合异构外部数据，并设计7类27项挑战性记忆特征，以系统性暴露当前方法的弱点。

**方法关键点**  
- **六维用户画像**：从身份、性格、特质、关系、物品、当前状态六个维度构建结构化画像，通过JSON schema约束保证动态更新的一致性和可控性。
- **LOOP生成机制**：循环执行“规划→推演→演化→修剪”，以概率p控制事件正负走向，让用户轨迹自然产生长尾波动和突发转折，确保对话的时空语义一致性。
- **异构外部源合成**：基于每日事件生成专业报告、个人日志、邮件等多种格式文本，利用Deep Research方法提升真实感和信息密度。
- **7类27项记忆特征**: 包括事实多跳、时间推理、信息聚合、幻觉检测、误导查询等，其中新颖的“误导查询”要求模型在检测到用户请求与其历史状态冲突时主动拒绝并提供约束符合的替代方案。
- **全流程Verifier审计**：在每个生成环节部署自动校验，输出评估报告供人工复核，最终问题保留率约40%，确保高质量评估。

**关键实验与结果**  
在10个用户、共计1,1764轮对话、2,180个外部文件、上下文500k-1M token的测试集上，评估了全上下文模型（GPT-4.1-mini、Gemini-2.5-Flash-Lite、Qwen2.5-14B-1M）、RAG基线（不同K值、混合检索）以及三个记忆框架（MemGPT、Mem0、MemU）。关键发现：①最强模型Claude Opus 4.5在含外部源时平均准确率仅38.1%；②误导查询下几乎所有方法准确率低于5%；③增加RAG检索量反致幻觉类性能下降（如从13.2降至11.2）；④检索召回率在Top-50时仍不足0.6，跨源聚合和上下文推理是主要瓶颈。最差特征集中在“隐式状态冲突与主动响应”（3.1%）和“相对位置定位”（10.5%），说明当前模型远不具备可靠的多源记忆与状态推理能力。
