---
title: 'ASARL: Autonomous Social-Aware Relevance Learning for QQ Search'
title_zh: ASARL：面向社交搜索的自主多智能体相关性学习框架
authors:
- Tao Su
- Jinjing Hu
- Xiao Wang
- Xingzhong Cao
- Hui Wang
affiliations:
- Tencent PCG
arxiv_id: '2607.26593'
url: https://arxiv.org/abs/2607.26593
pdf_url: https://arxiv.org/pdf/2607.26593
published: '2026-07-29'
collected: '2026-07-30'
category: MultiAgent
direction: 多Agent数据治理与搜索相关性学习
tags:
- Multi-Agent
- Social Search
- Relevance Learning
- LLM
- Preference Optimization
- Knowledge Distillation
one_liner: 通过多智能体协同数据治理与分阶段偏好对齐训练，实现社交搜索相关性理解的自动化与社交感知
practical_value: '- **多智能体数据标注流水线可迁移到电商搜索**：ReasonAgent 生成推理标签、CriticAgent 核查一致性、GenAgent
  生产长尾样本的闭环，能降低人工标注成本，缓解长尾查询覆盖不足，尤其适合大量非标品的电商搜索场景。

  - **分阶段训练策略值得复现**：先用领域特化的 Reasoning CoT 做 SFT 注入知识（Social Context Training），再用 DPO
  对齐真实点击信号（Preference-Guided Optimization），最后蒸馏到轻量模型（Social Distillation），这套流程可直接用于电商搜索相关性优化。

  - **社交属性的结构化建模思路可用**：将用户意图与社区/商品属性对齐，形成可解释的推理链，既能改善模型判断准确性，又能输出可读的排序理由，利于搜索诊断和运营。

  - **真实在线实验验证了收益**：在 QQ 频道和群搜索上，CTR 提升 1.36%~2.69%，Join Rate 提升 1.06%~2.59%，部署达 1200
  万 DAU，说明该方法可同时提升点击和深层转化，对电商搜索有直接参考价值。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
社交平台搜索的查询高度非正式，充满圈层用语和俚语，导致传统搜索相关性方法面临三大挑战：上下文差异（模型缺乏社交语义）、数据稀缺（长尾社区标注不足）与行为驱动动态（静态标注无法反映用户互动反馈）。需要一套能自动化生成高质量社交标注数据、并融合用户行为信号的相关性学习框架。  

**方法**  
- **多智能体协作数据治理**：ReasonAgent 依据预定义的 10 类社交属性（如年龄、定位、游戏等）进行意图‑属性匹配，输出“相关/部分相关/不相关”标签及推理链；CriticAgent 检查推理‑标签一致性、分布平衡性，并将反馈回传给 ReasonAgent 迭代修正（修正率约 21%）；GenAgent 针对长尾意图生成补充标题样本，经 Reason/Critic 校验后入库，形成高质量训练集。  
- **三阶段训练**：① Social Context Training（SCT）：用“推理+标签”和“仅标签”两类 prompt 进行 SFT，让模型学会社交感知推理；② Preference-Guided Optimization（PGO）：对模型预测与真实标签不符的样本，利用点击率、加入率信号验证后构建偏好对，以 DPO 损失对齐用户行为；③ Social Distillation（SD）：将 8B 教师模型的知识蒸馏到 RoBERTa 学生模型，服务在线低延迟需求。  

**实验**  
离线在 1.1M QQ 搜索 query‑title 对上评测，ASARL SCT+PGO 8B 取得 Macro‑F1 83.66、NDCG@4 77.93、ACC 84.52，显著优于微调后的 BERT、RoBERTa、LLMBase。消融显示全量三 Agent 比仅用 ReasonAgent 的 Macro‑F1 提升 2.59 点，Social‑Aware CoT + Label 训练比纯标签训练准确率高 4.78 点。在线 A/B 测试（20% 流量）：频道搜索 CTR +2.69%、JoinRate +2.59%、GSB +11.66%；群搜索 CTR +1.36%、JoinRate +1.06%、GSB +16.66%，验证了用户参与与平台增长双赢。
