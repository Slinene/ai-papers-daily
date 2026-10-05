---
title: 'Credit Where It Matters: Dependency-Aware Policy Optimization for Terminal
  Agents'
title_zh: 依赖感知的终端智能体策略优化
authors:
- Yu Li
- Guangfeng Cai
- Long-Fei Li
- Shuo Han
- Shengtian Yang
- Han Luo
- Kaibing Yang
- Lei Feng
affiliations:
- Southeast University
- Huawei Noah's Ark Lab
arxiv_id: '2610.03634'
url: https://arxiv.org/abs/2610.03634
pdf_url: https://arxiv.org/pdf/2610.03634
published: '2026-10-02'
collected: '2026-10-05'
category: Agent
direction: 终端 Agent · 依赖感知信用分配
tags:
- Terminal Agent
- Credit Assignment
- Policy Optimization
- RL
- Dependency Graph
- GRPO
one_liner: 提出 DepGPO，用命令间读写依赖图反向追踪，把优势分配到真正影响结果的步骤
practical_value: '- 对多步 Agent 业务（如推荐 Agent 先检索后排序再生成文案），可以借鉴依赖图思路：记录中间工具调用的读写资源，从最终业务指标反向追踪哪些调用真正影响了结果，再做细粒度
  credit assignment，减少无关步骤的梯度噪声。

  - 训练 LLM Agent 时，trajectory-level advantage 会平均分配到所有 step，导致无关操作也获得信号；可以按依赖相关性重分配
  advantage，只强化对最终 verifier 关注资源有贡献的 write/read 步骤，提升样本效率与训练稳定性。

  - 工程实现上只需保存 execution trace 并解析命令间文件/变量读写关系，成本较低；在终端、代码或工具调用类 Agent 的 RL 训练中易于落地。

  - 对电商搜索推荐中“多轮改写-召回-排序”的 Agent 链路，可以类比为命令依赖图，识别哪些改写或过滤动作对最终成交/点击有实际贡献，后续可用于诊断或弱监督信号设计。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

动机：终端 Agent 常通过 RL 训练完成多步命令任务，后续命令依赖前序命令的输出。现有 GRPO/DAPO 等 trajectory-level 或 step-level 信用分配不显式追踪命令间读写依赖，导致无关步骤也获得训练信号，削弱对关键步骤的学习。

方法关键点：提出 DepGPO，从执行轨迹构建命令依赖图，记录命令对资源的读/写关系；从任务 verifier 检查的资源出发反向追踪，找出真正影响最终结果的 writes 及其支持 reads；只对这些相关步骤分配 credit，并据此重新分布 trajectory advantage 到每一步。

关键结果：在复杂终端任务上，DepGPO 相比 GRPO/DAPO 等基线提升任务性能与训练稳定性，消融实验验证依赖追踪对信用分配的有效性。
