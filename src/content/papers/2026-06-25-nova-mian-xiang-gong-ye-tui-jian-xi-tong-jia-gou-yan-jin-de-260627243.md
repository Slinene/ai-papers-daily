---
title: 'NOVA: A Verification-Aware Agent Harness for Architecture Evolution in Industrial
  Recommender Systems'
title_zh: NOVA：面向工业推荐系统架构演进的验证感知多智能体框架
authors:
- Shaohua Liu
- Liang Fang
- Yilong Sun
- Shudong Huang
- Qingsong Luo
- Xiaoyang Chen
- Dongqiang Liu
- Chuangang Ma
- Zhenzhen Chai
- Henghuan Wang
affiliations:
- Tencent Inc.
arxiv_id: '2606.27243'
url: https://arxiv.org/abs/2606.27243
pdf_url: https://arxiv.org/pdf/2606.27243
published: '2026-06-25'
collected: '2026-06-26'
category: RecSys
direction: Agent辅助架构自动演进
tags:
- Multi-Agent
- Architecture Evolution
- Verification
- Silent Failure
- Industrial RecSys
one_liner: 将模型架构修改视为反馈驱动的搜索，用“架构梯度”指导修改并级联验证扼杀静默失败
practical_value: '- **架构搜索即反馈控制**：借鉴SGD思想构造不可微的“架构梯度”，聚合上一次修改、验证诊断、指标差量和轨迹记忆，指引下一次修改方向；该模式可直接用于线上模型的自动化调参/升级，比盲测更经济。

  - **多级验证阻断静默失败**：在真实训练前加入结构语义门（检查shape/mask/特征映射/融合路径），使可编译但结构错误的候选提前终止，并将失败模式存储为后续迭代的“禁止方向”，能大幅减少无效GPU消耗。

  - **风险分级与人工确认路由**：按任务复杂度分L1–L4，高风险或技能覆盖不足的修改自动切至Copilot模式要求人工确认，这种生产安全机制可直接嵌入AutoML或Agent
  pipeline。

  - **失败信号复用为搜索知识**：除指标反馈外，将语义验证和工程失败模式结构化存入轨迹记忆，形成可复用的禁止方向，让后续迭代自动避开已知坑点，这一工程化trick可显著提升迭代有效率。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
工业广告推荐模型的性能提升往往依赖架构级升级（如RankMixer、TokenMixer-Large），但这类改动涉及跨模块拓扑变化、特征路由、形状兼容等强约束，极度依赖专家经验且难以规模化。现有AutoML局限于超参数调优，通用LLM编码代理只保证代码可运行，却无法甄别“能跑但模型结构语义错误”的静默失败——这类候选会无声地损害AUC与线上指标。因此需要一种既懂得推荐架构约束，又能将验证结果反向指导搜索的自动化框架。

**方法关键点**
- **架构梯度（Architecture Gradient）**：受SGD启发，定义离散修改空间中的更新信号。每轮聚合上一次修改操作、验证诊断、ΔAUC反馈与轨迹记忆，输出三个部分：弱组件定位、建议修改方向、该轮禁止方向。据此选择下一步修改，使搜索具有方向性。
- **四级任务与双模式路由**：L1/L2覆盖原子调参与约束扩量，L3将顶会模块迁移到生产模型，L4为开放式创新。AutoRun自动执行业务覆盖充分的修改，Copilot对高风险或未覆盖修改要求人工确认，兼顾效率与安全。
- **多阶段验证级联**：结构语义门在训练前检查tensor形状、mask方向、特征-token映射、logit融合等语义约束；本地可执行性门阻断工程错误；离线AUC评估筛选有效候选；在线A/B最终验证。验证失败的诊断被录入轨迹记忆，作为后续的禁止方向，让验证从过滤器变为搜索指引。
- **多智能体编排**：由Main Agent协同初始分析、方案设计、代码生成、质量审查、本地测试、离线训练与在线实验七个子Agent，边界清晰，异常可重试或升级。

**关键结果**
- 实验在腾讯亿级用户广告推荐系统上进行，任务：L2 ScaleUp（参数协同扩量）和L3 Literature-to-Production（TokenMixer-Large迁移）。
- 与人类专家、ReActAgent-only、OpenHands、Optuna-TPE对比，NOVA在L2上获得99.0% LPR、54.5% EPR；在L3上取得86.7% LPR、60.0% EPR，EPR是人工循环的2倍以上，静默失败率仅30.8%。
- 消除实验表明，去除架构梯度反馈会使EPR从60%降至37.5%，去除方案设计骤降至18.2%，去除多候选生成与质量审查也显著拉低有效率。
- 线上A/B：L3候选对三个pCVR目标的GMV分别提升+1.25%、+1.70%、+2.02%，预测偏差降低37%–67%。
- 效率：一轮文献到生产周期的人工参与时间降低13倍以上（54u→4u）。

**核心洞察**
将验证诊断做成可重用的“禁止方向”织入搜索梯度，让架构演化不再盲目抛改，而是像专家一样从错误中学习。
