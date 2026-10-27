---
title: 'Work Agents: Systems, Capabilities, and Optimization'
title_zh: 工作智能体：系统、能力与优化
authors:
- Zishan Xu
- Enjun Du
- Mingqi Gao
- Cheng Yang
- Junhao Shen
- Zirong Chen
- Zhiyuan Yao
- Yifu Guo
- Yuquan Lu
- Jinyang Huang
affiliations:
- Shanghai Jiao Tong University
- The University of Hong Kong
- The Hong Kong University of Science and Technology (Guangzhou)
- Tsinghua University
- The Chinese University of Hong Kong
arxiv_id: '2610.35845'
url: https://arxiv.org/abs/2610.35845
pdf_url: https://arxiv.org/pdf/2610.35845
published: '2026-10-25'
collected: '2026-10-27'
category: Agent
direction: Agent 工作系统与优化框架
tags:
- Work Agents
- Foundation Models
- Agent Capabilities
- Harness Optimization
- Evaluation
one_liner: 以工作为中心给出工作智能体的系统级框架，用持久性与开放性刻画条件并划分五类数字工作，梳理能力与优化路径
practical_value: '- 用“工作持久性/开放性”给 Agent 任务分级：电商客服、推荐解释等低持久性对话可轻量处理；跨系统选品、投放、报表等高持久性任务需要状态化工作空间、checkpoint
  与回滚机制。

  - 五层工作形式可做架构拆分：对话层做查询理解，原子动作层做商品/内容编辑，多步层做依赖动作，工作流层做跨团队 handoff，工作空间层做跨对象依赖追踪；据此把
  LLM 调用边界和工具接口设计清楚。

  - 除模型微调外先优化 harness：工具说明、状态存储、错误恢复、RAG 上下文等往往能低成本提升搜索推荐 Agent 可靠性，再逐步引入 LoRA/SFT
  联合优化。

  - 评估以可验证工作产出为中心：定义任务完成率、交付质量、回滚率、依赖一致性等指标，避免只比 BLEU/ROUGE；对 push 文案生成/query 推荐也要看业务转化与可执行性。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：基础模型正从生成信息转向执行数字工作，Agent 已能跨工具、应用和工作流完成复杂任务，但缺乏统一视角理解其如何可靠完成委派工作，导致系统设计、能力评估和优化各自为战。

**方法关键点**：以工作为中心提出系统级框架，将工作 Agent 视为基础模型 + 运行时 harness，在状态化工作空间中执行任务并交付可验证结果。用两个维度刻画工作条件：工作持久性（状态保留多久、依赖多深）和工作开放性（环境与工具是否可变）。按任务范围和组织将数字工作分为五类：对话层、原子动作层、多步层、工作流层、工作空间层；对应识别五类核心能力族。进一步梳理模型优化、harness 优化以及二者联合优化路径，并从工作结果角度分析评估方法与指标。

**关键结果数字**：核心贡献是 2 个维度、5 种工作形式、5 个能力族的统一分类框架，并给出优化与评估的结构化地图；无传统实验指标，属于框架性综述，为可靠、可验证的工作 Agent 系统建设提供基础。
