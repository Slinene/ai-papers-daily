---
title: Reinforcement Learning from Rich Feedback with Distributional DAgger
title_zh: 基于分布式DAgger的丰富反馈强化学习方法
authors:
- Rishabh Agrawal
- Jacob Fein-Ashley
- Paria Rashidinejad
affiliations:
- University of Southern California
arxiv_id: '2606.05152'
url: https://arxiv.org/abs/2606.05152
pdf_url: https://arxiv.org/pdf/2606.05152
published: '2026-06-03'
collected: '2026-06-04'
category: Training
direction: LLM强化训练 · 自蒸馏信用分配
tags:
- Reinforcement Learning
- Self-Distillation
- Forward Cross-Entropy
- Credit Assignment
- Imitation Learning
- Monotonic Improvement
one_liner: 提出DistIL，用前向交叉熵代替反向KL，实现单调策略改进与未来感知信用分配，在科学推理、编码和数学难题上超越现有自蒸馏方法。
practical_value: '- **用前向交叉熵替代反向KL做策略蒸馏**：在电商Agent或推荐策略自蒸馏中，反向KL可能因对数比加权而抑制某些有效行为，改用前向交叉熵能直接向教师方向移动，获得单调改进保证，训练更稳定。

  - **未来感知的序列级信用分配**：拒绝局部token-wise梯度近似，保留对未来状态的梯度传播，可让Agent的早期决策（如对话策略中的首轮动作）得到准确的延迟奖励信号，避免收敛到次优策略，适用于多轮对话或推荐序列优化。

  - **黑盒教师兼容的样本估计**：DistIL只需从教师采样即可估计梯度，无需教师概率，方便利用外部黑盒模型、人工专家或带反馈的推理痕迹，在电商场景中可直接用用户行为日志或工具反馈来蒸馏策略，降低对教师内部结构的依赖。

  - **奖励对齐的下界优化解释**：前向交叉熵目标可被视为最大化教师加权的成功对数似然下界，直接提升Pass@N，这一视角可用于推荐系统的列表级评估优化，比如在生成式推荐中提升Top-K准确率。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：当前主流RLVR（可验证奖励的强化学习）只给最终答案一个二元信号，导致整个响应中每个token获得相同权重，信用分配极弱，且无法利用代码执行日志、专家修正等丰富反馈。现有自蒸馏方法（如SDPO用反向KL、OPSD用JS散度）虽然试图将稀疏奖励转化为token级指导，但存在两个根本缺陷：1) 最小化f-散度不能保证策略单调改进，即使教师更好，更新仍可能增加坏动作的概率；2) 局部token-wise梯度近似忽略了早期token对未来教师-学生分歧的影响，会收敛到严格次优策略。

**方法**：提出DistIL，一种分布式DAgger模仿学习变体。核心是优化前向交叉熵（H×）损失，在学生访问的状态上匹配教师分布，并采用完整的序列级梯度，包含教师加权局部模仿项和未来信用传播项。该设计允许仅从教师采样来估计梯度，支持黑盒教师。算法在PPO式信任域更新框架下实现，教师参数通过EMA更新。

**关键结果**：在科学推理（SciKnowEval L3）、编码（LiveCodeBench）和极难数学题（AIME24/25等）三个场景下，DistIL一致超越SDPO、OPSD、GRPO等基线。例如，在Qwen3-8B上，科学推理平均@16提升3.1点（5h）；编码任务中，Accuracy/Avg@16达到0.656（SDPO 0.643）；在GRPO完全无法提升的难题集上，DistIL比SDPO高3.8点（AIME25 Avg@16）。消融实验验证了未来信用分配和Top-100教师token采样的有效性。理论证明前向交叉熵满足单调改进、次线性悔恨界，并最大化教师加权的成功概率下界，从而提升Pass@N。
