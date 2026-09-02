---
title: 'From Language to Behavior: Scaling Sequence Transformers for Industrial Recommendation
  Ranking with Rec-Native Designs'
title_zh: 从语言到行为：面向工业推荐排序的推荐原生序列 Transformer 扩展框架 ReST
authors:
- Jie Chen
- Xiangqian Yu
- Yanchao Lian
- Tan Lu
- Run Yang
- Zhengchun Shang
- Xing Wang
- Cheng Chen
- Ke Hu
- Qiang Li
affiliations:
- ByteDance
arxiv_id: '2609.01240'
url: https://arxiv.org/abs/2609.01240
pdf_url: https://arxiv.org/pdf/2609.01240
published: '2026-09-01'
collected: '2026-09-02'
category: RecSys
direction: 序列 Transformer 推荐排序
tags:
- Sequential Transformer
- Dual-Gated Attention
- RoTE
- Shared-Prefix Serving
- CVR Ranking
- Scaling
one_liner: 提出 ReST，用双门控注意力、RoPE+RoTE、SRN 与共享前缀编解码，把行为序列 Transformer 扩展到生产排序并获在线收益。
practical_value: '- 训练期加 auxiliary sequence CVR head 是低成本缓解 sequence starvation 的实用
  trick：只用序列表征 + 广告/商品特征做 BCE，λseq=0.1 即可让序列 encoder 梯度 norm 提升 3 倍以上，离线 AUC 在多个 backbone
  上稳定 +0.07~0.22 pct；在 hybrid DLRM 排序里能直接复用。

  - 时间注入别只当 side feature：RoTE 用 rotary 方式按 head 分配秒/分/时/天/周/季/年多粒度物理时间，兼容 FlashAttention；比仅加
  delta-time 特征多带来约 +0.04~0.12 pct AUC，适合有强时间敏感性的电商/广告行为序列。

  - 双门控注意力只需 value gate + output gate 且用 sigmoid，就能以约 7.5% FLOPs 换 +0.06% AUC；QKV
  全门控更贵但收益不增。噪声大的点击/浏览序列建模可以优先试 O+V gate。

  - 架构上把能力分配给候选侧轻量 decoder 而不是继续堆 sequence encoder：projection-free KV 复用 encoder memory、token-specific
  parameterization 保持容量；encoder 加 MoE 多 500% 参数却 0 收益。训练用 user-level shared-prefix
  提 5.8x 吞吐，serving 共享 prefix 最多降 20x 序列计算，适合候选量大、user history 长的排序场景。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推荐排序把用户行为序列作为主 scaling 轴，但直接搬 LLM Transformer 有两个障碍：行为信号噪声大、时间不规则、监督稀疏；请求一侧 user history 被 N 个候选复用，序列侧与候选侧计算需求不对称。通用块在深度/宽度/长度上容易饱和，甚至出现 sequence starvation——非序列 DLRM 分支 shortcut 主 loss，序列模块梯度弱。

### 方法关键点
- 序列 encoder T：Dual-Gated Attention 用 value gate 做聚合前过滤、output gate 做聚合后调制，均用有界 sigmoid；RoPE+RoTE 分 head 编码序数位置与多粒度物理时间（秒到年）；SRN 结合 Mix-LN 和小初始化残差 α=0.01 稳定深层训练。
- 候选 decoder C：projection-free KV 直接复用 encoder memory，query 侧 token-specific parameterization 提升容量但几乎不增激活 FLOPs。
- 训练期辅助目标：aux sequence CVR head 只用序列表征+ad 特征，λseq=0.1 使序列 encoder 梯度 norm >3x；sigmoid contrastive 对齐序列与非序列用户表征。
- 系统 co-design：ULT 按 user 分组共享前缀训练提吞吐 5.8x；serving 共享前缀把序列计算从 N 次降到 1 次，最多降 20x。

### 关键结果
工业 TikTok Shop Ads：Base/Large 分别 +0.67%/+0.92% AUCΔ，超越 LLaMA、HSTU、parameter-matched Trans.；公开 ML-1M/ML-20M/Books 全最优。消融：O+V gate +0.06% AUC 只多 7.5% FLOPs；RoPE+RoTE +0.12%；SRN +0.08%；轻量 decoder +0.05% 且仅 +0.2% FLOPs；给 encoder 加 MoE 多 500% 参数无收益。线上 A/B：AUC +1.31%，Advv +11.93%，50ms P99 内，已全量。
