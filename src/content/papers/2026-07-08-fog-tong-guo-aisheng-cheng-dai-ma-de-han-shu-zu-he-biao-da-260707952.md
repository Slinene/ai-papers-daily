---
title: 'fog: Expressing Motion and Emotion through Function Composition of AI-Generated
  Code'
title_zh: fog：通过AI生成代码的函数组合表达运动与情感
authors:
- Vivian Liu
- Lydia Chilton
affiliations:
- Columbia University
arxiv_id: '2607.07952'
url: https://arxiv.org/abs/2607.07952
pdf_url: https://arxiv.org/pdf/2607.07952
published: '2026-07-08'
collected: '2026-07-13'
category: Multimodal
direction: 生成式运动与情感动画代码合成
tags:
- Motion Generation
- Emotion Expression
- LLM
- Code Generation
- Animation
- Function Composition
one_liner: 利用LLM生成可组合的运动函数类，实现Heider-Simmel风格动画中的语义动作与情感表达
practical_value: '- 将领域知识分解为动词、副词、情感等可组合的原子函数，并利用LLM生成其代码实现，这一范式可迁移至电商商品动画或推荐解释的生成：先定义基本原子动作（如展示、强调、对比），再让LLM组合生成个性化动画。

  - 交互界面结合直接操纵与动态生成的UI，可借鉴到推荐可视化配置工具中：允许用户拖拽调整动画参数，同时后台由LLM实时重新生成代码，实现快速迭代。

  - 利用LLM生成开放式运动词汇库，避免了手工编码每种动作，对于需要动态生成大量商品展示动画的场景（如千人千面的广告素材）有降本潜力。

  - 注意：该工作聚焦于Heider-Simmel抽象动画，直接用于电商/推荐需适配具体领域动作，但代码生成与函数组合的思想具有通用性。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

动机：创造富有表现力的运动和情感动画通常需要复杂的动画曲线和编程技能，非专家难以高效创作。

方法关键点：提出fog框架，将运动行为建模为可组合的Python函数类（动词、副词、情感、手势），每个函数通过修改实体内部状态（能量、速度等）来表达语义。用户通过自然语言提示让LLM生成这些函数，框架支持函数的顺序组合、条件组合等。配套的动画编辑器允许用户通过直接操纵调整参数，并动态生成相应的UI控件，形成“生成-操控-再生成”的循环。

关键结果：在感知评估中，452个fog生成的动画语义识别准确率达68%，比随机基线提升2.68倍；用户研究显示，专业与非专业用户都能借助该界面实现更快的迭代、更广的探索和更精细的控制。
