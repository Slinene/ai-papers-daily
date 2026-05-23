---
title: 'TransitLM: A Large-Scale Dataset and Benchmark for Map-Free Transit Route
  Generation'
title_zh: TransitLM：大规模无地图公交路线生成数据集与基准
authors:
- Hanyu Guo
- Jiedong Yang
- Chao Chen
- Longfei Xu
- Kaikui Liu
- Xiangxiang Chu
affiliations:
- AMAP, Alibaba Group
arxiv_id: '2605.22355'
url: https://arxiv.org/abs/2605.22355
pdf_url: https://arxiv.org/pdf/2605.22355
published: '2026-05-20'
collected: '2026-05-23'
category: Other
direction: 无地图公交路线端到端生成
tags:
- route generation
- public transit
- LLM
- dataset
- end-to-end
- sequence generation
one_liner: 发布1300万条公交路线记录的数据集，LLM训练后可直接从起终点生成结构化路线，无需地图或路由引擎
practical_value: '- 数据驱动的端到端路径生成模式可迁移至电商物流场景：用历史订单中的配送序列训练模型，跳过传统地图API和图搜索，直接生成包裹路由。

  - 大规模序列数据预训练能隐式学习网络拓扑和转移规律，类似于推荐系统中从用户行为序列学习物品间的转移概率，可用于下次点/线路的预测。

  - 模型将GPS坐标隐式映射到站点/门店的能力可用于处理用户模糊输入，减少精确地址解析依赖，提升抗干扰性。

  - 路线生成评估时需同时检查结构有效性、换乘次数、绕路比例等多维度指标，可借鉴论文提出的互补评估框架设计业务指标。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：传统公交路线规划依赖结构化地图和复杂路由引擎，而海量历史路线记录中隐含着丰富的换乘、站点偏好等知识，但缺乏能直接训练LLM生成路线的大规模数据。

**方法**：构建TransitLM数据集，包含4个中国城市（北京、上海、广州、深圳）超过1300万条真实公交规划记录，覆盖12万+站点、1.3万+线路。数据以text-to-text格式组织，输入为起终点GPS坐标，输出为完整公交路线序列（含上车、换乘、下车）。将LLM在该数据集上进行持续预训练，然后微调或在提示中引导生成。评估覆盖三种任务：标准路线生成、换乘感知生成、灵活偏好生成，同时考察结构有效性、换乘合理性、整体质量。

**关键结果**：经过TransitLM训练的模型在路线结构有效性上达到很高准确率，且能自动将任意GPS坐标隐式映射到实际站点，无需显式地图匹配。相比通用LLM，幻觉率大幅降低，证明完全从数据中学习公交路线规划是可行的。
