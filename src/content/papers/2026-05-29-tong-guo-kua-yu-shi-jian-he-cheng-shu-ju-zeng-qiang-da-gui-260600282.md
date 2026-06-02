---
title: Synthetic Data from Cross-Domain Events for Large-Scale Recommendation Systems
title_zh: 通过跨域事件合成数据增强大规模推荐系统
authors:
- Xiangyu Wang
- Yawen He
- Shivendra Pratap Singh
- Han Huang
- Mengtong Hu
- Sharath Ciddu
- Yi-Hsuan Hsieh
- Erik Groving
- Yi Ding
- Jieming Di
affiliations:
- Meta
arxiv_id: '2606.00282'
url: https://arxiv.org/abs/2606.00282
pdf_url: https://arxiv.org/pdf/2606.00282
published: '2026-05-29'
collected: '2026-06-02'
category: RecSys
direction: 跨域合成数据增强推荐
tags:
- synthetic data
- cross-domain recommendation
- data augmentation
- implicit feedback
- scalable recommendation
one_liner: 将跨域交互迁移建模为合成数据生成，以模型无关方式缓解目标域数据稀疏
practical_value: '- 解耦的数据驱动跨域增强：将源域交互转换为目标域格式的合成事件，不侵入下游模型架构，可在多个模型（排序、校准、出价等）间复用同一份合成数据集，显著降低工程耦合。

  - 采样优于确定性Top-K：实验证明从条件概率分布中采样生成合成事件，相比Top-1选择，能覆盖30%的目标物品目录（Top-1仅4%），显著提升多样性和泛化性能；该结论可推广到任何需要合成交互的场景。

  - 分布对齐提升效果：对合成事件按物品价值分桶下采样（bucket-wise downsampling），使其分布匹配原始数据，能带来额外0.13%的相对NE改善；简单有效的后处理trick。

  - 合成数据质量控制：过滤低置信度翻译事件、移除有分布偏移的特征（防止模型利用合成/真实域信息作弊）可提升模型校准度与排序质量，值得在合成数据生产流水线中直接落地。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
大规模推荐系统面临严重的隐式反馈稀疏问题（如转化率常低于1%），传统跨域推荐通过在模型层面共享嵌入或参数来迁移知识，但存在架构耦合、训练耦合和难以扩展至多个下游模型等局限。受LLM中合成数据成功的启发，本文提出将跨域事件迁移重新定义为合成数据生成问题，实现数据级而非模型级的迁移，从而更灵活、模型无关地利用源域丰富信号。

**方法关键点**  
- **两阶段框架SCALR**：第一阶段从源域事件（如浏览、内容互动）频次估计目标域物品的翻译分布 `P(i_T | u, j_S)`，再利用该分布采样生成合成事件；第二阶段下游模型在原始数据与合成数据上联合训练，通过权重 λ 控制合成数据影响。  
- **频次估计与概率采样**：基于跨域重叠用户计算共现条件概率，通过从分布中随机采样（而非确定性Top-K）产生合成事件，保障物品覆盖多样性。  
- **模型无关集成**：合成事件沿用目标域原始格式，任何推荐架构（双塔、Wide&Deep、FM、Transformer）仅需增加一个加权辅助任务即可引入跨域信号，无需改动模型结构。  
- **分布对齐与质量控制**：采用分桶下采样使合成数据价值分布匹配原始分布，过滤低置信度事件并移除泄露域信息的特征，进一步提升效果。

**关键结果**  
- 在工业级推荐平台的在线A/B测试中，SCALR在一主要模型上带来连续多周约0.14%–0.24%的转化率（CVR）提升，统计显著。  
- 离线对比：概率采样（覆盖面30%物品）vs Top-1（覆盖面4%），采样在评估集上相对NE改善0.25%，Top-1几乎无泛化提升；合成数据量增加单调提升效果，但存在收益递减。  
- 分布对齐：分桶下采样带来额外-0.13%相对NE增益，证实匹配原始分布的重要性。
