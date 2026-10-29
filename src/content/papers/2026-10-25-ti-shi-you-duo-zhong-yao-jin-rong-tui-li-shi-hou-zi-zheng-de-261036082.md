---
title: How Much Does the Hint Matter? Scope Conditions for Hindsight Self-Distillation
  in Financial Reasoning
title_zh: 提示有多重要？金融推理事后自蒸馏的边界条件
authors:
- Johnny Yu
- Cyril Gorlla
affiliations:
- University of California, Berkeley
- CTGT
arxiv_id: '2610.36082'
url: https://arxiv.org/abs/2610.36082
pdf_url: https://arxiv.org/pdf/2610.36082
published: '2026-10-25'
collected: '2026-10-29'
category: Training
direction: 事后自蒸馏 · 多步推理
tags:
- self-distillation
- hindsight
- reasoning
- on-policy
- LLM
- financial-reasoning
one_liner: 提出 Fin-SD，以学生自定位错误并生成提示、截断错误前缀进行事后自蒸馏，无需外部教师即可提升多步推理
practical_value: '- 在电商/Agent 中需要多步推理（优惠计算、库存规则、合规审核）但只能本地部署小模型时，可借鉴 Fin-SD：让学生自己生成提示、在正确前缀上条件蒸馏，无需外部教师或完整答案，适配数据驻留与隐私约束。

  - 关键 trick：提示内容不重要，监督位置才重要；可用通用/模板化反馈替代精写 critique，显著降低标注与生成成本，只需定位首个错误步骤即可施加有效监督。

  - 同家族更大模型生成提示没有额外收益，说明业务中不必调用 6 倍参数模型做教师或标注，小模型自蒸馏即可省算力。

  - 蒸馏后生成 token 少 9.5%，有利于降低 Agent 推理延迟和线上成本；通用推理/合规指标无退化，适合作为垂直推理增强的轻量后训练工序。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：金融机构受数据驻留限制只能部署开源小模型，但多步量化推理落后前沿；传统 on-policy distillation 依赖外部强教师，而 on-policy self-distillation 需要完整参考解。作者质疑完整参考信号是否必要。

**方法关键点**：Fin-SD 针对学生失败的题目：(1) 学生自己定位第一个错误推理步骤并写简短 critique；(2) 截断错误位置之前的轨迹作为正确前缀；(3) 冻结学生副本，以“前缀+提示”为条件生成教学轨迹；(4) 在 reverse KL 下用短 rollout 将该老师蒸馏回学生。全程无外部模型梯度。

**关键结果**：在 FinanceReasoning Hard 上 Fin-SD 较 base 提升 3.03pp；将 critique 替换为通用反馈获得相同增益，说明提示内容不重要、监督位置才关键；GPT-OSS-120B 提示不优于自写提示；Fin-SD 匹配完整参考解 OPSD 精度但生成 token 少 9.5%；MMLU-Pro 与 FinTrust 合规审计无显著退化。
