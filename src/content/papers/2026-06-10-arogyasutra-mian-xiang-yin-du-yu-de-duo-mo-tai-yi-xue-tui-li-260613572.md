---
title: 'ArogyaSutra: A Multi-Agent Framework for Multimodal Medical Reasoning in Indic
  Languages'
title_zh: ArogyaSutra：面向印度语的多模态医学推理多智能体框架
authors:
- Tanmoy Kanti Halder
- Akash Ghosh
- Subhadip Baidya
- Arijit Roy
- Sriparna Saha
affiliations:
- Indian Institute of Technology Patna
- Indian Institute of Technology Kanpur
- Prasannadeb Women's College
arxiv_id: '2606.13572'
url: https://arxiv.org/abs/2606.13572
pdf_url: https://arxiv.org/pdf/2606.13572
published: '2026-06-10'
collected: '2026-06-14'
category: MultiAgent
direction: 多智能体医学推理 · 多模态多语言
tags:
- Multi-Agent
- Multimodal
- Medical Reasoning
- Actor-Critic
- Indic Languages
- Tool Grounding
one_liner: 构建多语言多模态医学数据集并提出 actor-critic 多智能体框架，融合工具与双记忆机制提升推理精度。
practical_value: '- **Actor-critic 多智能体协作范式可迁移至电商客服或导购 Agent**：Actor 生成动作（如查询商品、调用
  API），Critic 评估合理性并存入双记忆（成功/失败轨迹），在线蒸馏后可压缩为小型决策模型，适合高并发场景。

  - **双记忆机制（成功经验池 + 失败经验池）可用于推荐 Agent 的反思与纠错**：在商品推荐、参数解析错误时，失败记忆提供负样本，配合 critic 评分驱动策略改进，比单纯正样本微调更稳健。

  - **工具接地（tool grounding）思路可借鉴到电商搜索 Agent**：将商品数据库、优惠规则、物流 API 等封装为工具，多智能体通过调用工具而非依赖模型记忆事实，减少幻觉，尤其适合频繁更新的促销活动。

  - **多语言低资源场景的蒸馏策略**：用教师多智能体在丰富数据上模拟推理轨迹，再蒸馏到学生模型，可快速覆盖小语种或方言搜索场景，降低标注成本。'
score: 7
source: huggingface-daily
depth: abstract
---

现有医疗多模态大模型（MLLM）以英文为中心，难以处理印度语言的复杂医学查询与多模态输入（如 X 光片），限制了低资源地区的医疗 AI 可及性。为此，作者首先构建了 ArogyaBodha——跨 8 个异构来源、覆盖 31 个身体系统、6 种影像模态和 21 个临床领域的大型多语言多模态医学问答数据集，包含英文和 7 种主要印度语言。在此基础上提出 ArogyaSutra，一个基于 actor-critic 的多智能体框架：Actor 负责逐步推理并调用医学工具（如症状检查器、影像分析器），Critic 对其决策进行动态评分；框架引入双记忆机制，分别存储成功与失败的推理轨迹，并通过存储的 actor-critic 仿真轨迹进行蒸馏，将协作智能体的知识压缩至单个学生模型。实验表明，该框架在所有印度语言上均提升了医学推理准确率，消融实验证实了各模块的有效性。
