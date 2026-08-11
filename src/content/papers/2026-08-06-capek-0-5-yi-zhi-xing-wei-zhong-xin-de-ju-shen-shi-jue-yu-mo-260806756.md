---
title: 'Capek 0.5: An Execution-Centric Vision-Language Model for Embodied Intelligence'
title_zh: Capek 0.5：以执行为中心的具身视觉语言模型
authors:
- Ying Chen
- Weizhen Li
- Zhe Hu
- Zhenjiang Li
- Rui Jiang
- Zhifeng Gu
- Lihuang Fang
- Jiangping Liu
- Lei Yi
- Jie Chen
affiliations:
- XPENG ROBOTICS
arxiv_id: '2608.06756'
url: https://arxiv.org/abs/2608.06756
pdf_url: https://arxiv.org/pdf/2608.06756
published: '2026-08-06'
collected: '2026-08-11'
category: Training
direction: 执行中心的能力整合与多专才合并训练
tags:
- Embodied AI
- Capability Taxonomy
- Model Merging
- Reinforcement Learning
- Policy Distillation
- Vision-Language Model
one_liner: 提出按执行阶段划分能力分类，通过专才强化学习与权重合并-蒸馏实现统一多模态模型
practical_value: '- **多能力统一模型训练范式**：以电商/推荐系统中的多任务（CTR/CVR/搜索相关性）为类比，可先将不同目标视为独立能力，各自训练专才（LoRA或独立头），再通过权重合并（如TIES-Merging）和路由蒸馏，得到一个推理开销低且保留各能力的统一模型，避免多模型部署。

  - **可验证奖励驱动的强化学习**：在推荐Agent的动作决策（如消息推送时机、优惠券发放）中，可利用规则/仿真环境构造可验证奖励（收益提升、转化率），直接用RL优化LLM策略，减少对人工偏好标注的依赖。

  - **能力分类指导系统设计**：借鉴“空间推理、时间理解、动作指导、状态验证”的分类，在搜索推荐Agent中显式拆分出“用户意图理解、长短期兴趣建模、item选择、结果验证”等子能力，使数据构造和训练目标更聚焦。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：机器人执行需要空间推理、时间理解、动作预测和状态校验等多种能力，但现有方法按孤立任务训练，缺乏围绕执行过程的整体整合。

**方法关键点**：
- 提出执行中心的能力分类法，将具身能力分为四族：空间推理、时间理解、动作指导、状态验证。
- 训练流程：先基于共享VLM骨干，为每项能力训练专才（RL + 可验证奖励，如IoU、成功标志），得到多个专才模型。
- 推理时统一：① 权重空间合并（如DARE-TIES），将专才参数融合为一个基模型；② 路由策略蒸馏，训练一个策略路由器，动态选择保留的专才行为，最终产出单一推理模型。
- 模型规模：分别实例化2B和35B-A3B MoE版本。

**关键结果**：
- 在多个公开具身基准上（含新提出的状态校验基准StateBench），统一模型相比初始VLM提升大多指标，能力保留率量化评估显示四类能力损失可控，并成功迁移至闭环仿真任务。
