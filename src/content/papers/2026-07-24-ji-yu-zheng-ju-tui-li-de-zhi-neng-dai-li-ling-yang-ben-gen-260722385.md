---
title: Agentic Root Cause Analysis through Evidence-Grounded Reasoning
title_zh: 基于证据推理的智能代理零样本根因分析框架
authors:
- Amaury Wei
- Olga Fink
affiliations:
- EPFL - IMOS Laboratory
arxiv_id: '2607.22385'
url: https://arxiv.org/abs/2607.22385
pdf_url: https://arxiv.org/pdf/2607.22385
published: '2026-07-24'
collected: '2026-07-27'
category: Agent
direction: 工业诊断 · Agent推理
tags:
- AgentRCA
- Root Cause Analysis
- LLM
- Digital Twin
- Evidence-Grounded Reasoning
- Zero-shot
one_liner: 零样本Agent框架结合数字孪生与LLM推理，迭代收集证据并评估假设，实现可解释工业根因诊断，性能比肩全监督方法
practical_value: '- **Agent推理模式迁移**：将“假设生成-证据收集-假设验证”的迭代闭环引入推荐/搜索系统的异常诊断（如CTR骤降、召回池突变），可利用LLM生成可疑原因假设，调用监控工具获取统计证据，自动定位根因。

  - **数字孪生思路**：构建线上系统的正常行为孪生模型（如流量分布基线、转化率时序基线），作为“正常期望”参考，Agent通过对比实时行为与孪生模型残差来识别异常根源，摆脱对故障标注数据的依赖。

  - **可解释诊断链**：借鉴透明推理轨迹，在业务诊断中输出可审计的因果链（观察症状→排除归因→确认主因），提升算法团队排障效率，并可沉淀为知识库。

  - **零样本冷启动应用**：针对罕见故障或新上线模块的异常，无需历史故障样本，直接基于系统领域知识图谱和实时数据驱动逻辑进行诊断，快速响应。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：工业系统根因分析依赖人工假设与证据收集，现有数据驱动方法黑箱不可解释，且需大量故障标注数据。需要一种零样本、可解释的自动化诊断框架。

**方法**：提出AgentRCA，一个零样本代理框架。核心组件：
- **数据驱动数字孪生**：建模系统正常动态，作为期望行为基线。
- **工具增强LLM代理**：集成统计检验、残差分析等工具，迭代执行“假设生成-证据收集-假设评估”循环。
- **推理流程**：代理观测异常症状，生成候选物理故障假设；调用工具计算残差、执行假设检验；根据统计证据更新假设概率，最终选择最符合观测的根因。

**关键结果**：在真实多相流设施和大规模化工厂数据上，零样本AgentRCA的诊断性能与全监督基线的XGBoost、因果发现等方法相当（F1超过0.85）。输出透明推理链，显式关联症状与物理原因，且无需任何故障训练样本。
