---
title: 'SkillsVote: Lifecycle Governance of Agent Skills from Collection, Recommendation
  to Evolution'
title_zh: SkillsVote：Agent 技能生命周期治理框架
authors:
- Hongyi Liu
- Haoyan Yang
- Tao Jiang
- Bo Tang
- Feiyu Xiong
- Zhiyu Li
affiliations:
- MemTensor (Shanghai) Technology
arxiv_id: '2605.18401'
url: https://arxiv.org/abs/2605.18401
pdf_url: https://arxiv.org/pdf/2605.18401
published: '2026-05-17'
collected: '2026-05-20'
category: Agent
direction: Agent 技能生命周期管理与受控进化
tags:
- Agent Skills
- Skill Library
- Recommendation
- Evolution
- Attribution
- Lifecycle Governance
one_liner: 将 Agent 技能视为生命周期制品，通过归因控制实现从采集、推荐到进化的闭环，提升长期任务表现。
practical_value: " - 技能库的质量治理：对技能进行环境需求、质量、可验证性 profiling，只允许通过验证的技能进入推荐池，避免低质量技能污染上下文。电商知识库或工具库可借鉴相似准入设计。\n\
  \ - 任务前技能精炼：不将全量技能直接暴露给 agent，而是通过一次 agentic search 生成精简的技能集与使用指南，降低无关上下文的干扰。类似在\
  \ RAG 中，用轻量 agent 先检索、再压缩后再送入主模型。\n - 执行后归因与证据门控：将长轨迹按子任务切分，区分结果是由技能引导、自主探索还是环境因素导致，仅将可复用的成功探索用于技能库更新。对于电商多步\
  \ Agent 的对话/操作日志，可借此提取高置信度经验并避免误更新。\n - 离线 + 在线进化组合：先用历史任务构建冷启动技能库，再在新任务流中在线增量进化。生成式推荐系统中，可先用离线数据训练初始知识库（如促销规则），再通过线上反馈受控扩展。"
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
长链 LLM Agent 执行会留下轨迹，但原始轨迹噪声大、难以复用。社区已出现大量 Agent 技能（SKILL.md）生态，然而这些技能冗余、质量参差不齐，且无差别更新容易污染未来上下文。因此需要一个治理框架，控制哪些技能在任务前暴露给 agent，以及哪些执行证据能够回写技能库。  

**方法关键点**  
- **技能库构建与画像**：从 GitHub 采集百万级开放技能，对每个技能进行环境需求、质量、可验证性三维画像；对通过验证的技能自动合成可执行任务，记录实际运行表现。  
- **推荐即 agentic search**：任务执行前，用一个单独的推荐 agent 在技能库目录中检索、阅读 SKILL.md 和相关资源，选出少量高相关、低冗余的技能，并生成压缩后的使用指南注入主 agent 的指令中，而非将全库直接暴露。  
- **子任务级归因**：执行后，将完整轨迹分解为子任务（最小语义完整单元），记录每个子任务的结果证据类型（环境反馈/人工偏好/无信号），并将成败归因于技能、自主探索或环境因素。  
- **证据门控进化**：只有成功且包含可复用探索的子任务才允许触发技能更新；对同一改进多次出现的证据做聚合，以最小改动编辑现有技能或创建新技能，禁止无证据或弱证据的写入。  

**关键结果**  
- Terminal‑Bench 2.0：离线进化（从48个历史任务构建库）将 GPT‑5.2 的准确率提升 **+7.9 pp**，GPT‑5.4 mini 提升 +5.8 pp；在线进化（从空库开始）分别提升 +2.7 pp 和 +1.1 pp。  
- SWE‑Bench Pro：在线进化使 GPT‑5.2 解决率从 47.6% 升至 50.2%（+2.6 pp），GPT‑5.4 mini 从 46.9% 升至 49.0%（+2.1 pp）。  
- 推荐消融：不加推荐直接暴露技能库时负迁移显著（平均损失‑6.7 pp），加入推荐后损失消失，正收益由 +3.3 pp 提至 +6.0 pp。  

**最值得记住的一句话**  
技能库进化必须由**证据‑归因‑门控**闭环驱动，否则无差别更新会污染 agent 上下文，抵消覆盖面的增益。
