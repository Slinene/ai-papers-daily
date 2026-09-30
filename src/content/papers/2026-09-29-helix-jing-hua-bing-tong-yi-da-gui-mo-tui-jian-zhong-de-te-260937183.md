---
title: 'HELIX: Purified and Unified - Rethinking Feature Interaction and Sequence
  Modeling for Large-Scale Recommendation'
title_zh: HELIX：净化并统一大规模推荐中的特征交互与序列建模
authors:
- Yuntao Zheng
- Miao Zhang
- Yadong Ding
- Yanchuan Tang
- Lixiyu Chen
- Hao Wang
- Quan Li
- Shiying Cai
- Yue Lin
- Jiayu Li
affiliations:
- Data - Global E-Commerce Recommendation Video Team
arxiv_id: '2609.37183'
url: https://arxiv.org/abs/2609.37183
pdf_url: https://arxiv.org/pdf/2609.37183
published: '2026-09-29'
collected: '2026-09-30'
category: RecSys
direction: 统一特征交互与序列建模的排序架构
tags:
- Recommendation
- Feature Interaction
- Sequence Modeling
- Scaling Law
- KV Cache
- Transformer
one_liner: 用单向可复用 KV cache 与 Mixup-PerToken-FFN 联合扩展特征交互和序列建模，电商视频 GMV/用户提升约 6%
practical_value: '- 把候选无关的用户行为序列编码成**可复用 KV cache**，候选侧只做 cross-attention 读取，强制单向信息流。这样在
  serving 多候选、training 多样本时都能摊销 encoder 成本；如果搜广推系统里要接入用户长序列，这是可落地的架构选择。

  - 异构特征交互可考虑用 **Mixup-PerToken-FFN** 替代 self-attention：参数免费的 Mixup 按通道切片重组 token，再用
  token-wise SwiGLU 做非线性交互，比 self-attention 更适配稠密异构特征，且省计算。

  - 序列 encoder 采用**金字塔 query 压缩**：按特征重要性给每条序列分配最近 token 预算，而不是全局截断或统一池化；配合 padding-free
  变长执行，能显著降低长序列训练成本。

  - 训练稳定性上，对 SwiGLU 的 gate/up 分支做**非参数归一化**可以避免 FP16 激活溢出；QK-Norm 和 value-side gated
  attention 在推荐排序模型里也有稳定 AUC 增益。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
工业推荐排序模型通常沿两条轴扩展：异构特征交互和用户行为序列建模。单独扩展任一轴都会遇到收益天花板和较差的 scaling-law 斜率，而现有统一架构存在自注意力不适合异构 token、一步式混合分散行为检索、双向信息流导致用户侧序列状态无法跨候选复用等问题。

**方法关键点**
- **三流 tokenization**：MixTokenizer 将非序列特征映射为 M 个候选相关 mix-token；SeqTokenizer 分别处理候选无关 U-only 序列和候选相关 U×C 序列，加入 [SINK] token，并在拼接前按序列内部分配位置编码。
- **MixFormer**：由 cross-attention 检索 U×C 序列和 Mixup-PerToken-FFN 做特征交互交替组成；Mixup 参数免费地按通道切片重组 token，避免 self-attention 的二次注意力计算。
- **SeqFormer Encoder**：对 U-only 历史做非因果 self-attention + FFN，采用金字塔 query 压缩；最终层输出候选无关的 K/V cache，供后续跨候选和跨样本复用。
- **SeqFormer Decoder**：候选侧 mix-token 只从 reusable cache 中 cross-attention 检索，再做 MPTF 交互；信息流严格单向，避免用户侧状态被候选污染。
- 训练细节：QK-Norm、value-side gated attention、非参数 Gate-Up-Norm、GQA、LayerScale 等稳定训练并提升效果。

**关键实验**
在 TikTok 电商视频推荐内部数据集上，与生产基线 RankMixer + Transformer 及 OneTrans 对比：HELIX-L 以 358M 参数、35.28G FLOPs 取得 CTR AUC +0.21%、CTR UAUC +0.82%、CVR AUC +0.17%、CVR UAUC +1.38%；优于更大计算量的 OneTrans。S→XXL 配置下 CTR/CVR AUC 随 FLOPs 呈可预测的 power-law 增长。在线 A/B 测试中，电商视频点击/用户 +2.06%，GMV/用户 +5.99%，支付订单/用户 +6.10%。

**最值得记住的一句话**
把候选无关用户序列做成可复用 KV cache，并强制单向信息流，使特征交互和序列建模可以不对称联合扩展，同时保留生产级摊销能力。
