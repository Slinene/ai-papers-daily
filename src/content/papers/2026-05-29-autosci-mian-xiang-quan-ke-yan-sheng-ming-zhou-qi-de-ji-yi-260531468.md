---
title: 'AutoSci: A Memory-Centric Agentic System for the Full Scientific Research
  Lifecycle'
title_zh: AutoSci：面向全科研生命周期的记忆中心多智能体系统
authors:
- Weitong Qian
- Beicheng Xu
- Zhongao Xie
- Bowen Fan
- Guozheng Tang
- Jiale Chen
- Xinzhe Wu
- Mingtian Yang
- Chenyang Di
- Jiajun Li
affiliations:
- Peking University
arxiv_id: '2605.31468'
url: https://arxiv.org/abs/2605.31468
pdf_url: https://arxiv.org/pdf/2605.31468
published: '2026-05-29'
collected: '2026-06-01'
category: MultiAgent
direction: Agent · 多智能体协作与自进化科学发现
tags:
- Memory
- MultiAgent
- Scientific Discovery
- Evolving
- DAG
one_liner: 提出 AutoSci，通过结构化持久记忆、流程控制、多智能体增强与自进化，实现跨项目可复用的全周期科研自动化。
practical_value: '- 借鉴 SciMem 的分区记忆设计：长期知识记忆（领域/论文/概念/方法/研究者等实体）与活跃研究记忆（想法/实验/稿件/评审）分离，电商
  Agent 可类比用户兴趣图谱、商品知识库与当前会话状态的隔离，避免上下文污染与幻觉。

  - SciDAG 的多智能体 DAG 编排模板：通过可复用的算子图（生成、辩论、精炼、评审等）自适应执行复杂任务，可用于推荐系统中的多路召回融合、策略辩论、解释生成等，条件边实现动态流程控制。

  - SciEvolve 的自进化机制：将用户反馈、实验失败等信号转化为版本化更新，可迁移到 Agent 系统的持续优化中，例如定期分析对话失败模式，自动调整 prompt、工具选择或流程步骤，提升系统鲁棒性。

  - 信任守护（Trust Guard）设计：对记忆写入进行形式与内容双重验证，可引入到电商知识库更新或模型生成内容的校验环节，避免错误信息传播至下游决策。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**  
科学研究长期依赖人工协调文献、想法、实验、稿件和评审，过程碎片化且复用性差。现有 LLM 驱动的科研智能体多聚焦单次任务或局部能力，缺乏贯穿全生命周期的持久记忆与自我进化机制，难以形成可积累、可进化的研究环境。

**方法关键点**  
AutoSci 构建了一套记忆中心、模块化的智能体系统，共四大模块：
- **SciMem**：模式管控的研究记忆，分离长期知识记忆（Topic、Paper、Concept、Method、People 等实体，含类型化关系图）与活跃研究记忆（Idea、Experiment、Manuscript、Review 等带生命周期状态的实体），通过双向流动实现知识跨项目累积。
- **SciFlow**：五阶段科研生命周期（文献→构思→实验→写作→反驳），通过 Harness 提供状态记录、上下文构建、验证阻断、反馈路由和可恢复编排，保证长周期执行的可审计与可续接。
- **SciDAG**：DAG 形多智能体增强层，内置 generate、variation、debate、refine、review 等可复用算子，以自适应算子图应对困难阶段，并配有阶段专用模板。
- **SciEvolve**：从用户、实验和评审信号中启动 /dream、/forge、/morph 三条进化路径，分别优化 SciMem 结构、SciFlow 技能流程和 SciDAG 模板，实现全系统版本化演进。

**关键结果**  
在 GPU 内核优化和生物医学药物发现两个端到端案例中，AutoSci 完成了从文献消化到论文生产的完整流程，耗时分别为 27.3 和 22.6 小时。生成的论文通过 ICLR 自动化评审获得 6.3/10 和 5.8/10 的分数。其中 GPU 案例中，系统自主筛选出最佳研究方向，执行包含灵敏度分析、主实验、消融和中间数据审计的实验套件，最终生成 157 个全正确内核，几何平均加速比达 1.52 倍（剔除退化基线后 1.18 倍），并给出反馈机制贡献 1.58 倍增益的消融证据。
