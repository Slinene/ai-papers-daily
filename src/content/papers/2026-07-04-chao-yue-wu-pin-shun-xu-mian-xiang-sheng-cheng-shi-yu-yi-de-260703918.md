---
title: 'Beyond Item Order: Temporal Gap Tokenization for Generative Recommendation
  with Semantic IDs'
title_zh: 超越物品顺序：面向生成式语义ID推荐的时间间隔分词
authors:
- Chengkai Huang
- Tianqi Gao
- Hongtao Huang
- Quan Z. Sheng
- Lina Yao
affiliations:
- University of New South Wales
- Macquarie University
- CSIRO's Data61
arxiv_id: '2607.03918'
url: https://arxiv.org/abs/2607.03918
pdf_url: https://arxiv.org/pdf/2607.03918
published: '2026-07-04'
collected: '2026-07-07'
category: GenRec
direction: 生成式推荐 · 时序建模
tags:
- Semantic IDs
- Generative Recommendation
- Temporal Gap
- Tokenization
- Sequential Recommendation
- Time-Aware
one_liner: 提出 ChronoSID，通过在物品表征学习和序列生成中注入离散时间间隔令牌，显著提升语义ID生成式推荐效果
practical_value: '- 将交互间隔按 log-scale 离散为固定桶（<1h, 1h~1d, 1d~1w, 1w~1mo, ≥1mo）作为特殊 token
  插入编码器输入，解码器不变，工程改动小，可直接增强现有语义ID生成式推荐模型。

  - TA-FAMAE 在物品表征训练中增加辅助时间间隔回归任务，可作为正则项迁移到基于掩码自编码的商品 embedding 预训练中，在不改动线上推理的前提下提升序列建模对时间漂移的鲁棒性。

  - 间隙 token 注入策略对编码器长度仅增加 1/3，训练开销可控（训练时间增幅 7%~29%），适合电商场景下的大规模序列建模。

  - 长间隔场景（如≥1个月回访）推荐质量提升更明显，特别适合电商中促销召回、换季推荐等用户兴趣易漂移的场景，可作为召回粗排环节的时序增强插件。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
当前基于语义 ID（Semantic IDs）的生成式推荐将用户历史处理为静态物品编码序列，完全忽略交互间的时间间隔。然而，用户行为连续性随时间衰减：同一类别复购率随间隔增加显著下降，且跨品类衰减模式普遍存在。这种“时间盲视”导致模型无法区分密集连续浏览与长期回归后需求变化的差异，限制了生成式推荐在兴趣漂移场景下的表现。  

**方法关键点**  
1. **两阶段时序注入**：ChronoSID 在不改变量化阶段的前提下，分别在物品表征学习和序列生成两个层面引入时间信息。  
2. **TA-FAMAE（Time-Aware Field-Aware Masked Auto-Encoding）**：在物品表征训练时，对目标物品的屏蔽字段重建损失中增加辅助头，预测该物品与前一交互的对数时间间隔，以 0.1 权重正则化，使表征天然携带时序可预测性。  
3. **间隙令牌离散化与交替插入**：将历史交互间隔按 log-scale 离散为 5 个固定桶（<1h, 1h-1d, 1d-1w, 1w-1mo, ≥1mo），并与特殊起始令牌共同构成 gap tokens。在 T5 编码器输入中，按“gap token → 物品3级语义ID”的交替序列拼接，每物品增加 1 token，使编码器直接感知时序节奏，而解码器仍仅生成物品语义ID。  
4. **管道兼容性**：物品量化沿用 ReSID 的 GAOQ（全局对齐正交量化），保证实验控制变量，仅替换编码器输入结构。  

**关键实验**  
- 在 Amazon-2023 的 8 个子集（Musical Instruments, Video Games, Industrial Scientific, Baby Products, Arts Crafts Sewing, Sports Outdoors, Toys Games, Beauty Personal Care）上评测。  
- ChronoSID 在所有数据集上超越 TIGER、LETTER、EAGER、UNGER、ETEGRec 及最强基线 ReSID，例如在 Musical Instruments 上 Recall@5 从 0.0388 提升至 0.0417，NDCG@10 从 0.0325 提升至 0.0346；Video Games 上 Recall@10 从 0.0898 提升至 0.0927。  
- 消融显示：仅加 gap tokens 已带来主要增益，TA-FAMAE 提供额外小幅正则贡献；长间隔（>1周）测试实例上 ChronoSID 相对提升更显著，验证了对兴趣漂移场景的有效性。  
- 效率方面，训练开销较 ReSID 增加 7%~29%，推理每样本延迟仍控制在毫秒级，可接受。  

**一句话结论**  
时间间隔令牌化是一种低成本、高收益的时序增强方案，值得在生成式语义ID推荐流程中即插即用。
