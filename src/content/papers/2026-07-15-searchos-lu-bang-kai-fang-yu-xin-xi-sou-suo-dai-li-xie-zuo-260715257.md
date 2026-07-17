---
title: 'SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration'
title_zh: SearchOS：鲁棒开放域信息搜索代理协作框架
authors:
- Yuyao Zhang
- Junjie Gao
- Zhengxian Wu
- Jiaming Fan
- Jin Zhang
- Shihan Ma
- Yao Yao
- Weiran Qi
- Chuyan Jin
- Guiyu Ma
affiliations:
- Renmin University of China
- Ant Group
arxiv_id: '2607.15257'
url: https://arxiv.org/abs/2607.15257
pdf_url: https://arxiv.org/pdf/2607.15257
published: '2026-07-15'
collected: '2026-07-17'
category: MultiAgent
direction: 多Agent协作搜索 · 状态驱动流水线调度
tags:
- Multi-agent system
- Search agent
- Stateful orchestration
- Relational schema completion
- Evidence graph
- Pipeline parallelism
one_liner: 用关系模式补全、状态外部化与流水线调度构建稳健多Agent搜索系统，大幅提升信息收集完整性与效率
practical_value: '- **共享搜索状态外部化**：借鉴SOCM，将推荐/搜索Agent的上下文（如用户画像、已覆盖类目、缺失属性）存为显式的Frontier
  Task、Evidence Graph和Coverage Map，避免多轮交互中遗忘或重复采集，可直接用于电商中的长会话购物助手或广告素材搜集Agent。

  - **流水线并行调度提效**：采用事件驱动的任务分发，每次Agent槽空闲时立即填充未覆盖的schema缺项，消除Batch同步等待，可在多路并行召回或多源信息聚合推荐系统中降低延迟、提高吞吐。

  - **中间件拦截机制**：在模型与工具调用之间插入中间件，自动完成证据锚定、覆盖率更新、重复循环检测和预算管控，无需依赖模型自身记忆，这一范式可迁移到Agentic推荐系统的可靠执行层，例如拦截商品搜索API调用并抽取结构化属性。

  - **分层可复用技能库**：将搜索策略与站点访问封装为Strategy / Access技能，支持按任务和源头路由，有效减少试错次数；在推荐系统中可类似地抽象数据源访问（如商品库、评价接口）为技能，加速不同垂类场景的Agent开发。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
长程开放域信息搜索中，随着交互轮次增加，Agent容易丢失任务进度，陷入重复查询、死循环，浪费搜索预算，最终答案完整性和可靠性下降。现有单/多Agent系统将规划、进度、证据和失败都当成瞬时对话内容，缺乏系统级的持久状态管理。

**方法关键点**  
1. **关系模式补全形式化**：将信息搜索定义为带接地引用的关系模式补全——发现实体、填充属性，每个value锚定到具体来源URL和片段，使进度可量化。  
2. **Search-Oriented Context Management（SOCM）**：将共享搜索状态外部化为四个持久构件：**Frontier Task**（带依赖的任务池）、**Evidence Graph**（原子证据及其溯源）、**Coverage Map**（每个schema单元格的填充状态）和**Failure Memory**（无效查询、不可访问网站等失败记录）。Agent通过角色特定投影访问状态，而非遍历全量历史。  
3. **流水线并行编排**：采用Orchestrator‑Worker架构，通过Continuous Dispatch按优先级即时填充执行槽，消除了同步Batch的闲置等待，在高并发下提升槽位利用率和吞吐。  
4. **Search Tool Middleware Harness**：在Agent循环的三个节点——模型调用前（注入上下文、技能、裁剪历史）、工具观察后（提取、绑定、提交证据，更新Coverage）以及停滞/预算超限时（注入纠正指令或终止分支）——进行系统级拦截，确保可靠性。  
5. **层次化搜索技能**：预建280个技能，分为Orchestrator（全局协调）、Strategy（任务无关的查询重构、多跳推理等）和Access（针对特定网站的检索与提取，可包含可执行代码），按需路由复用，减少试错。

**关键实验**  
在WideSearch（200道真实跨域宽搜）和GISA（373道结构化搜索）两个基准上评测。与ReAct、Plan‑and‑Solve等单Agent及A‑MapReduce、Web2BigTable等多Agent基线相比：  
- WideSearch **Item F1 80.3**（提升4.3点），Row F1 56.5（提升2.0点）。  
- GISA **Set F1 76.5**（大幅领先最强基线13.4点），Table、List、Item类型指标也全面领先。  
消融证实：动态schema规划超越固定单/多表；流水线调度减时24.3%且F1更高；中间件能有效重定向停滞搜索；技能库使搜索时间缩短36.6%，搜索调用减少39.1%，且Row F1提升3.4点。  

**关键洞察**  
“搜索状态应由系统维护，而不是反复从交互历史中推断”——这一思想贯穿设计，将搜索进度、证据和失败显式化为可操作的中间件状态，是迈向鲁棒多Agent信息协作的关键一步。
