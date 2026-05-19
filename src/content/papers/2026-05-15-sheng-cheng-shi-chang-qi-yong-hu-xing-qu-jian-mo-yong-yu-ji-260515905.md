---
title: Generative Long-term User Interest Modeling for Click-Through Rate Prediction
title_zh: 生成式长期用户兴趣建模用于点击率预估
authors:
- Jiangli Shao
- Kaifu Zheng
- Hao Fang
- Huimu Ye
- Zhiwei Liu
- Bo Zhang
- Shu Han
- Xingxing Wang
affiliations:
- MeiTuan
arxiv_id: '2605.15905'
url: https://arxiv.org/abs/2605.15905
pdf_url: https://arxiv.org/pdf/2605.15905
published: '2026-05-15'
collected: '2026-05-19'
category: RecSys
direction: 生成式长期用户兴趣建模
tags:
- CTR Prediction
- User Interest Modeling
- Generative Retrieval
- Long-term Behavior
- Industrial Recommender System
one_liner: 提出生成式长期兴趣模型GenLI，用目标无关的生成分布代替目标中心检索，实现兴趣多样性和效率提升
practical_value: '- **生成式兴趣分布替代目标中心检索**：业务中可借鉴IGM思想，用近期行为生成多类兴趣向量（显式、隐式、相对），再通过哈希查表选择长期行为，避免每次请求都与全量行为做相似度计算，大幅降低线上延迟。

  - **多兴趣分布设计提升推荐多样性**：显式/隐式/相对三种分布的监督信号（点击行为、曝光行为、差值）可迁移到电商推荐或广告中，帮助显式刻画短期、隐式刻画长期、相对趋势捕捉兴趣变化，增强召回或排序阶段的多样性。

  - **行为检索的O(1)查分方式**：将离散兴趣分布与行为ID取模后直接查概率，可作为轻量级GSU部署，尤其适合物料数海量、行为序列超长的场景，比SIM/ETA的复杂哈希或内积更省资源。

  - **端到端可插拔框架**：GenLI作为即插即用的长期兴趣模块，可嵌入现有CTR模型，工程上只需在损失函数中加入显式/隐式兴趣辅助损失（标签来自点击或曝光项），线上部署改动小，A/B测试证实RPM提升1.5%+。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
长期用户兴趣建模是CTR预估的核心，但主流二阶段框架（GSU + ESU）存在三个缺陷：GSU仅关注与目标相关的行为，丢失多样兴趣；匹配式检索需对每个历史行为计算相似度，耗时随序列增长；成对比较忽略行为间交互，导致兴趣刻画不准确。为此，论文首次将生成式方法引入长期兴趣建模。

**方法关键点**
- **兴趣生成模块（IGM）**：用多头注意力处理最近${l}$个短期行为，生成三个${N}$维离散兴趣分布——显式兴趣（以点击项为标签）、隐式兴趣（以曝光项为标签）和相对兴趣（显式减隐式），目标无关，全面反映实时兴趣。
- **行为检索模块（BRM）**：将行为ID对${N}$取模，直接从分布中查得分数，选各分布top-${k}$行为，复杂度${O(1)}$，总复杂度${O(L+(l+K)d_h)}$，远低于SIM/TWIN的${O(L d_h)}$。
- **兴趣融合模块（IFM）**：对三种检索出的行为分别用目标注意力聚合，再通过门控机制融合成长期兴趣特征。
- **训练**：端到端学习，联合CTR损失与显式/隐式兴趣损失。

**关键结果**
- 公开数据集：Amazon Books 上 AUC 达0.7564（+0.61% vs TWIN），TaoBao 上达0.9552（+1.03% vs TWIN）。
- 工业数据集：AUC 0.7463，比最佳基线高0.22%，且推理耗时仅4.6ms，低于TWIN的7.9ms。
- 在线A/B：CTR提升0.776%，RPM提升1.567%，已部署服务亿级用户。
- 消融实验证实三种兴趣分布均有效，缺少显式兴趣影响最大；GenLI在更少检索行为数时优势更显著，验证了目标无关检索的全面性。

> 生成式建模不再“为每个目标去检索”，而是先画出用户当下的兴趣图谱，再按图索骥——这让兴趣特征更完整，也让检索从全量比较蜕变为一次查表。
