---
title: 'Breaking Entropy Bounds: Accelerating RL Training via MTP with Rejection Sampling'
title_zh: 打破熵的限制：多token预测与拒绝采样加速强化学习训练
authors:
- Yucheng Li
- Huiqiang Jiang
- Yang Xu
- Jianxin Yang
- Yi Zhang
- Yizhong Cao
- Yuhao Shen
- Fan Zhou
- Rui Men
- Jianwei Zhang
affiliations:
- Qwen Team, Alibaba Inc.
arxiv_id: '2606.12370'
url: https://arxiv.org/abs/2606.12370
pdf_url: https://arxiv.org/pdf/2606.12370
published: '2026-06-09'
collected: '2026-06-11'
category: Training
direction: LLM强化学习训练加速 · 多token预测
tags:
- Multi-Token Prediction
- Rejection Sampling
- TV Loss
- RL Training
- Speculative Decoding
one_liner: 揭示RL阶段熵升高与MTP接受率的负线性关系，通过拒绝采样与TV损失将接受率提至95%，实现1.8倍训练加速
practical_value: '- **拒绝采样替代贪婪采样**：在电商对话式推荐或Agent策略生成中，当使用MTP（或多token生成）加速推理时，若模型因在线学习（如RL更新）导致输出分布偏移，应使用概率拒绝采样而非贪婪接受，以保持高接受率和加速比。

  - **端到端优化接受率指标**：推荐或生成模型中若采用多步草稿验证机制（如Sequential Recommendation中的beam search加速），可设计类似TV
  loss的目标函数，直接最大化多步联合接受率，替代中间步骤的KL或交叉熵损失，可提升整体推理吞吐。

  - **预训练加速模块避免在线开销**：在RL训练的rollout阶段，MTP模块可在RL开始前用端到端损失充分训练并冻结，避免在线更新引入的计算代价和分布波动，这对需要稳定服务的推荐Agent尤其有用。

  - **熵监控指导加速策略**：实际部署中，可监测生成熵值动态调整MTP步长或是否启用加速，当熵上升时自动切换到拒绝采样或回退到逐token生成，平衡效率与质量。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM的RL训练中，rollout生成是主要瓶颈。多token预测（MTP）可通过投机解码加速，但在RL过程中模型分布变化导致MTP接受率急剧下降，加速效果有限。

**方法关键点**：
1. **理论发现**：RL阶段熵的增加与MTP接受长度呈显著负线性关系，即熵越高，多步预测的接受度越低。
2. **概率拒绝采样**：相比贪婪采样，概率采样（按draft模型概率接受）能显著缓解熵带来的接受率退化。
3. **端到端TV损失**：现有MTP训练目标（交叉熵或KL）未直接优化多步联合接受率，提出总变分（TV）损失，直接最大化多步拒绝采样的接受率，在数学推理、代码和智能体任务上将接受率提升约10%，最高达95%，带来额外25%的吞吐增益。
4. **离线MTP训练策略**：RL前用e2e TV损失训练MTP模块并固定，整个RL过程中接受率和加速比保持稳定，无需昂贵的在线更新。

**关键结果**：在Qwen3.5/3.6/3.7模型的异步RL训练中，Bebop方法实现最高1.8倍的端到端加速。
