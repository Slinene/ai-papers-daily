---
title: Personalized Communication Skills for Agentic Recommender Systems
title_zh: 面向智能推荐系统的个性化沟通技能框架
authors:
- Zongwei Wang
- Min Gao
- Guangyu Hu
- Xinyi Gao
- Junliang Yu
affiliations:
- 重庆大学
- 昆士兰大学
arxiv_id: '2608.08417'
url: https://arxiv.org/abs/2608.08417
pdf_url: https://arxiv.org/pdf/2608.08417
published: '2026-08-09'
collected: '2026-08-11'
category: Agent
direction: Agent 通信 · 个性化技能路由
tags:
- Agentic Recommender Systems
- Agent Communication
- Skill Routing
- Failure-Driven Evolution
- Perspective Narrowing
one_liner: 提出 why-what-how-who 技能库与个性化路由，让智能推荐代理通过外部用户互补证据纠正视角狭窄
practical_value: '- **构建可复用的沟通技能库**：借鉴 why-what-how-who 层次结构，在电商/广告推荐的 Agent 评估环节，预先定义决策缺陷（冷启动/选择冲突等）→
  信息需求 → 交互协议（单人/多人协作/竞争）→ 顾问选择（相似用户/信任用户），形成可查询的模板库，避免每次对话都从零设计 prompt。

  - **动态路由替代固定通信流程**：利用 LLM 根据当前用户状态、候选集与已有证据，依次从四个层次选择最合适的技能节点，而非采用单一对话策略；可用于推荐解释、争议推荐二次确认等场景。

  - **失败驱动的自动进化**：当 Agent 的最终选择出错时，诊断通信失败的原因并自动生成新的子技能或同级技能，实现技能库的自我扩展；可迁移到在线推荐策略迭代中，从
  bad case 自动归纳新规则。

  - **可控的通信成本与性能平衡**：实验表明，多轮用户-顾问交互能持续提升 Hit@1（3 轮达最优），但顾问内部过多讨论反而有害；部署时可设置最大交互轮次，并在顾问间采用简洁的单轮协议，以较低
  API 成本（<0.01$/用户）换取显著推荐增益。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现有 LLM 驱动的 UserAgent 在评估推荐候选时仅依赖自身历史，容易产生视角狭窄（perspective narrowing），忽视互补的偏好信号。引入其他用户作为顾问 Agent 可提供外部证据，但统一的通信流程无法适应不同决策状态（如冷启动、选择犹豫、新颖性不确定）。因此需要一种个性化、可复用的通信技能框架。

**方法关键点**：
- 构建 **why-what-how-who 四层公共技能库**：why 层诊断决策缺陷（冷启动、候选冲突、新颖疑虑等）；what 层将缺陷转化为具体信息任务（缩小犹豫集、搜索感兴趣子集、比较候选等）；how 层选择顾问交互协议（单人、多人协作、多人竞争）；who 层根据相似度、信任度、经验等检索合适顾问。
- **个性化技能路由**：为每个用户在每个推荐轮次，LLM 路由器依次从技能库中条件排序并选择最合适的节点，形成完整通信路径，避免固定流程。
- **失败驱动技能进化**：分析错误决策的通信轨迹，定位失败层，区分三种原因：（1）技能不足 → 生成子技能细化现有技能；（2）能力缺失 → 生成新的同级技能；（3）路由不当 → 仅修正路径而不更新技能库。技能库在训练中迭代进化。

**关键结果**：
- 在 LastFM、Epinions、LibraryThing 三个数据集上，将 AgentCom 叠加于 SASRec、GBS、AFL、iAgent、MemRec 等 backbone，Hit@1 均获得显著提升（例如 SASRec 在 LastFM 上从 0.0155 提升至 0.2019；MemRec 在三个数据集上分别提升 1.8%、2.4%、8.4%）。
- 消融实验证明每一层及进化机制均为有效贡献；去除所有层时性能大幅下降。
- 超参数分析显示，最大通信轮数设为 3 时性价比最高；过多顾问内部讨论（>1 轮）反而损害性能。
- 案例分析表明 AgentCom 能纠正视角狭窄、澄清模糊偏好，但也会因过度强调次要特征导致误判。

**核心洞察**：用结构化的 why-what-how-who 可复用技能库替代通用对话，使 Agent 能动态组合外部证据，是提升推荐决策鲁棒性的高效且低成本的路径。
