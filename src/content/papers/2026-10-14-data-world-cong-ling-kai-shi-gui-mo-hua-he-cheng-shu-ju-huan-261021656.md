---
title: 'Data World: Scaling Data Environments from Scratch'
title_zh: Data World：从零开始规模化合成数据环境
authors:
- Zhanli Li
- Zeyuan Xu
- Chaoxu Pang
- Zeyuan Liu
- Anyang Ji
- Te Sun
- Kongcheng Zhang
- Wenbo Xu
- Xubin Yue
- Shipeng Luo
affiliations:
- Nanjing University
- Meituan
- Zhongnan University of Economics and Law
- Hunan University
- Shanghai Jiao Tong University
arxiv_id: '2610.21656'
url: https://arxiv.org/abs/2610.21656
pdf_url: https://arxiv.org/pdf/2610.21656
published: '2026-10-14'
collected: '2026-10-17'
category: MultiAgent
direction: 多智能体环境生成与数据代理训练
tags:
- Data Agents
- Multi-Agent
- Synthetic Environments
- RL-zero
- Benchmark
- Data Synthesis
one_liner: 多智能体引擎从显式机制合成数据环境和任务，产出训练数据并RL-zero训练数据代理，基准大幅提升
practical_value: '- **数据合成范式可迁移到推荐 Agent 训练**：先定义用户偏好机制或环境规则，再生成可观测行为序列（点击、购买），让 Agent
  反推机制并产出策略。相比收集真实数据，这种方式规避隐私且天然携带 ground truth，适合构建 RL reward。

  - **多智能体审计确保任务可解性**：在生成模拟环境时，让独立角色检查目标是否可从观测文件恢复，避免生成无解或歧义任务。在电商场景中，可用一个智能体生成用户模拟，另一个验证推荐理由是否成立，减少无效标注。

  - **用 rubric 同时作为评估和 RL 奖励**：不必依赖人工轨迹蒸馏，结构化评分标准可直接作为 reward，降低标注成本。对于推荐系统的解释生成、策略优化等开放式任务，可设计类似
  rubric 让模型在无监督数据上自我改进。

  - **人类偏好筛选提升任务真实性**：从大规模合成任务中筛选最接近真实业务问题的子集构建评测集，可借鉴到 query 推荐、商品文案生成等任务，快速构造高质量离线
  benchmark。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：数据代理（用代码处理异构文件并生成分析洞察）的训练数据获取困难，环境构建成本高、受隐私和知识产权限制，开放式发现缺乏可验证的真值。核心洞察是：在生成文件之前，先定义文件背后的世界机制。

**方法关键点**：提出 Data World 多智能体引擎，从显式机制出发合成环境、任务和评估 rubric。独立审计检查目标是否可从观测文件恢复，确保任务可解；rubric 同时用于评估和 RL 奖励。通过人类偏好筛选问题真实性，构建 DataWorld-Bench（100 任务、50 个 held-out worlds、16 个领域）；引擎另产出 2,135 个训练任务，来自 1,037 个 disjoint worlds。

**关键结果数字**：评估 10 个前沿模型显示基准仍具挑战性，尤其在 insight discovery 上存在 computation–insight gap。用 RL-zero（无轨迹蒸馏）在合成任务上训练 Qwen3.6-35B-A3B 得到 DataWorld-35B-A3B，在 DataWorld-Bench 上提升 7.06 点，DAComp +14.28，DABstep-Hard +20.90，JobBench +12.13。
