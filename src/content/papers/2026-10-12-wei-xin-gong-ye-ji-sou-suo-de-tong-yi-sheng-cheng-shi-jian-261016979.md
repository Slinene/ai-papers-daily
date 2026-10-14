---
title: 'WeGR: Unified Generative Retrieval for Industrial Search Systems in WeChat'
title_zh: 微信工业级搜索的统一生成式检索框架 WeGR
authors:
- Jiajun Han
- Guoxin Ma
- Felix
- Liangsheng Xu
- Ruiqi Yu
- Yingdi Guo
- Zongbing Wang
- Xinhua Ye
- Chenyan Hua
- Xin Xie
affiliations:
- Tencent Penguin Island
arxiv_id: '2610.16979'
url: https://arxiv.org/abs/2610.16979
pdf_url: https://arxiv.org/pdf/2610.16979
published: '2026-10-12'
collected: '2026-10-14'
category: GenRec
direction: 生成式检索 · SID 构建 + RL 偏好优化
tags:
- Generative Retrieval
- Semantic ID
- Codebook Collapse
- GRPO
- Industrial Search
- DHPO
one_liner: 联合行为感知 SID 构建与动态 horizon RL，解决生成式检索中的码本坍塌和奖励稀疏
practical_value: '- SID 构建：将 query-item / item-item 协同信号作为对比学习损失加在连续表征上，并通过分离的 projection
  head 避免直接干扰 codebook；同时使用 codebook refresh（只对第一层，EMA 阈值重置）和残差保真 + 碰撞正则化，能显著提升 codebook
  利用率，避免 SID 坍塌。这些 trick 可直接迁移到电商 Semantic ID 学习。

  - RL 稀疏 reward：如果直接使用点击/订单作为 outcome reward，GRPO 会因 exact match 而大面积失效。借鉴 DHPO 的动态
  horizon 课程，把 SID 前缀匹配作为早期 reward，逐步扩展到完整 SID，并只更新对应前缀 token，既不需要离线训练 ranker，也避免
  beam search 的分布偏移。

  - 多正样本 SFT：工业搜索 session 内通常有多个正反馈 item，MSFT 同时拟合所有正样本，可作为 RL 的稳定正则项，防止 policy 在稀疏
  reward 下遗忘检索能力；建议与新策略 RL 联合训练，权重 0.5 左右可参考。

  - 工程部署：生成式检索替换传统多路召回能直接减少进入粗排的候选量（本案 -38.10%），带来 CPU/GPU 和延迟收益；可考虑先 additive，再逐步加大替换比例验证收益。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

工业级搜索系统常用多路召回+粗排+精排级联，带来复杂性和计算开销。生成式检索（GR）把 item 表示成 Semantic ID 并直接生成候选，有望统一检索流程，但面临两个核心难点：SID 构建难以同时保留协同信号并维持 codebook 利用率；RL 偏好优化因 exact SID match 的 outcome reward 极度稀疏，导致大量采样轨迹无学习信号。

WeGR 在微信电商搜索中解决这两点：
1) **CoCo-VAE**：将 query-to-item 和 item-to-item 协同信号注入连续表征，而非约束离散 codebook，解耦协同学习与码本优化；配合第一层 codebook refresh（EMA 跟踪 usage，对 dead codeword 重置）和 Fidelity Anti-collapse Regularization（sample 级残差保真用 soft top-K 加权重建，codeword 级碰撞正则惩罚 assignment 集中），缓解 codebook collapse。
2) **DHPO**：利用 SID 层次结构，动态扩展 reward 评估和 policy optimization 的 horizon——训练从 prefix 匹配开始，逐步到完整 SID 匹配；每个 stage 只对前 h 个 token 更新策略，准确分配信用，不依赖辅助 reward model。同时引入 MSFT 对 session 内多个正样本同时 SFT，稳定训练。

离线实验在 Click/Order 各 20k 数据集上，CoCo-VAE 相比 RQ-Kmeans HR@6 提升 4.47%/1.28%，DHPO 相比 TPMA-GRPO HR@6 提升 2.18%/2.03%。线上 A/B 测试 V1.2 移除 80% 传统召回候选，订单/CTR/CVR 相对提升 2.539%/1.508%/1.381%，pre-ranking 候选减少 38.10%，CPU/GPU 使用节省 25.5%/26.1%，延迟降低 21.7ms 和 15.4ms。

最值得记住的一句话：生成式检索落地需同时解决 SID 的语义质量和 RL 的 reward 密度，CoCo-VAE 保持协同信号且防码本坍塌，DHPO 用层次化课程让行为 reward 从稀疏变得可用。
