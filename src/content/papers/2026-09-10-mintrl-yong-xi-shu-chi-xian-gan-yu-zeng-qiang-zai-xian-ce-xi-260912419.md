---
title: 'MInTRL: Off-policy Intervention can boost On-policy RL'
title_zh: MInTRL：用稀疏离线干预增强在线策略强化学习
authors:
- Mingyu Chen
- Yefan Tao
- Gerald Friedland
- Xuezhou Zhang
- Chris Kong
affiliations:
- Amazon Web Services
- Boston University
arxiv_id: '2609.12419'
url: https://arxiv.org/abs/2609.12419
pdf_url: https://arxiv.org/pdf/2609.12419
published: '2026-09-10'
collected: '2026-09-16'
category: Training
direction: LLM 强化学习 · 半在线纠错
tags:
- MInTRL
- RLVR
- off-policy intervention
- advantage regression
- LLM reasoning
- GRPO
one_liner: 提出 MInTRL：在 on-policy rollout 中由 judge 做稀疏局部纠错，并用 advantage-regression
  目标免去 importance sampling
practical_value: '- 在线 RL/Agent 训练中，不要整段用 teacher 轨迹做 SFT 或 off-policy；可在 rollout
  里让 judge 按 chunk 定位 first error，只替换错误后缀，随后控制权还给当前策略。工程上按 `\n\n` 或 code fence 切 step，限制
  judge reviews 次数和 continuation 长度，把干预 token 占比控制在约 2–4%，收益最稳。

  - 对混合来源轨迹（模型自生成 + 专家修正），不要用 GRPO/PPO 加 importance ratio，改用 sequence-level advantage
  regression：`A(x,y)=r(x,y)-V_ctrl(x)`，回归 `log πθ/πt` 到 `A/β`；value baseline 只从纯 on-policy
  control rollouts 估计，能显著降低修正 token 带来的方差。

  - 干预 token 的 anchor 可以设为常数 `κ`，不必依赖 teacher log prob，避免低概率专家 token 被当前策略过度约束；当 base
  policy 已经较强时，再用原 `πt` anchor 更稳定。

  - 只在训练早期开启 intervention，后期关闭切换为纯 on-policy RL；没有更强教师模型时，可以用 privileged context 让同一模型做
  self-judge，对电商/Agent 业务更友好。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
RLVR 通常坚持 on-policy，但有限采样下模型很难发现自己能力之外的推理路径；完全 off-policy 的蒸馏又带来明显分布偏移。核心问题是如何在不牺牲可学习性的前提下扩展探索。

**方法关键点**
- **半在线 rollout**：生成时当前策略 `πt` 默认控制，由 judge–intervention policy `πJI` 周期性 review；发现错误时截断至最早错误 step，生成短 correction，随后立即把控制权还给 `πt`。
- **免重要性采样的训练目标**：采用 sequence-level advantage regression，`L(θ)=E[(β log πθ/πt − A*)²]`，其中 `A*=r−V_ctrl`；混合来源轨迹可直接作为回归样本，无需 behavior-policy importance ratio。
- **实现细节**：value baseline 仅从纯 on-policy control rollouts 估计；对干预 token 用常数 anchor `κ` 或原 `πt` 概率做松弛；只在训练前期启用 intervention，后期回到纯 on-policy RL。

**关键实验与结果**
在 Qwen3-1.7B / 4B 上做数学和代码 RLVR，对比 GRPO、OPD、MENTOR、SFT+GRPO。1.7B 数学平均：MInTRL-Const 35.45，最强基线 OPD 21.84；代码平均 61.95，最强基线 OPD 47.83。4B 数学 55.73 vs GRPO 52.71，代码 72.63 vs GRPO 65.83。消融显示干预强度与收益呈倒 U 型，约 2–4% 的 intervention token 占比最佳；self-judge 和高低不同 judge 模型下仍有效。

**最值得记住的一句话**：训练带 verifiable reward 的 LLM/Agent 时，不追求完全 off-policy 或纯 on-policy，少量（约 2–4%）局部专家纠错 + 回归式 RL 目标最划算。
