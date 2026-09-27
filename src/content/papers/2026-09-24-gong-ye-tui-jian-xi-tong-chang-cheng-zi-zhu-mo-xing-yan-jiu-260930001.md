---
title: 'Advancing Model Research in AgentX: Long-Horizon Autonomy for Industrial Recommender
  Systems'
title_zh: 工业推荐系统长程自主模型研究：AgentX-Model 双智能体框架
authors:
- Shuang Yang
- Zijie Zhuang
- Changxin Lao
- Pengbo Xu
- Hanwen Xu
- Yusheng Huang
- Han Gao
- Guanchen Wang
- Tianbao Ma
- Linxun Chen
affiliations:
- Kuaishou
arxiv_id: '2609.30001'
url: https://arxiv.org/abs/2609.30001
pdf_url: https://arxiv.org/pdf/2609.30001
published: '2026-09-24'
collected: '2026-09-27'
category: MultiAgent
direction: Agent 多智体协作优化
tags:
- AgentX-Model
- Autonomous Research
- Recommender Systems
- Multi-Agent
- Long-Horizon
- Experiment Replay
one_liner: 双智能体分隔提案规划与实验执行，以四类研究动作持续迭代推荐模型，实现工业场景长程自主研究
practical_value: '- 可采用「提案规划 Agent + 实验执行 Agent」双上下文隔离：Research Agent 只看摘要、diff、测量汇总，不加载全部训练日志；Model
  Agent 专注代码与训练调试。适合把已有实验平台改造成长程自动迭代。

  - 实验归档必须保存每轮最佳实现而非只存最后版本：业务中 48% 的多轮实验最后轮低于中间最佳；保留 round-specific diff、evaluation
  context 和诊断观察，可让后续实验直接复用最佳起点。

  - 评估要同时报告 business baseline、direct parent、strongest ancestor 三个增量，避免把继承上游增益误判为新方案贡献；对推荐模型迭代平台尤其重要。

  - 任务调度先用固定轮转（Reproduce/Follow-up/Composition/Diagnose）+ Agent 候选选择即可，复杂 Bandit/Joint
  不一定带来稳定效率提升；工程上可先落地简单规则。

  - 业务校准问题（如广告 PCOC 偏差）应先做 Diagnose 实验收集证据，再设计修复，不要直接调大损失权重；论文实验显示通过统计校正因子可降低 22%
  以上误差且保留排序增益。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
工业推荐研究靠一连串实验推进，但现有 Agent 系统通常止步单次实验，无法把实验结果转化为下一个研究问题。AgentX-Model 要解决的是“如何让上一个实验的最佳实现、测量和未解决问题成为下一次实验的起点”。

## 方法关键点
- **双 Agent 架构**：Research Agent（Assembler+Auditor）负责从论文、业务反馈、历史结果形成并独立审查提案；Model Agent 执行多轮代码修改、训练、测量，返回代码与未解决问题。
- **共享研究状态** \(S_t=(I_t,E_t,Q_t)\) 保留每轮代码和测量，不覆盖最佳实现；比较参考分为业务基线、直接父代、最强可比祖先，分别计算 \(\Delta base\)、\(\Delta parent\)、\(\Delta path\)。
- **四个研究动作**：Reproduce 引入机制，Follow-up 针对改进，Composition 测试互补而非堆模块，Diagnose 收集证据指导修复。
- **任务分配解耦**：人类规则固定轮转与 Agent 候选选择分开；通过依赖感知历史回放评估选择策略。

## 关键实验
- 约 25 天生产：636 个模型变更实验，560 个 AUC 超业务基线；场景 A 最佳 AUC +0.023669。
- 在线 A/B：获客效率 +10–15%，目标段广告花费 +15–20%，观看时长 +0.3–0.8%；watch-time 模型 FLOPs/参数约降 10%。
- 持续研究中，Follow-up 7/77、Composition 5/120 超所有可比祖先；校准修复 PCOC 误差降低 22.8%/22.7%。
- 历史回放：473 节点，固定轮转 + Agent 候选选择与更复杂 Bandit/Joint 无一致效率差异。

## 最值得记住的一句话
把实验的 best-round 代码和诊断观察作为一等公民保留，并区分 parent/path/baseline 参考，才能支撑真正长程的自主研究。
