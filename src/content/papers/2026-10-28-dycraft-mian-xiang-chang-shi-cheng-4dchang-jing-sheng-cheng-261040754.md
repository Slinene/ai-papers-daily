---
title: 'DyCraft: An Agentic System for Long-Horizon 4D Scene Generation'
title_zh: DyCraft：面向长时程4D场景生成的Agentic系统
authors:
- Jeff Tan
- Hang Dai
- Zeqian Long
- Yanzhe Lyu
- R. Kenny Jones
- Shangzhe Wu
- Chen Geng
- Jiajun Wu
affiliations:
- Stanford University
- University of Cambridge
arxiv_id: '2610.40754'
url: https://arxiv.org/abs/2610.40754
pdf_url: https://arxiv.org/pdf/2610.40754
published: '2026-10-28'
collected: '2026-11-12'
category: Agent
direction: Agent长时程3D/4D生成
tags:
- Agentic System
- 3D Scene Generation
- 4D Animation
- Storyboard
- Motion Authoring
- GPT-6
one_liner: 把长时程动画拆成静态场景、3D关键姿态分镜和局部运动生成，让coding agent稳定产出物理可信的4D场景
practical_value: '- 长流程生成任务不要一次性写全量脚本：拆成「计划→静态骨架→关键帧/状态→局部分镜填充」，每一步可独立验证。对应电商商品短视频脚本、落地页动态布局或3D商品展示生成，可以先用静态布局/分镜确认，再生成动态内容。

  - 引入显式中间表示（如3D storyboard / key poses）作为 grounding，让agent只解决相邻状态之间的局部问题，避免单次推理承担过长时空依赖。搜索推荐agent中可用类似「决策关键状态图」或「推荐链路关键帧」降低长链路生成的失败率。

  - 把物理约束、规则校验封装成工具（motion authoring tools），而不是让模型直接输出所有参数；在电商agent中可以把预算约束、库存状态、排序规则、风控策略封装成可调用工具，提升可控性与可修复性。

  - 利用「bare agent一次性脚本化导致物理违规」的结论：对多步决策/生成任务，应设计分阶段验证、可局部修复的流程，避免默认端到端单次生成，这对自动出价、多轮商品文案改写等长链路Agent同样适用。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：前沿coding agents能生成高质量3D场景和资产，但长时程动画仍常常物理不可信——物体穿插、缺少支撑、运动不自然。裸agent通常一次性脚本化完整动画，难以验证并分离复杂时空约束。受人类动画师实践启发，DyCraft把动画分解为coding agent能可靠解决的步骤。

**方法关键点**：
- 先将用户prompt扩展为详细计划并构建静态场景。
- 构建3D storyboard的关键动画姿态，每个关键帧是一个静态3D场景，可独立构建和调试。
- 分镜将问题分解为已验证的起止状态对，agent用一组motion authoring tools在相邻状态之间生成局部运动。

**关键结果**：在24个长时程、多镜头动画任务上评估，覆盖人形机器人、人/动物角色和物理机构。相比Codex中的native GPT-6 agent及先前agentic baselines，DyCraft显著减少物理违规，生成更高质量的动画3D场景，人类评审也更偏好其输出。
