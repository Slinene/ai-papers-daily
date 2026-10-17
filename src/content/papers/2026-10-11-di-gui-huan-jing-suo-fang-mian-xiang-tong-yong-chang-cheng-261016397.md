---
title: Recursive Environment Scaling for General Long-Horizon Agents
title_zh: 递归环境缩放：面向通用长程智能体的难度递增方法
authors:
- Lingxiao Jing
- Zhengbo Jiao
- Yichen Xiang
- Bofan Zhu
- Lingbei Meng
- Yan Ni
- Haorui Chen
- Ran Ran
- Zhirong Shen
- Yuheng Yang
affiliations:
- UESTC
- HKUST
- CUHK (SZ)
- THU
- WU
arxiv_id: '2610.16397'
url: https://arxiv.org/abs/2610.16397
pdf_url: https://arxiv.org/pdf/2610.16397
published: '2026-10-11'
collected: '2026-10-17'
category: Agent
direction: Agent 环境难度缩放与课程训练
tags:
- Environment Scaling
- Agent Training
- SFT
- Long-Horizon Agents
- Benchmark Difficulty
one_liner: 提出 RES 框架，固定任务目标、递归变换信息访问/资源关系/执行依赖，提升环境难度并增强 SFT
practical_value: '- 借鉴 RES 的环境缩放机制做难度课程：在电商 Agent/对话推荐模拟器中，固定任务目标（如找商品、比价）不变，逐步限制信息可见字段、增加资源约束或依赖更多工具调用，生成难但语义一致的训练轨迹。

  - execution-grounded checks 相当于自动质检：对生成的难环境不仅检查语法，更用可执行环境验证是否仍可完成，避免产生不可解任务，这对生成
  Agent 训练样例有直接参考。

  - 递归继承持续累积难度：可把多轮变更叠加，形成难度递增轨迹，用于课程学习或困难样本挖掘，避免每次从头构造。

  - 结论显示同轨迹数下 RES 轨迹 SFT 全面优于原始轨迹：在推荐/搜广推 Agent 数据稀缺时，可优先构造变化环境扩充训练集，比单纯堆原始成功轨迹更划算。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：长程 Agent 评测与训练需要大量不同难度环境，但现有任务/轨迹/工具缩放会同时改变多个轴，难度来源纠缠，环境效应难以隔离。

**方法关键点**：RES 固定核心任务目标、约束与完成条件，由 Proposer 变换信息访问、资源关系、执行依赖；execution-grounded checks 验证候选；接受的变化跨轮继承，产生关联环境用于配对评估与训练轨迹收集。

**关键结果**：在 294 个初始任务、三个 benchmark 上，所有六个评估模型成功率下降，Claw-Eval-Live 下降 57.14–77.14 pp；相同轨迹数与优化设置下，RES 轨迹 SFT 在全部九个模型–基准比较中优于原始轨迹 SFT 7.00–14.61 pp；消融表明递归继承与依赖组合是难度增加的重要来源。
