---
title: 'Scaling Large Reasoning Models beyond Human Supervision: A Path toward Superintelligence'
title_zh: 将大型推理模型扩展到人工监督之外：通往超级智能之路
authors:
- Zhiqin Yang
- Jingwen Fu
- Yuhan Liu
- Hengyu Liu
- Yonggang Zhang
- Kainan Cao
- Zizhuo Zhang
- Chenxin Li
- Ruibin Yuan
- Jiahao Pan
affiliations:
- The Hong Kong University of Science and Technology
- Zhongguancun Academy
- Xi’an Jiaotong University
- The Chinese University of Hong Kong
- The University of Hong Kong
arxiv_id: '2608.31075'
url: https://arxiv.org/abs/2608.31075
pdf_url: https://arxiv.org/pdf/2608.31075
published: '2026-08-30'
collected: '2026-09-01'
category: Training
direction: LRM 自监督扩展训练路径综述
tags:
- LRM
- RLVR
- Self-supervision
- Reward hacking
- Curriculum learning
- Agentic learning
one_liner: 提出奖励轴与经验轴的双维分析框架及 L0-L4 五级阶梯，系统阐述 LRM 在减少人工监督下的扩展路径与风险
practical_value: '- 在电商/广告 Agent 中，可借鉴「可验证奖励」设计：将业务规则、成交结果、用户后续行为等转化为自动校验信号，减少对人工标注的依赖，逐步从
  L1 过渡到 L2/L3。

  - 引入「经验质量评估」与「反馈保真度监控」：对模型生成的交互轨迹、推荐解释等建立自动评分器，防止在自主探索中出现课程坍塌或奖励黑客，类似推荐系统里的多样性约束。

  - 构建模拟环境或沙盒，让 LLM Agent 在推荐/搜索 pipeline 中自我生成课程并迭代，但需加入对抗性校验和人工抽查作为安全阀。

  - 注意反馈漂移：在自动奖励下，模型可能偏向表面指标（如点击率）而牺牲长期用户体验，需同时监控策略能力、反馈保真度和经验质量三个维度。'
score: 7
source: huggingface-daily
depth: abstract
---

## 动机
大型推理模型（LRM）在数学、代码等结果可自动验证的任务上，通过 RLVR 取得了显著提升。但开放域和 Agentic 任务缺乏可靠奖励，人工监督无法跟上模型生成经验的规模与复杂度，需要探索如何在人类监督逐渐退出的情况下持续改进。

## 方法关键点
论文从两个相互关联的维度梳理扩展路径：
- **奖励轴**：从逐实例人工判断，到可复用验证器，再到无需人类反馈的自动奖励。
- **经验轴**：从人工策划的任务和环境，到自生成课程、构造环境，最终到自主协同进化。

连接两个维度提出 L0–L4 五级阶梯，明确每一级中哪些学习环节仍受人工控制。同时系统分析了自主化过程引入的风险：奖励黑客、反馈漂移、课程坍塌、环境错误。

## 评估与结果
提出应从三个互补对象评估系统：策略能力（policy capability）、反馈保真度（feedback fidelity）、经验质量（experience quality）。论文没有给出具体实验数字，但提供了结构化框架和持续更新的 GitHub 仓库，用于跟踪该方向最新进展。该工作为构建自我持续学习系统、迈向超级智能提供了路径图与开放问题清单。
