---
title: 'OpenDeepThink: Parallel Reasoning via Bradley--Terry Aggregation'
title_zh: OpenDeepThink：基于Bradley-Terry聚合的并行推理
authors:
- Shang Zhou
- Wenhao Chai
- Kaiyuan Liu
- Huanzhi Mao
- Qiuyang Mang
- Jingbo Shang
affiliations:
- UC San Diego
- Princeton University
- University of Washington
- UC Berkeley
arxiv_id: '2605.15177'
url: https://arxiv.org/abs/2605.15177
pdf_url: https://arxiv.org/pdf/2605.15177
published: '2026-05-14'
collected: '2026-05-15'
category: Reasoning
tags:
- Test-time compute
- Bradley-Terry
- LLM-as-Judge
- Codeforces
- Parallel Reasoning
- Evolutionary Algorithm
one_liner: 无需外部验证器的并行测试时推理框架，通过成对比较与Bradley-Terry排名实现选择与突变。
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

## 动机

测试时计算扩展是提升LLM推理的主要方向，但主流方法沿单条推理链增加深度，面临错误传播风险。并行采样多条候选解虽然自然，却引入选择瓶颈：缺乏真实验证器，点式LLM评判噪声大且存在正向偏差（准确率仅59%），无法可靠区分优劣。

## 方法关键点

OpenDeepThink提出基于种群的并行推理框架，无需外部验证器：
- **种群进化**：维护 n 个候选解，进化 T 代。每代随机配对候选进行成对比较（K=4 次/候选），由同一LLM担任裁判，输出胜负关系和自然语言反馈。
- **Bradley-Terry聚合**：将成对比较结果拟合为全局排名，内部化对手强度，形成可靠软验证器（配对准确率86%）。
- **精英保留与突变**：按BT分数保留前25%精英，丢弃底部25%，前75%（含精英）基于对比反馈进行突变，允许放弃原有方案。最终通过更密集的成对比较（M=10）选择最优解。
- **并行性**：所有比较和突变独立并行，整个流程顺序深度仅8次LLM调用，总预算约285次API调用/问题。

## 关键结果

- **竞赛编程**：在CF-73+NOI-119共192题上，Gemini 3.1 Pro有效Codeforces Elo提升**405点**，Hard难度（pass@1≤35%）BT top-1准确率从23%升至**50%**，pass@1从11%升至36%。
- **跨模型迁移**：相同超参数应用到Gemini 3 Flash和2.5 Pro，均取得正向提升，无需重调。
- **反馈信号**：突变主要受益于**负反馈**，正反馈与无反馈无显著差异；成对负反馈的拯救率比无反馈高24%（+68 vs +44）。
- **HLE多域基准**：客观可验证领域（数学、物理）可见增益（+5~+17），主观领域（人文社科）反而下降（-25~-30），表明框架有效性取决于LLM裁判的可信度。

核心洞察：当点式评判不可靠时，成对比较与Bradley-Terry聚合可将并行采样的选择瓶颈转化为进化动力，而无需任何领域特定基础设施。
