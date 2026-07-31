---
title: 'MemHarness: Memory Is Reconstructed, Not Replayed'
title_zh: 记忆应被重构而非回放：基于GRPO的LLM Agent经验动态适配框架
authors:
- Rong Wu
- Daocheng Fu
- Licheng Wen
- Xuemeng Yang
- Shu Zou
- Jianbiao Mei
- Yuxin Wang
- Hairong Zhang
- Yu Yang
- Tao Hu
affiliations:
- Zhejiang University
- Shanghai Artificial Intelligence Laboratory
- Fudan University
- Shanghai Innovation Institute
- Shanghai Jiao Tong University
arxiv_id: '2607.28272'
url: https://arxiv.org/abs/2607.28272
pdf_url: https://arxiv.org/pdf/2607.28272
published: '2026-07-29'
collected: '2026-07-31'
category: Agent
direction: Agent记忆重构机制
tags:
- Memory Reconstruction
- LLM Agents
- GRPO
- Negative Transfer
- OOD Robustness
- Decision Making
one_liner: 提出记忆重构范式，让LLM Agent基于当前状态改编检索经验，端到端GRPO训练，防止负迁移并提升OOD鲁棒性
practical_value: '- 在电商对话推荐或搜索Agent中，检索到的历史经验（如成功对话策略、用户偏好）不应原样拼接，可设记忆重构模块，根据当前查询状态动态改写经验，避免性能负迁移。

  - 使用GRPO等强化学习算法端到端训练记忆重构策略，使模型学会在适当的时候信任或调整记忆，提升在冷启动或新品类（OOD）场景的鲁棒性。

  - 用户行为序列记忆库可与当前上下文结合，生成个性化引导向量，替代静态的偏好嵌入，增强推荐解释性和交互效果。

  - 经验重构可作为辅助训练目标，与主任务联合优化，既显式抑制错误记忆干扰，又潜在提升模型内在推理能力，适用于离线策略学习场景。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有记忆增强的LLM Agent大多将检索到的经验作为静态文本逐字回放，直接注入上下文，忽视了存储经验的抽象性与决策时刻具体状态间的差异，常导致负迁移（即误导决策）。人类却会依据当下情境重构记忆。

**方法**：提出MemHarness框架，抛弃回放范式。每个决策步，统一策略模型以当前状态为条件，对检索到的经验进行批判与重构，生成情境化的指导信息后再行动。记忆重构能力通过GRPO端到端训练自然涌现，无需人工标注重构标签。

**结果**：在ALFWorld和WebShop两个基准上，MemHarness显著超越纯强化学习与静态记忆增强基线；在分布外（OOD）测试中表现强鲁棒性。分析表明，重构目标不仅阻断了负迁移，还在训练中充当潜在指导，根本上提升了模型的内在推理能力。
