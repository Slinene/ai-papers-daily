---
title: 'Co-ReAct: Rubrics as Step-Level Collaborators for ReAct Agents'
title_zh: Co-ReAct：将评估标准作为ReAct智能体的步骤级协作者
authors:
- Jiazheng Kang
- Bowen Zhang
- Zixin Song
- Jiangwang Chen
- Xiao Yang
- Da Zhu
- Guanjun Jiang
affiliations:
- Qwen Applications Business Group of Alibaba
- Tsinghua University
arxiv_id: '2605.23590'
url: https://arxiv.org/abs/2605.23590
pdf_url: https://arxiv.org/pdf/2605.23590
published: '2026-05-22'
collected: '2026-05-25'
category: Agent
direction: Agent 步骤级评估标准引导
tags:
- Rubric
- ReAct
- GRPO
- Listwise Ranking
- Step-level Guidance
- Agentic Search
one_liner: 训练一个基于评分标准的生成器，以步骤级方式指导ReAct智能体的搜索决策，并通过列表式GRPO优化与专家排名的一致性，显著提升深度研究任务性能。
practical_value: '- 电商搜索Agent构建中，可引入步骤级评分标准（rubric）明确每步目标（如“需覆盖2023-2025年新品”、“指定英文源”），提升信息收集的精准度与全面性。

  - 训练一个轻量评判标准生成器，用列表式RL微调使其输出具有甄别力的准则，可作为即插即用组件注入现有ReAct、Best-of-N等方案，平均提升1-15%性能且无需改动原有决策机制。

  - 注入+验证+重试机制：动作执行前用生成的标准进行校验，未达标则带反馈重试，此模式可有效降低错误动作率，适用于推荐系统的分步式查询扩展或多轮决策。

  - 排名对齐的列表式奖励设计（Spearman相关系数）对生成式推荐中Semantic ID排序、候选动作评估等场景有借鉴意义，用全局排名代替逐对偏好能提供更丰富的梯度信号。'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：ReAct风格的多步搜索智能体主要依赖自身判断决定搜索什么、何时停止，常产生冗余浅层的轨迹，缺乏外部步骤级质量信号。先前工作将评估标准（rubric）作为训练奖励或事后评估器，是评估性的而非动作指导性的。Co-ReAct重新定位评估标准为推理时步骤级动作选择信号，以解决深度研究中搜索决策不精准的问题。

**方法**：1) 偏好数据采集：从真实ReAct轨迹的分支点采样候选动作，由多模型专家（Claude、Gemini、GPT）进行列表式排名并聚合为共识排序，用于监督。2) 评估标准生成器训练：基于Qwen3-14B，使用GRPO优化，奖励为生成的标准诱导的动作排名与专家排名的斯皮尔曼等级相关系数，使用列表式而非成对比较，鼓励标准具有区分力而非仅表面合理。3) 推理流程：采用注入-验证-重试五元组（Rubric, Reason, Act, Verify, Observe）。每步先由生成器产生条件化的评估标准并注入上下文；动作提出后由独立验证器对照标准检查，若未通过则带反馈重试一次，从而纠正错误动作。

**关键结果**：在DeepResearchBench和SQA-CS-V2上，Co-ReAct在Qwen3-8B/14B上与Self-Refine、Best-of-N、Step-Back、CRITIC对比，8B模型上改善约0.9%，14B模型上改善显著（DRB +7.9%，SQA +4.6%）。消融实验表明列表式训练、RL优化和验证三者必不可少；未训练的评估标准甚至损害性能。评估标准生成器可作为即插即用组件改进Best-of-N、Step-Back等基线（最高+14.8%）。Co-ReAct显著增加了检索文档量和引用来源（+66%），且利用率最高。
