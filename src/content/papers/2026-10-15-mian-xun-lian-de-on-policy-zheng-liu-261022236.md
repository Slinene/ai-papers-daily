---
title: Training-Free On-Policy Distillation
title_zh: 免训练的 On-Policy 蒸馏
authors:
- Bangji Yang
- Jiajun Fan
- Zhaoyu Zhu
- Hongbo Ma
- Ge Liu
affiliations:
- University of Illinois at Urbana-Champaign
- Tsinghua University
arxiv_id: '2610.22236'
url: https://arxiv.org/abs/2610.22236
pdf_url: https://arxiv.org/pdf/2610.22236
published: '2026-10-15'
collected: '2026-10-18'
category: Training
direction: 无训练模型蒸馏与多专家聚合
tags:
- Training-Free Distillation
- On-Policy Distillation
- Model Merging
- Least Squares
- LLM
one_liner: 提出免训练 on-policy 蒸馏，仅用前向传播和最小二乘逐层合并多个专家模型，无需梯度更新
practical_value: '- 多领域专家模型合并：若业务中有多个针对不同场景（如推荐、搜索、广告）微调的模型，可借鉴 TF-OPD 通过前向计算几百个 rollout
  提取输入二阶矩，逐层最小二乘融合，无需联合训练，节省算力和迭代时间。

  - 模型融合的精度提升：相比简单 task arithmetic 权重平均，逐层最小二乘匹配专家输出分布能保留更多能力；在推荐模型做多目标融合或跨域迁移时可引入此方法提升融合质量。

  - 数据筛选策略：论文发现去除重复循环的生成 token 显著提升融合效果（AIME25 从 task arithmetic 水平到专家水平），提示在蒸馏或融合数据准备中应重点清洗低质量重复内容，避免噪声影响层权重估计。

  - 工程部署：融合只需每专家数 GPU 小时的前向计算，适合快速将多个专家模型合并为通用模型上线，尤其适用于需要频繁更新多领域能力的 Agent 或推荐系统。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：RL 从可验证奖励训练领域专家模型，各专家只擅长单一领域，合并需要再次 RL 或蒸馏，计算开销大。

**方法**：发现当专家共享基座模型时，蒸馏可转化为逐层线性最小二乘问题：融合模型每个线性层需在专家自身生成分布上重现专家输出，只需该分布输入的二阶矩。通过一次前向传播处理几百个 rollout 即可估计这些二阶矩，然后求解闭式解，完全无需梯度更新。此方法称为 TF-OPD。

**关键结果**：在 Olmo 3 7B 上，每专家仅需数 GPU 小时前向计算，融合后的通用模型在七个数学和代码基准上保持大部分专家增益；在 AIME25 上，剔除重复循环的生成 token 后，融合模型从 task arithmetic 水平提升至专家水平，显示数据质量对融合效果至关重要。
