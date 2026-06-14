---
title: Adaptive Turn-Taking for Real-time Multi-Party Voice Agents
title_zh: 多方实时语音代理的自适应轮流说话
authors:
- Soumyajit Mitra
- Prabhat Pandey
- Abhinav Jain
- Shanmukha Sahith
- K V Vijay Girish
affiliations:
- Amazon AGI
- IIT Kharagpur
arxiv_id: '2606.13544'
url: https://arxiv.org/abs/2606.13544
pdf_url: https://arxiv.org/pdf/2606.13544
published: '2026-06-11'
collected: '2026-06-14'
category: Agent
direction: 多方语音代理 · 流式推理与角色扮演
tags:
- Turn-taking
- Multi-party
- Voice Agent
- Speech LLM
- Chain-of-Thought
- Role-Playing
one_liner: 提出 ModeratorLM，根据分配角色自适应调整多方语音对话中的轮流行为，精度提升超40%，召回提升超70%。
practical_value: '- **角色条件控制代理行为**：在电商客服或语音导购场景中，可为代理显式指定角色（如促销导购、售后专员），模型将根据角色调整轮候策略和响应风格，提升对话自然度。

  - **流式 chunk-wise 推理与 CoT 增强**：采用分块流式语音大模型，结合 Chain-of-Thought 推理，可在低延迟下完成复杂的轮流决策，适合对实时性要求高的电音语音交互。

  - **合成对话数据生成**：RolePlayConv 数据集构造方法利用了角色多样性合成，可低成本生成特定业务场景的训练数据，减少人工标注成本。

  - **减少误打断**：提出的方法显著降低误打断率，在呼叫中心或语音工单等场景中可避免重复澄清，改善用户体验。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有语音代理在双人对话中可通过声学/语义线索实现轮流说话，但在多方对话中面临重叠语音、动态抢话和非中心化的轮次分配，难以准确判断何时开口与闭嘴。

**方法**：提出 ModeratorLM，一个基于角色扮演的语音代理。核心是让代理根据显式分配的角色（如主持人、参与者等）调节其轮流行为。系统构建在 chunk-wise 流式语音大模型上，实时处理语音流，并引入推理增强变体，在对话上下文基础上进行 Chain-of-Thought 推理以做出轮次决策。同时构造了大规模合成数据集 RolePlayConv，包含多种角色和对话场景。

**结果**：在真实会议数据和 RolePlayConv 上，相比无条件基线，ModeratorLM 的轮流说话精度提升超过 40%，召回率提升超过 70%，误打断次数大幅减少，证实了角色条件与推理增强对多方对话轮流管理的有效性。
