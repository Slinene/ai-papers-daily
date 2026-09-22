---
title: 'SocioVerse2: A Longitudinal Dynamic Social Simulation Framework under a Human-AI
  Co-evolutionary Paradigm'
title_zh: SocioVerse2：人机共进化范式下的纵向动态社会模拟框架
authors:
- Xinnong Zhang
- Jiayu Lin
- Jia Wang
- Yixu Huang
- Xinyi Mou
- Yingqian Wu
- Jingcong Liang
- Shijun Lei
- Jianing Shi
- Guanying Li
affiliations:
- Shanghai Innovation Institute
- Fudan University
- King's College London
- Tongji University
- Northwestern Polytechnical University
arxiv_id: '2609.24911'
url: https://arxiv.org/abs/2609.24911
pdf_url: https://arxiv.org/pdf/2609.24911
published: '2026-09-21'
collected: '2026-09-22'
category: MultiAgent
direction: 多智能体社会模拟框架
tags:
- Social Simulation
- Generative Agents
- Human-AI Co-evolution
- Longitudinal Simulation
- Counterfactual Intervention
- Agent Infrastructure
one_liner: 提出 SocioVerse2 框架，以双循环与智能基础设施支持可干预、可控制、纵向的社会模拟研究
practical_value: '- 借鉴双循环架构：将“环境模拟/用户行为演化”与“策略实验控制”解耦，建立可版本化的实验流水线，支持反事实对比（如推荐策略变更后的预估影响），提高实验可复现性。

  - 引入可编辑状态与检查点：对推荐/广告实验流程进行版本化管理和回滚，便于追踪策略变化及归因；类似 MLflow 但更侧重流程控制。

  - 构建环境服务保证时点一致性：在电商场景中，用户行为、商品库存等数据有强时效性，离线评估模拟时需按时间点取一致快照，避免数据穿越；其服务化设计可直接迁移到仿真平台。

  - 利用生成式智能体池做用户模拟：构建多 persona 池和可组合技能，模拟用户群体，用于推荐系统的冷启动策略预演、广告投放模拟和 AB 测试代理评估。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有社会模拟平台仅能验证集体行为、对齐截面数据或使用自主智能体辅助研究，缺乏对模拟内容干预和研究者对过程控制的支持。SocioVerse2 将 SocioVerse1.0 扩展为人机共进化范式，围绕两个循环与一个基础设施构建。

**方法**：纵向模拟循环在演化环境中模拟目标人群，通过干预派生反事实分支；可控研究循环将研究本身作为可编辑状态，支持状态版本更新；智能基础设施提供可组合技能与研究者检查点、五类人格池的人口服务，以及覆盖21个真实信号源且具有时点一致性的环境服务。

**结果**：在三个案例族、七个案例研究中验证，包含复现经典基于智能体的模型、用真实记录模拟政策过程，以及超出响应模型知识截止时间的宏观经济指标即时预测。该框架使案例从系统演示提升为实质性学科研究。
