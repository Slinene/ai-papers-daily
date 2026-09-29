---
title: 'Beyond Teacher Assignment: Domain-Normalized Multi-Teacher On-Policy Distillation'
title_zh: 超越教师分配：领域归一化的多教师在线策略蒸馏
authors:
- Xin Li
- Hao Jiang
- Xin Gao
- Annan Wang
- Yuchen Xie
- Jinghao Guo
- Xingwei Qu
- Yichi Zhang
- Chau Yuen
affiliations:
- Nanyang Technological University
- Yale University
- University of Manchester
arxiv_id: '2609.35347'
url: https://arxiv.org/abs/2609.35347
pdf_url: https://arxiv.org/pdf/2609.35347
published: '2026-09-27'
collected: '2026-09-29'
category: Training
direction: 多教师策略蒸馏 · 领域归一化
tags:
- Multi-Teacher Distillation
- Reinforcement Learning
- Domain Normalization
- LLM Post-training
- Policy Distillation
one_liner: 提出 DN-MOPD，按领域反馈 spread 重缩放，解决多教师策略蒸馏中反馈尺度失衡问题
practical_value: '- 在多任务/多专家蒸馏或 RL 融合时，不要只做任务路由，还要监控并平衡不同 reward/teacher 反馈的尺度；可提前统计各领域反馈的标准差，按该值重缩放，避免高方差信号主导共享模型。

  - 如果在线估计 spread 成本高，可直接使用离线测得的固定领域权重，论文表明固定权重接近测量值时性能相当，便于工程落地。

  - 对电商搜索推荐中的多目标强化学习（如点击率、转化率、GMV 约束），不同目标 reward 方差差异大，容易让某个目标主导策略，可借鉴按目标 spread
  归一化再加权。

  - 在 Agent 或多 teacher 集成场景，评估各 teacher 反馈分布，优先降权高方差域，而不是单纯提升弱势域，控制实验显示调低主导域反馈是关键。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：RL 后训练常产生多个领域专家（数学、代码、指令遵循），但部署需要单一模型。多教师在线策略蒸馏（MOPD）通过按 prompt 领域路由让专家逐 token 指导学生；然而路由只决定“谁教”，未决定反馈强度。作者在 Qwen3.5 三个尺寸上发现 MOPD 学生未能超越最佳单专家，数学收益几乎丢失；原因是反馈分布不平衡，指令遵循反馈的 spread 数倍于数学，主导学生更新。

**方法**：提出 Domain-Normalized MOPD（DN-MOPD），保留路由，对每个领域的反馈按其实测 spread（如标准差）重缩放，平衡不同领域对共享学生的更新幅度。

**结果**：在六个公开基准上，DN-MOPD 在所有模型尺寸、三个随机种子、两种答案长度限制下平均分均超越 MOPD，并恢复大部分数学增益。控制实验表明增益主要来自调低指令遵循反馈而非单纯调高数学；且固定领域权重接近 DN-MOPD 测量值时性能相当。结论：合并专家需同时决定“谁教”和“教多强”。
