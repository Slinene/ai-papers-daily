---
title: 'SAKI: Maximal-Coupling-Routed Teacher Supervision for On-Policy Distillation'
title_zh: SAKI：基于最大耦合路由的在线策略蒸馏教师监督
authors:
- Miteto Wei
- Xiaohan Wang
- Zehao Chen
- Jiajun Chai
- Sichao Liu
- Li Wang
- Haoyuan Xu
- Zhaoyu Hu
- Wei Lin
- Guojun Yin
affiliations:
- Meituan
- KTH Royal Institute of Technology
arxiv_id: '2609.36601'
url: https://arxiv.org/abs/2609.36601
pdf_url: https://arxiv.org/pdf/2609.36601
published: '2026-09-28'
collected: '2026-09-30'
category: Training
direction: On-policy 蒸馏 · 最大耦合监督路由
tags:
- On-policy distillation
- Maximal coupling
- Teacher-guided rollout
- Speculative decoding
- Knowledge distillation
one_liner: 将教师引导 rollout 中的最大耦合修正事件作为 token 级监督路由信号，在信任域内自适应分配教师 Top-1 监督
practical_value: '- 在推荐/广告 LLM 的 on-policy 蒸馏或 RL 微调中，可直接复用 TRB 式几何桥接（q ∝ p^{1-β}
  T^β，约束 D_KL(q∥p)≤ε）替代纯 student/teacher rollout，减少弱模型早期状态偏移；ε 同时控制 rollout 偏差和 teacher
  监督频率，便于工程轻量调控。

  - 把最大耦合的 accept/correction 事件作为自适应课程信号，比按 TV/KL 标量加权更精准：只在需要干预的 token 上触发 teacher
  argmax 强监督，其余位置保留 RKL；这种「稀疏、冲突自适应」的路由可迁移到生成式出词、query 生成、Agent 多步 rollout 的 token
  级监督设计。

  - 在线教师推理成本高，可借鉴 speculative block verification：student 草稿 K tokens，teacher 批量验证，first
  rejection 后丢弃后续 KV 并从修正 token 恢复，既保持 exact-q 分布又获得 4.22× 吞吐提升；对需要在线 teacher 参与的策略学习/蒸馏系统有直接工程价值。

  - 若业务中有强生成模型作为 teacher、弱模型作为 student，可在高冲突前缀用 teacher Top-1 做硬标签拉齐，而不是始终用分布 KL；论文表明
  teacher-mode 比 teacher-sampled 在数学推理上 +0.62 Mean@8 / +1.56 Pass@8，模式寻求更适合冲突位置。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机

On-policy distillation 虽然通过让学生在自己的轨迹上训练来缓解训练/推理状态不匹配，但当学生明显弱于教师时，早期错误会累积，使教师被迫在自身策略下很少访问的坏前缀上提供监督，削弱知识迁移质量。此前 TRB 通过 trust-region 行为桥接改进了「在哪里采样」，但仍然保留统一的 reverse-KL 目标，没有区分不同位置是否适合相同监督。SAKI 关注的核心是：当 guided rollout 不得不覆盖学生提议时，该位置应该获得与普通接受位置不同的监督。

## 方法关键点

- **信任域几何桥接**：在每步构造 q ∝ p^{1-β} T^β，选择满足 D_KL(q∥p)≤ε 的最大 β，使 rollout 分布向教师靠拢但不偏离学生过远。
- **最大耦合采样**：学生先提出 z∼p，以 min(1, q(z)/p(z)) 接受；否则从残差 [q-p]+ 采样修正 token。修正事件概率正好是 TV(p,q)，且 ≤ sqrt(ε/2)，因此 ε 同时约束轨迹偏差和干预频率。
- **耦合路由监督**：接受位置保留 sampled-token RKL 损失；修正位置切换为对教师最高概率 token 的 NLL 损失。两者解耦：修正 token 控制下一个前缀，教师 Top-1 控制局部参数更新。该路由完全内生，无需额外阈值或 token 选择启发。
- **Engine-resident exact-q rollout**：用 speculative block verification 实现：学生草稿 K=8 tokens，教师批量验证，遇首次拒绝后立即采样残差修正、丢弃后续 KV 并恢复，保证与顺序采样完全相同的 q 分布和耦合语义。

## 关键结果

在 Qwen3-4B-Base-GRPO 教师蒸馏 0.6B/1.7B 学生、DAPO-Math-17K 训练、七个数学推理 benchmark 上评估。相对 TRB：1.7B 学生 Mean@8 从 27.9 到 29.0，Pass@8 从 44.6 到 47.5；0.6B 学生 Mean@8 从 17.2 到 18.4，Pass@8 从 33.6 到 35.6。Placement control 显示：修正位置路由优于同等预算的随机放置和 TV 加权放置；固定前缀分析表明修正触发监督在高冲突位置带来更大且持续的 teacher alignment。Engine-resident 实现较外部循环 exact-q 的 matched-workload 吞吐提升 4.22×。

## 最值得记住的一句话

修正事件不是外部启发，而是最大耦合下最小干预概率 TV(p,q) 的产物，同一信任域半径同时约束 rollout 偏差与稀疏监督频率。
