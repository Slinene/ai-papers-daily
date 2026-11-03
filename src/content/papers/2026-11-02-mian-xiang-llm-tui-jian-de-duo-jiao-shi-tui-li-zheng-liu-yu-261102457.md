---
title: Multi-Teacher Reasoning Distillation for LLM Recommendation with Self-Exploration
title_zh: 面向 LLM 推荐的多教师推理蒸馏与自探索框架 MUSE
authors:
- Liangbo Ning
- Siyuan Liang
- Yi Zhou
- Yifeng Zhang
- Qing Li
- Wenqi Fan
- Dacheng Tao
affiliations:
- The Hong Kong Polytechnic University
- Nanyang Technological University
arxiv_id: '2611.02457'
url: https://arxiv.org/abs/2611.02457
pdf_url: https://arxiv.org/pdf/2611.02457
published: '2026-11-02'
collected: '2026-11-03'
category: RecSys
direction: 推理增强推荐 · 多教师蒸馏
tags:
- Reasoning Distillation
- LLM4Rec
- Multi-Teacher
- Contrastive Learning
- Self-Exploration
- Rank-Gain Utility
one_liner: MUSE 构建多教师+学生自探索候选池，用 Rank-Gain 效用筛选并对比蒸馏，让 LLM 推荐器学到真正有益的偏好推理
practical_value: '- **用下游排名收益做无标注推理筛选**：RGUA 直接以 ground-truth item 的全库排名提升作为推理轨迹效用，避免人工标注，很适合电商/广告中大量交互日志。工程上只需轻量
  encoder 算候选 rank，不必引入 LLM evaluator，成本低。

  - **多教师 + 学生自探索的候选池设计**：先让多个 teacher LLM 生成候选，再随训练逐步增加学生采样数量，让模型逐渐摆脱 teacher 知识上限。业务中可对重要用户/类目建立多
  LLM 候选池，用 ranking 指标筛选后再蒸馏。

  - **双对比损失解耦“生成”和“利用”**：ConDistill 让 generator 拉开高/低效用推理的 likelihood；ConUtil 让 encoder
  强制在好推理下比坏推理更接近目标 item，防止模型只依赖历史行为而忽略推理信号。该思路可迁移到多任务推荐排序中，用对比目标强化特征利用。

  - **训练与推理效率可复用**：teacher 推理预生成并缓存，推理时只需 student 单次生成，vLLM 延迟与 R2ec 相当；业务可离线跑多教师，在线保持轻量。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：推理增强推荐中，知识蒸馏比 RL 更稳定，但现有方法依赖单一固定 teacher，受限于教师异质能力、教师知识上限和低质推理监督。教师能写出流畅理由，但未必对下游推荐排名有效；不加区分地蒸馏会浪费算力，甚至强化误导性偏好证据。

**方法关键点**：MUSE 分三阶段。1) 多教师候选池 + 渐进式学生自探索：多个 teacher LLM 生成候选推理，同时学生随训练 epoch 逐步增加采样条数，扩展候选池，突破 teacher 天花板。2) Rank-Gain Utility Assessment (RGUA)：对每条候选推理，计算 ground-truth item 在全库中相对无推理输入的排名提升，归一化后作为效用分，选出最高/最低效用轨迹作为正负对。3) 双对比训练：ConDistill 让学生 generator 对高/低效用推理的归一化 likelihood 差达到与效用差相适应的 margin；ConUtil 让 encoder 在高效用推理下比低效用推理更靠近目标 item；联合 NCE 和 SFT 训练。

**关键实验**：在 Amazon 三个数据集（CDs and Vinyl、Musical Instruments、Video Games）上，学生模型用 Gemma-2-2B / Qwen2.5-3B。相比 LangPTune、R2ec、RecSAVER 等，MUSE 一致最优。例如 CDs 上 Qwen2.5-3B，MUSE N@5=0.0295，R2ec=0.0243，H@5=0.0421 vs 0.0362；Musical Instruments 上 Gemma-2-2B，MUSE N@5=0.0195，R2ec=0.0174。消融证明多教师、自探索、RGUA、双对比均有增益；训练时间与 R2ec 相当，推理延迟不增加。

最值得记住的一句话：**用下游排名提升而非文本流畅度来评估推理轨迹，是让蒸馏真正服务于推荐目标的关键。**
