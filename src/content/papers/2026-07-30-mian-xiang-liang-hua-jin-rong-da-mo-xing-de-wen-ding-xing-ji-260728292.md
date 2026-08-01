---
title: 'CACHE-UK: A Stability-Aware Memory Editor for Sequentially Updated Quantized
  LLMs in Finance'
title_zh: 面向量化金融大模型的稳定性感知记忆编辑器
authors:
- Anubhav Lakra
- Yue Feng
affiliations:
- Indian Institute of Technology Madras, Chennai, India
- University of Birmingham, Birmingham, United Kingdom
arxiv_id: '2607.28292'
url: https://arxiv.org/abs/2607.28292
pdf_url: https://arxiv.org/pdf/2607.28292
published: '2026-07-30'
collected: '2026-08-01'
category: LLM
direction: 量化LLM的序列记忆编辑稳定性
tags:
- Quantized LLMs
- Memory Editing
- LoRA
- Catastrophic Forgetting
- Continual Learning
- Finance
one_liner: 提出CACHE-UK框架，通过低秩适配器、领域优先模块和稳定性控制器，缓解4-bit量化LLM在序列编辑中的灾难性遗忘
practical_value: '- **量化推荐模型的实时事实更新**：在电商推荐中，商品信息（价格、库存、描述）频繁变化，可在4-bit量化部署的LLM推荐模型上借鉴CACHE-UK的rank-1
  LoRA机制，将更新隔离在低秩子空间，避免全参数扰动引起的推荐质量雪崩。

  - **抗遗忘的增量知识注入**：稳定性控制器跟踪“退化债务”的理念可迁移到推荐模型的持续学习，当新商品或活动上线时，通过闭环监控减少对已有用户兴趣建模的覆盖。

  - **内容自适应的编辑强度**：领域优先模块根据输入内容调整编辑幅度，可类比于推荐中不同物品类型（爆款 vs. 长尾）采用差异化的更新步长，提升精细控制。

  - **低资源下的工程可行性**：整套框架专为量化模型设计，适合边缘推理或低延迟场景，可参考其适配方案让推荐模型的在线事实更新更省资源。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：金融领域LLM面临市场法规等事实快速更新，而4-bit量化虽利于部署，却引发“量化稳定性危机”——序列记忆编辑时性能灾难性退化。现有编辑方法在量化下失效。

**方法关键点**：提出CACHE-UK，包含三个核心组件：
1. **Rank-1 LoRA扰动机制**：仅在低秩适配器子空间内进行编辑，避免直接修改量化权重的高扰动。
2. **金融领域优先模块**：根据输入内容的领域相关性自适应调整编辑强度，金融术语获得更大更新幅度。
3. **闭环稳定性控制器**：持续追踪编辑造成的“退化债务”，通过反馈机制防止灾难性遗忘，使模型在连续多次编辑后仍保持原有能力。

**关键结果数字**：在4-bit量化的OpenLLaMA-3B模型及88,021篇英国金融文档上评估。相比适配后的基线方法，知识退化减少11–17%（最稳定效果）；测试集泛化成功率最高达28%，比最强基线提升6个百分点，但绝对泛化率仍较低。
