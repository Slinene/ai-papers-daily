---
title: 'The Teacher Is a Direction, Not a Destination: Extrapolating RL-Induced Representation
  Residuals in On-Policy Distillation'
title_zh: 教师是方向，而非终点：在策略蒸馏中沿RL诱导表示残差外推
authors:
- Hao Li
- MeiJia Chen
- Weijie Ren
- Donghan Li
- Zijun Tian
- Jingchun Huang
- Naibo Wang
affiliations:
- University of Science and Technology of China
- Rutgers University
- Zhejiang University
- Independent Researcher
arxiv_id: '2609.36484'
url: https://arxiv.org/abs/2609.36484
pdf_url: https://arxiv.org/pdf/2609.36484
published: '2026-09-28'
collected: '2026-10-01'
category: Training
direction: LLM 蒸馏与RL训练优化
tags:
- on-policy distillation
- representation residual
- RL teacher
- hidden-state distillation
- extrapolation
one_liner: 提出 RIDE，在隐藏状态空间外推教师相对其RL前基座残差，稳定超越教师并优于输出空间外推
practical_value: '- 同初始化蒸馏场景下，把 RL 教师相对基座模型的隐藏状态差作为方向而非仅作为终点，可在策略蒸馏中稳定超越教师；推荐/Agent
  模型中若需合并多个领域专家或把 RL 结果蒸馏回 base，可复现类似残差外推目标。

  - 输出空间 log-ratio 外推对采样噪声按 (λ−1)² 放大，教师与 base 差距小时尤其不稳定；改用逐层隐藏状态回归可消除条件方差，更适合生成式推荐或对话式
  Agent 的稳定训练。

  - 语言模型 head 各向异性会削弱隐藏状态残差，弱方向承载大部分能量但输出监督只接收小部分；在蒸馏或轻量适配时，对中间层表示做直接回归能保留更多 RL 带来的行为变化。

  - λ 是一个轻量外推系数，λ=1 退化为普通 OPRD；实际业务可从小幅 λ>1 开始，既继续 RL 方向又避免格式/长度崩溃。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
RL 训练后的教师模型不仅在输出分布上给出目标，其隐藏状态相对 RL 前基座的位移构成一个可继续的方向。但在输出空间外推该方向时，LM head 的各向异性会严重衰减表示残差：最弱的 512 个 head 方向承载 79.8% 的残差能量，却只保留 30.0% 的 logit 能量；同时基于采样 token 的 log-ratio 外推会按 (λ−1)² 放大噪声，导致训练不稳定，尤其当教师距离基座较近时学生甚至会退化。

### 方法关键点
- 设定同初始化：教师 π_T = RL(π_B)，学生从 π_B 初始化，三者共享表示空间；在每条学生生成的 rollout 上，对同一前缀计算冻结教师与基座在每层、每位置的隐藏状态差 Δ = h_T − h_B，作为 RL 诱导残差。
- RIDE 将蒸馏目标从教师状态外推至 h* = h_T + (λ−1)Δ = λh_T + (1−λ)h_B，并用逐层均方误差回归学生隐藏状态；λ=1 时完全退化为 OPRD。
- 该回归在固定 rollout 下等价于最大化方向奖励 r(h)=⟨h−h_T, Δ⟩ 并加二次惩罚 −1/2‖h−h_T‖²，解释为表示空间中的 KL 约束 RL 外推；梯度确定，无采样 token 噪声。
- 监督所有 L 层和最后 k=2,000 个响应位置，损失按 λ^{-2} 缩放。

### 关键实验
在四个 base/RL-teacher 对上评估：R1-Distill-1.5B→JustRL-1.5B、Qwen3-4B→Just-Qwen3-4B、Llama-3.2-3B→Just-Llama-3.2-3B、Phi-4-mini→Just-Phi-4-mini；使用 DAPO-Math-17K 提示，AIME24/AIME25/AIMO 的 Avg@16。RIDE 是唯一在四对上均值都超过 RL 教师的方法，相对教师分别 +1.08/+0.48/+0.32/+0.34；在 R1-Distill 对上 RIDE 为 56.38，超过 OPRD 54.50 和 teacher 55.30，而 ExOPD 仅 49.87。λ sweep 显示 RIDE 在 λ=1.25 最优且 λ∈[1.15,1.35] 均优于 OPRD；ExOPD 则在 λ>1 后崩溃，验证了噪声放大分析。方向消融中随机、反向、错配起点、错配轨迹的控制均比 RIDE 低约 1 分，证明增益来自 RL 诱导残差方向本身。

最值得记住的一句话：**表示空间中的残差方向比输出空间中的 log-ratio 更完整、更稳定，让蒸馏学生可以沿着教师走过的 RL 轨迹继续前进，而不是停在教师终点。**
