---
title: 'Knowing When to Teach: Learning from Teachable Prefixes in Multilingual Reasoning
  Distillation'
title_zh: 知道何时教：多语言推理蒸馏中的可教前缀学习
authors:
- Jaewon Cho
- Minseo Yoon
- Jinyoung Park
- Jinwoo Seo
- Jaewon Chu
- Alice Oh
- Hyunwoo J. Kim
affiliations:
- KAIST
- Korea University
arxiv_id: '2611.08179'
url: https://arxiv.org/abs/2611.08179
pdf_url: https://arxiv.org/pdf/2611.08179
published: '2026-11-05'
collected: '2026-11-06'
category: Training
direction: 多语言推理蒸馏 · 可教前缀筛选
tags:
- On-Policy Distillation
- Multilingual Reasoning
- Teacher Drift
- Self-Distillation
- Reasoning
one_liner: 提出 TOPSD，用 teacher-student 似然定位教师漂移起点并验证可教前缀，只对能恢复正确的前缀做蒸馏。
practical_value: '- 业务蒸馏/自我蒸馏数据质量：如果用 LLM 蒸馏推荐文案、商品描述或 Agent 轨迹，不要对整条轨迹做 token-level
  蒸馏；可复用 TOPSD 的“可教前缀”筛选：用 teacher-student likelihood 差异找到模型开始漂移的位置，只保留教师能从中恢复正确答案的前缀作为监督样本，减少错误
  token 的噪声。

  - 多语言/低资源场景：论文观察到低资源语言 Teacher Drift 更早，业务中做多语言 query 改写、商品标题生成或客服回复时，低资源语言应设置更严格的可教性门槛或更早引入教师强监督，否则蒸馏收益会下降。

  - 在线/离线数据质量信号：teacher-student 似然分歧可作为样本难度和错误位置的细粒度信号，用于数据筛选、主动学习或标注优先级；相比只看整句 reward，更容易定位哪个
  step 该干预。

  - 对 Agent 轨迹训练：如果训练多步 Agent（如搜索-推荐-解说），可以在中间步骤验证教师能否恢复正确结果，只对“可教”片段做模仿学习，避免模型复制错误中间动作。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**
On-Policy Self-Distillation (OPSD) 用同一模型参考解作教师，在自生成轨迹上做 token-level 蒸馏，可提升推理能力。但多语言推理中，学生中间步骤出错不断累积时，教师可能跟随学生错误而非纠正，称为 Teacher Drift；分析显示低资源语言中 drift 更早出现。

**方法关键点**
TOPSD 先用教师和学生在各 token 的似然差异估计漂移起点，选出候选监督前缀；随后验证教师从该前缀继续生成是否能恢复正确答案，只对通过验证的前缀施加蒸馏。这样把监督限制在“可教”的局部轨迹上，避免教师被学生带偏。

**关键结果**
在 10 种语言、3 个模型尺度的多语言数学推理上，TOPSD 一致优于 OPSD，尤其在低资源和中等资源语言上提升明显。
