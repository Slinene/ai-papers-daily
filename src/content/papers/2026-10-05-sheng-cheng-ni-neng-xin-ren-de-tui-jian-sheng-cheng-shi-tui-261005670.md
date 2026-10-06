---
title: 'Generate What You Can Trust: Content Credibility in Generative Recommenders'
title_zh: 生成你能信任的推荐：生成式推荐中的内容可信度
authors:
- Zhuo Cai
- Guanghao Wu
- Shoujin Wang
- Peilin Zhou
- Victor W. Chu
affiliations:
- University of Technology Sydney
- New York University Abu Dhabi
arxiv_id: '2610.05670'
url: https://arxiv.org/abs/2610.05670
pdf_url: https://arxiv.org/pdf/2610.05670
published: '2026-10-05'
collected: '2026-10-06'
category: GenRec
direction: 生成式推荐 · 可信度约束
tags:
- Generative Recommendation
- Semantic ID
- Discrete Diffusion
- Content Credibility
- RQ-VAE
- Fake News
one_liner: 提出 CreGR，通过可信度感知 tokenizer 和离散扩散非对称掩码策略，在保持生成精度的同时显著降低不可信内容曝光
practical_value: '- 在商品/内容 Semantic ID 构建中，把 LLaMA/BERT 内容 embedding 与 SASRec/双塔协同
  embedding 拼接后再做 RQ-VAE，可显著降低 token collision；电商场景可将标题、描述与行为 embedding 融合，得到更具辨识度的
  SID。

  - 如果业务要抑制低质/违规内容又不想牺牲用户兴趣信号，可借鉴「非对称掩码」：离散扩散训练时只降低不可信 item 最后一个 token 的 mask 概率，前序
  topical token 保持不动；hard 版直接置 0，soft 版按 token 到可信/不可信簇中心的距离加权。

  - 有内容质量/安全标签时，可在 RQ-VAE 损失中加入可信度正则：把隐向量投影到专用子空间，做类内紧凑、类间分离，避免相似主题但真伪不同的内容共享 SID
  token。

  - 评估侧可引入 CR@N（推荐列表可信占比）和 HC@N（HR 与 CR 的平衡指标），作为线上负责任推荐的辅助监控；论文显示 15% 标签噪声下 CR@5
  仅轻微下降，方案对标签噪声有一定鲁棒性。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：生成式推荐用 Semantic ID 直接生成物品 token，但现有方法只优化准确率，忽略内容可信度，可能推荐 fake news 或健康 misinformation，带来用户不信任和平台声誉风险；已有可信推荐方法都停留在 embedding matching，无法迁移到生成式推荐。

**方法关键点**：
- 可信度感知 tokenizer：用 LLaMA2-7B 编码标题/描述，拼接 SASRec 协同 embedding 后输入 RQ-VAE；新增 credibility regularization，在专用子空间促使可信/不可信物品类内紧凑、类间分离，避免事实相悖内容共享 token。
- 精度保持的可信度导向生成器：基于离散扩散，提出非对称掩码概率降低策略，只对不可信物品最后一个 token 降低 mask 概率，保留前序 topical token；hard 版 wi=0，soft 版用 token 到可信/不可信簇中心距离的 sigmoid 加权。
- 训练目标结合历史可信度损失和目标可信度损失；推理用离散扩散 beam search 生成 top-N。

**关键实验**：在 PolitiFact、GossipCop、MHMisinfo 三个带可信度标签的真实交互数据集上，对比 TIGER、LETTER、LLaDA-Rec、Disco 等 baseline。CreGR 在 CR@5/CR@10 和 HC@5/HC@10 上全面最优，例如 PolitiFact CR@5 达 0.9855（soft）/0.9959（hard），GossipCop HR@5 0.5855、NDCG@5 0.4984 仍保持最优或次优；同时 token collision 率降到 0% 左右，15% 标签噪声下 CR@5 仅从 0.9855 降至 0.9780。

**最值得记住的一句话**：可信度不应该靠后置过滤，而应嵌入生成式推荐的两个核心阶段——token 化阶段解耦可信信号，生成阶段只压制不可信 item 的末尾 token，不牺牲用户的 topical 兴趣。
