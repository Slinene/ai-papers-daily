---
title: 'AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement'
title_zh: AI4AI-Bench：评估LLM智能体设计训练算法实现递归自我改进
authors:
- Yizhe Chi
- Wenyi Li
- Deyao Hong
- Xiaoqiu Wang
- Mingju Gao
- Kaisen Yang
- Bingxiang He
- Youjie Zheng
- Calvin Xiao
- Qinhuai Na
affiliations:
- Navers Lab
- Einsia.AI
- Tsinghua University
arxiv_id: '2608.20318'
url: https://arxiv.org/abs/2608.20318
pdf_url: https://arxiv.org/pdf/2608.20318
published: '2026-08-20'
collected: '2026-08-21'
category: Eval
direction: LLM Agent 训练算法设计基准
tags:
- Recursive Self-Improvement
- Training Algorithm
- LLM Agent
- Benchmark
- Algorithmic Design
one_liner: 构建10任务基准，评估LLM智能体重写训练算法实现递归自我改进的能力，最强仅得0.250分
practical_value: '- 构建内部Agent能力基准时，可采用「冻结代码仓库+固定隐藏评估器+统一归一化分数」的范式：对不同任务的不可比指标映射到同一量纲，0为无信息模型，0.1为基线仓库算法，1为任务最优，便于横向对比各种Agent配置。

  - 结论提示：多数LLM Agent在优化任务中只做数据收集或超参数调优，很少真正改变模型学习规则。在电商推荐/广告场景中，若用Agent自动优化训练pipeline，需显式检测其是否只调参而不改update
  rule，否则提升有限。

  - 推理努力（reasoning effort）主要提高Agent「敢于修改核心训练算法」的概率（8%→64%），但对最终得分提升有限。业务上若让Agent做模型优化，增加思考预算可能带来更多探索行为，但需要配合约束和评估器防止无效改动。

  - 工程实现上，对Agent提交的代码在隔离环境下从零重跑并限制计算预算（4h重写/12h重训），可防止作弊并确保公平，适合作为自动化优化任务的评估标准。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**  
递归自我改进（RSI）要求AI系统能改进产生AI系统的过程，核心是训练算法本身；然而现有基准多靠收集数据或调超参数取胜，无法单独评估智能体设计训练算法的能力。  

**方法关键点**  
AI4AI-Bench包含10个冻结的研究仓库，覆盖10个训练算法家族。每个任务中，智能体有4小时单卡B300预算重写训练算法；提交代码从零重跑最多12小时，由对智能体隐藏的固定评估器评分，并与原算法在同一过程下对比。因10个指标不可比，统一映射到单一量表：0为无信息模型，0.1为仓库自带算法，1.0为任务最优。  

**关键结果数字**  
29个配置（6个系统×10任务）平均得分0.166，最强系统仅0.250，即只缩短了原算法到最优距离的不到20%。多数提交未改变模型学习方式；少数改变学习规则的平均0.226，其余仅0.126。增加推理努力主要提升改变学习方式的意愿（从8%到64%），平均分从0.094升至0.196。作者发布任务套件、评估器及所有评分提交以保证可重复性。
