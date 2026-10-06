---
title: 'BRANCH-MoE: Balance-Aware Tree Routing for Large Embedding Models'
title_zh: BRANCH-MoE：面向大规模嵌入模型的平衡感知树路由
authors:
- Gang Fu
- Adel Javanmard
- MohammadHossein Bateni
- Vahab Mirrokni
affiliations:
- Google Research
- University of Southern California
arxiv_id: '2610.06725'
url: https://arxiv.org/abs/2610.06725
pdf_url: https://arxiv.org/pdf/2610.06725
published: '2026-10-05'
collected: '2026-10-06'
category: Training
direction: MoE 树形路由与负载均衡
tags:
- MoE
- Routing
- Load Balancing
- Tree Routing
- Sparse Models
- Training
one_liner: 提出将专家置于二叉树叶节点的BRANCH-MoE，用到达加权EMA锚点在没有辅助损失的情况下保持负载均衡并诱导共路由局部性
practical_value: '- 在大规模 CTR/推荐模型中用 MoE 做稀疏专家时，可把 flat top-K 门控换成树形路由：每个内部节点用到达加权均值做
  score 中心化（训练用 batch 均值，推理用 EMA），可省掉 auxiliary load-balancing loss 及其调参，同时降低子树饿死风险。

  - 树路径天然给出专家二进制地址，可按 prefix 把专家/embedding 分配到设备或参数服务器域；推理时可依据上层 margin 预判是否跨域通信，降低
  token 分发成本，适合多级缓存/分片的大规模稀疏 embedding 部署。

  - 工程实现上：线性 node map 的树结构局部性最强（UCI 上树距离 0.71 vs 随机 0.817）；换成 MLP 会削弱局部性并提高 load CV，需在目标数据上验证。对输入特征要避免稀有二值列被
  z-score 放大成巨大 spike，否则会诱导专家 collapse（Covertype 上需 pin 低方差列）。

  - 该方法无辅助损失即可均衡负载，但 Criteo 上 load CV 高于 flat 方法（0.115 vs ≤0.006）；若业务对 per-batch 均衡极敏感，可能仍需要
  capacity factor 或调度兜底。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

Flat MoE 路由有三个麻烦：专家利用率不平衡，专家索引只是无结构分类标签，防早期 collapse 要靠 auxiliary loss 或外部 bias。这对大规模 CTR/推荐模型的多专家分布式部署尤其麻烦：既要额外调负载均衡损失，又没有可用的拓扑局部性来减少通信。

方法关键点：
- 将 E=2^D 个专家放在深度 D 的完全二叉树叶节点；每个内部节点输出标量分 f_j(x)，可用线性 map 或小 MLP。
- 每节点维护到达加权 EMA 锚点 ν_j；训练时用当前 batch 的到达加权均值 bν_j 做中心化，推理用 EMA ν_j 作为固定偏置 b_j=-ν_j，分支概率 p_j=σ(f_j(x)-a_j)。
- 掩码级联从根到叶计算完整 leaf 概率，再 top-K 选择；K=1 不归一化，K>1 对选中 gate 重归一。
- 不引入 auxiliary load balancing loss。

理论给出：线性路由 + log-concave 到达分布下，精确锚点保证每个 soft leaf 质量至少 (2e)^{-D}；EMA 有显式 noise-lag trade-off；冻结路由器下专家执行频率控制专家 SGD 收敛；树 prefix 对齐设备放置时，上层 margin 可约束跨域通信。

实验用 E=16、top-4，在 Criteo CTR、Covertype、HIGGS、YearPredictionMSD 上对比 Switch softmax、DeepSeek-V3 dynamic bias、Skywork logit-normalized、Hash。质量与最强 baseline 持平：Covertype CE 0.2372 最低；Criteo logloss 0.44596 与 Skywork/DeepSeek 无显著差异；HIGGS/MSD 也在 seed noise 内。局部性上，UCI 三个数据集线性 map 的归一化树距离为 0.710–0.718，比随机专家对 0.817 降低 12–13%，而所有 flat 路由距随机只有 3.5% 内；Criteo 上未观察到局部性。无辅助 loss 下 UCI load CV 0.09–0.23，与带 auxiliary loss 的 Switch/Skywork 相当。

最值得记住：树形路由 + 到达加权锚点，把负载均衡和拓扑局部性内建进路由几何，而不是靠损失项或事后调度。
