---
title: 'EnvOS: Auditing Computer-Use Agents When the World Moves On : Phenomenon-Based
  Task Construction, Certification, and Evidence-Based Evaluation'
title_zh: EnvOS：审计动态变化环境下的计算机使用智能体——基于现象的任务构建、认证与证据评估
authors:
- Ankush Kadu
- Athira Gopal
- Niharika Singh
- Arpit Jain
- Aswanth Krishnan
affiliations:
- QpiAI, Bangalore, India
arxiv_id: '2610.40246'
url: https://arxiv.org/abs/2610.40246
pdf_url: https://arxiv.org/pdf/2610.40246
published: '2026-10-29'
collected: '2026-11-01'
category: Eval
direction: 智能体动态环境可靠评估
tags:
- computer-use agents
- dynamic environments
- evaluation
- stale information
- grading
- certification
one_liner: 提出 EnvOS 框架，在执行前认证环境变化、任务可解性和评分器，执行后基于存档证据复核判决，可靠评估动态环境中的计算机使用智能体
practical_value: '- 在电商/广告的 Agent 评估中，主动构造「陈旧信息」场景：让价格、库存、政策等状态在任务中途被后台流程或其他 Agent
  修改，检验模型是否在关键动作前重新读取源数据，避免仅靠静态测试集漏掉此类失败。

  - 借鉴 EnvOS 的评估前置认证：上线 Agent 评估前，先验证环境变化是否按预期触发、任务在变化后是否仍可解、自动评分器是否能区分正确与错误轨迹，防止评估本身的
  bug 干扰模型能力判断。

  - 自动评分后增加独立的证据复核环节：从运行日志/截图等存档证据中，用与评分器解耦的代码二次确认判决，减少误判；在压测中发现简单日志检查漏检率高，需设计更严格的证据校验。

  - 若业务中有可验证的业务规则（如订单状态流转、审批条件），可仿照 EnvOS 用种子生成环境并由审计后的自动验证器评分，为 Agent 提供可验证奖励，适合用于
  RLVR 训练，优化会话策略或多步操作。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

**动机**：LLM 驱动的计算机使用智能体在真实软件中执行多步任务时，环境状态可能在中途发生变化，例如预约被移动、政策被修订、记录被更新。此时测试智能体非常困难：失败可能来自智能体本身，也可能来自变化未正确触发、更新未送达智能体、评分器误判。需要能可靠构建和认证「任务中环境会变化」的评估框架。

**方法关键点**：EnvOS 框架在两个阶段提供保障。在智能体运行前，EnvOS 自动检查每个环境变化是否按设计触发、变化后任务是否仍可解、评分器是否能区分正确和错误行为；在每次运行后，由独立代码基于存档证据重新检查评分判决。框架被应用于「陈旧信息」场景：智能体已经看到的某个值，在它据此行动之前发生了变化。EnvOS 环境由种子生成，并由经过审计的自动验证器评分，因此可直接作为基于可验证奖励的强化学习训练环境。

**关键结果数字**：在诊所预约任务中，Claude Opus 5 无额外提示时成功 0/16 任务，提醒重新检查来源后为 2/16，直接显示更新值后为 15/16，显示更新值相对提醒的提升在多重检验校正后仍显著（p=0.00293）。在保险理赔审批任务中，Opus 5 自行重新检查并成功 10/10，而 Claude Sonnet 5 从 1/10 上升到 9/10（再次显示当前政策后），但该提升在校正后不显著。对评分系统进行压力测试：在盲设的损坏情节中，EnvOS 管道未将 26 个任一误判为干净；在外部生成集上捕获 25/39 个错误，而简单日志检查仅捕获 4 个。
