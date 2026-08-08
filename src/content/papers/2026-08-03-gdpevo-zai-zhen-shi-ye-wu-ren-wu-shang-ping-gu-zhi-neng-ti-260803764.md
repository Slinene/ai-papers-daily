---
title: 'GDPevo: Evaluating Agent Self-Evolution on Real Business Tasks'
title_zh: GDPevo：在真实业务任务上评估智能体自我进化
authors:
- Leijun Zhou
- Zhihao Liu
- Xiang Qu
- Chenxu Liu
- Yifei Liu
- Yanke Yu
- Jingzhe Xu
- Xuejun Wu
- Buyue Qian
- Xi Chen
affiliations:
- PrismShadow
- New York University
arxiv_id: '2608.03764'
url: https://arxiv.org/abs/2608.03764
pdf_url: https://arxiv.org/pdf/2608.03764
published: '2026-08-03'
collected: '2026-08-08'
category: Agent
direction: Agent自进化评估基准与数据生成
tags:
- Agent Self-Evolution
- Benchmark
- Enterprise Workflows
- Rule Hybridization
- Data Contamination
- Evaluation
one_liner: 基于企业工作流的可归因自进化基准GDPevo，通过规则杂交评估智能体从经验中持续改进的能力，揭示当前水平远未成熟。
practical_value: '- **规则杂交可作为推荐评估的模拟框架**：将商品推荐规则拆解为原子规则，通过控制训练/测试规则子集的重叠度，系统评估推荐模型或Agent的冷启动、规则组合泛化能力，比随机划分更有解释力。

  - **自动化数据管道设计可借鉴**：通过规则模板自动化生成多样化的业务任务，能够快速构建和更新测试集，对抗数据污染，适合电商场景中持续评估模型迭代，避免指标膨胀。

  - **自进化增益的量化方法**：通过留出任务中训练前后准确率的差异来测量进化效果，这种归因设计可以迁移到评估LLM-based推荐或对话系统在记忆、工具使用等非参数状态更新后的实际收益。

  - **低自进化水平警示**：当前智能体即使经过进化，距离预言机上限仍有巨大差距，提示在电商/广告Agent中，简单的few-shot或记忆增强可能无法解决深层推理，需要更高层次的技能习得机制。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现有智能体自进化评估基准多局限于非经济场景，难以将测试增益归因于训练经验，且易受数据污染影响，缺乏对真实业务工作流中智能体自适应能力的可靠度量。

方法关键点：提出GDPevo基准，基于CRM、ERP、金融、医疗等GDP相关企业工作流。其核心机制为规则杂交：将每个工作流分解为细粒度的原子业务规则，在训练任务中分配这些规则的不同子集，在留出测试任务中通过重组规则来确保测试时性能提升可直接归因于训练期习得的规则经验。这一设计同时使基准具有可扩展性，可通过自动化管道快速生成新版本（V1:120个任务，V2可两天内扩至240个任务），有效应对数据污染。

关键结果：在4种智能体（不同harness+模型组合）及4种监督类型下评估，自进化一致地将留出任务准确率最高提升16.44个百分点；但最优进化智能体仍远低于完全信息预言机的91.6%上限，表明当前智能体的自我进化能力远未挖掘充分。
