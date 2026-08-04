---
title: 'SKT: Skill-Use Training at Scale via Verified Synthetic Data Generation'
title_zh: SKT：通过验证合成数据训练语言模型使用Agent技能
authors:
- Zelin Tan
- Yiqun Zhang
- Hao Li
- Zhiyao Cui
- Hejia Geng
- Shao Zhang
- Hangfan Zhang
- Yang Chen
- Xiaosong Wang
- Lilong Wang
affiliations:
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2608.02287'
url: https://arxiv.org/abs/2608.02287
pdf_url: https://arxiv.org/pdf/2608.02287
published: '2026-08-02'
collected: '2026-08-04'
category: Agent
direction: Agent技能合成数据训练
tags:
- Agent Skills
- Synthetic Data
- Skill-Use Training
- Verified Data Generation
- LLM Agents
- Multi-Agent Data Synthesis
one_liner: 提出SKT数据合成流水线，通过多阶段验证生成可执行任务与忠实轨迹，SFT后模型技能利用率显著提升。
practical_value: '- **技能化业务逻辑**：将电商搜索/推荐中的查询改写、过滤规则、策略编排等模块封装为“Skill”，用SKT流水线自动生成大量可验证任务与执行轨迹，训练模型掌握这些原子操作及组合使用。

  - **验证驱动的数据质量**：借鉴其规则验证器+代理验证器+难度控制的多层验证框架，尤其技能依赖性检查（有技能 vs. 无技能评分差），确保合成数据的正确性和技能依赖性，避免低质量数据损害模型原有能力。

  - **跨工具框架复用**：混合来自不同Agent harness（如DeepAgents、OpenCode）的轨迹训练单一模型，可实现一个模型在多种交互协议（如REST/WebSocket、自建Agent框架）上复用，降低多端维护成本。

  - **技能覆盖与扩展性**：SFT收益随训练技能池规模单调上升，可规划技能库的增量扩展路线，通过持续合成更多技能数据逐步提升模型的复合技能使用能力。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：Agent Skills（封装领域知识的指令包）数量已达百万级，但现有LLM并不能自然地有效识别、应用并协调这些技能。已有工作多聚焦于技能检索、内化或参数化表示，而忽略了对模型“何时、如何、以何种顺序使用技能”能力的直接训练。本文指出这种技能使用能力是可合成数据训练的，并提出了SKT流水线。

**方法关键点**：
- **三阶段流水线**：①技能筛选——用评判器挑选适合构建可执行任务的技能，并保证多技能组合的互补性；②任务合成与验证——基于模板生成包含指令、环境、参考答案、评估器的任务包，依次通过规则验证器（路径、执行满分）、代理验证器（语义完整性、无泄露、技能依赖性测试：有技能得分必须高于无技能）和难度控制（避免过易），失败任务经反馈修复重新进入管道；③轨迹合成与验证——使用强教师模型在harness中执行任务，保留完全成功且忠实使用每一项技能的轨迹，拒绝的rollout不反馈重试。
- **训练**：在保留的轨迹上做SFT，损失仅掩码助手生成的思考、工具调用和回答部分，让模型学习完整的技能使用决策链。

**关键结果**：
- 基于2000个公开技能合成4000个任务、27,164条高质量轨迹。在Qwen3.5-9B和Gemma 4 E4B-IT上训练后，跨SkillsBench、MolBench-Bind、AgentSkillOS、SkillEval四个基准匹配harness评测中，平均提升3.20–18.91个百分点；移除技能后增益骤降至0.53–5.69，证明模型学的是“使用外部技能”而非内部化。
- 未经验证的合成数据训练反而导致4个基准全面下降（最高-19.5），凸显验证的必要性。
- 跨harness转移保留约50%的匹配harness增益，混合harness训练可使单一模型在不同harness下接近专用模型水平。
- 训练技能数从100增至2000，SkillEval得分单调上升（55.2→72.5）。

**核心洞察**：高质量、验证后的合成数据是训练Agent技能使用能力的可扩展手段，其收益随技能覆盖面扩大而持续增长，且能跨工具框架泛化。
