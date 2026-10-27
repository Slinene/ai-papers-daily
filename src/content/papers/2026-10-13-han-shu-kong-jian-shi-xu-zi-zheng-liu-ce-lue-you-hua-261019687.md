---
title: Function-Space Temporal Self-Distillation for Policy Optimization
title_zh: 函数空间时序自蒸馏策略优化
authors:
- Aryan Das
- Arnab Bhattacharya
- Vinay Kumar Verma
affiliations:
- Indian Institute of Technology Kanpur
arxiv_id: '2610.19687'
url: https://arxiv.org/abs/2610.19687
pdf_url: https://arxiv.org/pdf/2610.19687
published: '2026-10-13'
collected: '2026-10-27'
category: Training
direction: 强化学习策略优化与自蒸馏
tags:
- RLVR
- Self-Distillation
- Policy Optimization
- Temporal Memory
- Privileged Adaptation
one_liner: 提出FSPO单策略框架，以历史分布为固定时序目标并引入特权分歧校正，实现稳定高效的策略优化
practical_value: '- 在训练LLM-based推荐Agent或对话策略时，可采用“历史分布作为固定时序目标”的思路，不维护独立teacher模型，减少显存（论文中峰值从70GB降至56GB），适合资源受限的迭代训练。

  - “特权分歧校正”可用来抑制模型生成路径中局部过高的token概率，防止在稀疏奖励下过早收敛到次优回复，类似推荐系统中对高置信度但低转化动作的惩罚。

  - “可靠性自适应接地”策略：当模型自生成证据多次失败时自动加强外部参考监督（如规则、知识库），可迁移到电商Agent的工具调用或商品推荐解释中，提高事实准确性。

  - “质量与覆盖感知记忆”只保留验证过的行为并改善特权演示，可用于构建在线学习中的经验回放池，优先存储高奖励且多样性的轨迹，优化长尾场景。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：RLVR使用标量奖励对整条响应进行粗粒度监督，造成信用分配困难，尤其当奖励稀疏或所有采样响应得到相同结果时。自蒸馏虽能提供token级指导，但自教师模型随学生同步更新，目标不稳定，需要额外正则。

**方法**：提出FSPO，一个单策略框架，结合当前特权适应与函数空间时序巩固。核心是存储稀疏历史next-token分布作为固定时序目标，实现时序分离而无需维护持久teacher模型。此外引入三个关键组件：特权分歧校正显式抑制局部被高估的动作；可靠性自适应接地在自生成证据反复失败时加强参考监督；质量与覆盖感知时序记忆保留被验证的行为并改善特权演示。

**结果**：在推理和工具使用基准上，5小时训练预算内FSPO达到最高平均精度，较最强基线平均提升约4个百分点；在Olmo3-7B-Instruct上峰值内存从约70GB降至56GB。
