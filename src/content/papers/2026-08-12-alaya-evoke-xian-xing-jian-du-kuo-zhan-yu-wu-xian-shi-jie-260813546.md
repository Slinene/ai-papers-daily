---
title: 'Alaya-EVOKE: From Linear-Scaling Supervision to Endless World'
title_zh: Alaya-EVOKE：线性监督扩展与无限世界生成
authors:
- Yuanyang Yin
- Gongxuan Wang
- Yifan Zhan
- Chuanhao Li
- Kaipeng Zhang
- Feng Zhao
affiliations:
- MoE Key Lab of BIPC, USTC
- Shanghai Innovation Institute
- Alaya Lab
arxiv_id: '2608.13546'
url: https://arxiv.org/abs/2608.13546
pdf_url: https://arxiv.org/pdf/2608.13546
published: '2026-08-12'
collected: '2026-08-15'
category: Multimodal
direction: 交互式世界模型 · 长时记忆与蒸馏
tags:
- World Model
- Long-Horizon Generation
- Sparse Attention
- Distillation
- External Memory
- Linear Scaling
one_liner: 外部化世界状态并重新设计长时域教师，蒸馏出3步无CFG学生模型，实现持久记忆与持续生成
practical_value: '- 外部可索引记忆库：将长会话状态存入 camera-indexed world state bank，按当前视图检索相关片段，避免上下文无限增长；在电商用户行为序列建模中可维护外部用户状态库，按当前
  query/item 检索相关历史，而非全量塞入 prompt。

  - 长时域教师训练：使用 chunk-wise 分组稀疏注意力 + 检索远处帧 + 线性注意力全局状态实现线性成本长序列监督；在序列推荐或会话模型训练长行为序列时可借鉴此架构降低计算与内存。

  - 蒸馏方案：用 30 秒长时域 distribution-matching 目标 + self-forced rollouts 将长时一致性迁移到 3 步学生模型，并去除
  CFG；在生成式推荐/文案生成中可用类似 rollouts + 分布匹配蒸馏提升 few-step 生成质量。

  - chunk 级条件控制：支持在序列中途改变 prompt 和事件，适合交互式推荐/Agent 长任务中分段注入新指令，保持响应性。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：交互式世界模型需同时满足持久记忆、低延迟交互和长时域生成，但这些需求冲突——历史存于上下文或 KV cache 导致成本持续增长；few-step 生成能力受限于 teacher。

**方法关键点**：
- 将持久世界状态外部化为 camera-indexed world state bank，按视图检索相关信息，保持 denoiser 上下文有界。
- 重新设计 teacher 支持长时域监督：稀疏注意力结合 chunk-wise 分组、检索远处帧和线性注意力全局状态，使内存与计算线性增长。
- 用 30 秒 distribution-matching 目标 + self-forced rollouts 蒸馏到 3 步学生模型，无需 CFG，提升抗长期内容漂移能力，同时保持条件控制。

**关键结果**：单张 H200 上 384×640 分辨率每 1.5s chunk 生成耗时 2.11s；3 步世界模型在 WBench 达 SOTA，在 VBench-Long 与 VBench-2.0 视觉质量保持竞争力。
