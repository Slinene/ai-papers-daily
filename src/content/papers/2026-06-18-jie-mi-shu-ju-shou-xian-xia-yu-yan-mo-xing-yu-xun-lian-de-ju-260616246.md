---
title: Demystifying Training-Time Augmentation for Data-Constrained Language Model
  Pretraining
title_zh: 解密数据受限下语言模型预训练的训练时数据增强
authors:
- Michael K. Chen
- Xikun Zhang
- Fan Bai
- Zhengding Hu
- Zhen Wang
affiliations:
- UC San Diego
- RMIT University
- Bloomberg AI
arxiv_id: '2606.16246'
url: https://arxiv.org/abs/2606.16246
pdf_url: https://arxiv.org/pdf/2606.16246
published: '2026-06-18'
collected: '2026-06-24'
category: Training
direction: 训练时增强 · 多轮训练正则化
tags:
- data augmentation
- pretraining
- overfitting
- data-constrained
- autoregressive
- regularization
one_liner: 系统研究三类训练时增强（token噪声、序列置换、目标偏移）缓解自回归模型在多轮数据训练时的严重过拟合
practical_value: '- 当训练数据有限需反复遍历（如用户行为序列）时，可在自回归下一行为预测中引入随机 token 替换或 masking 作为增强，延迟过拟合，降低验证损失。

  - 组合多种增强类别（如随机替换 + 序列逆序 + 偏移预测）能进一步降低最小验证 loss，可作为通用训练 trick 加入推荐模型的预训练或微调流程。

  - 目标偏移预测（预测未来第 k 个 token）可迁移到用户长序列建模中，强制模型学习更长期的依赖，减轻短视过拟合。

  - 该方法实现简单，不改变模型结构，适合在现有自回归推荐（如 SASRec 类）或 LLM-based 生成式推荐中快速实验。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：语言模型预训练正进入数据受限、算力充裕的新阶段，固定语料需多轮重复使用。标准自回归下一词预测在此场景下严重过拟合：很快达到最优然后持续恶化。亟需一种正则化手段使模型能从有限数据中更高效地提取可泛化信号。

**方法**：提出三类正交的训练时数据增强，作为隐式正则化器：
- Token 级噪声：随机掩码（预测被掩 token）或随机替换为任一词汇；
- 序列置换：预测顺序从右至左，或采用 Fill-in-the-Middle（给定上下文预测中间）；
- 目标偏移预测：将预测目标由 xt 改为 xt+i（i>1），强制建模更长距离依赖。
对每种增强及组合进行系统消融，在同样数据、同等计算预算下比较验证 loss。

**关键结果**：单独使用任一增强均可延迟过拟合且相对基准降低验证损失，其中随机 token 替换效果最优；组合不同类别增强能进一步压低最小验证损失。实验证实训练时增强能有效缓解自回归预训练的数据低效性，为数据受限 regime 提供了一条简单可行的路径。
