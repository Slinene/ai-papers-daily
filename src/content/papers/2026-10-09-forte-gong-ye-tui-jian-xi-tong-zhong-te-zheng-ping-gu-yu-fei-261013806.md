---
title: 'FORTE: A Production Framework for Feature Evaluation and Deprecation in Industrial
  Recommender Systems'
title_zh: FORTE：工业推荐系统中特征评估与废弃的生产框架
authors:
- Vishnu Arun
- Adam Obeng
- Tianyou Wang
- Zilin Ren
- Mukuntha Narayanan Sundararaman
- Han Wang
- Shivin Thukral
- Zhixiang Wang
- Saurabh Vishwas Joshi
- Darren Reger
affiliations:
- Pinterest
arxiv_id: '2610.13806'
url: https://arxiv.org/abs/2610.13806
pdf_url: https://arxiv.org/pdf/2610.13806
published: '2026-10-09'
collected: '2026-10-12'
category: RecSys
direction: 推荐系统特征生命周期管理与模型降本
tags:
- Feature Deprecation
- Feature Importance
- Perturbation
- A-B Testing
- Model Efficiency
- Industrial Recommender Systems
one_liner: 模型无关的特征废弃框架，用高效扰动、分组验证、在线A/B和血缘追踪实现安全删除特征
practical_value: '- **用 pooled perturbation 替代逐特征推理**：把原始 batch 和扰动 batch 一次加载进内存，每个实验只做一次字典选择，边际成本极低；在
  3M 行数据上 300 个实验耗时从线性降低 54 倍，可以支撑每日全模型特征重要性扫描。

  - **候选特征集必须做 grouped perturbation**：单特征 permutation 会高估可加价值，且特征交互导致固定顺序边际中有相当比例（38.6%）为负；只筛选单特征重要性会漏掉交互依赖，上线前必须对嵌套候选集做联合扰动验证。

  - **单 permutation 在 150k 样本规模下已足够稳定**：重复 permutation 只带来方差线性下降，而扩大样本量直接缩小 σ²；若目标是特征排序而非精确重要性值，把算力投向更有代表性的样本比重复
  permutation 更划算。

  - **完整特征废弃依赖 lineage 追踪**：只从模型删除特征收益有限，必须通过 registry 找到所有下游消费者，逐级 block dataloader、dataset、ingestion、logging，才能实现存储、训练、服务端到端节省。

  - **在线 guardrail 是最终裁决**：离线 neutral 的多个候选集，最激进的组合可能触发次要指标回归；应让多个 nested 候选集同时进入
  A/B，由在线护栏筛选安全操作点，而不是依赖离线指标定最终规模。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
生产推荐系统存在特征生命周期不对称：加特征只需提升某个指标，删特征却必须保证所有指标不回归。由于特征交互、数据漂移、A/B 带宽争夺、多模型协调等原因，特征废弃很难被优先处理，导致无效特征长期残留，白白消耗训练、存储和推理成本。真正瓶颈是有限的在线 A/B 带宽。

**方法关键点**
- **时序特征重要性**：每日运行 perturbation，结合均值、排名稳定性和拟合斜率生成候选集，默认条件保守，需跨所有输出头和窗口通过。
- **高效扰动实现**：Dataset Virtualization + Pooled Execution，一次 materialization 服务所有扰动实验；对 dense/sparse/ragged 类型做类型感知的 permutation 和 ablation。
- **分组扰动**：对嵌套候选集做联合扰动，捕捉特征交互；固定顺序边际与 order-averaged Shapley 估计用于诊断排序敏感性，但不作为生产阶段。
- **单 permutation 方差控制**：基于 ROC-AUC 的 bounded-differences 证明 σ² = O(1/n)，经验验证 150k 样本单 permutation 的特征排序已足够稳定，建议 R=1，把算力用于更大样本。
- **血缘追踪与废弃**：维护实时 feature-model mapping，确定特征无下游模型引用后，分阶段 block dataloader → dataset → ingestion → logging 完成下线。

**关键实验**
- 在 Search Relevance 模型上，111 个特征中筛选出 3 个嵌套候选集（32/48/59 特征），离线全中性，但在线最大组触发次要指标回归；最终去除 48 个特征，即 43.2% 特征量，serving throughput 提升 2%，参数减少 2.3%。
- 在大型 Pin Ranker 上，去除 8 个特征后，trainable parameters 减少 29.9%，serving throughput 提升 19.8–25.5%，推断成本下降约 10%，年训练成本节省数十万美元。
- 运行时：pooled execution 使 300 个实验耗时减少 54×，运行时间随实验数增长仅为 N^0.20~N^0.27，而非线性。
- 189 个特征组的 grouped perturbation 显示，38.6% 的固定顺序边际为负，individual deltas 高估可加价值；order-averaged 总效应精确（SE 0.008%），但单个特征份额识别不稳定。

**最值得记住的一句话**：特征废弃的瓶颈不在计算重要性，而在 A/B 带宽稀缺，因此需要用廉价的离线扰动把候选集缩到足够小，再用在线实验做最终安全裁决。
