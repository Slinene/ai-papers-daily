---
title: 'Taylor-Calibrate: Principled Initialization for Hybrid Linear Attention Distillation'
title_zh: 泰勒校准：混合线性注意力蒸馏的原则性初始化
authors:
- Zhongzhu Zhou
- Qingyang Wu
- Junxiong Wang
- Mayank Mishra
- Shuaiwen Leon Song
- Ben Athiwaratkun
- Chenfeng Xu
affiliations:
- The University of Sydney
- Together AI
- University of California, Berkeley
- The University of Texas at Austin
- Microsoft
arxiv_id: '2606.16429'
url: https://arxiv.org/abs/2606.16429
pdf_url: https://arxiv.org/pdf/2606.16429
published: '2026-06-14'
collected: '2026-06-20'
category: LLM
direction: 高效 LLM 架构的蒸馏初始化
tags:
- linear attention
- distillation
- initialization
- Taylor expansion
- Gated DeltaNet
one_liner: 利用泰勒展开匹配教师注意力统计量，让混合线性注意力学生初始化更好，节省 4.9-9.2 倍训练代价
practical_value: '- 电商推荐场景的用户行为序列 Transformer 可部分替换为 Gated DeltaNet，并用 Taylor-Calibrate
  初始化，无需重训即可获得低延迟推理与更小 KV cache。

  - 知识蒸馏时，可直接借鉴定量匹配教师注意力的初始化策略，避免学生早期不稳定的动态重建，加速推荐大模型压缩。

  - Agent 的长期记忆模块若使用线性注意力，可复用泰勒统计初始化思想，用少量数据对齐教师记忆读写门控，提升记忆一致性。

  - 方法仅需少量校准数据、无反向传播，可在线快速将预训练推荐模型转为高效推理架构，大幅降低工程上线成本。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：将预训练 Transformer 转为 Gated DeltaNet 等混合线性注意力模型能大幅降低长上下文推理开销，但直接复制参数初始化会导致学生动态失配，大部分蒸馏步骤浪费在修复初始状态上。  
**方法**：提出 Taylor-Calibrate，分两步：① 基于泰勒展开，利用教师注意力矩阵的局部统计量，解析地设定学生的 value 投影、memory 衰减系数、write gate 和 output gate；② 进行轻量的逐层输出对齐，使每层级联匹配教师输出。全过程无反向传播，只需前向传播少量数据。  
**结果**：在四种教师设置和三种保留层策略下，Taylor-Calibrate 使学生零样本能力大幅提升（代表性消融中最高 88 倍改进），达到同一恢复目标所需蒸馏 token 数量减少 4.9–9.2 倍。
