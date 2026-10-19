---
title: 'Beyond the Answer: Student-Conditioned Trace Construction for Reasoning Distillation'
title_zh: 超越答案：学生条件化的推理轨迹构建与蒸馏
authors:
- Shaoang Li
- Yanhang Shi
- Yufei Li
- Mingfu Liang
- Frank Shyu
- Sandeep Pandey
- Luke Simon
- Xi Liu
- Jian Li
affiliations:
- Stony Brook University
- Meta AI
arxiv_id: '2610.23831'
url: https://arxiv.org/abs/2610.23831
pdf_url: https://arxiv.org/pdf/2610.23831
published: '2026-10-16'
collected: '2026-10-19'
category: Reasoning
direction: 推理蒸馏 · 学生条件轨迹构建
tags:
- Reasoning Distillation
- Trace Construction
- Student-Conditioned
- Knowledge Distillation
- LLM
one_liner: 提出 ReDiST，以学生自身尝试为起点构建并筛选推理轨迹，提升推理蒸馏效果
practical_value: '- 可借鉴 ReDiST 的“学生条件化”轨迹筛选：在微调推荐/Agent 推理模型时，不要直接用统一 CoT 数据，而是用目标小模型自身的失败尝试作为种子，再结合证据与正确答案改写，能提升学习效率。

  - 用 frozen “student-matched reader” 对候选轨迹打分：以 answer recovery 和 verified-answer
  probability 排序，过滤掉目标模型难以模仿或信息冗余的轨迹；可用于电商多跳问答、广告归因解释等数据清洗。

  - 蒸馏时加 auxiliary answer loss 平衡中间推理与最终答案监督，避免小模型只学会模仿冗长/不适配的推理格式，却答不对。

  - 评估轨迹教学价值时，应在源任务与跨分布 benchmark 同时验证；不同监督配方的排名可能反转，避免单看源域指标选定方案。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：同一答案对应的推理轨迹不一定适合特定学生模型；仅靠最终答案监督不足，但直接用原始轨迹可能因步骤缺失/冗余/表达不匹配而失效。

方法关键点：ReDiST 从学生自身尝试出发，对“答案正确但推理不理想”的草稿结合证据修订，对失败草稿结合正确答案补充引导，生成候选轨迹。随后用冻结的、与学生能力匹配的 reader 对原始与编辑候选打分排序，指标为答案恢复率和给定问题/证据/轨迹下验证答案的概率。最后蒸馏选中轨迹，并用 auxiliary answer loss 平衡中间轨迹与最终答案监督。构建与筛选离线完成，推理只使用蒸馏后的学生模型。

关键结果：实验在 QA 基准上，ReDiST 在源任务与跨基准上均优于仅用答案、原始轨迹及若干轨迹选择/改写基线；且不同监督配方在源与迁移基准上的排序可能不同，说明需跨分布评估轨迹教学效用。
