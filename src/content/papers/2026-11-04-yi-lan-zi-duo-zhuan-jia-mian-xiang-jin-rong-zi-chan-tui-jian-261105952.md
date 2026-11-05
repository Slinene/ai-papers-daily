---
title: 'One Basket, Many Experts: Decorrelated Re-ranking for Financial Asset Recommendation'
title_zh: 一篮子多专家：面向金融资产推荐的去相关重排序
authors:
- Ryuki Unno
- Keigo Sakurai
- Koshi Watanabe
- Keisuke Maeda
- Takahiro Ogawa
- Miki Haseyama
affiliations:
- Hokkaido University
arxiv_id: '2611.05952'
url: https://arxiv.org/abs/2611.05952
pdf_url: https://arxiv.org/pdf/2611.05952
published: '2026-11-04'
collected: '2026-11-05'
category: RecSys
direction: 金融资产推荐 · 去相关后处理重排序
tags:
- Financial Recommendation
- Re-ranking
- Diversification
- Risk-Adjusted Return
- Relevance-Performance Tradeoff
one_liner: 提出 DSER 后处理重排序，保留高相关推荐并用去相关资产替换部分槽位，将相关性-收益权衡显式化为可调参数 m
practical_value: '- 把业务目标（GMV、收入、退货率、长期用户价值等）拆成显式可调的后处理重排 knob，而不是混进排序模型 loss。设置替换槽位数
  m，运营/产品可直接读取相关性-业务指标 trade-off 曲线，审计友好，便于策略调整。

  - 对推荐列表高度集中在热门、同质化商品的场景（电商爆款、广告大盘），可采用 satellite 替换策略：保留 top-k 高相关结果，其余用与头部低相关但业务指标更优的商品替换，提升列表整体业务价值；替换对象可以按与已选集合的相关性、期望收益贡献进行贪心或打分选择。

  - 后处理重排模块与既有排序模型解耦，无需重新训练，适合快速上线和 A/B 测试；可离线在不同 m 下评估相关性损失和业务指标增益，再设定运营区间，降低风险。

  - 论文指出收益来源并非低波动而是高回报高波动资产，这提醒在电商多样化中需区分“降低同质化风险”和“引入高潜力但高波动商品”，避免盲目最小化相似度而忽略业务收益来源。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：金融资产推荐通常只优化相关性，即推荐用户会购买的资产；但服务商还关心推荐篮子整体的风险调整收益，这影响用户参与和费用收入。高相关推荐往往集中在少数热门资产，这些资产收益高度相关，限制了风险调整收益的上限，导致相关性与收益目标难以同时达到。

**方法关键点**：提出 Decorrelated-Satellite Expert Re-ranking（DSER），将推荐列表分成两部分：保留来自专家跟随列表的最相关推荐，其余槽位用收益去相关的替代资产替换。替换槽位数 m 是服务商设定的单一整数旋钮，使相关性-收益权衡成为显式、可审计的选择，而不是隐藏在模型中。该方法本质是后处理重排，与原有排序模型解耦。

**关键结果**：在公开 FAR-Trans 零售经纪数据集上，替换少量槽位就能在轻微相关性损失下提升风险调整收益，且收益在现实交易成本和典型零售组合规模下仍然存在。作者发现，最小化相关性本应降低组合波动，但数据中最低相关资产反而波动更大、收益更高，因此收益主要来自高回报而非低波动。权衡不对称：相关性成本在不同市场阶段保持一致，而收益依赖于阶段。
