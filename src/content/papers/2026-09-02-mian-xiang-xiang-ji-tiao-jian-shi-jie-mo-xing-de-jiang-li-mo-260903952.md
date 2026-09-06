---
title: 'WorldReward: Reward Modeling for Camera-Conditioned World Models'
title_zh: 面向相机条件世界模型的奖励建模方法 WorldReward
authors:
- Yibin Wang
- Zehan Wang
- Junshu Tang
- Zhimin Li
- Yujie Zhou
- Jiazi Bu
- Pengyang Ling
- Feng Han
- Zhixiong Zhang
- Long Xing
affiliations:
- Fudan University
- Tencent Hunyuan
- Shanghai Innovation Institute
- Shanghai Jiao Tong University
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2609.03952'
url: https://arxiv.org/abs/2609.03952
pdf_url: https://arxiv.org/pdf/2609.03952
published: '2026-09-02'
collected: '2026-09-06'
category: Multimodal
direction: 多模态奖励建模 · VLM 视频评估
tags:
- World Model
- Reward Model
- VLM
- Preference Optimization
- Video Generation
- RLHF
one_liner: 用 VLM 将长视频按动作分块并投票聚合，统一评测动作一致性与视觉质量
practical_value: '- 长序列生成（如多步商品推荐、对话式导购、视频广告脚本）中，可借鉴“动作对齐分块 + 结构化证据 + 逐块决策投票”的思路，避免长上下文稀释局部关键信号，适合构建
  LLM 评估器或奖励模型。

  - 偏好数据构建可复用其管线：先由 frontier VLM 生成结构化判断，再用工具化 agent 审计和定向人工复核，降低标注成本并提高一致性，适用于内容生成质量评估、AIGC
  审核等场景。

  - 在电商多模态生成（如商品视频、虚拟试穿）中，建议拆分“任务完成度”与“画质/自然度”双 reward 分别聚合，避免单一指标失衡，便于 RL 后训练。

  - 若业务涉及“按指令生成视频/图片”，可参考其 benchmark 设计：按人类偏好分维度（动作/外观/运动）测量 reward model 一致性，而非只看整体分数，从而更精准定位模型短板。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**  
相机条件世界模型生成交互视频时，需同时保证动作执行和视觉质量。现有奖励方法要么基于几何轨迹评估动作但无法判断视觉，要么基于图像质量但忽略动作执行与时间动态。直接让 VLM 判断整段长视频和完整动作序列，会因上下文过长而遗漏短时局部动作证据。

**方法关键点**  
WorldReward 将配对视频按动作对齐切块，对每个块组织结构化视觉证据，评估动作一致性与视觉质量，再通过投票聚合成视频级偏好。训练数据由前沿 VLM 生成结构化判断，经多轮工具化 agent 审计和定向人工复核，构建大规模推理增强偏好数据集。同时提出 WorldReward-Bench，人类标注基准，度量奖励模型在动作一致性、外观质量、运动质量三个维度上与人类偏好的一致性。

**关键结果**  
在 WorldReward-Bench 上，WorldReward 三项一致性均最高，分别超过 GPT-5.5 3.42、1.45、3.56 个百分点。用于 HY-WorldPlay 1.5 的 RL 后训练后，短到长时域的动作执行和视觉质量均得到一致提升。
