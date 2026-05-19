---
title: General Preference Reinforcement Learning
title_zh: 通用偏好强化学习
authors:
- Muhammad Umer
- Muhammad Ahmed Mohsin
- Ahsan Bilal
- Arslan Chaudhry
- Andreas Haupt
- Sanmi Koyejo
- Emily Fox
- John M. Cioffi
affiliations:
- Stanford University
- The University of Oklahoma
- Independent Researcher
arxiv_id: '2605.18721'
url: https://arxiv.org/abs/2605.18721
pdf_url: https://arxiv.org/pdf/2605.18721
published: '2026-05-18'
collected: '2026-05-19'
category: Training
direction: 多维偏好在线RL · 抗reward hacking
tags:
- Online RL
- Multi-dimensional Preference
- GRPO
- Reward Hacking
- LLM Alignment
- General Preference Model
one_liner: 用多维度偏好嵌入与漂移控制实现在线RL的开放任务对齐，无需标量奖励
practical_value: '- 在推荐系统的多目标优化（如点击率、转化率、多样性）中，可借鉴GPM的k个子空间独立建模不同指标，采用**per-dimension组相对优势归一化**，防止单一指标主导梯度，避免信息茧房或过度商业化。

  - **漂移监控器**可复用到多任务RL：跟踪各目标方差份额，当某维度过度集中时自动降低其权重并收紧策略约束（如KL惩罚），实现动态平衡，无需外部验证信号。

  - 向量化的奖励结构能**天然抑制单轴投机**：只有在所有维度共同改善时优势才增加，这一性质可直接应用于拒止推荐策略的“作弊”行为。

  - 工程上，GPRL直接替换现有GRPO管线，仅需冻结一个偏好模型提供多维分数，计算开销与标量RM相当，适合大规模在线学习场景。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：LLM后训练中，在线RL擅长数学/代码等可验证任务，而开放域对齐只能用标量奖励模型，极易**奖励攻击**——政策会过度优化奖励最敏感的单一维度（如长度），损害其他品质。问题根源在于标量奖励是多维人类偏好的不完整代理。

**方法关键点**：
- **奖励源**：使用General Preference Model (GPM)，将每个响应嵌入k个二维子空间，通过反对称双线性形式建模多维度偏好（可表达非循环偏好）。
- **多维优势估计**：为每个子空间独立计算组内相对优势（均值-标准差归一化），确保各维度在统一的单位方差尺度上贡献，避免量级差异造成主导。然后用GPM的特征值加权聚合。
- **闭环漂移控制**：监控维度优势的方差分布α(t)与初始分布的KL散度D(t)；当D(t)超过阈值，按式(9)重调维度权重并收紧KL系数，迫使政策重新平衡各维度。
- **与GRPO一致的目标**：直接将多维优势代入GRPO的裁剪替代目标，k=1时退化为标量GRPO，可无缝接入现有在线RL框架。

**关键结果**：基于Llama-3-8B-Instruct，用Skywork-Reward训练GPM，在UltraFeedback上在线采样。
- AlpacaEval 2.0长度控制胜率**56.51%**，比GRPO+BT高14.59点，同时平均长度最短(1600 tokens)。
- Arena-Hard v2、MT-Bench、WildBench上也全面超越DPO、SimPO、SPPO、GPO及GRPO+BT。
- 消融：多维归一化比全局归一化高约4点；漂移控制器在长训练中避免退化，第5轮差距达8-11点。

**核心洞见**：多维归一化使任何单轴的增量被其余维度约束，优势梯度天然拒绝单轴投机，这为开放任务RL提供了一条不依赖外部评估信号的抗攻击路径。
