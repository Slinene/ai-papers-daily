---
title: 'AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems'
title_zh: AgentX：面向工业推荐系统的智能体驱动自我迭代
authors:
- Changxin Lao
- Fei Pan
- Guozhuang Ma
- Han Li
- Huihuang Lin
- Jijun Shi
- Kangzhi Zhao
- Kun Gai
- Mo Zhou
- Qinqin Zhou
affiliations:
- Kuaishou
arxiv_id: '2606.26859'
url: https://arxiv.org/abs/2606.26859
pdf_url: https://arxiv.org/pdf/2606.26859
published: '2026-06-25'
collected: '2026-06-26'
category: MultiAgent
direction: 多智能体闭环驱动推荐策略与模型自进化
tags:
- Multi-Agent
- Self-Evolution
- Recommender System
- LLM
- A-B Testing
- Production
one_liner: 生产部署的多智能体闭环，自主生成、实现、评估并进化推荐实验，实现业务收益的复利增长。
practical_value: '- **构建推荐迭代闭环智能体**：将“想法→代码→A/B评估→知识沉淀”全流程 agent 化，把工程师从重复性劳动（拉数据、改配置）中解放，直接复用至电商/广告推荐策略迭代，显著提升实验并发量与产出速度。

  - **证据加权生成与防重复机制**：用实验 KB、系统 KB、数据分析、模型研究四类知识源对候选想法打分，自动过滤重复、不可行或违背护栏的策略，避免“重新发明失败”，可借鉴到搜索推荐实验管理平台。

  - **生产代码可靠性保障**：通过仓库模式查询、DSL 检查器、静态 lint 等多维验证，防止 LLM 生成代码时的属性幻觉和注册缺失，大幅降低人工介入，适合在自动化投放引擎或特征平台落地。

  - **离线模型研究的可信归因**：强制每个模型改动声明因果链和可观测量，并用专家投票与日志确定性提取来判断收益是否可信，防止无法归因的 AUC 增益污染知识库，对工业级
  AutoML 或模型迭代管线有直接参考意义。

  - **基于轨迹的自我进化（SGPO）**：利用执行轨迹的语义梯度持续优化 prompt，形成“越用越强”的飞轮，可迁移至其他需要持续改良的 agent 系统（如广告文案生成、动态排序策略优化）。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推荐系统迭代长期依赖工程师手工进行数据分析、编码、上线和归因，创新速度与人力数量线性绑定，大量时间消耗在重复性工作上，且经验难以沉淀。现有 LLM 驱动的 AutoML 或研究自动化大多离线闭环，缺乏真实在线反馈、工业规模验证和持续进化能力。AgentX 旨在将推荐迭代重构为多智能体驱动的自我进化闭环，让 agent 自主完成从模糊意图到安全上线的完整链路，并通过在线 A/B 结果持续优化自身，实现“工程师杠杆”向“系统复利”的转变。

### 方法关键点
- **多智能体闭环架构**：Brainstorm Agent（想法生成与证据加权筛选）→ Developing Agent（在线策略与离线模型双轨实现）→ Evaluation Agent（安全部署与护栏否决的 A/B 判决）→ Harness Evolution（基于轨迹的语义梯度提示优化，持续提升各 agent 能力）。
- **Brainstorm Agent**：使用实验 KB、系统 KB、数据分析、模型研究四类知识源对候选想法进行加权评分，过滤重复、不可行或违反业务约束的提案，并将输出分为“可实施”“需探查”“远期储备”三个成熟度状态。
- **Developing Agent**：在线策略开发通过仓库模式查询、DSL 检查、静态 lint 等工具强制属性校验，杜绝幻觉；代码质量用八个维度（属性幻觉、注册完整性、人工干预等）加权打分。模型开发要求声明因果链和可观测量，经专家共识投票和确定性指标提取，仅当因果链全部验证时才记录收益。
- **Evaluation Agent**：对接工业 A/B 平台，自动安全流量分配、CUPED/DiD 统计判决与护栏否决，同时将负结果结构化资产化，为后续迭代提供约束。
- **自进化（SGPO）**：收集每次实验的完整轨迹，通过语义梯度优化反向更新各 agent 的 prompt 与流程，实现长期性能累积提升。

### 关键结果
- 在快手主 feed 和生活服务推荐场景部署三周，3 个 AgentX worker 将 374 个初始想法转化为 10 个可上线实验，人均产出每周翻倍。
- 相比人类工程师，实现 8× 的并发实验能力和 3.7× 的商业价值，用户 APP 使用时长提升 0.561%，年化收入增量超过 1 亿元人民币。
- 自我进化效果：随着时间推移，agent 代码错误率下降，实验成功率上升，证明闭环持续改进的有效性。
