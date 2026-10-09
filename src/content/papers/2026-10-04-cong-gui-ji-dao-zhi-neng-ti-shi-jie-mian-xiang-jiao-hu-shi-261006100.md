---
title: 'From Traces to Agentic Worlds: Agentic Language World Models for Interactive
  Environment Simulation'
title_zh: 从轨迹到智能体世界：面向交互式环境模拟的智能体语言世界模型
authors:
- Quanyu Long
- Xiao Chen
- Jianda Chen
- Haozhen Zhang
- Qisheng Hu
- Jianzhu Bao
- Wenya Wang
affiliations:
- Nanyang Technological University
- The Hong Kong Polytechnic University
arxiv_id: '2610.06100'
url: https://arxiv.org/abs/2610.06100
pdf_url: https://arxiv.org/pdf/2610.06100
published: '2026-10-04'
collected: '2026-10-09'
category: Agent
direction: Agent 世界模型与轨迹仿真
tags:
- Trace2Env
- Agentic World Model
- LLM Agents
- Environment Simulation
- Stateful Simulation
- Learning-Free
one_liner: 无训练的 Trace2Env 从历史轨迹构建 worldbook，让世界模型 Agent 实现有状态交互仿真，提升长程一致性与动作回放有效性。
practical_value: '- 在电商/搜索/Agent 场景，历史交互日志（session、操作记录、客服工作台）很丰富但线上系统不可复现，可借鉴 Trace2Env
  用轨迹构建 worldbook：按环境 schema、grounded evidence、induced behavioral knowledge 三层组织，无需训练即可搭离线仿真环境。

  - 多轮仿真必须维护 persistent episodic state：购物车、筛选条件、已浏览商品、会话目标等要显式建模并跨轮更新，否则策略评估会在长程动作后失真；这是当前
  prompt-based 世界模型的薄弱点。

  - 评估不要只看 next observation 相似度，可加入 long-horizon replay validity：把仿真器中生成的动作回放到真实系统，看动作是否仍然有效，能更直接反映环境保真度。

  - Learning-free 做法适合快速冷启动业务环境模拟，但需注意轨迹覆盖偏差；如果历史日志噪声大或缺乏典型状态转移，worldbook 检索出的后果推断可能不稳定，建议用
  schema/证据检索做硬约束。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：训练和评测 LLM Agent 需要高保真环境，但真实系统往往不可访问或难以复现；历史交互轨迹却普遍存在，因此可以考虑直接从轨迹恢复环境知识。

**方法关键点**：Trace2Env 不重建可执行环境，而是将历史轨迹构造为可复用 worldbook，包含环境 schema、grounded evidence、induced behavioral knowledge 三层信息；运行时世界模型 Agent 查询 worldbook，并维护 persistent episodic state 来推断每个动作的 observation 和长期状态效应。整个过程 learning-free。

**关键结果**：在 9 个环境中，Trace2Env 相比传统 prompt-based LWM 提升了 next-observation 保真度和长程交互一致性；多轮交互中，基于 Trace2Env 生成的动作回放到真实环境时保持有效的比例更高，说明其能更好保留前序动作的后果。
