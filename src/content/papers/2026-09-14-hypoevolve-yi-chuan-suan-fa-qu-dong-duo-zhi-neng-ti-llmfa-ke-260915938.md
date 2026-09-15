---
title: 'HypoEvolve: Genetic Algorithms Enable Multi-Agent LLMs to Discover Scientific
  Hypotheses'
title_zh: HypoEvolve：遗传算法驱动多智能体LLM发现科学假设
authors:
- Jieyuan Liu
- Mengzhou Hu
- Jefferson Chen
- JungHo Kong
- Pratibha Jagannatha
- Yiming Gao
- Dexter Pratt
- Hsin-Yuan Lee
- Zhiting Hu
- Trey Ideker
affiliations:
- University of California San Diego
- Texas A&M University
- Carnegie Mellon University
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2609.15938'
url: https://arxiv.org/abs/2609.15938
pdf_url: https://arxiv.org/pdf/2609.15938
published: '2026-09-14'
collected: '2026-09-15'
category: MultiAgent
direction: 多智能体遗传算法优化科学假设生成
tags:
- Multi-Agent LLM
- Genetic Algorithm
- Scientific Discovery
- Drug Repurposing
- Population-based Search
one_liner: 用遗传算法协调多智能体LLM，通过种群迭代生成科学假设，在药物重定位评估中DepMap selectivity达0.171
practical_value: '- 多智能体+遗传算法可迁移到广告文案、搜索query、商品描述的生成：把候选文案/query视为种群，多个agent分别负责生成、批判、修改，适应度函数使用CTR、转化率等线上/离线信号，而不仅靠LLM评分。

  - 显式定义协作规则（选择、交叉、变异）可以分离模型能力与协作收益，便于A/B测试不同agent配置；在推荐系统中可固定生成模型，替换协作策略来验证多agent架构的实际价值。

  - 评估设计借鉴外部证据：药物重定位用DepMap/Open Targets等外部数据，业务中可用用户行为日志、搜索点击日志、成交数据作为外部评估，避免仅用LLM
  judge或人工标注。

  - 外部信号做适应度时注意选择偏差和泛化：论文验证了held-out癌症类型上的泛化，业务中可验证创意/query生成在未见过品类/场景上的表现，防止过拟合历史数据。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：科学假设发现需要综合证据、评估、修正，现有系统将多agent与进化搜索结合，但不同协作形式如何影响假设质量尚未明确。需要一个框架保留科学角色并支持组合、修订、保留规则，以分离模型科学能力与协作收益。

**方法关键点**：提出HypoEvolve，将协作显式化为对假设种群的连续更新。使用generation genetic algorithm协调专门化LLM agents，分别负责整合机制论证、重新考虑假设、评估证据与可检验性。每代定义科学判断与新提案如何重塑种群，使协作效果可测试。

**评估**：围绕可解释干预机制的假设，用药物重定位连接靶点级生物学声明，将DepMap和Open Targets适配为互补外部证据度量。在34种癌症类型上与6个基线比较，HypoEvolve两项指标得分最高；DepMap selectivity达到0.171，最强基线为0.115；对单遍生成的提升还泛化到held-out癌症类型。结果表明多智能体遗传算法能超越单个模型，验证了AI研究团队在自主科学中的潜力。
