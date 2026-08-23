---
title: Rule-Compliant Visual Spatial Planning for Multimodal Large Language Models
title_zh: 面向多模态大语言模型的规则遵循视觉空间规划
authors:
- Yu Chen
- Ting Lei
- Yaoyi Li
- Jia Cai
- Zhecen Wu
- Yang Liu
affiliations:
- Peking University
- Yinwang Intelligent Technology Co., Ltd
arxiv_id: '2608.20237'
url: https://arxiv.org/abs/2608.20237
pdf_url: https://arxiv.org/pdf/2608.20237
published: '2026-08-20'
collected: '2026-08-23'
category: Reasoning
direction: 多模态大模型规则遵循空间规划
tags:
- MLLM
- Spatial Planning
- Rule Following
- Benchmark
- Disentangled Planning
one_liner: 提出RuleMaze基准和DMP方法，解耦感知、执行与规则验证，提升MLLM在规则约束下的空间规划与泛化
practical_value: '- 可借鉴DMP的解耦设计：将感知、执行、规则验证拆分为独立模块，便于在业务Agent中注入可解释的合规性检查，避免端到端黑盒违反约束。

  - 使用Language-Logic-Function Hybridization自动生成规则并转化为逻辑验证器，可复用于构建带约束的策略评测集或训练数据，降低人工构造规则成本。

  - 在需要严格遵循业务规则的Agent任务（如营销活动路径规划、多步骤推荐流程、广告投放策略）中，分离式规划能提供中间轨迹，便于调试和规则动态更新。

  - 论文场景为迷宫导航，与推荐系统核心链路距离较远，但规则验证与执行解耦的思想可作为构建可信Agent系统的参考。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

动机：多模态大语言模型（MLLMs）在显式或未见规则约束下的视觉空间规划能力尚不清晰。此类任务要求模型同时理解空间布局、解释自然语言规则并规划有效动作。现有评测缺乏可控的规则遵循场景。

方法：作者提出RuleMaze基准，要求MLLM在迷宫中导航并遵守不同复杂度的自然语言规则。为可扩展地构建规则，提出Language-Logic-Function Hybridization：自动生成自然语言规则并翻译为逻辑表示和可执行验证器，消除手工规则工程。针对规则遵循与泛化，提出Disentangled Multimodal Planning（DMP），通过可解释推理原语将感知、执行和规则验证分离。这种解耦促进了对更复杂和未见规则的系统化泛化，并提供透明的中间规划轨迹。

结果：实验表明，与端到端文本规划基线相比，DMP在规则遵从和规划成功率上有显著提升。RuleMaze为研究MLLM中基于规则的空间规划提供了原则性基准。代码已开源。
