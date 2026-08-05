---
title: 'ReflectRL: Learning from Golden Negative Trajectories via Reflective-to-Direct
  Reasoning'
title_zh: ReflectRL：从专家失败轨迹中学习反射推理以提升策略训练
authors:
- Jinhe Bi
- Chennan Zhou
- Zengjie Jin
- Aniri
- Shuo Lu
- Wenke Huang
- Hu Cao
- Xun Xiao
- Zhihong Zhu
- Volker Tresp
affiliations:
- National University of Singapore
- Ludwig Maximilian University of Munich
- Technical University of Munich
- Nanyang Technological University
- Peking University
arxiv_id: '2608.03972'
url: https://arxiv.org/abs/2608.03972
pdf_url: https://arxiv.org/pdf/2608.03972
published: '2026-08-04'
collected: '2026-08-05'
category: Training
direction: 强化学习 · 反射推理训练
tags:
- Golden Negative Trajectories
- Reflective Reasoning
- On-Policy RL
- GRPO
- Policy Transition
one_liner: 利用专家模型失败轨迹（黄金负样本）进行反思式推理，并通过策略过渡将能力迁移至直接推理
practical_value: '- **利用高质量负样本作为反思提示**：在搜索推荐场景，可将高置信度负反馈（如用户未点击的精选商品）作为“反思上下文”引入策略训练，引导模型显式分析失败原因并纠正，提升困难样本的利用效率。

  - **反射到直接的训练过渡**：采用余弦衰减等平滑调度，将反思式提示逐步替换为直接提示，使模型内化纠错能力，最终无需额外上下文即可产出高质量决策，适用于RLVR和蒸馏范式。

  - **轻量级即插即用**：无需新增模型、参数或梯度，仅通过预先生成的负样本轨迹和模板切换实现，工程实现成本低，可直接嵌入现有 on-policy 训练管线。

  - **缓解熵坍缩、缩短推理长度**：反射训练能维持策略探索度，避免过早收敛，同时在推理时生成更简洁的决策链，有助于降低在线服务延迟。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：当前 on-policy 训练（如 GRPO、OPD）依赖高质量轨迹，专家模型失败轨迹常被当作负样本丢弃。作者发现“反射优势”：对于困难问题，基于专家失败轨迹的反思推理比直接从头求解更容易成功，且专家失败轨迹（Golden Negative Trajectories, GNT）比模型自身或弱模型失败轨迹更有效，因为它保有更长的正确推理前缀和局部错误线索。

**方法关键点**：
- **反射接口设计**：定义直接推理（仅原始问题）和反射推理（问题 + 专家失败轨迹）两种提示模板，模型在反射模式下定位错误、修复推理并给出正确答案。
- **反射到直接策略过渡**：训练中逐渐减少反射模式的比例（如余弦衰减），最终全部使用直接推理，使模型内化纠错能力。
- **统一优化范式**：在 RLVR 中混合不同接口的 rollout 组，共用同一 verifier 和 GRPO 目标；在 OPD 中将失败轨迹作为教师侧特权上下文，学生侧始终直接推理，蒸馏纠错能力。
- **零额外开销**：GNT 离线生成，训练中仅增加前填充的 KV cache，且随反射比例衰减而趋于零。

**关键实验结果**：
- 在 Qwen2.5-Math-7B 上，ReflectRL 将 GRPO 的 ID 基准均值从 37.0 提升至 42.4，OOD 均值从 20.9 提升至 40.0。
- 在 DAPO、OPD 及多种模型尺寸（1.5B–8B）上均一致提升，训练更新速度快、响应长度更短（800+ → 420 tokens）、策略熵更高，有效避免熵崩塌。
- 消融实验证实 GNT 质量优于自生成或弱模型失败，且正确前缀与错误区间共同驱动反射增益。

**核心洞见**：*“反思一个高质量的错误轨迹，比从零开始直接解决问题更有效。”*
