---
title: Environment-free Synthetic Data Generation for API-Calling Agents
title_zh: 面向 API 调用 Agent 的无环境合成数据生成
authors:
- Seanie Lee
- Sanjoy Chowdhury
- Chao Jiang
- Cheng-Yu Hsieh
- Ting-Yao Hu
- Alexander T Toshev
- Oncel Tuzel
- Raviteja Vemulapalli
affiliations:
- Apple
arxiv_id: '2607.16900'
url: https://arxiv.org/abs/2607.16900
pdf_url: https://arxiv.org/pdf/2607.16900
published: '2026-07-17'
collected: '2026-07-21'
category: Agent
direction: Agent 训练 · 合成数据生成
tags:
- Agent
- Synthetic Data
- LLM Simulation
- API Calling
- Data Generation
one_liner: 仅凭 API 规范，用 LLM 模拟世界模型生成完整交互轨迹，无需可执行环境即可训练 API 调用 Agent
practical_value: '- 可直接应用于电商搜索/推荐 Agent：无需搭建完整 API 后端（如商品查询、订单状态 API），仅凭接口文档即可生成大量多轮训练轨迹，降低环境依赖。

  - LLM 模拟 API 响应时，通过注入任务上下文和交互历史保持状态一致性，可借鉴该思路为推荐 Agent 生成会话数据（如用户连续查询、筛选、下单）。

  - 使用 LLM 评委过滤低质量轨迹，确保数据质量，可复用该自动质控流水线于企业内的 Agent 训练数据生产。

  - 方法不依赖具体领域，可快速适配新 API 生态，适合多业务线（如搜索、广告、客服）快速冷启动 Agent 训练。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：训练 API 调用型 LLM Agent 需要大量多步交互轨迹，但构建带有可执行 API 和真实数据库的环境成本极高，限制了数据的规模化。  
**方法**：仅提供 API 规范，利用 LLM 作为即时世界模型。流程为：① 由 LLM 依据 API 生成多样化任务；② 教师 Agent 逐步完成任务，同时 LLM 模拟器根据任务上下文和历史动态生成一致的合成 API 响应；③ LLM 评委过滤低质量轨迹。整个过程无需任何可执行环境，生成轨迹涵盖信息检索和状态修改类任务。  
**结果**：在 AppWorld 和 OfficeBench 两个挑战性基准上，用合成数据微调的模型取得显著性能提升，证明有效的监督信号可完全来自无环境合成，为跨 API 生态的 Agent 训练提供了可扩展方案。
