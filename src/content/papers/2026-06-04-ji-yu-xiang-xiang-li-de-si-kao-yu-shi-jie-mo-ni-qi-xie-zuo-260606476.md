---
title: 'Thinking with Imagination: Agentic Visual Spatial Reasoning with World Simulators'
title_zh: 基于想象力的思考：与世界模拟器协作的Agent视觉空间推理
authors:
- Chenming Zhu
- Jingli Lin
- Yilin Long
- Peizhou Cao
- Tai Wang
- Jiangmiao Pang
- Xihui Liu
affiliations:
- The University of Hong Kong
- Shanghai AI Laboratory
- Shanghai Jiao Tong University
- Fudan University
- Beihang University
arxiv_id: '2606.06476'
url: https://arxiv.org/abs/2606.06476
pdf_url: https://arxiv.org/pdf/2606.06476
published: '2026-06-04'
collected: '2026-06-07'
category: Agent
direction: Agent视觉空间推理 · 世界模拟器
tags:
- Spatial Reasoning
- World Simulator
- VLM
- Reinforcement Learning
- View Consistency
- Agentic AI
one_liner: 提出Astra框架，通过RL训练VLM策略决定何时调用世界模拟器生成新视角图像，提升多视图空间推理能力
practical_value: '- **工具调用的决策学习**：Agent仅在想象观察优于直接回答时才调用世界模拟器，这种“何时使用工具”的策略可迁移到对话推荐Agent中，避免过度依赖外部信息导致延迟和误导。

  - **两阶段RL课程设计**：先通过行为克隆预热工具使用，再用RL优化调用决策，这种分阶段训练策略可用于训练推荐Agent学习何时调用知识检索或用户画像补充信息。

  - **视一致性训练保证证据可靠**：通过位姿和内容一致性约束训练世界模型，确保生成的观察与实际一致；类似地，在多模态推荐中生成商品描述或图像时，可引入一致性损失提升信息真实性。

  - **Agent与环境交互的闭环框架**：Astra将视觉推理转化为“观察-想象-推理”循环，在电商场景中，可构建模仿用户浏览行为的模拟环境，让推荐Agent主动探索生成更合理的推荐理由。'
score: 7
source: arxiv-cs.CV
depth: abstract
---

**动机**：VLMs在空间推理中受限于所见图像和文本链式思维，难以推断未观察布局、维持跨视角一致性或从替代视角推理。当仅提供少量自我中心观察时，模型常表现不佳。

**方法**：提出Astra框架，将空间推理转化为Agent与世界模拟器交互的想象过程。Astra包含两个核心组件：Astra-VL是基于Qwen3-VL的VLM策略，通过RL训练学会在需要时生成自然语言相机运动指令；Astra-WM是基于Bagel的世界模拟器，接收指令并生成新视角的想象观察。为确保想象证据可靠，Astra-WM经过视一致性微调，同时优化位姿和内容一致性。RL训练采用世界模拟器在环的两阶段课程：先行为克隆让模型学会工具使用范式，再通过RL优化调用时机，使其仅在想象优于直接回答时调用模拟器。

**结果**：在MMSI-Bench上，Astra-WM将模拟器增强的Gemini-3-Flash从45.1提升至49.5；Astra-VL将Qwen3-VL骨干从29.8提升至38.8。在MindCube上，从36.8提升至42.7。消融实验表明，世界模拟器与Agent策略缺一不可，有效的世界模型增强推理需要学习何时、何地及如何想象。
