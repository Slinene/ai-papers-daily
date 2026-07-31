---
title: 'Flux-OPD: On-Policy Distillation with Evolving Contexts'
title_zh: Flux-OPD：使用进化上下文的策略蒸馏
authors:
- Yuran Wang
- Zekun Wang
- Bohan Zeng
- Ruixu Zhang
- Wenxuan Liu
- Liu Yang
- Yifan Dai
- Yang Shi
- Bozhou Li
- Chengzhuo Tong
affiliations:
- Peking University
- Kling Team
- Tsinghua University
- Shanghai Jiao Tong University
- Zhongguancun Academy
arxiv_id: '2607.28022'
url: https://arxiv.org/abs/2607.28022
pdf_url: https://arxiv.org/pdf/2607.28022
published: '2026-07-29'
collected: '2026-07-31'
category: Training
direction: 进化上下文下的策略蒸馏方法
tags:
- On-Policy Distillation
- Evolving Contexts
- Reverse KL Decomposition
- Contextual Correction
- Open-Ended Tasks
one_liner: 通过反向KL分解揭示蒸馏目标为几何平均，用进化上下文进行校正和加权，解决开放域任务缺乏可验证奖励的问题
practical_value: '- **动态上下文的思路可迁移到实时偏好学习**：在推荐/Agent场景，用户实时行为轨迹类似论文中的进化上下文，可以周期性地从学生最新生成结果中提取偏好信号，注入蒸馏目标，持续对齐用户兴趣变化。

  - **几何平均作为多教师融合目标更稳健**：当多个教师分布（如不同模态、不同专家）存在冲突时，取几何平均而非算术平均能强化高一致性下的监督，减弱分歧影响，可用于多目标蒸馏或ensemble融合。

  - **冲突项作为自适应加权信号**：方法中利用冲突项（−log Z）动态调节上下文影响力，类似于多任务学习中根据梯度冲突调整损失权重；电商推荐中多目标（如点击率与转化率）冲突时，可借鉴该机制去无痛地平衡。

  - **校正锚点策略可稳定生成式推荐训练**：将上下文差异作为修正信号叠加在稳定锚点（如常规教师分布）上，避免蒸馏目标剧烈震荡，适合需要保持生成稳定性的场景（如商品描述生成、广告文案改写）。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
开放域任务（如视频生成prompt优化、医疗问答）缺乏可验证奖励，难以直接用RL训练。上下文（如经验、规则）虽能传达任务偏好，但固定上下文一旦被学生吸收，后续便无额外监督，需要随学生能力进化。然而，在训练中直接使用进化上下文会导致蒸馏目标不稳定，且多上下文间冲突会恶化监督信号。

**方法关键点**
1. **反向KL分解**：将on-policy context distillation (OPCD) 的目标分解为：
   - 蒸馏项：学生与多个上下文条件教师分布的**归一化几何平均**之间的KL散度。
   - 冲突项（−log Z）：衡量教师分布间的不一致程度，该值越大表示冲突越大。
2. **迭代训练**：将单次训练分割为多轮迭代，每轮从当前学生生成的轨迹中提取新上下文（由教师总结经验），用于下一轮蒸馏，实现上下文随学生进化。
3. **上下文校正（Contextual Correction）**：
   - 计算上下文差异信号：Δ = log q_geo − log q_0，其中q_geo是多个上下文条件教师的几何平均，q_0是无上下文的教师。
   - 将蒸馏目标构建为 q_target = softmax(log q_0 + λ Δ)，λ控制修正强度。q_0作为稳定锚点，仅注入Δ带来的偏好信息，避免直接使用q_geo带来的剧烈震荡。
4. **上下文加权（Contextual Weighting）**：
   - 利用冲突项δ = −log Z 作为指标，通过 λ = α clip(1 - δ/τ, λ_min, λ_max) 动态调整修正强度，当教师分布一致时加强修正，冲突时减弱修正。

**关键实验**
- 数据集与任务：视频生成prompt优化（VPO数据集，评估VBench/Video-Bench）、医疗问答（RaR-Medicine+HealthBench）。
- 对比基线：vanilla OPD、固定上下文的OPCD、交替更新上下文的OEL。
- 主要结果：
  - 在Qwen3-VL-Instruct 4B学生/8B教师设置下，VBench总分80.18（vs OPD 79.28，OPCD 79.02，OEL 76.86）。
  - 在Qwen3 1.7B学生/8B教师的医疗问答上，HealthBench得分20.61（vs OPD 19.63，OPCD 19.53，OEL 19.66）。
  - 训练稳定性：Flux-OPD损失平稳下降，OEL出现损失尖峰；在IF-Eval上的指令遵循能力也优于OPD。

**核心洞察**
反向KL下的蒸馏目标天然是上下文条件教师分布的几何平均，利用这一性质可分解出冲突项，进而设计稳定的进化上下文蒸馏范式。
