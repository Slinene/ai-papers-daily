---
title: 'Behavior-Adaptive Conversational Agents: Toward a Fluid Personality Framework'
title_zh: 行为自适应对话代理：动态人格框架
authors:
- Hasibur Rahman
- Smit Desai
affiliations:
- Northeastern University
arxiv_id: '2607.01034'
url: https://arxiv.org/abs/2607.01034
pdf_url: https://arxiv.org/pdf/2607.01034
published: '2026-07-01'
collected: '2026-07-06'
category: Agent
direction: 对话代理人格动态适配
tags:
- conversational agents
- personality adaptation
- behavior change
- LLM
- fluid personality
- contextual calibration
one_liner: 提出根据任务情境动态协调LLM对话代理的隐喻角色和人格强度的流体人格框架
practical_value: '- 电商客服Agent可根据用户情绪与问题类型动态切换人格：售后场景选用低强度共情的“辅导员”，售前咨询选用中等强度专业的“导购”，提升信任与转化。

  - 生成式推荐解释系统适配用户个人特质：对理性用户用“专家工具”隐喻、低强度表达，对易受影响的用户用“教练”角色、中等激励性语言，改善解释接受度。

  - 广告文案生成Agent根据产品类别（功能品 vs. 情感品）和投放渠道（搜索 vs. 信息流）灵活调整隐喻角色与语气强度，避免千篇一律的助手口吻。

  - 为对话式推荐系统设计人格状态机，基于对话上下文（问答、闲聊、任务引导）自动切换代理角色，维持交互连贯性与用户沉浸感。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

**动机** 现有LLM对话代理多数采用固定化的人格与角色，在动态任务情境（如医疗信息查询、健身指导、反思学习）中容易导致信任下降、享受度降低。已有研究表明，中等程度的人格表达（而非极低或极高）在目标导向任务中能提升信任与采纳意愿，且适配上下文的隐喻角色（如教练、导师）比千篇一律的助手更优。然而，代理如何根据情境动态校准仍缺乏框架。

**方法关键点** 提出**流体人格框架**，联合自适应两大维度：(1) **隐喻角色**——根据任务性质在教练、导师、图书管理员/工具等之间切换；(2) **人格表达强度**——在低、中、高三档间调整，取决于任务上下文、用户目标与特质、情境紧迫性。框架设计不固定单一风格，而是将人格作为可基于规则或学习的动态函数。

**关键结果** 本文为框架草图，尚无实验数据。基于先导研究推断，动态适配人格与隐喻有望改善健康、教育等场景中的对话代理效果，后续需实证验证。
