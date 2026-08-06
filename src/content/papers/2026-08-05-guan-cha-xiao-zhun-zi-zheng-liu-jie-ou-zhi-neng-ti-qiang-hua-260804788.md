---
title: Agentic Reinforcement Learning with Observation-Calibrated Self-Distillation
title_zh: 观察校准自蒸馏：解耦智能体强化重放信号的混杂因子
authors:
- Yi Yang
- Cong Qin
- Xiaodan Liu
- Chishui Chen
- Qing Dong
- Yan Zhang
- Cao Liu
- Zhao Yang
- Lu Pan
- Jiaye Lin
affiliations:
- Meituan LongCat Interaction
- Nanjing University
- Peking University
- McMaster University
- Fudan University
arxiv_id: '2608.04788'
url: https://arxiv.org/abs/2608.04788
pdf_url: https://arxiv.org/pdf/2608.04788
published: '2026-08-05'
collected: '2026-08-06'
category: Agent
direction: Agent 强化学习 · 令牌级信贷分配
tags:
- Agent
- RL
- Self-Distillation
- GRPO
- Token-level Credit Assignment
- Privileged Information
one_liner: 通过对比含/不含未来观察的结构化重放视图消除支架混杂，为GRPO提供校准的令牌级更新信号
practical_value: '- **特权重放信号的混杂控制**：在使用未来反馈或后见之明信息进行令牌级监督时，可构造“完整视图”与“消融视图”（如仅屏蔽关键未来信息，保持格式、动作支架一致），取两者分数差作为残差，剔除由重放格式、支架引入的偏好偏移，从而使特权信号更干净地归因于目标信息。

  - **选择性校准高不确定步骤**：按旧策略的序列平均负对数似然排序，只对每个轨迹中前20%高困惑度步骤施加令牌级精细化信号，既能提供有效指导，又避免对低价值步骤引入噪声，提升训练效率与稳定性（计算开销仅增1.4%）。

  - **保向调幅的集成方式**：在政策优化时保持原始轨迹级优势的方向不变，仅用校准信号按比例缩放更新强度（如 \(bA_{text{cal}} = bA \cdot
  (1+\beta \cdot \text{sgn}(bA) \cdot q)\)），易于嵌入现有GRPO/PPO框架，无需额外损失项或辅助目标。

  - **适用于多步交互型Agent**：该思路可直接迁移至对话推荐、搜索代理等多轮交互场景，利用后续用户反馈或环境状态构建结构化对比视图，实施步骤级信用分配，提升策略学习对关键行动环节的敏感度。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
LLM智能体通常通过GRPO等强化学习方法训练，但轨迹级稀疏奖励无法区分每个令牌的贡献。On-Policy Self-Distillation (OPSD) 通过特权重放为令牌提供细粒度监督，然而我们发现：当未来环境观察作为特权信息时，重放视图不仅引入观察，还引入额外的格式和未来动作支架，导致令牌分数变化混杂了观察信息与支架效应（图1、图2）。若不校准，直接使用该偏差会误导令牌级更新。

**方法关键点**  
- **结构匹配重放视图**：对每个选定交互步，构造 Full 视图（含实际未来观察+未来动作模式）和 Observation-Ablated 视图（仅将未来观察替换为“Observation: not provided”，其余完全一致），由此计算观察残差 \(e = \delta_F - \delta_A\)，消除共享支架影响。  
- **令牌校准信号**：将残差经 tanh 映射为 \(q \in [-1,1]\)，表示两个视图对同一令牌的支持差异。  
- **高不确定步骤选择**：按旧策略下每步的平均负对数似然排序，只对每条轨迹中前20%的高困惑度步骤施加校准，避免全量噪声。  
- **保向调幅集成GRPO**：将原始轨迹级优势 \(bA\) 调制为 \(bA \cdot (1 + \beta \cdot \text{sgn}(bA) \cdot q)\)，保持更新方向，调整令牌级强度，\(\beta=0.5\)。  
- 训练流程：同GRPO的 rollout–advantage计算–更新循环，仅增加一步双视图重评分与残差计算，开销极小（约1.4%）。

**关键结果**  
- 基准：ALFWorld（具身操作）、WebShop（产品搜索）、Search-QA（检索问答），模型规模 Qwen3-1.7B/4B/8B。  
- 对比方法：GRPO、OPSD、GRPO+OPSD、RLSD、SDAR。  
- ALFWorld Qwen3-4B 成功率：GRPO 70.6 → OCSD 82.8 (+12.2)；WebShop success 73.7；SearchQA Avg EM 47.5。  
- 消融证实移除观察消融教师、随机选步、全步校准、去掉方向对齐均导致性能下降。残差信号与局部环境反馈的AUROC达0.707，优于Full support的0.654。
