---
title: 'Anti-Periodic Positional Encoding: Möbius Boundary Conditions Make In-Context
  Retrieval Reliable'
title_zh: 反周期位置编码：莫比乌斯边界条件实现可靠的上下文检索
authors:
- Ji Ho Bae
affiliations:
- JRTI, Seoul
arxiv_id: '2607.21405'
url: https://arxiv.org/abs/2607.21405
pdf_url: https://arxiv.org/pdf/2607.21405
published: '2026-07-23'
collected: '2026-07-24'
category: Training
direction: 反周期位置编码 · 训练稳定性
tags:
- Rotary Positional Encoding
- Anti-Periodic
- Needle-in-a-Haystack
- Training Stability
- Seed Lottery
- Long Context
one_liner: 提出反周期频率阶梯的 Möbius RoPE，以零困惑度代价消除检索种子彩票，使准确率从 63% 升至 90%
practical_value: '- 在 LLM 推荐或 Agent 中，直接将部分注意力头的 RoPE 频率改为反周期阶梯（奇数倍 π/N），可零成本提升长用户行为序列中关键项的检索稳定性，避免因随机种子导致的性能大幅波动

  - 混合编码（25% 注意力头使用 Möbius 频率）使困惑度无损失，可作为工程插件在不重新预训练的情况下提升模型对长对话或搜索历史的可靠回忆能力

  - 该编码在训练窗口内的单针检索任务上效果显著，适用于电商场景中从用户长时段历史里精准抽取特定事件（如某次购买、点击）的需求

  - 反周期边界条件建立了序列两端的确定性耦合，可能有助于位置敏感的注意力机制，可用于改进现有推荐模型中的位置嵌入设计'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：标准 RoPE 位置编码在小模型上下文检索中存在严重的种子彩票现象，相同预训练仅因随机种子不同，needle-in-a-haystack 准确率从 14% 到 86% 剧烈波动，严重影响长上下文信息提取的可靠性。

**方法关键点**：提出 Möbius RoPE，将旋转频率阶梯设为 θ_i = π(2i+1)/N，每个旋转平面跨训练上下文按 π 的奇数倍前进，形成反周期边界条件（holonomy = -1），使序列两端通过狄利克雷“偶极子”确定性耦合。这是首次在位置编码中引入反周期结构。实验预训练 48 个模型（6 个 160M 参数臂、3 个 410M 参数臂，各使用 2B FineWeb-Edu tokens），混合臂将 25% 注意力头的频率替换为 Möbius 频率。

**关键结果**：混合模型困惑度无损失（29.66 vs. 29.72），但在上下文 512 时 NIAH 准确率从 63.3%±31.4% 提升至 90.3%±5.7%，最差种子准确率从 14% 升至 86%，方差检验 p=0.013-0.029，在 410M 规模下（Levene p=0.040）同样显著。消融表明同频段非周期或周期频率无此效果；将训练好的模型频率表换回标准 RoPE 会破坏检索能力，尤其损害远端针检索。纯 NoPE 短期检索更可靠但困惑度高 13% 且外推最差。混合方案兼顾基线困惑度与高可靠性下限，只需一行频率表替换即可为模型提供零成本检索保险。
