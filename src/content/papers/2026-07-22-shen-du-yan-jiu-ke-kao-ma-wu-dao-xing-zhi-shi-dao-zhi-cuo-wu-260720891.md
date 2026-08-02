---
title: Is Deep Research Reliable? Misleading Knowledge Induces False Conclusions
title_zh: 深度研究可靠吗？误导性知识导致错误结论
authors:
- Pengyu Zhu
- Lijun Li
- Longju Yang
- Sen Su
affiliations:
- Beijing University of Posts and Telecommunications
- Shanghai Artificial Intelligence Laboratory
- Chongqing University of Posts and Telecommunications
arxiv_id: '2607.20891'
url: https://arxiv.org/abs/2607.20891
pdf_url: https://arxiv.org/pdf/2607.20891
published: '2026-07-22'
collected: '2026-08-02'
category: Agent
direction: Agent 可靠性评估与误导知识防御
tags:
- Deep Research
- Misleading Knowledge
- False Conclusions
- LLM Agents
- Reliability
- Evaluation
one_liner: 构建误导性知识评估框架，发现深度研究智能体易受虚假信息影响，错误结论采纳率高达54.7%
practical_value: '- **Agent 信息源验证设计**：可借鉴 MisKnow-Agent 的误导文档构造方式（控制权威性、风格），评估搜索/推荐
  Agent 在面对看似可信但错误信息时的鲁棒性，尤其适用于长周期市场分析、竞品调研等场景。

  - **多阶段验证架构**：论文表明预/后研究防御（如交叉模型验证）能减轻但无法消除错误采纳，启示在 RAG 或 Agent 流程中，需在证据进入中间状态时（如每次检索后）就进行实时验证与修正，而非仅依赖最终报告。

  - **错误采纳率指标 (FCAR)**：可直接复用 FCAR 作为系统脆弱性指标，量化注入误导信息后 Agent 输出错误结论的比例，指导防御策略的迭代优化。

  - **权威性偏见干预**：发现权威来源和正式风格的误导文档更易被采纳，在推荐或搜索 Agent 中可针对性设计去偏模块，如训练模型区分权威度与可信度，避免权威光环效应。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Deep Research 智能体在开放信息环境中进行长程研究时，可能遭遇看似可信但事实错误的误导性知识，而现有研究缺乏对这种脆弱性的系统评估。

**方法**：提出 MisKnow-Agent 评估框架，可控制地构造具有不同权威级别、来源风格的误导文档，并在 DeepResearch Benchmark 任务上生成 5,933 个高质量实例。对 DeerFlow、WebThinker（搭配三种 LLM）以及 Gemini Deep Research 进行注入实验，定义报告级错误结论采纳率（FCAR）衡量危害。

**关键结果**：引入单一误导文档后，平均 FCAR 从无注入对照组的 0% 飙升至 54.7%。FCAR 受任务生命周期阶段、框架设计、来源权威性和呈现风格显著影响，而搜索结果排名和额外文档数量影响有限。交叉模型验证器在集中语料验证时能一致识别误导，但长程研究流程中仍会被采纳，揭示出集中验证与工作流级证据使用的脱节。预/后研究防御组合能减轻但无法完全消除错误采纳，建议在证据进入中间态时就进行持续验证与修正。
