---
title: 'Pelican-Unified 1.0: A Unified Embodied Intelligence Model for Understanding,
  Reasoning, Imagination and Action'
title_zh: Pelican-Unified 1.0：统一理解、推理、想象与行动的具身基础模型
authors:
- Yi Zhang
- Yinda Chen
- Che Liu
- Zeyuan Ding
- Jin Xu
- Shilong Zou
- Junwei Liao
- Jiayu Hu
- Xiancong Ren
- Xiaopeng Zhang
arxiv_id: '2605.15153'
url: https://arxiv.org/abs/2605.15153
pdf_url: https://arxiv.org/pdf/2605.15153
published: '2026-05-14'
collected: '2026-05-17'
category: Agent
direction: 具身智能 · 统一多模态基础模型
tags:
- Embodied AI
- Unified Model
- VLM
- World Model
- Video Generation
- Action Prediction
one_liner: 首个按统一原则训练的具身基础模型，用单一VLM实现理解、推理、想象与行动，同规模下多项性能最优
practical_value: '- **统一多任务的架构思路**：用一个VLM同时承担理解与推理，将场景、指令、历史动作映射到共享语义空间，避免多个专家系统的拼接，降低系统复杂度，适合电商场景中需要融合文本、图像、用户行为序列的多任务统一建模。

  - **未来生成器联合预测视频与动作**：通过同一去噪过程同时产生未来视觉和未来行动，并将语言、视频、动作损失回传至共享表示，这种联合训练能让模型学到更丰富的环境动态表征，对需要想象用户未来行为的推荐模型有启发，可以尝试在用户序列预测中同时生成行为与上下文。

  - **自回归思维链生成与潜变量投影**：VLM在单次前向中输出任务、动作和未来导向的思维链，并将最终隐状态投影为潜变量，作为未来生成的Condition，这类似于将推理过程显式化为离散Token再总结为稠密向量，可以借鉴到Agent决策或推荐解释中，提升推理的可控性和下游生成质量。

  - **一个Checkpoint保持各能力竞争力**：实验表明统一训练不会导致能力妥协，对工业部署友好，可减少线上模型数量和版本管理成本，适合电商中需要同时具备理解、推理、想象能力的基础模型建设。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：当前具身智能系统通常需要独立模型分别负责环境理解、任务推理、未来想象和行动预测，导致系统集成复杂、训练不一致。本工作旨在用一个统一基础模型同时覆盖这四种能力，并在不牺牲单能力性能的前提下简化架构。

**方法**：Pelican‑Unified 1.0以单一VLM作为统一理解和推理模块，将场景图像、指令、视觉上下文、动作历史全部映射至共享语义空间，并自回归地生成任务、动作和未来导向的思维链，最终隐状态投影为一个稠密潜变量。统一未来生成器（UFG）基于该潜变量，通过同一去噪过程同时生成未来视频帧和未来动作序列，由两路模态专用输出头分别解码。语言、视频和动作损失全部反向传播到共享表示中，实现理解、推理、想象与行动的端到端联合优化。

**结果**：一个模型权重在所有任务上均取得强结果：在8个VLM评测上平均64.7分，为同规模模型最佳；WorldArena上66.03分排名第一；RoboTwin动作预测达93.5分，位列第二。证明统一范式能够保留专项模型的强性能，同时将四种能力集成至单一模型。
