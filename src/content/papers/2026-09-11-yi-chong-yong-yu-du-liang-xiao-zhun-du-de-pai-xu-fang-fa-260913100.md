---
title: A Ranking Approach for Measuring Calibration
title_zh: 一种用于度量校准度的排序方法
authors:
- Anirban Chatterjee
- Rina Foygel Barber
affiliations:
- Boston University
- University of Chicago
arxiv_id: '2609.13100'
url: https://arxiv.org/abs/2609.13100
pdf_url: https://arxiv.org/pdf/2609.13100
published: '2026-09-11'
collected: '2026-09-14'
category: Eval
direction: 模型校准度量 · rankECE
tags:
- calibration
- rankECE
- model evaluation
- probabilistic forecast
- ranking
one_liner: 提出 rankECE，基于相邻预测概率比较的校准误差度量，比常用分箱 ECE 近似更准确
practical_value: '- 在广告/推荐系统的 CTR、CVR 预估中，模型概率校准直接影响竞价与排序；现有校准评估常用分箱 ECE，但分箱宽度和边界选择会影响结论。rankECE
  基于相邻点比较，无需设置分箱，更适合在线模型监控和 A/B 测试中的校准对比，尤其当正样本稀疏时。

  - 可以将其作为离线评估流程的补充指标，与 AUC、LogLoss 一同监控校准质量；实现时可将预测分数排序后计算相邻点差异的加权平均，工程上容易对接现有特征和标签存储。

  - rankECE 对局部校准偏差更敏感，适合发现模型在特定预测概率区间（如高点击率头部流量）的系统性偏误，便于业务方定位问题。

  - 注意该度量最初针对二分类概率校准，如果推广到多分类或 Learning-to-Rank 场景需要适配，例如对每个类或每个位置计算局部校准。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：概率预测的校准性对下游决策至关重要，但常用的 ECE 在无假设条件下无法保证精确估计，实际中常用的分箱近似 ECE 存在偏差且依赖分箱选择。

方法：rankECE 不依赖固定分箱，而是基于排序相邻点的预测概率比较来度量校准误差。具体做法是比较每个样本与其邻近样本的预测概率和真实标签的一致性，利用局部秩信息构造统计量。理论分析给出 rankECE 与 ECE 的界限，证明其在较弱假设下能更好代理真实 ECE。

结果：实验在模拟和真实数据上验证，rankECE 比常用的分箱 ECE（如等宽分箱、等频分箱）更准确、更稳健，特别是在样本量较小或数据分布不均时优势明显。rankECE 提供了一种更可靠的校准度量替代方案，减少了对分箱超参数的敏感度。
