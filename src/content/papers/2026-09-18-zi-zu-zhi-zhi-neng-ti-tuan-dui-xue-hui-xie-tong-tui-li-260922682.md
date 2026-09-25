---
title: Self-Organizing Agent Teams Learn to Reason Together
title_zh: 自组织智能体团队学会协同推理
authors:
- Aneesh Pappu
- Mirac Suzgun
- Yongchan Kwon
- Federico Bianchi
- Batu El
- Mykel J. Kochenderfer
- Hancheng Cao
- James Zou
affiliations:
- Stanford University
- Together AI
- Emory University
arxiv_id: '2609.22682'
url: https://arxiv.org/abs/2609.22682
pdf_url: https://arxiv.org/pdf/2609.22682
published: '2026-09-18'
collected: '2026-09-25'
category: MultiAgent
direction: 多智能体协作策略学习
tags:
- MultiAgent
- Self-Organization
- Teamwork Strategy
- Reasoning
- Demonstrability
- Evolutionary Search
one_liner: 固定智能体团队从历史协作中学习可迁移的团队协作策略，无需预设任务分解即能超越最强成员与路由上限。
practical_value: '- 多 agent 协作流程（roles/phases/information flow）可作为可学习资产，用小型训练集通过进化搜索离线优化；冻结策略
  bank 在线复用，避免 test-time 动态规划，降低延迟与成本，适合搜索推荐中的多模型融合、query 理解或排序后 rerank 流水线。

  - 引入“路由 oracle”作为强 baseline：只聚合成员独立回答且完美选择的上限，能区分团队增益是来自选择还是真正协同推理。业务中评估多 agent
  系统时，应同时报告 coverage 与 final accuracy，定位瓶颈在生成还是选择。

  - “demonstrability”指标（外部模型判断正确推理的可辨识度）与团队增益高度相关，可用于预判哪些任务适合多 agent 协作；在电商场景可用来识别需要多模型会诊的高价值
  query 或商品。

  - 异构模型组合（强推理 + 校对/审计 + 多样化生成）比同构团队或单模型线性化更有效；具体 trick：将某成员观察到的优势转化为显式角色（如 auditor），并让该角色只在特定
  phase 参与，保留多样性的同时隔离错误。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
现有 LLM 多智能体系统依赖固定协议（debate, Mixture of Agents）或预先路由子任务，无法在解结构未知时通过互动组合部分推理；人类团队能通过协作学习组织方式。本研究探索固定智能体团队能否从历史协作中学习可复用的团队协作策略，实现“协作计算”（交换、挑战、修复、综合），产生任何成员独立无法得出的解。

**方法关键点**
- 提出 Self-Organizing Agent Teams (SAT)：用 DSL 表示团队策略，包括有序对话阶段、参与成员、轮数、信息流（local vs summary）、全局/角色 prompt。
- 从初始策略（独立求解 + 辩论 + majority vote）开始，指定最强成员做“团队反思”，在小训练集上检查历史执行记录，提出变异策略；每轮最多 3 个候选，每个源问题 6 轮变异。
- 通过语义泄漏审计和验证探针过滤问题特定内容，确保策略问题无关；最终按 coverage 贪心选择冻结 10 个互补策略。
- 测试时对所有策略运行生成候选解和证书；单一评委选择最终答案。
- 关键 baselines：best member、routing oracle（完美选择独立答案）、self-consistency、self-reflection、debate、Mixture of Agents、homogeneous team（同构模型执行同样策略）、linearization（最强单模型串行执行所有 phase）。

**关键结果**
- 数学物理团队（o3-mini, Claude Sonnet 4, DeepSeek-V3；15 个 AIME-2024 训练题）在 5 个 benchmarks 平均 66.7%，最强成员 48.8%，routing oracle 59.0%，linearization 58.7%。AIME 2026 上超 routing oracle 13.4 个百分点。
- 知识逻辑团队（Gemini-2.5-Flash, Llama-4-Maverick, GPT-4.1；25 个 GPQA 训练题）平均 72.8% 最高，但低于 routing oracle 79.6% 覆盖率；coverage 87.9%，selection 差距大。
- 跨 8 个 benchmarks，demonstrability（外部评委对正确/错误推理的判别率）与团队相对最强成员增益的 Spearman ρ=0.90, p=0.005。

**最值得记住的一句话**
组织本身可以成为智能体能力——固定模型集合能学会如何一起推理，产出任何成员独立无法得到的解决方案。
