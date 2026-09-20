---
title: 'WeVisDoc: From Coverage to Capability for Robust End-to-End Document Parsing'
title_zh: WeVisDoc：从覆盖到能力的鲁棒端到端文档解析
authors:
- Hao Yu
- Kang Liu
- Linnan Zhao
- Jiabo Zhan
- Chong Sun
- Chen Li
- Jing Lyu
affiliations:
- WeChat Vision, Tencent Inc.
arxiv_id: '2609.20423'
url: https://arxiv.org/abs/2609.20423
pdf_url: https://arxiv.org/pdf/2609.20423
published: '2026-09-16'
collected: '2026-09-20'
category: Other
direction: 文档解析 · 数据为中心
tags:
- Document Parsing
- Data-Centric
- Degradation Synthesis
- Diagnostic Clustering
- Robustness
one_liner: 两阶段数据为中心框架用残差聚类诊断定向补强，在多个文档解析基准上领先
practical_value: '- **残差聚类驱动难例挖掘**：Stage II 对 Stage I 解析器的错误在固定视觉-结构簇内做聚类统计，再定向构造或重分配数据预算。推荐/搜索场景可借鉴该思路，将线上
  bad case 按用户意图、query 类型、页面模板等维度聚簇，定位系统化薄弱点后定向补训练数据或调采样权重。

  - **结构保持的退化合成**：通过保持文档结构不变、只合成图像退化（模糊、噪声、透视变形等）来扩展训练分布。在电商场景中，可对商品图、用户上传的实拍图做类似退化增强，提升模型对低质输入（如暗光、遮挡、压缩噪声）的鲁棒性，尤其适合作图质量不稳定的
  UGC 内容。

  - **target-token 预算重分配**：根据诊断结果把有限训练 token 从已饱和区域转移到薄弱区域. 对应到推荐系统训练，可根据验证集分片表现动态调整各数据源的采样比例或训练步数，避免在简单样本上浪费算力。

  - **两阶段数据迭代范式**：Stage I 广覆盖，Stage II 精准补强，形成可复用的数据飞轮。工程上可落地为：先全量构造基线数据, 再通过定期离线评估识别性能洼地，并用自动化诊断报告指导下一轮数据标注与增强，比盲目扩大数据量更高效。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：文档解析需要在多样布局和采集条件下保持稳定，但训练语料偏向常见文档类型和干净数字页面。单纯扩大数据覆盖无法系统化定位并解决解析器的残余弱点。

**方法关键点**：提出两阶段数据为中心框架。Stage I 通过异构数据和结构保持的退化合成，扩大语义、结构、外观三方面覆盖。Stage II 使用留出探针在固定视觉-结构簇内测量 Stage I 解析器的残余错误，基于诊断结果定向构造数据并重分配 target-token 预算。

**关键结果**：WeVisDoc-4B 在 OmniDocBench v1.6 上 Overall 达 95.38，在 PureDocBench 三条轨道的平均 Overall 为 75.54，四个设定均领先比较的端到端解析器。Stage II 相比 Stage I，2B 和 4B 模型在两个基准的 Overall 均有提升，退化轨道增益更大，其中 4B 在 Real Degraded 轨道提升 4.03 分。
