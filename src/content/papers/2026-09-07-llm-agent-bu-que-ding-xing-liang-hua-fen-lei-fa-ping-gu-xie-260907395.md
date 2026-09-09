---
title: 'Uncertainty Quantification for LLM Agents: A Taxonomy, an Evaluation Protocol,
  and an Empirical Study'
title_zh: LLM Agent 不确定性量化：分类法、评估协议与实证研究
authors:
- Moule Lin
- Qizhen Lan
- Shuhao Guan
- Weipeng Jing
- Jiexin Fan
- David Gregg
- Goetz Botterweck
affiliations:
- Trinity College Dublin, Ireland
- University of Texas Health Science Center at Houston, USA
- University College Dublin, Ireland
- Northeast Forestry University, China
arxiv_id: '2609.07395'
url: https://arxiv.org/abs/2609.07395
pdf_url: https://arxiv.org/pdf/2609.07395
published: '2026-09-07'
collected: '2026-09-09'
category: Agent
direction: Agent 轨迹级不确定性与校准
tags:
- Uncertainty Quantification
- LLM Agents
- Calibration
- Trajectory
- TC-ECE
- Agent Evaluation
one_liner: 提出三轴分类法与轨迹级校准指标 TC-ECE，揭示 Agent 步级校准无法推出轨迹级校准
practical_value: '- 在构建推荐/搜索 Agent 时，不要只监控最终答案置信度；在 planning、retrieval、tool call 每个步骤输出
  confidence，并在轨迹检查点评估 TC-ECE。尤其在多步召回/排序/重写流程中，早期错误会累积，需要 mid-trajectory 干预信号。

  - 不要把每步置信度相乘作为整体可靠性：步骤间相关性会导致低估或高估，建议拟合轨迹级校准器或使用生存因子 q_t，并对前缀可靠性分层监控。

  - 多 Agent 协作（如 query 理解、召回、排序、出价等模块）中，相似训练历史导致相关性错误共识；需要加权仲裁，保留不同意见，不能简单平均。

  - 论文发现 Agent 自述置信度不一定可靠，建议与简单基线（如 step-index）对比；部署前离线用真实轨迹校验。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：LLM 从单轮问答演变为长期规划、调用工具、检索记忆、多智能体协作的 Agent；错误在早期产生并沿轨迹累积，单轮 UQ 方法无法捕捉。需要一个评估 Agent 何时可信的协议。

**方法**：
- 三轴分类：来源轴 A（aleatoric/epistemic/tool/accumulated/inter-agent）、方法轴 B（verbalized/sampling/token prob/conformal/ensemble/propagation/abstention/training）、阶段轴 C（planning/tool/retrieval/memory/multi-step/multi-agent）。
- 形式化定义 step-level 和 trajectory-level calibration；通过反例（相关/反相关两步骤）证明步级校准不构成轨迹级校准；Proposition 2 用 prefix-coupling 系数给出边际乘积误差界；用生存因子 q_t = 1 - λ_t 描述条件成功率。
- 提出 TC-ECE：在轨迹多个检查点分别计算校准误差，避免平均掩盖后期过置信。

**关键实验**：在四个模型、三个任务、最长 50 步的真实 Agent trace 上计算 TC-ECE；Agent 自述置信度未能一致优于简单 step-index 基线；汇聚所有检查点会掩盖后期阶段的过自信；ALFWorld 中前缀耦合系数为正，边际乘积低估前缀可靠性。

**最值得记住的一句话**：一个置信度数字不够：需要按轨迹检查点评估不确定性，步级校准不能推出轨迹级校准。
