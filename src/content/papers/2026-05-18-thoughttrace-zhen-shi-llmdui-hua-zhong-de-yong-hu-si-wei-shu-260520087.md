---
title: 'ThoughtTrace: Understanding User Thoughts in Real-World LLM Interactions'
title_zh: ThoughtTrace：真实LLM对话中的用户思维数据集
authors:
- Chuanyang Jin
- Binze Li
- Haopeng Xie
- Cathy Mengying Fang
- Tianjian Li
- Shayne Longpre
- Hongxiang Gu
- Maximillian Chen
- Tianmin Shu
affiliations:
- Johns Hopkins University
- Massachusetts Institute of Technology
- Google Research
arxiv_id: '2605.20087'
url: https://arxiv.org/abs/2605.20087
pdf_url: https://arxiv.org/pdf/2605.20087
published: '2026-05-18'
collected: '2026-05-21'
category: RecSys
direction: 用户思维采集与对齐 · 用户行为预测
tags:
- user thoughts
- human-AI interaction
- dataset
- alignment
- behavior prediction
- conversational AI
one_liner: 首个大规模用户思维数据集，揭示对话中未言明的意图与反应，并展示其在行为预测与模型对齐中的价值。
practical_value: '- 电商对话推荐：采集用户未显式表达的任务动机、内容/风格期望等‘理由’，构建用户意图特征，提升对话式推荐中自然语言理解的深度。

  - Agent对齐：用户对助手回复的‘反应’（如内容相关性、呈现风格不满）可直接作为细粒度偏好信号，用于DPO/RLHF训练，比从后续消息推断偏好更准确、更密集。

  - 用户模拟器：训练模型同时预测下一轮消息及对应的思考（理由+反应），生成更贴近真实用户认知过程的模拟对话，用于离线评估和强化学习环境。

  - 工程落地：若业务场景允许，可在交互后收集用户事后标注的‘当时想法’，作为高价值训练信号；即使非侵入式，也可将点击、停留时长等作为思考的弱代理变量。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有对话AI数据集仅捕获用户说了什么，完全忽略其内心思考，如任务动机、上下文约束、对回复的隐性评价等。这些未言明的认知背景直接影响对话走向和满意度，但在真实交互中大量流失。为填补这一空白，作者提出用户思维（thoughts）作为新数据模态，并首次大规模采集真实对话中用户的自我报告思维。

**方法**  
- 构建实时对话标注平台，招募1058名参与者在20个不同对话模型上完成真实任务，并在每轮发送消息前标注‘理由’（为何这样问），对每轮助手回复标注‘反应’（有何感受）。  
- 最终得到2155段对话、17058轮交互、10174条思考标注，附带人口统计和AI使用习惯元数据。  
- 思考分为7类理由（如任务动机、上下文约束、内容/风格期望）和5类反应（如明确肯定、内容相关性不满、呈现风格不满等）。  
- 通过嵌入距离、LLM语义覆盖评分及前沿模型推断实验，证明思考与表面消息存在显著差异且难以从上下文自动推断。

**关键结果**  
- 思考与消息的语义重叠度有限：理由的平均覆盖得分仅3.22/5，反应更只有2.00/5。  
- 前沿LLM推断思考的平均相似度仅2.93（理由）和2.54（反应），证实其隐式性。  
- 思考增强的下一轮用户消息预测相比纯对话历史带来41.7%的相对提升。  
- 基于思考的不满反应生成思考引导的改写（thought-guided rewrites），并用DPO微调Qwen3.5-4B，在Arena-Hard上比消息引导改写高4.5%，比基准模型提升25.6%，同时发现思考能捕获2.2倍于消息的负面反馈。

**核心洞察**  
“用户思考是对话中的‘暗物质’——不显式出现，却主宰着交互的引力方向。一旦被显性标注，它就变成预测意图和校准偏好的最强监督信号。”
