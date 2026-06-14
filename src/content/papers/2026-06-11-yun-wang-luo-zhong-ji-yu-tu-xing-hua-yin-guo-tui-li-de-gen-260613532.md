---
title: Graphical Causal Reasoning for Root Cause Analysis in Cloud Networks
title_zh: 云网络中基于图形化因果推理的根因分析
authors:
- Fabien Chraim
- Dominik Janzing
- John Evans
affiliations:
- Amazon Web Services
arxiv_id: '2606.13532'
url: https://arxiv.org/abs/2606.13532
pdf_url: https://arxiv.org/pdf/2606.13532
published: '2026-06-11'
collected: '2026-06-14'
category: Reasoning
direction: 故障根因分析 · 因果图推理
tags:
- Root Cause Analysis
- Causal Discovery
- Granger Causality
- Cloud Networks
- Graphical Models
- Fault Diagnosis
one_liner: 提出基于Granger因果与条件独立的因果图构建及时间滞后概率推理的根因分析方法，在35个云网络事件上召回率达85.7%
practical_value: '- 因果图构建思路可迁移至推荐系统故障排查：利用Granger因果检验从系统指标时序中发现变量间因果关系，自动化定位根因，减少人工规则维护。

  - 论文提出的时空分组策略与自动化本体可借鉴到电商系统事件关联分析，通过聚合相似实体和事件降低因果图复杂度，提升推理效率。

  - 时间滞后条件概率的推断方法可为在线系统异常检测提供可解释的根因排序，尤其适用于存在传播延迟的微服务链路。

  - 对Agent工作流监控有益：当多Agent交互出现问题时，可借鉴该方法从日志信号中构建因果图，辅助追踪决策级联失败的源头。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：云网络故障会产生大量因果与症状信号混合的时间序列，传统规则驱动的根因分析难以适应动态拓扑和事件关联，需要一种数据驱动、可解释的因果推理方法。

**方法**：
1. 引入时空分组策略和自动化本体，先将高维告警事件降维为少量有意义的实体。
2. 使用二值化时间序列，对每对实体进行双变量Granger因果检验和条件独立性测试，构建有向因果图。
3. 在因果图上为每条边分配时间滞后条件概率，通过图遍历计算各候选根因节点的概率得分，输出排序列表。

**结果**：在35个标注的生产事件中，模型在85.7%的事件中成功召回正确根因，74.3%给出精确匹配。已实际部署并处理超过800个真实事件，获得网络工程师积极反馈。
