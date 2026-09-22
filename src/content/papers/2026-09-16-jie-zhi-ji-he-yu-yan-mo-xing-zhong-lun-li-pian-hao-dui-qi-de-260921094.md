---
title: 'Geometry of Values: Task Vector Composition for Ethical Preference Alignment
  in Language Models'
title_zh: 价值几何：语言模型中伦理偏好对齐的任务向量组合
authors:
- Utkarsh Agarwal
- Monojit Choudhury
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2609.21094'
url: https://arxiv.org/abs/2609.21094
pdf_url: https://arxiv.org/pdf/2609.21094
published: '2026-09-16'
collected: '2026-09-22'
category: Training
direction: 任务向量组合与伦理偏好对齐
tags:
- task vectors
- DPO
- multilingual
- ethical alignment
- task arithmetic
- Llama
one_liner: 用任务向量正交化隔离价值偏好方向，实现可逆的伦理立场迁移
practical_value: '- 任务向量正交化技巧可迁移到 LoRA/DPO 微调：将特定风格/价值方向的 task vector 对 general instruction
  following 方向做正交，能分离出干净的方向，便于做可控模型编辑，避免引入无关偏移。

  - 在推荐/生成式候选排序中要警惕 first-option bias：论文发现 Llama-3.2-1/3B 强第一选项偏差，plain fine-tuning
  和 DPO 都能修正到 >98% 准确率，说明简单的 SFT 即可消除位置偏差，值得在评估集上验证。

  - 多语言价值冲突数据构造思路可复制：跨境电商或跨语言 Agent 场景中，可构建类似两选项困境集，用于评估模型在公平性、安全策略上的跨语言一致性。

  - task arithmetic 实现立场反转：实验中通过向量加减获得相反伦理立场的模型，可借鉴用于生成式推荐中在不重新训练的情况下切换风格或安全策略，如保守/探索、品牌调性等。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：LLM 在需要权衡冲突道德价值的场景中隐藏偏见，跨语言指令跟随脆弱，且小模型 out-of-the-box 偏差更明显。

方法：构建 12,000 实例的两选项道德困境数据集，覆盖三种价值对冲突：Honesty vs. Justice、Justice vs. Autonomy、Autonomy vs. Honesty，并翻译为印地语、阿拉伯语、西班牙语、中文。基准 GPT-5-mini 在无 policy 时跨五语言一致偏向 Honesty over Autonomy。Llama-3.2-1/3B 表现出强 first-option bias；plain fine-tuning 与 Direct Preference Optimization 均消除该偏差，准确率提升至 >98%。为解耦数据相关性学习与抽象价值，提出 task vector transfer 实验：计算特定价值偏好方向的任务向量，将其对 general instruction following 向量正交化，再用 task arithmetic 获得相反立场模型，验证该方向能有效隔离特定价值偏好。

关键结果：GPT-5-mini 存在跨语言一致的 Honesty over Autonomy 偏向；Llama 模型的 first-option bias 可被 SFT/DPO 修正；正交化后的 task vector 能实现可逆的伦理立场迁移。
