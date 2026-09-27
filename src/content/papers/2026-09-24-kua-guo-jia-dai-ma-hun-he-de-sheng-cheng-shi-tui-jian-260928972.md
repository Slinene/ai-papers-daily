---
title: Cross-Country Code-Mixing for Generative Recommendation
title_zh: 跨国家代码混合的生成式推荐
authors:
- Yuan Gao
- Hao Deng
- Haibo Xing
- Yi Xu
- Lingyu Mu
- Jinxin Hu
- Yu Zhang
- Xiaoyi Zeng
affiliations:
- Alibaba International Digital Commerce Group
arxiv_id: '2609.28972'
url: https://arxiv.org/abs/2609.28972
pdf_url: https://arxiv.org/pdf/2609.28972
published: '2026-09-24'
collected: '2026-09-27'
category: GenRec
direction: 生成式推荐 · 跨国家 code-mixing
tags:
- Generative Recommendation
- Cross-Country
- Code-Mixing
- Semantic Codebook
- Sequential Recommendation
- Data Augmentation
one_liner: 将多语言 code-switching 思想迁移到跨国家生成式推荐，用 token 级双约束替换和上下文自适应重加权，使小市场显著受益
practical_value: '- 跨市场 ID 隔离时，先建共享语义 codebook（多模态内容 + 跨国家行为 i2i 采样 softmax + RQ-VAE），再在
  token 级做数据增强；这比直接替换 item ID 更可控，适合跨境电商/广告召回。

  - 替换条件要叠加“静态语义”和“动态市场属性”：token Hamming 距离约束捕获协同结构，价格/热度/受众按国家分位桶化后余弦相似度捕获市场适配；只靠内容相似会掉点。

  - 对合成样本引入 stop-gradient 上下文权重 w=Pθ(y''|x)/(Pθ(y|x)+Pθ(y''|x))，训练中原序列做分母，可自动降低不合语境的替换；默认
  p=10%、k=10%、λ=0.5 有较好鲁棒性。

  - 上线指标参考：离线看国家分层平均，A/B 全量 10% 流量得到广告收入 +1.77%、订单 +2.64%，适合直接作为跨市场生成式推荐 ROI 预期。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

动机：跨境电商平台通常为每个国家独立建模，用户/物品 ID 完全隔离，传统跨域推荐依赖的共享用户或物品重叠不存在。生成式推荐虽然可以把各国物品映射到统一 token 空间，但训练序列仍按国家切分，跨国家知识只在参数层共享，数据层缺乏混合共现信号，导致大市场无法帮助小市场。该工作借鉴多语言 code-switching 语料，构造跨国家混合序列。

方法关键点：
- 共享语义 codebook：用多模态编码器获得内容嵌入，联合跨国家两塔 i2i 采样 softmax 注入行为共现，再用 RQ-VAE 将物品编码为 length-4 token 序列；该 codebook 同时作为 GR tokenizer 和替换空间。
- 双约束 code-mixing：候选需满足 token Hamming 距离 ≤ τ 且 side info（价格、受众、热度等按国家分位桶化）cosine 相似度 ≥ τ_s；以比例 k 替换原序列与目标中的 token，生成跨国家 twin。
- 上下文自适应重加权：用原序列下模型对替换目标的预测概率计算权重 w=sg[Pθ(y'|x)/(Pθ(y|x)+Pθ(y'|x))]，stop-gradient 避免梯度污染，loss 中自动降权不合语境的混合样本。

关键结果：在 6 国工业广告数据集上，CMRec 相对最佳 baseline GenCDR 平均 Recall@10 +3.01%、Recall@100 +5.27%、NDCG@100 +4.28%；Amazon M2 上 Avg6 Recall@10 +4.02%、Recall@100 +6.04%；小流量国家提升更大。在线 A/B 广告收入 +1.77%、订单 +2.64%。消融显示 token 距离约束贡献最大，去掉后 Recall@100 掉 4.59%；去掉上下文重加权掉 2.27%。

最值得记住：跨国家 shared codebook + token 级双约束替换 + 模型自适应降噪，是打通跨市场生成式推荐的关键。
