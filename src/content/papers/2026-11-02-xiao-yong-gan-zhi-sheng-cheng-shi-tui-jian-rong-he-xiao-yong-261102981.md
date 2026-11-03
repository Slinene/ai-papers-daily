---
title: 'Utility-Aware Generative Recommendation: Utility-Enriched Semantic Codes and
  Utility-Guided Decoding'
title_zh: 效用感知生成式推荐：融合效用语义编码与效用引导解码
authors:
- Yang Hu
- Duo Wang
- Ning Li
- Kang Li
- Junda She
- Chengcheng Guo
- Kuo Cai
- Bin Liu
- Youhua Liu
- Xiaoshuang Chen
affiliations:
- Kuaishou Technology
- Peking University
arxiv_id: '2611.02981'
url: https://arxiv.org/abs/2611.02981
pdf_url: https://arxiv.org/pdf/2611.02981
published: '2026-11-02'
collected: '2026-11-03'
category: GenRec
direction: 生成式推荐 · 效用感知 SID 与解码
tags:
- Generative Recommendation
- Semantic ID
- Utility-Aware Decoding
- Beam Search
- Multi-Objective
- Lookup-Free Quantization
one_liner: 将多目标效用写入SID末级并引导beam search，降低高价值候选被剪枝
practical_value: '- UE-SID 思路可直接迁移到电商/广告的 Semantic ID 体系：前几级保持语义量化不变，只在末级用 LFQ 释放弱判别
  semantic bits，替换为 GMV、转化率、客单价、时长等 utility bucket。新商品上线或爆款衰减时只更新 utility bits，不重训
  generator/tokenizer，适配目录高频变化。

  - UGD 的工程实现很适合低风险上线：复用 decoder 隐状态 + stop-gradient，只训练轻量共享 MLP 和行为专用 token head；beam
  search 打分用 logp + λ Σ w_m Norm(q_m)，无需额外 backbone 前向，QPS 几乎不降。多目标权重配置化，可随时切换不同业务目标。

  - 对比 RL 和 post-rerank：UGD 在每一步 prefix 剪枝时估计 utility，避免 GRPO 只在完整 sequence 上优化而无法顾及中间剪枝；也比后排序更能保留已剪掉的高价值候选。做生成式召回/query
  生成时可优先考虑这种 decode 端 utility 引导，而不是加重训练端 RL。'
score: 10
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
SID 生成式推荐通常只靠多模态语义量化和 next-token likelihood，无法充分表达点赞、长播、完播、分享等 post-exposure utility。beam search 按生成概率剪枝，会提前丢弃高 utility 但生成概率不高的路径；训练期 RL 或生成后 rerank 都无法完全恢复这些候选。  

**方法关键点**  
- **UE-SID**：前 L-1 级继续用 residual K-means，末级改为 lookup-free quantization（LFQ）生成 B bits 二进制码；从弱判别 semantic bits 中释放 B_u bits，编码 item 级 utility bucket，不增加 SID 长度或词表。支持每小时刷新 utility bits、每周重校准 bucket 边界，新 item 在线编码。  
- **UGD**：复用 decoder 各步 hidden state，经 stop-gradient 共享 MLP 得到 utility 表示；每个行为有独立 token-level head，预测 watch time / long view / like / share 等多目标。beam score = cumulative logp + λ Σ w_m Norm(q_mv)，utility 仅在当前步参与剪枝，不跨步累积。训练损失 = LNTP + β Lutility，stop-gradient 避免干扰生成主干。  

**关键结果**  
KuaiRand 上 UAGR Recall@3=2.7741、NDCG@3=2.2740，较最强 baseline 分别提升 7.74% 和 16.52%；UE-SID 的 ICR=0.9902、Gini=0.00500、Entropy=8.0918。Ablation 中 UGD 单独带来最大提升；相比 GRPO、post-rerank 均更优。快手生产环境 A/B：app usage time +0.074%、video watch time +0.206%、video views +0.164%，QPS 仅 -0.03%，已全量部署。  

最值得记住的一句话：utility 要在 SID 表征和 beam search 解码两个环节显式编码，而不是只靠训练端对齐或后排序。
