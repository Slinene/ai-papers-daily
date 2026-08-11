---
title: 'Se-DPO: Self-Evolving Token Credit for Direct Preference Optimization'
title_zh: Se-DPO：自演化令牌信用用于直接偏好优化
authors:
- Wenxiao Zhao
- Shu Wang
- Ying Nian Wu
affiliations:
- University of California, Los Angeles
- Shanghai AI Laboratory
arxiv_id: '2608.09568'
url: https://arxiv.org/abs/2608.09568
pdf_url: https://arxiv.org/pdf/2608.09568
published: '2026-08-10'
collected: '2026-08-11'
category: Training
direction: 偏好对齐 · 令牌级自适应KL正则化
tags:
- DPO
- Token Credit
- KL Regularization
- Preference Optimization
- Implicit Reward
- Self-Evolving
one_liner: 通过在线从模型自身隐式奖励与参考熵中动态学习每令牌KL预算，解决DPO均匀加权的次优问题。
practical_value: '- **动态重要性加权思想可迁移至推荐场景**：类似给用户行为序列中不同位置 token 分配不同 KL 预算，推荐系统中可对用户历史行为的不同步数或不同特征维度分配不同的正则化强度或学习权重，避免平均主义，让关键决策点有更大优化自由度。

  - **在线重要性更新机制**：静态重要度在训练后期会严重失配，Se-DPO 定期从模型当前状态更新信用。这启发在在线学习排序模型或生成式推荐中，可引入周期性重估每个样本/特征重要性的机制，而不是训练前一次性固定。

  - **轻量校准网络的设计模式**：用一个小 MLP 融合强度（\(|\hat{r}_t|\)）与不确定性（\(H_{\text{ref}}\)）两个信号，输出信用。推荐系统可类似设计一个轻量子网络，结合预估的重要度与置信度来动态调节损失权重，几乎无额外成本。

  - **无需外部信号的在线信用提取**：只用模型自身隐式奖励和参考熵，无需教师模型或额外标注。在缺乏外部监督的生成式推荐或 Agent 任务中，可仿照此方法利用模型内部信号进行自适应样本加权。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
DPO 在聚合 token 级 log-prob 比率时采用均匀求和，默认所有 token 对偏好贡献相同，这与人类判断集中在少数关键 token 的事实不符。已有 token 级重要性方法通常从外部模型或固定快照获取信号，忽略了训练过程中重要性自身的演化。本文作者发现，DPO 的隐式奖励 \(\hat{r}_t\) 在训练历程中持续变化，早期与后期 top-\(|\hat{r}_t|\) token 的重叠率仅约 56%，静态分配会越来越陈旧。因此需要一种在线、自演化的 token 信用分配机制。

**方法关键点**  
- **问题形式化**：将每 token 的 KL 惩罚系数 \(\beta_t\) 替换为可变的，定义 token 信用 \(c_t = \beta / \beta_t\)，则偏好 logit 为 \(\sum_t c_t \hat{r}_t\)。
- **最优信用的方差最小化分析**：在独立噪声假设下，最小化偏好 logit 方差且保持信号强度的非负信用解为 \(c_t \propto |r_t^*|/\sigma_t^2\)，即信用正比于隐式奖励幅度、反比于估计噪声。噪声可通过参考模型熵 \(H_{\text{ref}}\) 代理。
- **自演化信用网络**：用轻量 MLP \(f_\phi(|\hat{r}_t|, H_{\text{ref}})\) 实时学习两个信号的映射，输出信用，并经序列内均值归一化以防止坍缩。训练含预热阶段，初期用均匀信用，之后随策略模型更新在线计算信用。
- **训练方式**：仅需标准 DPO 的前向计算额外增加 \(H_{\text{ref}}\) 和校准网络的前反向，开销约 6.85%，无需外部模型。

**关键结果**  
在 Llama-3-8B-Instruct、Llama-3.2-3B-Instruct、Gemma-2-2B-it 上，使用 PairRM 或 ArmoRM 标注的 UltraFeedback 数据。Se-DPO 在 AlpacaEval 2 和 Arena-Hard 上一致提升：Llama-3-8B (ArmoRM) 上 AE2 胜率达 50.6%（+9.8 点 vs. DPO），Arena-Hard 43.3%（+7.0 点），均超越 TGDPO 等外部模型方法。消融显示静态信用提升有限，双信号与在线更新缺一不可。

**一句话总结**：DPO 训练的隐式奖励一直在变，让信用跟着变比固定更重要。
