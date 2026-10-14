---
title: Unlocking Token Rewards via Training-Free Reward Attribution
title_zh: P2T：免训练将过程奖励分解为 Token 级奖励
authors:
- Sitong Wu
- Haoru Tan
- Bin Xia
- Xichen Zhang
- Jingyao Li
- Shaofeng Zhang
- Xiaojuan Qi
- Bei Yu
- Jiaya Jia
affiliations:
- Chinese University of Hong Kong
- Hong Kong University of Science and Technology
- University of Hong Kong
arxiv_id: '2610.18704'
url: https://arxiv.org/abs/2610.18704
pdf_url: https://arxiv.org/pdf/2610.18704
published: '2026-10-13'
collected: '2026-10-14'
category: Training
direction: RL 奖励归因 · Token-level reward
tags:
- Token-level Reward
- PRM
- GRPO
- Training-Free
- Reward Attribution
- RL
one_liner: 提出训练免费的 token 级奖励归因方法，用梯度一阶泰勒近似从 PRM 分解过程奖励，加速 RL 训练并提升推理表现
practical_value: '- 若业务中已有可微分的奖励模型（如用户满意度预测、转化模型、Critic、视觉质量模型），可直接用其梯度对生成序列做 token/action
  级归因，无需训练新 reward model；公式简单：token influence ≈ ∇_{e_i} R(E)·(e_i - e_null)，一个 backward
  pass 拿到全序列。

  - 将粗粒度奖励作为 baseline 再叠加归一化影响权重，而非直接用影响分数作为奖励，能显著降低梯度噪声；η 从 0.25 到 1.0 都稳，业务上无需精细调参。选择
  null token 用模型 padding token 比 EOS/zero embedding 更稳。

  - 训练 Agent/生成式推荐策略时，如果只有最终 outcome label（点击/转化/任务成功），可接入现成 PRM 或可微分 reward model，用
  P2T 方式分解到每个 action/token，加速 RL 收敛；论文显示达到同等效果可少 3-4 倍训练步数。

  - 注意 PRM 质量决定上限；若 PRM 在目标域不可靠，收益有限，应先验证 PRM 在该域判断准确，且 α 可从小增大。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

动机：RL 微调 LLM 推理依赖 outcome reward 导致稀疏反馈；step-level PRM 仍较粗，token 级奖励模型训练昂贵且伪标签噪声大，代理指标语义不对齐。需要一个低成本、有原则、鲁棒的方法提取 token 级监督。

方法关键点：
- 定义 token 归因分数 I_i = R(E) - R(E_{i←∅})：将第 i 个 token 替换为 null token 后 PRM 奖励的变化。
- 直接计算需 N 次 PRM 前向；用一阶泰勒展开 I_i ≈ ∇_{e_i} R(E)^T(e_i - e_∅)，一次前向+反向即可获得所有 token 的影响分数。
- 在 step 内对 |I_i| 归一化得到权重 w_i，重分配 process reward：R^{P2T}_i = Rs + η w_i Rs；Rs 作为 baseline，η 控制重分配强度，默认 0.5。
- 与 GRPO 集成：advantage = outcome advantage + α * P2T token reward，α 默认 1.0。
- null token 选 PRM 的 padding token 最佳。

关键结果：在多模态和文本模型共 40 个 model-benchmark 对中，GRPO+P2T 全部优于 GRPO，平均提升 +2.5% 到 +9.4%。Qwen2.5-Math-7B 在 AIME24 +11.5%；DeepSeek-R1-Distill-Qwen-1.5B 在 MinervaMath +14.2%；Qwen2.5-VL-7B 在 MathVista +4.9%。对比现有 token 级方法 PRIME/SPRO，平均高 +4.7% / +2.3%。更难的竞赛题收益更大；训练效率上达到同样 test 精度可少 3-4 倍步数。消融显示重分配本身贡献 +3.2%，仅加入 step-level reward 只 +2.6%。

最值得记住的一句话：用现成 PRM 的梯度做一阶泰勒分解，把 step-level reward 重新分配到 token，零训练成本获得高质量 token 信用分配。
