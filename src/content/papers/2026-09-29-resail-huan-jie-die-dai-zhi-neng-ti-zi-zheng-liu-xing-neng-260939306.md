---
title: 'ReSAIL: Mitigating Collapse in Iterative Agent Self-Distillation'
title_zh: ReSAIL：缓解迭代智能体自蒸馏性能崩溃
authors:
- Shengjie Jin
- Hengbo Xu
- Zelong Sun
- YuJie Guo
- Zhiwu Lu
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
arxiv_id: '2609.39306'
url: https://arxiv.org/abs/2609.39306
pdf_url: https://arxiv.org/pdf/2609.39306
published: '2026-09-29'
collected: '2026-10-08'
category: Agent
direction: Agent 自蒸馏训练稳定化
tags:
- Iterative Self-Distillation
- Privileged Information
- Agent Training
- Knowledge Distillation
- Collapse Mitigation
one_liner: 提出 ReSAIL 插件，通过选择特权信息影响大的步骤蒸馏并保持特权条件分布，平均提升 22.5% 成功率
practical_value: '- 在电商导购/客服 Agent 的迭代自蒸馏训练中，若教师有特权信息（如用户真实意图、后续转化、库存），避免直接用线上部署轨迹蒸馏，可借鉴
  ReSAIL：选择 PI 影响大的步骤蒸馏，并用教师 PI 条件输出作为正则，稳定多轮迭代。

  - 离线数据选择可用 sensitivity 指标：计算 teacher 在有无 PI 下输出分布差异，筛选差异大的交互步骤，提升数据效率，减少无效样本。

  - 工程实现上，在学生训练 loss 中加入与冻结 teacher 的 KL 散度（针对 PI 条件分布），即使部署时无 PI 也能保持隐式行为一致性，防止下一轮
  teacher 退化。

  - 对搜索推荐中的 query 改写/推荐解释 Agent，若使用 oracle 信息（点击/购买标签）自蒸馏，可沿用“保留特权行为”思想，避免多轮迭代后策略漂移。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：迭代自蒸馏让 LLM agent 从部署轨迹中学习，实现递归自我改进，但现有方法在多轮循环中出现部署性能和带特权信息（PI）任务性能的同步下降（collapse）。

**方法关键点**：ReSAIL 作为插件增强迭代 PI-based 自蒸馏。它选择 PI 对 teacher 预测影响最大的交互步骤进行蒸馏，并平衡不同轨迹上的蒸馏损失；同时用冻结 teacher 的 PI 条件输出分布对学生进行正则，无论在选中或未选中步骤上，以保留 PI 条件行为供下一轮监督。

**关键结果**：在 ALFWorld 和 TextCraft 上，ReSAIL 跨模型规模三个循环持续提升，添加到自蒸馏基线后最终循环成功率平均绝对增益 22.5%；在 AITZ 上，敏感度引导的离线数据选择也提升了多模态 GUI agent 的动作预测准确率。首次证明更鲁棒的学习机制可缓解迭代自蒸馏中的性能崩溃。
