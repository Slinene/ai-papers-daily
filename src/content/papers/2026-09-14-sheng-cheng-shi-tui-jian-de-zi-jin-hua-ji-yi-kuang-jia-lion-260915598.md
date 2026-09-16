---
title: Self-Evolving Memory for Generative Recommendation
title_zh: 生成式推荐的自进化记忆框架 LION
authors:
- Xinyu Lin
- Zhuosong Jiang
- Zixiao Suo
- Siqin Wang
- Hanqing Zeng
- Hanchao Yu
- Yinglong Xia
- Jiang Zhang
- Aashu Singh
- Fei Liu
affiliations:
- National University of Singapore
- Meta AI
arxiv_id: '2609.15598'
url: https://arxiv.org/abs/2609.15598
pdf_url: https://arxiv.org/pdf/2609.15598
published: '2026-09-14'
collected: '2026-09-16'
category: GenRec
direction: 生成式推荐 · 持续学习与记忆隔离
tags:
- Generative Recommendation
- Continual Learning
- Sparse Memory
- Evolution Conflict
- User Modeling
- KV Memory
one_liner: 用稀疏 KV 记忆层隔离不同用户行为模式的梯度，缓解生成式推荐持续进化中的进化冲突
practical_value: '- 在持续更新生成式推荐或 LLM4Rec 模型时，不要直接全参 fine-tune；可以插一个固定大小的稀疏 KV 记忆层，用
  Top-K 激活按用户行为模式路由，隔离头部/长尾梯度冲突，避免高频用户主导模型更新。

  - 想强化长尾或低频行为，可加 consolidation loss：对记忆增强后的用户表示直接预测 next item；注意该 loss 必须加在“隔离后的表示”上，直接加在共享
  backbone 反而会引入额外梯度冲突。

  - 做用户长期偏好建模可用“全序列 query + 近期窗口计算”的非对称设计：仅用完整历史去激活记忆 slot，主 Transformer 仍只消费最近几条交互；既能捕捉长期行为模式，又不增加推理序列长度。

  - 稀疏 KV 记忆参数固定为 2Nd，不随用户规模增长；实验表明 N=4096,K=32 与 N=65536,K=8 性能几乎一致，工程上可大幅压缩参数，替代
  per-user embedding 或 LoRA，降低部署成本。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
真实场景中用户偏好持续变化，生成式推荐需要持续自进化。但现有持续微调或蒸馏方法直接更新共享的自回归参数空间，会导致“进化冲突”：高频/头部行为模式的梯度在数量级上压过低频/长尾模式，且两者优化方向可能冲突，最终头部用户性能提升而长尾用户被忽视，整体指标受损。

## 方法关键点
LION 在 T5 生成式推荐 backbone 中插入稀疏 Key-Value 记忆层：
- **稀疏激活**：用户 query 来自完整交互历史，通过 Top-K 选择激活跃的 memory slots，对应 values 加权聚合后加入 hidden state；不同行为模式被路由到不同 memory 路径，实现 isolated memorization。
- **非对称设计**：主干 Transformer 只消费近期窗口，但 memory query 使用完整历史，兼顾长期模式与推理效率。
- **consolidation loss**：对记忆增强后的用户表示直接做 next-item 预测，为长尾行为提供更强监督；最终损失为 L_rec + λ L_con。
- 理论分析表明：稀疏激活将梯度冲突限制在重叠 slot，冲突比 ≤ |O|/K；噪声方差降低带来更快收敛；参数规模固定为 2Nd，不随用户数增长。

## 关键结果
在 Amazon Games/CDs/Toys 三个数据集上，按时间切分为 5 个 period，用户按活跃度分 G1-G5 组，对比 Replay、SAIL-PIW、PISA、RecICL、LSAT、PESO、TIGER。LION 相比 TIGER 的 Recall@10 提升分别为 Games +29.8%、CDs +35.5%、Toys +15.6%；对 inactive 用户 G3-G5 的提升更显著，并在所有 period 保持稳定。梯度余弦由负转正，验证了对进化冲突的缓解。消融显示：仅加 consolidation loss 而无需稀疏记忆会伤害性能，稀疏记忆 + 全序列 query + consolidation 组合最有效；记忆规模压缩 16 倍几乎不降性能。

**最值得记住的一句话**：生成式推荐的持续进化不应在全共享参数空间里直接更新；用稀疏 KV 记忆隔离不同行为模式的梯度，并只对记忆隔离后的表示做强监督信号，是解决头部/长尾冲突的有效方式。
