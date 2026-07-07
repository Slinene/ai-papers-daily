---
title: 'Autonomous Information Seeking: A Roadmap for Agentic Recommender Systems'
title_zh: 自主信息寻求：Agentic 推荐系统的路线图
authors:
- Xinyu Lin
- Yashar Deldjoo
- Sunhao Dai
- Honghui Bao
- Xiaopeng Ye
- Fatemeh Nazary
- Wenjie Wang
- Tommaso Di Noia
- Jun Xu
- Tat-Seng Chua
affiliations:
- National University of Singapore
- Polytechnic University of Bari
- Renmin University of China
- University of Science and Technology of China
arxiv_id: '2607.04433'
url: https://arxiv.org/abs/2607.04433
pdf_url: https://arxiv.org/pdf/2607.04433
published: '2026-07-05'
collected: '2026-07-07'
category: RecSys
direction: Agent 推荐系统自主性等级与范式综述
tags:
- Agentic RS
- Level of Autonomy
- Multi-Agent
- RAG
- LLM Agent
- Survey
one_liner: 提出融合自主性等级与三种代理范式的统一分类法，系统梳理 LLM 代理如何改造推荐系统
practical_value: '- **用 LoA 定位架构取舍**：把自家系统映射到 L0–L5 谱系，明确当前痛点是工具调用（L3）、单 Agent 规划（L4）还是多
  Agent 协同（L5），避免一上来就堆多 Agent。

  - **Agent 辅助而非替代**：多数业务不需要 Agent 端到端取代原有推荐 pipeline。借鉴 L2–L3 的检索增强与工具驱动辅助模式，用 LLM
  Agent 做意图理解、约束推理、解释生成，保持原有召回/排序的稳定性。

  - **Memory 设计三件套**：采纳 working/episodic/semantic memory 的分层设计，用短期对话摘要、跨 session 偏好记忆、语义知识库支撑个性化决策，在电商中可对应“购物车-历史订单-品类偏好”记忆体系。

  - **多 Agent 协作的通信成本**：从 manager–worker、debate–judge 等协作协议中选型时，优先用结构化工具调用管道而非自由对话，降低长链路中的
  token 消耗与错误累积，并提前设计轨迹级评估指标。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
推荐系统正在从被动排序向主动、多步决策演进，用户目标越来越复杂（如度假规划、预算约束下的搭配推荐）。LLM 虽然增强了语言与推理能力，但多数 LLM-based RS 仍是反应式的，缺乏规划、工具使用和持久记忆。因此，系统性地定义 Agentic 推荐系统（ARS）的自主性等级和架构范式，成为统一快速增长文献、指导工程实践的基础需求。

## 方法关键点
- **自主性等级（LoA）框架**：从 L0（被动排序）到 L6（概念级群体智能），聚焦 L2–L5，主要维度包括任务范围/规划风格、上下文意识/记忆、交互灵活性、自适应能力。
- **三大代理范式**：
  - *Agent-assisted*：代理辅助传统推荐管道，承担意图理解、检索增强、工具调用（L2–L4）。
  - *Agent-as-recommender*：代理端到端负责推荐，单 Agent 或多 Agent 协作（L4–L5），内部划分 Profile、Memory、Tool-using、Workflow、Optimization 五模块。
  - *Agent-as-user-simulator*：代理模拟用户或环境，用于数据合成、评估与鲁棒性测试（L4–L5）。
- **检索增强推荐**：通过偏好接地、物品接地、上下文扩展三功能角色细化 RAG，并引入多步检索流（粗到细、迭代反思、多源融合），支撑 L2 能力。
- **工具驱动辅助**：工具可分为 RecTools、外部信息、属性过滤、多模态工具，代理学习调度而非直接推荐，提升 L3 可控性。
- **单 Agent 推荐器**：利用统一 Profile、分层 Memory（working/episodic/semantic）、ReAct/Plan-then-Execute/Reflex 等工作流，实现自主目标分解与反思。
- **多 Agent 推荐器**：采用 Manager–worker、debate–judge、谈判等协作协议，将认知负载分散到规划、检索、排名、解释、安全等专门代理。

## 关键结果
- 论文统计显示，2024 年至 2025 年 Agentic RecSys 论文数量增长约 3 倍（从约 30 篇到 90 余篇），Agent-as-Recommender 保持主导，Agent-as-Simulator 占比从 13.3% 升至 24.7%，反映模拟评估需求激增。
- 自主性等级方面，L4（单 Agent）始终占 40% 以上，L5（多 Agent）从 22.2% 升至 28.6%，表明从工具辅助向多 Agent 协同的迁移趋势。
- 评价维度上，现有工作关注推荐有效性、输出质量、Agentic 过程质量，但缺乏轨迹级评估和仿真校准，这些被列为开放挑战。

## 最值得记住的一句话
推荐系统正从“模型排序”转向“系统追逐目标”，自主性等级成为理解 Agentic RecSys 架构取舍的第一把钥匙。
