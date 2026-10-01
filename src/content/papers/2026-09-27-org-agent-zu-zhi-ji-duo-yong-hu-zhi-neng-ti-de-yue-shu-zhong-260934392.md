---
title: 'Org-Agent: Beyond Personal Assistants Towards Organizational Agents'
title_zh: Org-Agent：组织级多用户智能体的约束中心推理框架
authors:
- Luyao Zhuang
- Yujing Zhang
- Zijin Hong
- Yilin Xiao
- Xiao Huang
affiliations:
- The Department of Computing, The Hong Kong Polytechnic University, Hong Kong SAR
arxiv_id: '2609.34392'
url: https://arxiv.org/abs/2609.34392
pdf_url: https://arxiv.org/pdf/2609.34392
published: '2026-09-27'
collected: '2026-10-01'
category: Agent
direction: 组织级多用户 Agent 约束感知调度
tags:
- Organizational Agent
- Task Dependency Graph
- Multi-User LLM
- Constraint-Aware Execution
- Agent Memory
- Tool-Augmented
one_liner: 提出约束中心的组织级智能体框架，用任务依赖图加约束感知工具同时提升跨用户决策与记忆利用
practical_value: '- 多角色协作工作流：把运营、风控、商品等多方请求拆成原子子任务并构造 Task Dependency Graph，拓扑排序后先解决依赖（如先取库存/风控结论再出促销方案），可避免
  LLM 一次性处理全部上下文时的遗漏与冲突。

  - 显式建模组织约束：将用户身份、权限、信息归因、时效、冲突解决规则做成节点属性或元数据过滤条件，执行时按 asker 身份过滤记录（如 author=UserID
  + phase），能显著降低越权泄露和错误归因，适合客服/审批类 Agent。

  - 证据获取工具三件套：相似度评分（lexical+semantic，α=0.5 平衡）+ 条件过滤 + 关系遍历（reply/decision 边），比纯 RAG
  或全量建图更准且成本更低；多轮对话、售后记录、团队消息流检索可直接复用。

  - 执行记忆 Read/Write：把前置节点结果写进 structured records/running summary，下一节点组装上下文时读取；在选品→定价→投放等长链路推荐
  Agent 中维护执行记忆，可减少重复检索和上下文丢失。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：组织场景下，一个共享 agent 要同时协调多用户请求并利用跨用户交互知识，但现有 LLM agent 多为单用户设计。简单拼接多用户历史和请求，无法显式表达身份、权限、信息归因、时效、冲突解决和完成条件等组织约束，导致决策遗漏与信息误用。

**方法关键点**：Org-Agent 把执行组织为三阶段。①任务依赖图构建：LLM 将待处理请求拆成 inquiry/decision/response 三类原子子任务，以 DAG 边编码依赖，新输入触发图更新。②依赖感知调度：拓扑排序给出执行顺序，保证每个节点在前提节点之后执行，可层内并行。③约束感知节点执行：每个节点上下文由基础上下文（节点目标、相关用户信息、相关约束）与执行记忆读取拼装；证据获取工具包括相似度评分（混合 BM25 和 dense，α=0.5）、条件过滤（按 author/role/phase 等元数据）和关系遍历（沿回复/决策边）；记忆管理工具 Read/Write 维护 accumulated execution memory。

**关键实验**：在 GroupMemBench 745 个多用户问答上，GPT-4o-mini 下平均准确率 44.03%，超过 BM25 的 37.72% 和最强记忆系统 Hindsight 的 38.79%，而 token 仅 5.5M，远低于 Hindsight 117.5M。在 MUSES-Bench 1183 个多用户决策场景上，平均分 72.39% vs vanilla 64.12%，其中 Meeting 成功率 +23.15pp；DeepSeek 和 Qwen 骨干下也一致提升。消融：去掉依赖或工具均降点；随用户数增加，性能衰减更慢（Queue 每多一人 -0.35 vs vanilla -1.75）。

**最值得记住的一句话**：把组织约束显式做成任务依赖图与检索/过滤/关系遍历工具，比单纯给 LLM 塞多用户历史更稳、更省，是单智能体向组织级智能体迁移的可复用路径。
