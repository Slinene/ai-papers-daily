---
title: 'PIVOT: Progressive Intervention via Online Teacher Correction'
title_zh: PIVOT：通过在线教师纠正进行渐进式干预
authors:
- Zhihao Yang
- Boyuan Zheng
- Puhui Tan
- Yukun Chen
- Kuan Zhang
- Longze Chen
- Jiaming Li
- Renke Shan
- Lu Wang
- Xianpei Han
affiliations:
- University of Chinese Academy of Sciences
- Tsinghua University
- Chinese Information Processing Laboratory, Institute of Software, Chinese Academy
  of Sciences
- School of Advanced Interdisciplinary Sciences, University of Chinese Academy of
  Sciences
arxiv_id: '2610.40576'
url: https://arxiv.org/abs/2610.40576
pdf_url: https://arxiv.org/pdf/2610.40576
published: '2026-10-29'
collected: '2026-10-31'
category: Training
direction: 强化学习训练 · 在线教师干预
tags:
- RLVR
- Teacher-Student
- Token-level KL
- Sparse Reward
- Reasoning
- Intervention
one_liner: 在RLVR中插入教师纠正轨迹并施加token级KL监督，大幅提升困难推理任务的学习效率与最终表现
practical_value: '- 在电商/Agent多步决策任务中，RLVR常因稀疏奖励（最终是否成交、任务是否完成）而训练低效；可引入教师模型（如GPT-4/内部大模型）在失败轨迹上在线生成修正步骤，并把这些修正插入学生rollout，只对插入段做token级KL蒸馏，避免整条轨迹过度依赖教师导致不可学。

  - 当一组rollout全部失败时，结果奖励无梯度；可借鉴PIVOT的双重信号：先通过轨迹级干预保证至少部分轨迹包含正确片段，再对教师段做密集token级监督，这适合电商智能客服、商品推荐对话等场景中“用户不满意”的负样本利用。

  - 论文的消融表明，干预位置（如失败点附近）和KL监督范围（仅教师段vs全轨迹）对最终性能影响显著；在业务中可先小规模网格搜索这些超参数，避免教师信号过强导致学生退化为模仿教师，丧失RLVR的探索收益。

  - 若已有线上强模型可作为教师，PIVOT的在线纠正成本可控，适合将弱模型（部署端）通过RLVR+教师干预进行蒸馏式增强，用于推荐解释生成、搜索query改写等轻量生成任务。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：RLVR在困难推理任务中面临稀疏结果奖励问题：当一组rollout全部失败时，无法给出任何学习信号。更强的教师模型能提供额外指导，但如何整合教师信号使其既帮助学生接触到成功轨迹，又保持对学生可学习，仍待解决。

**方法关键点**：论文区分轨迹级干预（提升命中奖励轨迹的概率）与token级监督（提供密集目标）。单独使用任一机制可能不足。PIVOT将教师生成的纠正直接插入学生rollout的对应位置，并仅对这些被插入片段施加token级KL监督，同时保留原始RLVR目标；通过系统分析干预时机与监督方式，得到有效配方。

**关键结果**：在困难逻辑游戏和数学推理基准上，PIVOT一致超过现有方法，逻辑游戏avg@8从最佳基线的19.5%提升到35.6%，几乎翻倍。
