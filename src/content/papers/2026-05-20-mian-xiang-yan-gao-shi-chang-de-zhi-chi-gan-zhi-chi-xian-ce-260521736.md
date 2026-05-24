---
title: Support-aware offline policy selection for advertising marketplaces
title_zh: 面向广告市场的支持感知离线策略选择框架
authors:
- Prashant Shekhar
- Caroline Howard
affiliations:
- Embry-Riddle Aeronautical University, Daytona Beach, FL, USA
arxiv_id: '2605.21736'
url: https://arxiv.org/abs/2605.21736
pdf_url: https://arxiv.org/pdf/2605.21736
published: '2026-05-20'
collected: '2026-05-24'
category: RecSys
direction: 广告保留价策略的离线认证选择
tags:
- offline policy evaluation
- reserve price
- support-aware
- statistical certification
- ad marketplace
- replay methods
one_liner: 提出支持感知的离线决策框架，输出认证策略与验证候选，而非单纯的点估计排名
practical_value: '- 离线评估时不要只看平均收益提升，必须检查各细分群体（商户、地域等）是否无害，避免子群损害。

  - 引入支持度门控和统计显著性检验，过滤因样本不足或随机波动造成的伪优策略，降低多重比较风险。

  - 输出认证候选集而非单一最佳策略，引导在线做小流量验证，类似推荐系统中的`safe policy rollout`。

  - 评估中应考虑异质性反应，即不同广告主或用户对策略变化的响应可能逆转整体排名，可仿照按维度分组做敏感性分析。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：广告平台常用离线重放评估保留价策略，但依靠点估计挑选最优策略存在风险，包括弱阈值支持、多重比较陷阱、子群损害和投标人响应不确定性。现有方法仅提供估值或排序，缺乏支撑在线验证的决策依据。

**方法**：提出支持感知的离线决策框架。输入日志和策略目录，通过支持门控剔除数据支持不足的策略，再对剩余策略进行同时不确定性控制和统计主导检验，最终输出三类决策：认证通过策略、被统计主导的淘汰策略、以及需进一步在线验证的未解决候选。理论给出有限策略目录的统一保证：框架以高概率保留最佳通过门控的策略，仅消除具有可认证遗憾的策略。同时界定了支持局部化的重放泛化边界和信息论阈值分辨率极限。

**结果**：在iPinYou实时竞价数据集上，该框架将19种备选保留规则缩减为2条验证候选。冠军规则在第二季中获得47.66%的重放提升率，40.71%的同时下界提升率，第三季冻结验证中得到43.87%的重放提升率。并且在44个广告商、交易所和地区细分中认证无伤害。
