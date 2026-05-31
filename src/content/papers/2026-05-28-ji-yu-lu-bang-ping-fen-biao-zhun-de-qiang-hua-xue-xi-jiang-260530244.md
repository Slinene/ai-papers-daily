---
title: Reinforcement Learning with Robust Rubric Rewards
title_zh: 基于鲁棒评分标准的强化学习奖励方法
authors:
- Ya-Qi Yu
- Hao Wang
- Fangyu Hong
- Xiangyang Qu
- Gaojie Wu
- Qiaoyu Luo
- Nuo Xu
- Huixin Wang
- Wuheng Xu
- Yongxin Liao
affiliations:
- Huawei Technologies Co., Ltd.
arxiv_id: '2605.30244'
url: https://arxiv.org/abs/2605.30244
pdf_url: https://arxiv.org/pdf/2605.30244
published: '2026-05-28'
collected: '2026-05-31'
category: Training
direction: 多模态准则级强化学习奖励设计
tags:
- RLVR
- Reward Design
- Multi-modal
- Rubric
- Reinforcement Learning
one_liner: 将RLVR扩展到准则级验证，通过LLM抽取器+确定性验证器与LLM评判双路径、最小暴露和分层聚合，显著提升多模态模型性能
practical_value: '- 推荐/Agent 的多目标优化可借鉴分层聚合思想，将核心指标（如点击率、转化率）作为 essential criteria
  优先保障，辅助指标（如 diversity）按权重融合，避免多目标互相干扰。

  - 对于部分可验证的业务指标（如推荐结果是否符合政策规范），可采用“确定性规则提取 + LLM 评判”双路径奖励：先用规则快速检查硬约束，再用 LLM 评估主观质量，兼顾效率与灵活度。

  - 最小暴露策略（屏蔽 ground truth 或原始图片）可直接用于奖励函数设计，防止模型学习到利用奖励漏洞的采样行为，提升在线 RL 训练的稳定性。

  - rollout 组内分数缓解饱和的技巧可迁移到推荐策略梯度训练中，通过组内 baseline 或标准化避免模型过早收敛到次优策略。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：RLVR 依赖完全可验证的任务奖励，但视觉语言任务常为部分可验证，需多准则监督（如感知细节、推理步骤）。论文提出 RLR^3，将 RLVR 从任务级验证拓展到准则级验证。

**方法**：针对每个实例的评分标准（rubric），采用双路径执行：① 对于可机械验证的准则，用 LLM 作为提取器，从输出中提取关键信息后，由确定性验证器判分；② 对于不可验证准则，直接由 LLM 评判器打分。为防止奖励黑客，引入最小暴露策略——为提取器屏蔽标准答案，为评判器屏蔽图像。此外，采用分层聚合：将准则划分为 essential 和 additional 两类，优先保证 essential 得分，再按权重融合 additional 得分，并引入 rollout 组内归一化缓解分数饱和。

**结果**：在 Qwen3-VL-30B-A3B 模型上，15 个多模态基准测试中，RLR^3 一致优于 RLVR，相对基模型提升 4.7 分，且超越官方的 instruct-to-thinking 模型差距。对照实验证实，确定性验证和最小暴露显著降低了可利用的假阳性。
