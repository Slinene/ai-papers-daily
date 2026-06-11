---
title: 'Verifiable Environments Are LEGO Bricks: Recursive Composition for Reasoning
  Generalization'
title_zh: 可验证环境如乐高积木：递归组合实现推理泛化缩放
authors:
- Hao Xiang
- Qiaoyu Tang
- Le Yu
- Yaojie Lu
- Xianpei Han
- Ben He
- Le Sun
- Bowen Yu
- Peng Wang
- Hongyu Lin
affiliations:
- University of Chinese Academy of Sciences
- Institute of Software, Chinese Academy of Sciences
- Alibaba Group
arxiv_id: '2606.12373'
url: https://arxiv.org/abs/2606.12373
pdf_url: https://arxiv.org/pdf/2606.12373
published: '2026-06-09'
collected: '2026-06-11'
category: Reasoning
direction: 强化学习环境组合与推理泛化
tags:
- Reinforcement Learning
- Environment Composition
- Reasoning Generalization
- Verifiable Environments
- Recursive Composition
- LLM
one_liner: 将可验证环境抽象为可组合积木，通过递归算子自动生成复合环境，突破线性扩展瓶颈，提升LLM推理泛化能力
practical_value: '- **Agent 工作流合成**：可将单个工具或子任务视为可验证环境，利用 Sequential/Parallel/Select/Sort
  等算子自动组合出复杂工作流，用于训练 Agent 多步推理与规划能力。

  - **课程学习与难度控制**：通过递归深度和算子类型控制组合环境的复杂度，设计从简单任务到复杂多步推理的课程，稳定提升模型泛化性能。

  - **数据增强与复用**：少量基础任务环境通过组合即可生成大量多样化训练样本，降低人工设计与采集成本，尤其适用于电商场景中的客服对话、多轮谈判等需复杂推理的任务。

  - **推理链验证与奖励设计**：组合环境本身提供确定性验证，可直接构建 RL 奖励信号，无需额外标注，对构建自监督推理训练管线有直接启发。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：基于可验证环境的强化学习已被证明能增强大语言模型的推理能力，但手动构建或单独设计环境的方式扩展成本高、线性增长受限，难以支撑大规模推理泛化。

**方法**：提出 RACES 框架，将可验证环境视为可组合的原子模块，当某一环境的输出类型与另一环境的输入类型匹配时，即可通过定义好的算子（Sequential、Parallel、Sort、Select）自动融合成新的复合环境，支持递归组合，从而指数级扩展环境多样性。框架以 300 个基础环境实现，能诱导出多样的推理模式。

**结果**：在 DeepSeek-R1-Distill-Qwen-14B 和 Qwen3-14B 上，仅用复合环境训练，在六个未参与环境构建的推理基准上平均提升分别达 3.1 点（48.2→51.3）和 2.3 点（58.8→61.1）。且仅使用 50 个基础环境组合训练，即可达到与全部 300 个单独环境训练相当的性能，环境利用效率显著提升。
