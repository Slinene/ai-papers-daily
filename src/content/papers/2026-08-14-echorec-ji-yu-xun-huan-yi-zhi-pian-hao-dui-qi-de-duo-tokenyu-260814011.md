---
title: 'EchoRec: Multi-Item Prediction-Empowered Generative Recommendation via Cycle-Consistent
  Preference Alignment'
title_zh: EchoRec：基于循环一致偏好对齐的多Token预测生成式推荐
authors:
- Haokai Ma
- Aoqi Hu
- Yueao Xing
- Ruobing Xie
- Yonghui Yang
- Teng Tu
- Lei Meng
- Tat-Seng Chua
affiliations:
- National University of Singapore
- Beijing University of Posts and Telecommunications
- Tencent
- Shandong University
arxiv_id: '2608.14011'
url: https://arxiv.org/abs/2608.14011
pdf_url: https://arxiv.org/pdf/2608.14011
published: '2026-08-14'
collected: '2026-08-17'
category: GenRec
direction: 生成式推荐 · Multi-Token Prediction
tags:
- Generative Recommendation
- Semantic ID
- Multi-Token Prediction
- Cycle Consistency
- Preference Alignment
- Sequential Recommendation
one_liner: 用未来多步行为作顺序依赖的密集监督，并通过循环一致性对齐把整体偏好内化到解码表示，提升生成式推荐且在线零开销
practical_value: '- 未来行为可作为辅助监督：在训练时挂轻量 MTP 分支预测 t+2、t+3 商品，并让每个分支条件在前一个分支表示/上一步商品上，而不是从同一隐状态并行解码；能避免多个
  horizon 预测同质化，适合需要一次性生成多个候选、多创意、多坑位结果的广告/推荐场景。

  - 训练时新增的辅助分支共享主模型输出头、token embedding 和 decoding graph，推理时全部丢弃，线上延迟与显存几乎不变。这适合电商/广告高
  QPS 场景：用可接受的训练成本换在线零开销的指标提升。

  - 若业务中需要对齐多个表示（如用户向量与多意图向量、跨模态特征、多任务共享表示），单向 alignment 可能被 projector 吸收差异，造成“虚假对齐”；加反向
  projector 和 round-trip/cycle loss 可抑制这类问题，是一个可复用的训练 trick。

  - 当用户行为序列较长且噪声较多时，把目标从单点 next-item 改为多 horizon 整体偏好，会提升对噪声交互的鲁棒性；论文在 20% 随机替换噪声下相对提升反而从
  17.68% 增至 54.89%，对真实电商点击噪声有参考价值。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**

生成式推荐通常只做 next-item 预测，未来行为信息未被利用。论文先在 Amazon Game/Baby/Arts 上验证：当前交互 item 与未来 t+h item 的 SID overlap 显著高于随机对，lift 最高 21.02×（h=1），到 h=3 仍有 2.89×–8.79×，说明未来行为存在“语义回声”；但该回声随 horizon 衰减，说明需要顺序依赖建模。并行 MTP 结构会把不同 horizon 预测同质化：RPG-Par 的平均 inter-horizon Jaccard 为 62.73%，高于顺序 rollout 的 53.21%，且不提升即时目标 t+1 的性能。

**方法关键点**

- Horizon-aware Preference Generation (HPG)：在主分支 MTP-0 上链式增加 MTP-1/MTP-2，每个分支将前序分支表示与 shifted 序列 embedding 拼接，经 Proj 和单层 Transformer 后复用共享输出头，预测 in+2、in+3；仅添加少量参数。
- Verifiable Holistic-Preference Alignment (VHA)：把三个 horizon 的表示 stop-gradient 后聚合为 holistic preference z_f，用 Proj0→f 将 decoding representation z0_n 拉向 z_f；同时引入反向 Proj f→0 和双向 cycle loss，保证投影对可逆，抑制 rank-collapse 式虚假对齐。
- 最终 loss 组合为 L0 + λ1L1 + λ2L2 + λ_traceL_trace + λ_cycL_cyc；推理仅用 MTP-0，辅助分支和 projector 全部丢弃。

**关键实验**

在 Game/Baby/Arts 三个 Amazon 2023 数据集上，对比 EAGER、TIGER、LETTER、ETEGRec、SETRec、RPG。以 RPG 为 backbone，EchoRec(RPG) 的 HR@10/NDCG@10/HR@20/NDCG@20 相对提升在 Game 为 11.17%/11.35%/10.65%/11.02%，Baby 为 17.68%/21.40%/16.81%/20.68%，Arts 为 14.56%/18.29%/13.59%/17.38%；换 SETRec 后同样稳定提升 6.40%–17.68%。效率上，训练延迟增至约 2–3 倍，但推理延迟和显存与 backbone 几乎一致。

**最值得记住的一句话**

未来行为可以作为顺序依赖的密集监督，但必须链式建模并加循环一致性验证；否则并行 MTP 会坍缩为同质预测，单向对齐也容易被投影器“作弊”吸收。
