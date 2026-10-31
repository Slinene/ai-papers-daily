---
title: 'Every Token Needs Its Own Teacher: Multi-teacher Adaptive On-policy Self-distillation'
title_zh: 每个 token 都需要专属教师：多教师自适应 on-policy 自蒸馏
authors:
- Yifu Luo
- Chuang Ma
- Zeyu Chen
- Enkelejda Kasneci
- Qi Chen
- Gjergji Kasneci
affiliations:
- TU München
- Munich Center for Machine Learning
- Kyoto University
- ELLIS Institute Finland
- Aalto University
arxiv_id: '2610.40574'
url: https://arxiv.org/abs/2610.40574
pdf_url: https://arxiv.org/pdf/2610.40574
published: '2026-10-29'
collected: '2026-10-31'
category: Training
direction: LLM 后训练 · token 级多教师 OPSD
tags:
- On-policy Self-distillation
- Token-level Teacher Selection
- Multi-teacher
- KL Divergence
- Majority Voting
- Math Reasoning
one_liner: 提出 token 级自适应 on-policy 自蒸馏，用多教师池+多数投票+KL 为每个 token 选教师，数学推理最高提升+5.9
practical_value: '- 在生成式推荐 / query 生成 / 文案生成的 on-policy self-distillation 中，如果使用高质量参考（如人工标注、规则
  template）作为 privileged reference，建议构造多教师池：对参考做 prefix/suffix/random-span 截断、不同保留比例，而不是只用完整参考；再按
  token 选择教师，可避免过度尖锐监督。

  - 多数投票 + KL 距离是低成本的 token 级选择规则：先看候选教师对当前学生采样 token 的支持方向是否一致，再在一致子集里选 KL 最大的教师；不需要额外模型，可直接嵌入现有训练
  pipeline。

  - 消融表明，多教师池配随机选择或平均 loss 提升有限，真正收益来自自适应分配；因此如果业务上做多教师蒸馏，不能只做 ensemble，需要设计 token
  级选择策略。

  - 若在搜索/推荐 Agent 中让 LLM 生成推理或决策轨迹，可借鉴该 work 的 token 级教师干预评估法来快速诊断哪些位置需要更强监督，而不是整段统一加
  loss。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
On-policy Self-distillation (OPSD) 在 LLM 后训练中相比 SFT 与 RLVR 有优势：教师拥有特权参考，能提供 dense token 级信号，同时又在 student 自己采样的轨迹上训练，减少 exposure bias。但已有研究发现，过度暴露于特权参考会使教师分布过于尖锐，与学生学习动态不匹配，导致推理能力下降。现有 adaptive OPSD 只在 response 级调整参考暴露比例，所有 token 共享同一个教师；该工作质疑这一做法，认为 token 级偏好不同，需要为每个 token 选择专属教师。

## 方法关键点
- 通过 teacher-intervention 试点研究，在 student 生成的 response 中插入教师 continuation，再交还 student 完成，用 accuracy gain 衡量教师在该 token 位置的适配度。
- 三个发现：token 间教师偏好重叠仅约 50%；多数投票可得到可靠教师子集（约 80-90% 最优教师落在多数子集）；该子集中 KL 距离最大的教师平均增益最高。
- 构建 multi-teacher pool：由 full reference、prefix/suffix/random-span 三种截断策略和 0.5/0.75 两种暴露比例组成 7 个教师。
- token 级两阶段选择：先对每个 token 计算各教师的 advantage sign，取多数方向筛选教师；再在多数子集中选择 student-teacher KL 最大的教师作为该 token 的监督。
- 最终 loss 为对每个 token 使用其选定教师的 forward KL，替代单一教师。

## 关键实验
在 DeepMath-103k 上训练，在 AMC23、AIME24、AIME25 上评估，模型为 Qwen3-1.7B/4B/8B，对比 OPSD、SDPO、Paint。平均准确率提升：Qwen3-1.7B +5.9、Qwen3-4B +1.5、Qwen3-8B +2.8，均超过基线；在 AIME25 上提升尤其明显。消融显示：多教师池优于任何单个教师；token 级自适应分配显著优于随机选择或平均 loss；多数投票与 KL 选择两阶段都必要，去掉任一组件都会掉点。

## 最值得记住的一句话
教师偏好逐 token 变化，用“多数投票定方向 + KL 选信息量”能为每个 token 选中更合适的教师，从而显著优于单一教师或 response 级自适应。
