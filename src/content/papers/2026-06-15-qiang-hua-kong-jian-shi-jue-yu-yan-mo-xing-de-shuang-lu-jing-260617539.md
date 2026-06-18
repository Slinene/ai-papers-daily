---
title: Reinforcing Dual-Path Reasoning in Spatial Vision Language Models
title_zh: 强化空间视觉语言模型的双路径推理
authors:
- Yatai Ji
- An-Chieh Cheng
- Yang Fu
- Yukang Chen
- Han Zhang
- Zhaojing Yang
- Wei Huang
- Ka Chun Cheung
- Song Han
- Vidya Nariyambut Murali
affiliations:
- The University of Hong Kong
- NVIDIA
- University of California, San Diego
arxiv_id: '2606.17539'
url: https://arxiv.org/abs/2606.17539
pdf_url: https://arxiv.org/pdf/2606.17539
published: '2026-06-15'
collected: '2026-06-18'
category: Multimodal
direction: 多模态空间推理 · 强化学习
tags:
- Spatial VLM
- Dual-Path Reasoning
- Reinforcement Learning
- Chain-of-Thought
- 3D Grounding
- GRPO
one_liner: 提出SR-REAL框架，通过强化学习统一优化纯语言推理与检测-推理双路径，显著提升空间VLM推理能力
practical_value: '- 双路径策略可借鉴至多意图Agent设计：根据查询类型动态选择推理路径（如召回 vs 精排），避免单一链路的局限性

  - 冷启动SFT阶段构造结构化CoT推理链与区域-3D接口，类似推荐中融合视觉/文本特征的grounding设计

  - GRPO强化学习结合格式奖励与任务奖励，确保推理格式可控，避免自由文本退化，对Agent输出格式化有直接参考

  - 混合2D/3D和数据增强策略可用于构建更鲁棒的模型初始化，提升面向多样业务场景的泛化能力'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：空间视觉语言模型在几何感知上进步显著，但需要多步深度、距离、场景关系推理的任务仍具挑战，且不同空间查询最优策略不同：一些适合纯语言逐步推演，另一些需先显式3D定位再量化推理，现有方法未能统一。

**方法**：提出SR-REAL，为VLM配备两条互补推理路径：语言纯推理（LOR）和检测后推理（DTR）。DTR先通过区域令牌检测3D几何线索（中心点、边界框）再推理。训练分两阶段：冷启动SFT构建LOR/DTR链式思维监督，暴露区域到3D坐标接口，并混合2D/3D定位与通用VQA数据初始化；然后用GRPO强化学习联合优化两条路径，包含准确率奖励和格式奖励，DTR额外引入离散中心检测奖励提升几何对齐。

**结果**：在多个空间基准上大幅超越基线：单一RL检查点同时支持双路径，DTR在区域感知任务中因精确3D定位表现突出，LOR提升通用空间推理；联合训练产生相互促进；高质量混合冷启动数据对稳定RL和跨域迁移至关重要；模型无需逐任务微调即展现良好泛化性。
