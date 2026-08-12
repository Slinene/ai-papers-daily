---
title: 'SR-OPSD: Self-Referenced On-Policy Self-Distillation'
title_zh: 自我参照在线策略自蒸馏：将 Rényi 散度引入 OPSD 稳定训练
authors:
- Zhuo Sun
- Entong Li
- Yanlong Zhao
- Xiaoyuan Cheng
- Wenxuan Yuan
- Kaiyu Li
- Che Liu
- Huihang Liu
- Harrison Bo Hua Zhu
- Li Zeng
affiliations:
- Imperial College London
- Peking University
- University of Science and Technology of China
- Shanghai University of Finance and Economics
- Nanyang Technological University
arxiv_id: '2608.09745'
url: https://arxiv.org/abs/2608.09745
pdf_url: https://arxiv.org/pdf/2608.09745
published: '2026-08-10'
collected: '2026-08-12'
category: Training
direction: On-policy self-distillation · Rényi divergence
tags:
- On-policy self-distillation
- Rényi divergence
- Self-referenced target
- LLM post-training
- credit assignment
- policy optimization
one_liner: 通过参考锚定与 Rényi 投影解耦在线自蒸馏中的目标位置与投影几何，显著提升训练稳定性与多任务性能
practical_value: '- **在 LLM 推理训练（如 GRPO/SDPO）中替代 KL 散度**：当使用环境反馈或验证信号进行策略优化时，将目标构造为自我教师与参考策略的几何插值，并用
  Rényi 散度（可调阶数 ρ）替换前向/反向 KL，能稳定策略熵、避免模式塌缩，尤其适用于需要输出多样性的推荐文案生成、搜索词改写等任务。

  - **参控对反馈信息的依赖程度**：超参数 α 控制目标中自我教师（基于反馈）与参考策略的比例，业务中可据此调节模型对用户点击/转化信号的信任度，避免在噪声反馈下过拟合。

  - **冻结初始策略作为参考锚点**：将预训练初始策略冻结作为参考，保证训练后模型不严重偏离原有能力，适合在线上推理链路中逐步部署，降低上线风险。

  - **Rényi 投影的密度比温度控制**：ρ 参数可看作对教师-学生概率比的幂次调制，能在训练初期压制极高或极低比值的梯度影响，相当于一种自适应梯度裁剪，有助于在不稳定反馈环境下稳定训练。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

## 动机
在线策略自蒸馏（OPSD）通过将反馈信号转化为密集 token 级监督，辅助强化学习中的稀疏奖励，但现有方法多采用前向或反向 KL 散度，且自我教师与参考策略共同进化，导致目标分布与投影几何高度耦合：前向 KL 偏向模式覆盖但易受动作采样偏差影响，反向 KL 偏向模式寻求且可能强化学生偏见，造成训练不稳定或分布过度集中。

## 方法关键点
- **参考锚定目标构造**：将自我教师策略（持有额外上下文，如正确解答、反馈）与冻结的参考策略（初始策略）进行几何插值：\(\pi^\star_\alpha \propto (\pi_{\bar{\theta}})^\alpha (\pi_{\text{ref}})^{1-\alpha}\)，通过 α 控制对反馈信号的依赖程度。
- **Rényi 投影解耦目标与投影**：采用 Rényi 散度（阶数 ρ）将学生向上述目标投影，ρ 控制密度比的幂次调制，影响投影几何与对 token 概率比值的敏感度；ρ→1 还原为相应 KL 散度，0<ρ<1 可缓和极端比值。
- **梯度形式**：导出 logit 梯度 \(\partial D_\rho / \partial z_\theta(a) = \pi_\theta(a) - \tilde{\pi}_{\alpha,\rho,\theta}(a)\)，其中 \(\tilde{\pi}_{\alpha,\rho,\theta}\) 是按 \((\pi^\star_\alpha/\pi_\theta)^\rho\) 修正的分布，分离了自适应目标的位置（α）与投影方式（ρ）。
- **冻结上下文算法**：在每次 rollout 后固定上下文和目标，使用对应阶数 Rényi 散度做单步优化，教师采用 EMA 更新。

## 关键实验
- **科学问答（SciKnowEval）**：在化学、物理等五个子任务上，Qwen3-8B 和 OLMo-3-7B 初始化下，SR-OPSD 15 小时 Avg@16 领先于 SDPO 和 GRPO，五领域平均达 75.2（Qwen3-8B）和 68.9（OLMo-3），且训练中策略熵稳定，未出现 SDPO 的长程性能退化。
- **数学推理**：在 AIME 2024/2025、HMMT 2025 等五个困难 benchmark 上，使用 Qwen3-4B-Instruct，SR-OPSD 均优于 GRPO 和两种 KL 自蒸馏基线：平均 Avg@64 达 56.2（vs GRPO 55.0），Pass@64 达 78.4（vs GRPO 75.2）；相比前向 KL 的 OPSD 提升 9.4 Avg 点。
- **代码生成缩放**：在 LiveCodeBench v6 上，跨 Qwen3 0.6B–8B 四个量级，SR-OPSD 在 1.7B/4B/8B 上均取得最佳 pass-all 分数（32.0/46.2/50.1），较 GRPO 提升 2.7–8.9 个百分点。
- **消融**：仅参考锚定不配合 Rényi 投影时，JSD 或前向 KL 性能反降；引入 Rényi 后（ρ=0.95 + α=0.9）物理 Avg@16 达到 81.1，优于所有非 Rényi 变体。

## 核心启示
**自我参照目标与 Rényi 投影的协同是关键**：单纯替换目标或散度均不足，两者解耦后能分别控制“信任反馈多少”和“如何响应反馈”，为训练更稳定、更鲁棒的 on-policy 自蒸馏提供了新范式。
