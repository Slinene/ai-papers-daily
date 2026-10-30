---
title: 'WebAnything: From the Wild Web to Scalable Agent Environments'
title_zh: WebAnything：从野生网络到可扩展 Agent 环境
authors:
- Tianci Xie
- Zikun Cai
- Chaoyun Zhang
- Pinxue Guo
- Bingxuan Li
- Rui Zheng
- Hang Yan
affiliations:
- Zhejiang University
- Nanyang Technological University
- Shanghai Qiji Zhifeng Co., Ltd.
arxiv_id: '2610.37786'
url: https://arxiv.org/abs/2610.37786
pdf_url: https://arxiv.org/pdf/2610.37786
published: '2026-10-26'
collected: '2026-10-30'
category: Agent
direction: Web Agent 环境自动构建与规模化
tags:
- Web Agents
- Environment Construction
- Fine-tuning
- Trajectory Data
- Automatic Evaluation
one_liner: 全自动从真实 URL 重建可重置 Web 环境，构建 244 个网站并微调模型显著提升多项 agent 成功率
practical_value: '- 借鉴自动化环境构建架构：用浏览器自动化收集 DOM/资源/交互结果，配合独立验证器做质量门禁，可为电商类 Agent 搭建可回归的评测环境，避免手工维护镜像站。

  - 利用真实网站交互轨迹微调开源模型：从线上商品页、搜索流程捕获的轨迹数据经筛选后可作为高质量训练样本，微调 Qwen 等模型对导航、加购、表单填写等任务提升明显；重点保留任务多样性和失败重试样本。

  - 验证器 + 本地修复闭环可复用到数据管道或 RAG 索引构建：独立验证器检查生成内容并触发定向修复，减少人工介入，适合维护大规模商品知识库或 Agent 记忆。

  - 可重置环境支持多轮重跑与错误恢复，适合做 Agent 策略 A/B 测试；可将电商搜索链路中的商品抓取、竞品价格监控等流程抽象为可执行任务，加速迭代。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Web agent 训练评估需要多样、可执行、可重置的网站环境，现有人工镜像逐站工程成本高，生成式构建可能偏离真实网站，捕获回放则受捕获内容和回放能力限制。

**方法**：WebAnything 全自动框架从真实 URL 重建源锚定、可复用的网站环境，初始设置与授权后无需逐站手工实现或修复。Explorer-Builder 收集浏览器可观察结构、资源及交互结果；独立验证器检查冻结候选，指导本地修复或定向源重新捕获，保证环境与真实网站一致。

**结果**：自动构建 244 个网站 artifact，覆盖 14 个领域 53 个类别，支持 12,984 个已执行和接受任务。对比人工辅助 WebHarbor，三个保真度指标综合得分更高，盲审 12 胜 2 平 0 负。基于 5,856 条交互轨迹微调 Qwen3.5-9B，REAL 成功率提升 9.9 个百分点，Odysseys-Easy Rubric Avg 与 Task Avg 分别提升 6.25 和 6.32 个百分点，WebArena-Verified Overall 成功率提升 13.33 个百分点（固定 harness）。代码开源。
