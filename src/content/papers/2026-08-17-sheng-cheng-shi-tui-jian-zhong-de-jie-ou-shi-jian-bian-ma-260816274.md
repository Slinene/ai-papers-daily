---
title: Decoupled Temporal Encoding for Generative Recommendation
title_zh: 生成式推荐中的解耦时间编码
authors:
- Pengfei Jia
- Jingjian Wang
- Jingmao Li
- Ge Zhang
- Feng Shi
affiliations:
- Rajax Network Technology (Taobao Shangou of Alibaba)
- Yale School of Public Health
arxiv_id: '2608.16274'
url: https://arxiv.org/abs/2608.16274
pdf_url: https://arxiv.org/pdf/2608.16274
published: '2026-08-17'
collected: '2026-08-18'
category: GenRec
direction: 生成式推荐 · 时序解耦编码
tags:
- Temporal Encoding
- Generative Recommendation
- Transformer
- Positional Encoding
- Sequential Recommendation
- Industrial Deployment
one_liner: 将宏观时间动态与微观顺序先验解耦，轻量注入 Transformer，在淘系闪购广告在线提升 CTR +1.8%、RPM +3.0%
practical_value: '- 把时序建模拆成两条通路：输入层用紧凑 temporal primitives（recency decay、intra-day/weekly
  sinusoid、traffic burst）注入 item embedding；attention 层用 time-gated 的 relative-order
  bias，仅在时间间隔密集时激活。外卖、即时零售、广告等强时间规律场景可直接替换 RoPE/ALiBi。

  - 避免大 interval embedding table，DTE 只增加 238 个参数、0.47 KB FP16，在线延迟 +0.3%。工程上很适合已有
  Transformer ranking 管线插拔，不需要重构 backbone。

  - 个性化时间融合：用用户历史平均池化过 MLP + softmax 为每个 temporal primitive 生成权重，而不是统一静态时间嵌入。对上班族周末/工作日、午晚餐差异明显的用户更有收益。

  - 分析行为序列平均时间间隔可以指导是否启用顺序 bias：密集序列上收益最大；稀疏序列主要靠时间戳即可。可作为 A/B 分桶或模型开关参考。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
Transformer 生成式推荐多沿用 LLM 的位置编码，只表达离散顺序，忽略时间戳中的连续时间语义。外卖 / 即时零售用户行为存在多层时间规律：近期交互更强、午晚餐高峰、工作日与周末差异、促销引发的流量突发。已有时间感知方法通常把时间间隔、衰减、注意力偏置等混在一个表示或单一通路中，难以区分宏观时间动态与局部顺序线索。

## 方法关键点
DTE 将时间建模拆成两个互补模块：
- **Personalized macro-temporal module**：在输入侧把紧凑 temporal primitives 注入 item embedding，`e~_i = e_i + r * m(t_i)`。其中 `m(t_i)` 是四个分量的自适应混合：recency decay `exp(-λ Δt_i)`、intra-day sinusoid `sin(2π hour/24)`、weekly sinusoid `sin(2π weekday/7)`、以及 burst-sensitive variation `log(1 + ReLU(deviation))`。各分量权重由用户历史 average pooling 经轻量 MLP + softmax 生成，实现用户个性化时间建模。
- **Time-gated micro-sequential module**：在 self-attention 中加相对顺序偏置 `B_ij = -α · g(|Δt_ij|) · |i-j|`，门控 `g(|Δt|) = sigmoid(-γ(|Δt| - τ))` 只对时间密集的交互激活，避免稀疏场景下引入噪声顺序先验。
- 两个模块均轻量，且兼容现有 decoder-only ranking 骨架，部署成本极低。

## 关键实验
在工业数据集（淘宝闪购广告，400M 用户 / 5M 商品 / 2.5B 样本）和 KuaiRand 1K 上评估。离线 GAUC：工业 DTE 0.7098 vs 生产基线 BST+ALiBi 0.6982；KuaiRand 0.9243 vs 0.9110。参数仅增加 238 个，FP16 内存 0.47 KB，离线延迟 3.02 ms。在线 A/B 三周 20% 流量：CTR +1.8%，RPM +3.0%，平均服务延迟仅 +0.3%，已全量部署至淘系闪购广告推荐。消融显示 macro、micro、软门控、recency/periodicity/burst 均有正向贡献，其中 burst 在工业场景收益更大。

最值得记住的一句话：**把宏观时间上下文与微观顺序先验解耦，用轻量输入注入和门控注意力偏置，比把时间信息混在一个统一表示中更有效，且几乎不增加部署成本。**
