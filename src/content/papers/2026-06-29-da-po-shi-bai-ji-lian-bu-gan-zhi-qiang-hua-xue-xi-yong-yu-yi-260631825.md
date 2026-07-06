---
title: 'Breaking Failure Cascades: Step-Aware Reinforcement Learning for Medical Multimodal
  Reasoning'
title_zh: 打破失败级联：步感知强化学习用于医学多模态推理
authors:
- Junha Jung
- Minbyul Jeong
- Suhyeon Lim
- Sungwook Jung
- Jaehoon Yun
- Taeyun Roh
- Mujeen Sung
- Jaewoo Kang
affiliations:
- Korea University
- Upstage AI
- Kyung Hee University
- KAIST
- Hanyang University College of Medicine
arxiv_id: '2606.31825'
url: https://arxiv.org/abs/2606.31825
pdf_url: https://arxiv.org/pdf/2606.31825
published: '2026-06-29'
collected: '2026-07-06'
category: Multimodal
direction: 医学多模态推理 · 步级强化学习
tags:
- Multimodal LLM
- Reinforcement Learning
- Step-wise Reward
- Medical VQA
- Failure Cascades
one_liner: 提出MRPO算法，对错误路径早期推理步施加指数惩罚以抑制级联失败，显著提升医学多模态推理精度。
practical_value: '- 在推荐系统的多步推理场景（如解释生成、对话式推荐）中，可利用步骤级过程奖励解决稀疏奖励问题，定位并修复早期决策错误。

  - 工程实现上，可借鉴指数衰减惩罚机制：当整体任务失败时，对越早的推理步赋予越大负奖励，低成本增强RL训练信号。

  - 对于Agent框架中的多步规划，MRPO的步级反馈策略可直接迁移，提升长链任务的成功率与推理质量。

  - 该方法可与现有RL算法（如GRPO）轻松集成，仅需在奖励函数中增加步骤级惩罚项，侵入性小，适合快速实验验证。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有多模态LLM的医学图像推理训练主要以最终答案正确性为奖励（outcome-centric），导致稀疏归因问题，难以优化中间推理过程。分析发现，早期步骤的推理错误会引发级联失败，是医学VQA基准中预测错误的主要原因。

**方法**：提出Medical Reasoning-aware Policy Optimization (MRPO)，一种结合步级过程奖励的RL算法。当最终答案错误时，MRPO对轨迹中早期无效推理步骤的token分配指数级更大的惩罚，从而精准抑制失败源头，同时保持正确路径不受影响。该机制将稀疏奖励转化为密集的步骤级反馈，无需额外标注。

**结果**：在三个多模态LLM骨干上（包含Qwen3-VL-8B-Instruct），MRPO一致超越标准GRPO和近期RL基线。在Qwen3-VL-8B-Instruct上，甚至比大得多的HuatuoGPT-Vision-34B高出2.79分。关键指标：早期步骤推理失败率从64.0%大幅降至13.0%，验证了级联失败干预的有效性，最终答案准确率和推理质量双双提升。
