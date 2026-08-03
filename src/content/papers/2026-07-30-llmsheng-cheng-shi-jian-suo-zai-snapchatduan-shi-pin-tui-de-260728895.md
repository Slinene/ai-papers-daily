---
title: LLM-Based Generative Retrieval for Snapchat Content Recommendation
title_zh: LLM生成式检索在Snapchat短视频推荐中的工业级落地
authors:
- Liam Collins
- Jiwen Ren
- Donald Loveland
- Bhuvesh Kumar
- Clark Mingxuan Ju
- Xuan Guo
- Mo Li
- Alvin Hou
- Yi Cui
- Peng Yang
affiliations:
- Snap, Inc.
arxiv_id: '2607.28895'
url: https://arxiv.org/abs/2607.28895
pdf_url: https://arxiv.org/pdf/2607.28895
published: '2026-07-30'
collected: '2026-08-03'
category: GenRec
direction: 生成式推荐 · 语义 ID 与 LLM 工程落地
tags:
- Generative Retrieval
- Semantic ID
- LLM
- Recommendation
- Industrial System
- Co-engagement
one_liner: 首次部署 LLM 生成式检索：多模态 PPR 行为 SID + 两阶段词汇接地 + 推理优化，线上观看时长提升 0.37%
practical_value: '- **SID 构建加入 PPR 共现对比损失**：用 Pagerank 从用户-视频二部图挑选高质量正样本对，做对比学习，可显著缓解码本碰撞、注入协同信号，视频
  ID 唯一率从 16.8% 提升至 32.1%。电商推荐中可以用商品共购图或用户行为图生成类似正样本对，改善语义 ID 的区分度。

  - **两阶段 LLM 训练（CPT+SFT）**：先用视频描述做 SID 到文本的生成任务，冻住 LLM 只训练新加入的 SID embedding，使新 token
  与模型的语义空间对齐；再在用户交互序列上全量 SFT。CPT 可稳定提供额外 0.8%~1.2% 的 Recall/Pass@k 提升，且成本低（一次性训练），值得在引入新
  ID 体系时复用。

  - **高吞吐推理的工程组合**：TensorRT-LLM CUDA 原生 beam search 替换 Python 实现，结合分布式 worker-loop
  架构和异步 IO，实现 45.7 倍吞吐提升。对于需要大 beam 宽度的生成式推荐推理，这套组合可直接迁移。训练侧用动态序列打包 + FlashAttention-2
  变长支持 + torch.compile 获得 3.6 倍训练提速，同样适用于短序列用户行为训练。

  - **架构选择启示**：相同参数量下，decoder-only LLM（Qwen3）比 T5 encoder-decoder 在 SID 检索 Pass@32
  上高出约 1.5 倍，且缩放至 600M 仍保持显著优势，说明生成式检索应优先选用 decoder-only 预训练架构。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：生成式检索（GR）将推荐重述为基于用户行为序列生成语义 ID（SID）的序列预测任务，但其工业落地面临三个耦合挑战：如何设计高碰撞抵抗且富含协同信号的 SID，如何让 LLM 理解全新的 SID 词汇，以及如何在严格延迟和成本下高效训练与推理。现有 LLM-based GR 多停留在学术，缺乏大规模生产验证。

**方法关键点**：
- **多模态行为感知 SID**：用 Qwen3-VL 多模态嵌入 + 残差量化（RQ-VAE）构建视频 SID，并引入基于 Personalized PageRank（PPR）的共现对比损失（抽取高 PPR 得分的视频对作为正样本），码本利用率从 31.8% 提升至 49.1%，唯一 SID 比例从 16.8% 提升至 32.1%，大幅缓解碰撞。
- **两阶段 LLM 训练**：① 连续预训练（CPT）：冻住 LLM 主体，仅训练新 SID token 的 embedding，用 SID 生成视频文本描述的任务，使 token 与 LLM 世界知识对齐（Text-Grounding RSA 从 0.016 升至 0.322）；② 监督微调（SFT）：基于用户行为序列生成下一项 SID 进行全量微调。
- **高通量工程优化**：训练侧通过 torch.compile、FlashAttention-2 变长支持、动态序列打包，整体训练吞吐提升 3.63 倍；推理侧采用 TensorRT-LLM CUDA beam search、分散式 worker-loop 架构和异步 IO，端到端吞吐提升 45.7 倍。

**关键结果**：
- 离线 SID 检索：SnapLGR（Qwen3-0.6B）相比 T5 baseline，Pass@32 提升 2.27 倍，Recall@32 提升 2.40 倍。
- 线上 7 天 A/B 测试：相比 TIGER 式 T5 基线，观看时长 +0.37%，时长 +0.09%，深度会话 +0.18%，深度会话独立用户 +0.11%，全部显著。
- 消融发现：decoder-only 架构是最大增益来源（13M 时即领先 T5 1.51× Pass@32），模型缩放与预训练 CPT 提供次要但稳定的增益。
