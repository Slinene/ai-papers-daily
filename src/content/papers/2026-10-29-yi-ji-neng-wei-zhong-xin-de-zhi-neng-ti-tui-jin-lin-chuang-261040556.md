---
title: Advancing Clinical Genomic Analysis with a Skill-Centred Agent
title_zh: 以技能为中心的智能体推进临床基因组分析
authors:
- Qiaoyu Zheng
- Weike Zhao
- Yanjie Fan
- Ye Cao
- Mengqi Jiang
- Xiao Zhou
- Xiaoman Zhang
- Pengcheng Qiu
- Yongguo Yu
- Yanfeng Wang
affiliations:
- Shanghai Jiao Tong University
- Shanghai AI Laboratory
- Xinhua Hospital affiliated to Shanghai Jiao Tong University School of Medicine
- The Chinese University of Hong Kong
- Shanghai Chest Hospital, Shanghai Jiao Tong University School of Medicine
arxiv_id: '2610.40556'
url: https://arxiv.org/abs/2610.40556
pdf_url: https://arxiv.org/pdf/2610.40556
published: '2026-10-29'
collected: '2026-11-01'
category: Agent
direction: LLM Agent 技能编排与临床决策支持
tags:
- LLM Agent
- Skill Composition
- Clinical Genomics
- Human-AI Collaboration
- Task Retrieval
- Dependency Orchestration
one_liner: ClinGeX智能体组合105个可执行临床基因组技能，留出基准一致性71.7%，远超最强对比45.7%
practical_value: '- 技能化封装领域能力：将推荐/搜索系统中的召回、排序、过滤、解释等环节封装为可执行技能（API/工具），LLM 根据任务上下文检索并组合，而非直接生成，可显著提升可控性与可维护性，尤其适合多步骤重决策场景。

  - 任务特异检索与依赖感知编排：为不同业务场景（新品、促销、长尾商品）维护技能索引，按任务类型动态检索少量相关技能，减少 prompt 长度；同时用 DAG 管理技能依赖（先召回后排序、先过滤后解释），避免
  Agent 乱序调用。

  - 人机协作评估设计：借鉴其三条件对照（无 AI、通用 LLM、专用 Agent）和真实世界反馈，在电商运营/算法协作中量化专家采纳率与效率提升，避免只看离线指标。

  - 时间留出验证：采用 temporally held-out 切分评估，防止信息泄漏，推荐系统模型迭代中也应严格按时间切割验证集，评估泛化能力。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**  
临床基因组分析需整合不断更新的指南、数据库与计算证据，人工流程复杂且耗时，已成为精准医疗的瓶颈。  

**方法关键点**  
开发 ClinGeX，一个 LLM Agent，组合 105 个精心策划的可执行领域技能；通过任务特定检索（task-specific retrieval）从技能库中动态选取相关技能，并通过依赖感知编排（dependency-aware orchestration）按 DAG 顺序执行。技能作为封装好的可执行模块，由 Agent 负责分解任务、检索并调用，而非依赖模型直接生成结论。  

**关键结果**  
在 223 个时间留出基准案例上，ClinGeX 达到 71.7% 宏观平均任务级一致性，最强对比方法仅 45.7%。在 45 名临床基因组专业人士参与的三条件平衡人机协作研究中，ClinGeX 辅助将原始案例级一致性提升至：变异分析 51.1%、罕见病基因组解释 57.8%、分子肿瘤决策 64.4%，对比条件下仅为 15.6%、31.1%、20.0%，同时减少所有场景的解释时间。一个月真实世界评估中，11 名专家提交 96 次分析反馈，报告频繁采纳结论并节省时间。
