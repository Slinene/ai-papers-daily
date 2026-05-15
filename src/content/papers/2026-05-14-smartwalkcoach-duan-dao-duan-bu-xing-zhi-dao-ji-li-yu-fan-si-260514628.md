---
title: 'SmartWalkCoach: An AI Companion for End-to-End Walking Guidance, Motivation,
  and Reflection'
title_zh: SmartWalkCoach：端到端步行指导、激励与反思的AI伴侣
authors:
- Xianzhe Zhang
- Mingxuan Hu
- Bufan Xue
- Erick Purwanto
- Thomas J Selig
- Daniel Yonto
affiliations:
- 西安交通利物浦大学
arxiv_id: '2605.14628'
url: https://arxiv.org/abs/2605.14628
pdf_url: https://arxiv.org/pdf/2605.14628
published: '2026-05-14'
collected: '2026-05-15'
category: Agent
tags:
- Agent
- mHealth
- Conversational AI
- JITAI
- Context-aware
- Walking
one_liner: 集成路线规划、情境陪伴与总结反思的移动AI伙伴，实证表明动机性对话大幅提升用户积极情感和体验
score: 9
source: arxiv-cs.HC
depth: full_pdf
---

**动机**
步行有益身心健康，但现有App要么侧重导航而缺乏激励，要么偏重动机但缺乏实时地理上下文耦合，且多针对特定人群（如远足者），难以服务日常步行者。此外，路线规划常因用户对周边兴趣点认知有限而受阻，步行中又易因动机衰减而提前终止。因此，设计一个覆盖步行前、中、后全流程，并将情境感知的动机支持与导航融合的AI伴侣，对于降低认知负荷、维持参与和促进行为改变具有重要价值。

**方法关键点**
- 系统包含三个专业化、不直接通信的智能体：GeographyAgent（对话式兴趣点选取+调用地图API规划路线）、AccompanyAgent（基于虚拟地理围栏和步频检测的情境感知实时鼓舞与信息提示）、SummaryAgent（简短总结、下一步行动建议与可选社交分享）。
- 三者通过共享状态对象间接协作，并由一个轻量桥梁代理统一面向用户输入输出。所有智能体基于GPT-4o，采用工具调用范式分离语言推理与地理计算。
- AccompanyAgent 依据用户偏好频率将路线划分为虚拟地理围栏段，仅在进入新区段或检测到步频骤降时触发干预，遵循“少而精”的JITAI原则；干预措辞融合关系型代理的关怀-坚持-探索风格。
- 地图视图采用极简设计，仅保留必要导航线索，其余信息由代理在后台处理并以简要提示呈现，降低视觉注意负担。

**关键实验与结果**
- 采用AB/BA交叉设计，12名参与者各完成两次步行，一次为“信息+动机”条件，一次为“纯信息”条件，均在自然环境中进行，研究者步行陪同并观察。
- 线性混合模型显示，“信息+动机”相比“纯信息”显著提升了积极情感（β=-0.806, p<0.001, Cohen’s d=1.85，积极情感复合指标提升1.03分）和用户体验（β=-0.583, p=0.007, d=1.46），且无显著残留效应。
- 主题分析提炼出两大设计要旨：支持性、关系化的表达（用户偏爱“陪伴感”而非“冷冰冰的机器报告”）；上下文感知的时机（高频或不合时宜的提示（如过马路时）被视为干扰，而在疲劳或里程碑节点时的鼓励则备受好评）。

**最值得记住的一句话**
动机性、时机恰当的陪伴对话，即时步行中的短暂干预，亦能显著放大用户的正向情感与整体体验。
