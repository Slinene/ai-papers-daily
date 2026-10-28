---
title: 'KL-MOPD: Discrepancy-Aware Multi-Objective On-Policy Distillation for Generative
  Recommendation'
title_zh: KL-MOPD：面向生成式推荐的多目标在线策略蒸馏
authors:
- Weiqin Yang
- Yandong Wang
- Yuan Gao
- Hao Deng
- Jinxin Hu
- Jing Cao
- Jiawei Chen
affiliations:
- Zhejiang University
- Alibaba Group
- Alibaba International Digital Commerce Group
arxiv_id: '2610.36973'
url: https://arxiv.org/abs/2610.36973
pdf_url: https://arxiv.org/pdf/2610.36973
published: '2026-10-27'
collected: '2026-10-28'
category: GenRec
direction: 生成式推荐 · 多目标蒸馏
tags:
- Generative Recommendation
- Multi-Objective Distillation
- On-Policy Distillation
- KL Divergence
- Semantic ID
- E-commerce
one_liner: 用初始学生与教师 token 级 KL 差异加权，解决生成式推荐多目标蒸馏中的 token 级不平衡，提升联合目标
practical_value: '- 在生成式推荐（Semantic ID 逐 token 解码）中，多目标融合要下沉到 token 级做 on-policy 蒸馏，而不是只做
  item 级 loss 或分数融合；否则中间步骤的 token 错误会直接导致正样本检索失败。

  - 工程实现上，先用 initial student 和两个 teacher 计算每个 token 的 KL 散度，得到权重 alpha_{j,t} 并预计算一次；训练时直接作为
  token 蒸馏 loss 的加权系数，不增加额外前向/反向开销，适合线上大规模部署。

  - 若已有 CTR、CVR/GMV 等单目标 teacher，可以直接套用该加权方法：在每个 token 上给离学生更远的 teacher 更高权重，优先补强当前步骤的薄弱目标，缓解解码后期某目标被忽略的问题。

  - 电商广告场景验证：十亿级工业数据离线 joint metric +3.19%，线上 A/B 广告收入 +1.63%、GMV +2.20%，说明 token
  级多目标蒸馏能带来真实业务收益。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
生成式推荐把物品表示成 Semantic ID 并逐 token 解码，只有每一步都选对 token 才能命中正样本。但实际业务要同时优化点击（CTR）和转化/成交（CVR/GMV），传统 item 级多目标方法缺少 token 级监督，无法指导中间解码步骤。多目标在线策略蒸馏（MOPD）理论上适合生成式推荐，因为 on-policy 学习等价于最大化带 KL 正则的联合目标，且能提供 token 级监督。然而 vanilla MOPD 对两个 teacher 采用等权蒸馏，存在两个问题：token 级不平衡（同一 token 上两个 teacher 难度不同）和跨 token 不一致（更难蒸馏的 teacher 沿序列切换）。这导致每个目标在部分 token 上欠拟合，最终损害正样本检索。

**方法关键点**  
- 用初始学生与各 teacher 在 token t 的 KL 散度 d_{j,t} 衡量蒸馏难度；  
- 权重 alpha_{j,t} = d_{j,t}/(d_{c,t}+d_{v,t})，对更难蒸馏的 teacher 加强监督；  
- 权重只依赖 initial student 和固定 teacher，训练前预计算一次，训练时零额外开销；  
- 理论证明：在 additive joint objective 下，KL-MOPD 严格优于 vanilla MOPD，下界为 beta * S_KL - D_T L^3 / beta^2，其中 S_KL 与 token 上难度差异平方和正相关。

**关键实验**  
在 TencentGR、YooChoose、Taobao 三个公开数据集上，使用 TIGER 和 REG4Rec 两种 backbone，对比 RCE-KD、MTS24MM、SmartGR、GR4AD、TSGR、MOPD、SMOPD、TrustMOPD 等 8 个 baseline。KL-MOPD 在个体目标平均提升 +4.91%，联合目标平均 +4.12%；在十亿级工业数据集离线 joint metric 提升 3.19%；线上 A/B 测试广告收入 +1.63%、GMV +2.20%，且训练时间几乎无增加。

**最值得记住的一句话**  
在生成式推荐多目标蒸馏中，用初始学生与各 teacher 的 token-wise KL 作为权重，预计算一次即可在几乎零额外开销下解决 token 级蒸馏不平衡，显著提升联合目标。
