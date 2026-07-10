---
title: 'WebSwarm: Recursive Multi-Agent Orchestration for Deep-and-Wide Web Search'
title_zh: WebSwarm：面向深度和广度网络搜索的递归多智能体编排
authors:
- Xiaoshuai Song
- Liancheng Zhang
- Kangzhi Zhao
- Yutao Zhu
- Zhongyuan Wang
- Guanting Dong
- Jinghan Yang
- Han Li
- Kun Gai
- Ji-Rong Wen
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
- Kuaishou Technology
arxiv_id: '2607.08662'
url: https://arxiv.org/abs/2607.08662
pdf_url: https://arxiv.org/pdf/2607.08662
published: '2026-07-09'
collected: '2026-07-10'
category: MultiAgent
direction: 递归多智能体编排优化深度与广度搜索
tags:
- multi-agent
- recursive-delegation
- web-search
- LLM-agent
- orchestration
- information-seeking
one_liner: 通过动态递归委派将任务分解与四种搜索模式结合，并用网页结构探测和经验复用提升多智能体搜索的深度与覆盖度
practical_value: '- **递归分解与模式化协作**：将复杂查询递归分解为搜索节点，每个节点根据本地目标选择协作模式（精确查证、迭代验证、并行宽搜、集合枚举），可迁移到电商属性补全、多条件商品筛选、榜单构建等场景，避免固定流程的僵化。

  - **网页结构探测**：先轻量探测目标信息在站内的组织方式（按类目/品牌/属性聚合还是分散），再决定并行扩展的粒度，可减少搜索/爬虫调用量（实验中工具调用降低40%以上），适合电商中动态决定是遍历类目还是直接查聚合页。

  - **同胞节点经验复用**：在批量处理同质商品（如补全不同品牌的商品属性）时，先用少量样本抽取出有效的搜索模式、可靠数据源和失败路径，再注入后续节点，可显著提升“宽搜”的准确率，降低重复试错。

  - **模式化的搜索节点设计**：atom、deep、wide、entity_collect 四种模式对应了搜索系统中“精准查询、链式推理、宽表填充、开放集合召回”的典型需求，可为构建可编排的搜索代理提供工程化参考。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
LLM 驱动的网络搜索代理正从简单问答向需要深度推理与广泛信息覆盖的复杂任务演变。单 ReAct 代理受限于单一长轨迹和有限上下文，难以同时兼顾深度和广度；现有多代理系统常只在根层分解、采用固定协作模式且分解与网页信息结构不匹配，导致冗余检索或召回不足。  
**方法**  
提出 WebSwarm，一种渐进式递归多代理委派框架：  
- **递归搜索树**：根节点接收原任务，动态创建搜索节点，每个节点接收本地目标 (q) 与搜索模式 (m)，可自行解决或继续委派子节点，并将结果返回上层供进一步扩展或修正。  
- **四种搜索模式**：atom（直接查证）、deep（串行搜索-验证迭代）、wide（并行分治宽搜）、entity_collect（多路召回+去重验证），根据子任务瓶颈分配不同协作结构。  
- **网页结构引导**：对需宽扩展的节点，先执行轻量网页探测得到信息分布线索（集中型聚合页 vs 按维度分散），据此决定子节点扩展轴，避免错配。  
- **同胞节点经验复用**：在同质批量子任务中，先执行少量侦察节点，从轨迹中提取可用查询模式、可靠信源和无效路径，注入后续节点，提升求解质量与一致性。  
**实验**  
在 BrowseComp-Plus（深度搜索）、WideSearch（宽表收集）、DeepWideSearch（交织搜索）和 GISA（通用搜索）四个基准上，以 GLM-4.5 为基座，WebSwarm 相比 ReAct 代理：BrowseComp-Plus 准确率从 50.5→68.0（+17.5 点），WideSearch Item F1 从 64.61→74.37（+9.76），DeepWideSearch Item F1 从 46.63→58.40（+11.77）。在困难样本上优势更明显，且网页探测大幅降低工具调用（WideSearch 平均调用从 239.9 降至 137.0），在不同模型上均表现一致。  
**一句话核心**  
将搜索抽象为递归的“目标-模式”节点，让分解、协作与证据反馈共同演进，并用网页结构探测与兄弟节点经验做双轨引导。
