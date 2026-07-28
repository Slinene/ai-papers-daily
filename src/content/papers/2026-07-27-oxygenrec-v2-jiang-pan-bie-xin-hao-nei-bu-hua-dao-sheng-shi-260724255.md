---
title: 'OxygenREC-v2: Internalizing Discrimination into Generative Recommendation'
title_zh: OxygenREC-v2：将判别信号内部化到生成式推荐
authors:
- Guo Tang
- Hanye Wu
- Changjiang Han
- Qingyang Li
- Ming Zhang
- Xiangyu Qian
- Yanchen Qiao
- Huanjie Wang
- Zhi Ma
- Zhen Li
affiliations:
- JD.COM, Beijing, China
arxiv_id: '2607.24255'
url: https://arxiv.org/abs/2607.24255
pdf_url: https://arxiv.org/pdf/2607.24255
published: '2026-07-27'
collected: '2026-07-28'
category: GenRec
direction: 生成式推荐 · 行为内部化
tags:
- Generative Recommendation
- Behavior-Conditioned Generation
- Verifiable Reward
- Entropy-Aware Self-Distillation
- MoE Deployment
one_liner: 通过行为指令条件生成与熵感知特权自蒸馏，将点击/加购/下单信号直接注入生成式推荐，无需外部奖励模型
practical_value: '- **行为感知生成可直接复用**：在解码器前缀插入行为指令（如“点击”、“加购”、“下单”），让模型在生成 SEMANTIC
  ID 时根据业务目标切换候选分布，无需为不同场景维护多个模型。

  - **用可验证奖励替代人工奖励模型**：以生成结果与真实交互 SID 的 token 级匹配率（几何加权）作为 RL 奖励，避免训练独立排序模型带来的分布外打分和奖励
  hack 问题，大幅降低离线评估与维护成本。

  - **特权未来蒸馏可融入训练流程**：在训练时利用用户未来行为（点击及以上）作为教师前缀，提供更密集的偏好信号；通过熵门控只对低熵位置进行蒸馏，避免全位置蒸馏引入噪声，超参（蒸馏覆盖率
  20%）可直接借鉴。

  - **行为加权预训练即可带来明显提升**：即使不使用后训练，在预训练时丢弃仅曝光样本，按行为价值加权损失，已能将 HR@512 提升 0.58pp，可作为轻量级基线。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
生成式推荐（Generative Recommendation, GR）通过自回归解码 Semantic ID 统一了检索与排序，但现有工业系统依赖单独训练的排序模型作为事后奖励信号，引发去分布打分不可靠和奖励失配等问题。如何将点击/加购/下单等行为信号直接内部化到 GR 的训练目标中，是一个关键挑战。

**方法：IDGR（Internalizing Discrimination into Generative Recommendation）**
- **行为感知指令**：在解码器前缀添加行为指令 \(I_b\)（点击/加购/下单），使生成从第一步起就受目标行为条件，不同场景注入不同 \(I_b\) 即可切换候选分布。
- **行为感知预训练**：从用户日志中提取多行为目标，丢弃仅曝光样本，并按行为价值加权 NTP 损失，让指令与监督信号对齐。
- **后训练框架 EA-TOSD**：
  1. **可验证轨迹优化**：采样多条生成序列，以与真实 SID 的 token 级匹配率（几何加权）为奖励，选取最优轨迹进行强化学习，完全摆脱外部奖励模型。
  2. **特权教师自蒸馏**：教师共享学生骨干，但前缀加入用户未来交互行为（点击及以上），提供更精准的预测分布。
  3. **熵感知路由**：只在教师预测熵低于阈值的位置执行自蒸馏（反向 KL），高熵位置改用前向 KL 保持多样性，避免特权偏见。

**关键结果**
- 离线：在京东工业数据集上，HR@1 从 4.62% 升至 5.64%，HR@512 从 43.24% 升至 44.14%，全面超越外部奖励基线；对稀疏高价值的下单行为提升最大。
- 在线：3B-A1B MoE 部署于六个生产场景，UCTCVR 提升 1.6%-4.4%，GMV 提升 2.8%-6.8%。

**核心洞察**：将行为信号放在输入端条件生成，而非在输出端评分，是让 GR 真正实现行为感知的关键。
