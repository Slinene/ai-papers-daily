---
title: 'Your Agents Are Aging Too: Agent Lifespan Engineering for Deployed Systems'
title_zh: AI Agent也会老化：部署系统中的Agent寿命工程
authors:
- Jianing Zhu
- Yeonju Ro
- John Robertson
- Kevin Wang
- Junbo Li
- Haris Vikalo
- Aditya Akella
- Zhangyang Wang
affiliations:
- The University of Texas at Austin
arxiv_id: '2605.26302'
url: https://arxiv.org/abs/2605.26302
pdf_url: https://arxiv.org/pdf/2605.26302
published: '2026-05-24'
collected: '2026-05-29'
category: Eval
direction: Agent系统寿命工程与老化诊断
tags:
- Agent Aging
- Lifespan Engineering
- Memory Degradation
- Longitudinal Benchmark
- Counterfactual Diagnosis
one_liner: 首次定义Agent老化并构建纵向可靠性基准AgingBench，通过四种机制和诊断探针实现组件级归因。
practical_value: '- **部署后的纵向监控**：Agent可靠性会随时间退化，仅靠单次基准不足。电商推荐Agent（如长期对话助手）应建立老化曲线和半衰期指标，监控事实精度衰减。

  - **写时值保留策略**：压缩老化表明摘要会丢弃关键细节（如金额、约束）。在记忆写入时，可注入明确保留指令，或用结构化字段保存数值，防止“每日服药”这类泛化丢失。

  - **干扰诊断与检索增强**：干扰老化源于相似记忆混淆，可借鉴counterfactual探针区分是写入遗漏还是检索失败。对应到多用户推荐中，需对相似实体的记忆做硬性区分（如user
  ID后缀），并诊断是向量检索不准还是记忆未写入。

  - **维护后回归检测**：memory recompaction等操作会引发性能断崖。Agent上线后应在每次维护操作后运行关键事实的回归探测，对突变指标自动告警，类似软件CI/CD流程。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：AI Agent正从单次对话转向跨会话长期运行，但现有评测只看模型“首日能力”，忽略部署后随时间积累的记忆、压缩、修订等导致的可靠性退化——即“Agent老化”。实际系统中，即使模型权重冻结，Agent的状态仍在变化，行为测试可能正常而事实精度已悄然衰减。

**方法关键点**：
- 提出**Agent寿命工程（ALE）**，定义四种老化机制：压缩老化（写时摘要丢弃未来相关细节）、干扰老化（相似记忆积累导致检索混淆）、修订老化（事实更新未正确传播）和维护老化（memory flush/recompaction等操作触发回退）。
- 构建**AgingBench**：使用程序化生成器搭建带时间依赖DAG的多会话任务流，控制依赖密度、更新率、链深度、干扰对数量等老化压力，产出纵向老化曲线。
- **Counterfactual诊断**：通过三个探针阶梯（P1基线下运行，P2将检索替换为oracle，P3将写入+检索均替换为oracle）将端到端错误分解为Write Error、Read Error和Utilization Error，定位修复目标。

**关键结果**：
- 在7种场景、14个模型上，行为合规率（CVR）可能保持为0，而事实精度从0.90降至0.37，存在“沉默退化”。
- 修订老化并不随模型增大而单调改善，根源在于衍生状态（如累计预算）未显式维护。
- 自主Agent（OpenHands/Claude Code）中，工作区保真度始终高于下游召回准确率，表明瓶颈更多在Utilization阶段而非存储。
- 同一表面错误可能在写入/检索/利用三阶段不均衡分布，通用“增加内存”处方无效，需按诊断画像定向修复。

**核心洞见**：Agent的可靠性是整个系统harness的寿命属性，而非基础模型的快照指标；只有通过机制分解与组件级归因，才能让Agent优雅地老化。
