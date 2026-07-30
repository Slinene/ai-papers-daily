---
title: 'DecoEvo: Score-Decoupled Co-Evolution of Solver and Rubric-Generator Skills
  in Text Space'
title_zh: DecoEvo：文本空间中求解器与评分准则技能的解耦共进化
authors:
- Jiangwang Chen
- Zixin Song
- Junlin Liu
- Shuaiyu Zhou
- Haiyan Wu
- Haihan Shi
- Chenxi Zhou
- Hanqing Li
- Xiao Yang
- Da Zhu
affiliations:
- Tsinghua University
- University of Chinese Academy of Sciences
- Peking University
- Qwen Business Unit of Alibaba
arxiv_id: '2607.25675'
url: https://arxiv.org/abs/2607.25675
pdf_url: https://arxiv.org/pdf/2607.25675
published: '2026-07-27'
collected: '2026-07-30'
category: Training
direction: 文本空间共进化优化 · 自动评估准则生成
tags:
- text-space optimization
- co-evolution
- rubric generation
- LLM
- decoupled objectives
- prompt optimization
one_liner: 提出解耦共进化框架，分别优化求解器与评分准则生成器，避免评估准则退化并提升性能
practical_value: '- 在电商搜索/推荐场景中，当需要为生成式模型（如商品描述、推荐理由）自动设计评估标准时，可借鉴DecoEvo同时迭代优化生成策略和评分准则，避免人工制定准则的局限。

  - 解耦的准则更新机制（需求覆盖审核、响应区分度审计）可以单独用于改进现有的自动评估框架，提升评估维度覆盖和区分能力，尤其适合代理或多智体系统的在线性能诊断。

  - 该方法不修改模型权重，仅维护外部文本技能，工程实现轻量，适合在业务中快速试错多组提示词和评估标准，降低对模型内参数调整的依赖。

  - 在构建电商智能客服或对话Agent时，可利用criterion-level反馈不断挖掘回复弱点，驱动评分准则同步进化，实现更全面的闭环优化。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有文本空间优化方法固定评估标准，在开放性任务中求解器进步后，未被准则覆盖的维度会脱离优化信号；若直接进化准则，又可能因依赖当前求解器得分而退化（准则变简单）。需要一种能让求解器与准则协同进化的机制。

**方法关键点**：DecoEvo提出解耦共进化框架，在无黄金评分准则下同时优化*求解器技能*和*准则生成器技能*。求解器利用criterion-level反馈按各评估维度改进；准则生成器则通过两个独立审计信号更新——需求覆盖审计（检查所需维度是否齐全）和响应区分度审计（检查准则能否区分响应好坏），两者均与求解器总分无关。这种解耦使生成器聚焦于求解器新暴露的弱点，避免重复强调已满足的准则。

**关键结果**：在BBH、GSM8K、MATH、IFEval、MMLU等五个基准和GPT-4o-mini、Llama-3.1-8B-Instruct、Qwen2.5-7B-Instruct三个骨干上，DecoEvo均优于所有对比方法（包括SkillOpt），五基准平均相对提升2.8%-5.0%。
