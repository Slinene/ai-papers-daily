---
title: Claim-Level Reliability Assessment for Efficient Test-Time Reasoning
title_zh: 声明级可靠性评估：高效测试时推理
authors:
- Sen Xu
- Wei Wang
- Shixi Liu
- Jixin Min
- Yingwei Dai
- Zhibin Yin
- Yirong Chen
- Junlin Zhang
affiliations:
- Sina Weibo Inc.
arxiv_id: '2608.11994'
url: https://arxiv.org/abs/2608.11994
pdf_url: https://arxiv.org/pdf/2608.11994
published: '2026-08-12'
collected: '2026-08-13'
category: Reasoning
direction: LLM测试时推理 · 声明级证伪
tags:
- Test-Time Scaling
- Self-Consistency
- Falsification
- Verification
- LLM Reasoning
- Efficiency
one_liner: 提出声明级证伪的测试时计算重分配框架CLR，用关键声明验证替代额外采样，提升推理准确率并节省37% token
practical_value: '- 在Agent多步工具调用或推理链中，不要对整条trace打分，而是先抽取决策关键声明（decision-critical claims）进行定向验证，可避免常规token噪声稀释错误信号，提高错误步骤召回率。

  - 利用“构造难、证伪易”不对称性：对候选答案做语义证伪而非整体重生成，通过查找单点致命矛盾淘汰错误候选，比多数投票更省token且更准；可应用于排序/召回中的多候选融合。

  - 推理服务资源受限时，把额外算力从“多采样”转移到“验证器”：用轻量模型或规则对声明级证据做检查，工程上可获得类似本工作37% token节省，同时准确率提升。

  - 设计非线性可靠性评分抑制高置信错误共识，而不是简单平均置信度；对电商搜索中的query改写、答案生成等场景，可提升最终输出聚合质量。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

## 动机
测试时扩展（test-time scaling）通过增加采样或整体trace评估提升LLM推理能力，但整条trace的评估信号容易被大量routine tokens稀释，难以定位决定性错误。

## 方法关键点
提出声明级证伪（claim-level falsification）原则，并实现无训练的CLR框架：
- **关键声明抽取**：将每条推理trace压缩为紧凑的决策关键声明集合，隔离逻辑锚点。
- **语义证伪**：利用构造与反驳的不对称性——构造正确解需要完整无误推理路径，反驳错误声明只需找到单个致命缺陷。
- **负面证据搜索**：定向搜索矛盾点，压缩高置信错误trace的存活空间，通过非线性可靠性评分抑制错误共识。
- **计算重分配**：将测试时计算从额外采样转向针对性验证，降低总token消耗。

## 关键结果
在4个LLM与4个推理基准、匹配预算条件下，CLR普遍优于pass@1和self-consistency。在GPT-OSS-20B/CMIMC25上，CLR比pass@1高27.15个百分点，将self-consistency准确率从77.50%提升至82.19%，同时节省37.0% token。
