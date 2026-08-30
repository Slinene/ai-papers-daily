---
title: 'Skill Issue: Are Skills Language-Invariant in LLMs?'
title_zh: 多语言LLM技能一致性：自博弈评估
authors:
- Bobby Cheng
- Adam Gaber
- Zhengyuan Liu
- Catherine Arnett
- Omer Goldman
- Cheston Tan
- Leshem Choshen
affiliations:
- A*STAR
- Weizmann Institute of Science
- MIT-IBM Watson AI Lab
- University of Cambridge
- EleutherAI
arxiv_id: '2608.25832'
url: https://arxiv.org/abs/2608.25832
pdf_url: https://arxiv.org/pdf/2608.25832
published: '2026-08-25'
collected: '2026-08-30'
category: Eval
direction: 多语言LLM技能一致性评估
tags:
- multilingual LLM
- self-play
- skill evaluation
- text games
- cross-lingual consistency
one_liner: 通过多语言自博弈文本游戏，量化同一LLM在不同语言接口下的技能差异
practical_value: '- 多语言搜索/推荐中，模型技能会在语言接口变化时退化；上线前应做跨语言自博弈或类似对抗评测，而不只看知识基准分。

  - 如果业务需要多语言 Agent 决策，可固定中间推理语言（如统一用英文 CoT）并在输入层做语言映射，可能恢复部分性能；论文表明改变内部推理语言可提升决策质量。

  - 自博弈离线评测成本低、控制变量好，适合持续回归跨境/多语言版本的策略模型；可复用 TextArena 思路构建电商谈判、广告竞价等最小决策游戏。

  - 注意语言特有失败模式（空间推理、条件决策、最优 move 选择），对推荐解释或多语言文案生成可针对性加入语言校准和校验。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 多语言能力提升，但同一模型在不同语言下可用知识和技能可能不一致；已有工作多关注知识回答差异，缺少对决策/推理技能的隔离评测。

**方法关键点**：用多语言自博弈——两个同模型实例在文本游戏中对战，仅交互语言不同，模型、对手、规则、状态空间、可用动作均固定。基于 TextArena 构建多语言扩展，覆盖 8 种语言、6 类游戏（空间推理、不完全信息、资源分配、重复交互），评估三个开源权重模型。

**关键结果**：同一模型跨语言的对战强弱差异显著，胜率/失败边距、非法动作率、策略倾向均有系统性变化；具体失败集中在空间推理、基于卡牌条件的决策和最优走子选择。将中间推理语言改为特定语言（如英语）能恢复相当部分性能，说明语言对决策过程不同阶段影响不同。论文认为技能不一致是发展真正多语言模型的主要障碍。
