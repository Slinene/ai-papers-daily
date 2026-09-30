---
title: Do LLM Agents Execute the Plans They Declare? From Planning-Mode Declaration
  to Pattern-Specific Execution
title_zh: LLM Agent 是否执行所声明的计划？从规划模式声明到模式化执行
authors:
- Subba Reddy Oota
- Francisco Herrera
- Jordi Cabot Sagrera
- Marcos López de Prado
- Shadab Khan
affiliations:
- ADIA Lab, Abu Dhabi, United Arab Emirates
- University of Granada, Granada, Spain
- Luxembourg Institute of Science and Technology, Luxembourg
- Cornell University, Ithaca, USA
- Lawrence Berkeley National Laboratory, Berkeley, CA
arxiv_id: '2609.38108'
url: https://arxiv.org/abs/2609.38108
pdf_url: https://arxiv.org/pdf/2609.38108
published: '2026-09-29'
collected: '2026-09-30'
category: Agent
direction: Agent 规划声明与执行一致性诊断
tags:
- LLM Agents
- Planning
- Plan Execution
- Routing
- Trajectory Evaluation
- Process Metrics
one_liner: 提出 Planning-as-Routing：LLM 声明规划模式并由确定性路由器分派给对应执行器，显著缩小声明-执行差距，但模式选择仍是瓶颈
practical_value: '- 业务 Agent 设计：不要把 LLM 生成的计划仅仅作为 prompt 交给通用 ReAct loop；要把 planning
  mode 映射到可执行 control flow（predefined/sequential/hierarchical/search）。长链路任务（多步商品约束搜索、广告账户搭建、售后工单处理）优先用
  hierarchical/search 执行器，短任务用 predefined 更省成本。

  - 评估体系：新增 process-level 指标（plan adherence、plan-order faithfulness、declaration-execution
  preservation），不要只看最终成功率。可以用规则 verifier 或轻量 judge 检查轨迹是否按声明顺序执行，快速区分是选错模式还是执行漂移。

  - 路由与选型：做 planning mode 路由前，先跑 forced dispatch 得到每个模式在目标任务集上的 ceiling；如果 per-task
  oracle 相对 best fixed policy 的 headroom 很小，就不值得做复杂 selection，固定最优模式+多次重试更划算。

  - 少样本与选择先验：few-shot 对模式选择有正收益但不稳定，需按业务环境和模型分别验证；当前 LLM 零样本选择接近任务无关偏好，不要默认模型会为每个任务选对
  planning mode。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：LLM agent 通常会先规划再执行，但只看最终任务成功无法区分“选错规划模式”和“执行时偏离声明计划”。现有 planner–executor 系统可能在这两类失败中失效，因此需要专门诊断 Plan Declaration–Execution Gap，并研究不同任务和环境是否适合不同规划模式。

**方法关键点**：定义四类规划模式——Predefined、Sequential、Hierarchical、Search；比较三种条件：Flat ReAct、Plan+ReAct（声明但由通用 ReAct 执行）、Planning-as-Routing（LLM 声明模式后由确定性 router 分派给模式专用 executor）。通过规则 verifier 检查 plan-order faithfulness，用 forced dispatch 做 pattern-ceiling 分析，分离选择失败与执行失败。

**关键结果**：在 ALFWorld、Mind2Web、SWE-bench Verified、WebArena 上，通用 Plan+ReAct 仅 22–45% 轨迹保持声明结构，且计划越长保真度越低；模式专用执行将 ALFWorld DeepSeek 成功率从 0.48 提到 0.92，SWE-bench 从 0.36 提到 0.44。最强模式随环境和模型变化：ALFWorld/WebArena 多为 Search，SWE-bench 为 Hierarchical，Gemma 在 Mind2Web 为 Predefined。当前 LLM 的 top-1 模式声明不比任务无关偏好更好；few-shot 可提升选择，增益约 +0.004 到 +0.16。计划质量与任务成功仅弱相关。最值得记住的是：**可靠的 agent 规划既需要选对 planning mode，也需要用匹配的 executor 保留其结构；最终成功率会把这两种失败混在一起。**
