---
title: 'Mind the Gap: Bridging Behavioral Silos with LLMs in Multi-Vertical Recommendations'
title_zh: 弥合行为孤岛：利用LLM提升多垂域电商推荐冷启效果
authors:
- Nimesh Sinha
- Raghav Saboo
- Martin Wang
- Sudeep Das
affiliations:
- DoorDash Inc.
arxiv_id: '2606.06779'
url: https://arxiv.org/abs/2606.06779
pdf_url: https://arxiv.org/pdf/2606.06779
published: '2026-06-04'
collected: '2026-06-08'
category: RecSys
direction: 多垂直推荐 · LLM特征工程
tags:
- Multi-Vertical Recommendation
- LLM
- Cold-Start
- Hierarchical RAG
- Feature Engineering
- MTL
one_liner: 用分层RAG从富数据垂域推断用户分类偏好特征，注入排序模型解决冷启问题
practical_value: '- **LLM作语义特征提取器**：对用户餐厅订单与搜索等非结构化行为序列，通过分层RAG生成四层商品分类（L1-L4）的偏好特征，作为稠密用户画像直接注入排序模型，可迁移至电商多品类推荐冷启场景。

  - **分层推理 + 置信度过滤**：采用 cascade inference 从粗到细约束生成空间，设置 temperature=0.1、置信度阈值 0.8
  并强制只输出预定义分类节点，显著减少幻觉并保证特征一致性，该 prompt 设计方法可直接复用。

  - **工程降本关键措施**：prompt caching 将指令与全量分类静态部分缓存，仅追加动态行为序列；按用户新行为触发 just-in-time 特征更新，综合降低
  LLM 调用成本约 80%。

  - **MTL 特征接入方式**：将变长 taxonomy ID 列表经共享 embedding 表映射后做 mean pooling，再与已有 user/item
  特征拼接送入共享 MLP trunk，实现即插即用，不改变模型结构即带来全人群 AUC 相对提升 4.4%。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：多垂域电商平台（如 DoorDash）在杂货、零售等新兴品类面临严重的用户冷启问题，缺乏行为数据导致推荐不相关。与此同时，成熟垂域（如餐饮）积累了丰富的用户历史行为和偏好信号。本文提出利用 LLM 从富数据垂域迁移知识，通过生成结构化的分类偏好特征来桥接行为孤岛。

**方法关键点**
- **分层 RAG 特征合成**：基于内部四级商品分类体系，构建 cascade 推断流程：先识别粗粒度（L1/L2）偏好，再约束搜索空间生成细粒度（L3）分类，避免幻觉。融合餐厅订单（长期偏好）和搜索记录（短期意图）两类信号。
- **Prompt 工程**：设置 temperature=0.1，要求模型输出置信度≥0.8 的分类，仅允许使用预定义 taxonomy；按时间序列排列用户行为，帮助模型捕捉动态偏好；对 prompt 进行缓存优化（静态部分缓存）。
- **特征集成**：LLM 生成的 L2/L3 分类列表经共享 embedding + mean pooling 转化为固定维向量，与已有用户-物品特征拼接，输入 MTL 排序模型。模型为多目标（点击、加购、购买）联合学习，共享底层 MLP 后接 task-specific heads。
- **工程实现**：每日离线批处理计算特征，存入数据湖用于训练，同时写入在线特征存储供实时推断；采用 prompt caching 和按需更新使成本下降约 80%。

**关键实验**
- 离线评估：3 个月训练数据，15 天 holdout，对比基线 MTL 排序模型（仅用历史行为与物品特征）。
  - 全人群：AUC-ROC 相对提升 4.4%，MRR 提升 4.8%。
  - 冷启用户（新垂域无行为）：AUC-ROC 提升 4.0%，MRR 提升 1.1%。
  - 高活用户：AUC-ROC 提升 5.2%，MRR 提升 2.2%（搜索信号贡献最大）。
- 在线影子部署：全人群 AUC-ROC 提升 4.3%，MRR 提升 3.2%，与离线一致。
- 特征质量评估：人工评估显示搜索衍生特征个性化程度更高（高度个性化 70.7% vs. 订单 53.0%），LLM 法官评估趋势相同。

**核心启示**：LLM 可作为跨领域语义桥梁，将非结构化行为数据提炼为高保真、可复用的结构化偏好特征，低成本解决推荐系统冷启与知识迁移难题。
