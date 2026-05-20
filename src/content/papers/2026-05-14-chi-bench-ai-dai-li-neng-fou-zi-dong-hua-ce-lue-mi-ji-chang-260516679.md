---
title: 'CHI-Bench: Can AI Agents Automate End-to-End, Long-Horizon, Policy-Rich Healthcare
  Workflows?'
title_zh: CHI-Bench：AI 代理能否自动化策略密集、长周期的医疗工作流？
authors:
- Haolin Chen
- Deon Metelski
- Leon Qi
- Tao Xia
- Joonyul Lee
- Steve Brown
- Kevin Riley
- Frank Wang
- T. Y. Alvin Liu
- Hank Capps MD
affiliations:
- actA V A.ai
- Johns Hopkins Medicine
- Wellstar Health System
- Stanford University
- CMU
arxiv_id: '2605.16679'
url: https://arxiv.org/abs/2605.16679
pdf_url: https://arxiv.org/pdf/2605.16679
published: '2026-05-14'
collected: '2026-05-20'
category: Agent
direction: 面向策略密集长周期工作流的 Agent 评估
tags:
- Agent
- Healthcare
- Benchmark
- Long-Horizon
- Multi-role
- MCP
one_liner: 构建首个评估 AI 代理端到端自动化多角色、高策略密度医疗运营工作流的基准，当前最优方案仅完成 28% 任务。
practical_value: '- 多角色与策略密集工作流设计：在电商客服、售后纠纷、供应链协调等多角色交互场景中，可借鉴 χ-Bench 的“指令-技能书-多
  MCP 工具”架构，将企业内部业务规则编码为可被 Agent 调用的知识库与工具集，构建更贴近真实业务的长周期任务评估。

  - 长周期任务性能退化警示：实验表明单会话连续执行所有任务时成功率骤降至 3.8%，提示在电商推荐或订单处理 Agent 的部署中，需设计会话状态持久化、记忆压缩或子任务分拆等机制来对抗长上下文下的性能衰减。

  - 工具集成与标准化 MCP 接口：基准中 87 个工具通过 MCP 服务器暴露，为电商/推荐系统 Agent 集成复杂的业务 API（如商品搜索、营销规则引擎、物流查询）提供了工程参考，可复用其工具描述模式，降低
  Agent 与异构系统的对接成本。

  - 严格多级评估准则（pass³）：对于生成式推荐、Agent 辅助决策等对可靠性要求高的场景，可以引入 χ-Bench 的多维度通过标准（如轨迹正确性、产出文档质量、最终结果），避免单指标乐观估计，更真实反映
  Agent 在不可逆业务操作中的可靠性。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 AI 代理基准多集中在短程、单角色、低策略密度的任务，无法反映医疗、电商等真实行业中端到端工作流的复杂性：决策依赖大量规则库（policy density）、需多角色切换（multi‑role composition）以及多轮交互（multilateral interaction）。为填补这一空白，本文提出 χ‑Bench。

**方法**：χ‑Bench 覆盖三大医疗运营领域（提供方预授权、支付方利用管理、护理管理），每个任务要求代理在一个模拟 20 款医疗应用的沙箱中，通过调用 87 个 MCP 工具，依据一本含 1,290+ 篇文档的托管护理操作手册（skills），完成一系列角色特有的文书与操作，直至达成终止状态。评估采用任务完成率（pass¹）、轨迹判定正确率（pass²）和文书审查通过率（pass³）的三级严格准则。

**关键结果**：在 30 种代理/模型组合中，表现最佳的代理仅解决 28.0% 的任务，无一代理在 pass³ 上超过 20%，且若让代理单会话连续执行所有任务，成功率暴跌至 3.8%。结论表明当前代理在策略密集、角色组合、不可逆操作的真实企业场景中仍存在巨大能力缺口，类似的鸿沟极可能出现在其他企业级领域。
