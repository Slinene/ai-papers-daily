---
title: 'SPIN: Structural LLM Planning via Iterative Navigation for Industrial Tasks'
title_zh: SPIN：通过迭代导航实现工业任务的结构化LLM规划
authors:
- Yusuke Ozaki
- Dhaval Patel
affiliations:
- University at Albany
- Kwansei Gakuin University
- IBM
arxiv_id: '2605.14051'
url: https://arxiv.org/abs/2605.14051
pdf_url: https://arxiv.org/pdf/2605.14051
published: '2026-05-12'
collected: '2026-05-16'
category: Agent
tags:
- LLM
- Agent
- Planning
- DAG
- Execution
- Industrial
one_liner: 一种规划包装器，结合DAG验证与基于前缀的模拟器-批评家停止策略，提升工业LLM代理的执行效率与结构正确性
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
工业资产运维场景中，LLM 代理的规划器常输出结构非法或冗长的工作流，导致下游执行失败、工具/API 成本激增。现有工作侧重动作生成或结构化解码，却忽视规划器输出的可执行性校验与执行长度的成本控制。尤其当外部工具调用成为瓶颈时，早停策略带来的效率提升尤为重要。

### 方法关键点
- **可执行 DAG 契约**：要求规划器输出对齐的四列表（任务、代理、依赖、预期输出），由严格验证器检查索引连续性、依赖合法性与代理名有效性；若无效，反馈错误并迭代修复。
- **前缀评估与早停**：对验证后的 DAG 计划，逐前缀调用检索增强的模拟器预测执行结果，再由批评家输出结构化判断（状态、能否回答、理由）；一旦当前前缀足以回答用户查询，立即终止执行。
- **组件分工**：模拟器基于历史轨迹库进行状态估计，抑制重复与终止条件失察；批评家直接决定停止，控制执行长度。

### 关键实验
- 在 **AssetOpsBench** 的 261 个场景上，[SPIN] 相比全量执行基准显著降低外部成本：总执行任务数从 1061 降至 623（-41%），任务级完成率从 0.638 升至 0.706，工具调用从 11.81 降至 6.82，API 调用从 34.05 降至 19.97，运行时间从 198.44s 降至 143.53s；但内部 token 消耗略增（sent 111530→117592，recv 2590→5542）。
- 消融实验表明：移除模拟器后，重复步骤与过早终止故障回升；削弱批评家则导致执行长度反弹。
- 在 **MCP Bench** 的 18 个两服务器 grounding 任务上（无外部记忆），SPIN 同样提升规划有效性、依赖意识等质量指标，且对 Llama 4 Maverick 显著降低轮次与 token 开销。

### 一句话总结
SPIN 用额外的内部推理开销换取大幅外部执行成本降低，并在任务完成率上保持甚至略优，其核心价值在于首次将规划验证与基于前缀的代价敏感停止策略落地于工业代理流程。
