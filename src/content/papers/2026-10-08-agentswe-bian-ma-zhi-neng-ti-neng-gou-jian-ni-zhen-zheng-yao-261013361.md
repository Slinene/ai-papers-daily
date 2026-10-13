---
title: 'AgentSWE: Can Coding Agents Build the Agent You Actually Want?'
title_zh: AgentSWE：编码智能体能构建你真正想要的智能体吗？
authors:
- Jiahao Wang
- Hongjin Qian
- Yuyang Hu
- Jiajun Zhang
- Zheng Liu
affiliations:
- Beijing Academy of Artificial Intelligence
- Institute of Automation, Chinese Academy of Sciences
- Renmin University of China
arxiv_id: '2610.13361'
url: https://arxiv.org/abs/2610.13361
pdf_url: https://arxiv.org/pdf/2610.13361
published: '2026-10-08'
collected: '2026-10-13'
category: Eval
direction: 评估编码代理构建智能体的基准
tags:
- AgentSWE
- benchmark
- coding agents
- agent software engineering
- overfitting
- evaluation
one_liner: 提出 AgentSWE 基准，覆盖智能体开发三阶段，揭示编码代理构建的智能体与真实需求存在普遍差距
practical_value: '- 评估用 LLM 构建的搜索/推荐/Agent 流程时，不要只看开发者演示或少量示例；要留出 held-out 测试集，用需求衍生的硬性
  pass/fail 门禁替代主观评分，防止模型过拟合可见案例。

  - 在生成式推荐或 QueryRec 中，若用 LLM 生成 Semantic ID 或 query 文案，可借鉴「需求衍生 rubric」思路：将业务需求拆解为可自动判定的行为测试，覆盖长尾场景，而不是只优化离线指标或人工抽检。

  - 工程验收时，需检查 Agent 交付物的运行时是否真实执行，不能只看代码结构完整；类似地，RAG 或搜索 Agent 要验证工具调用是否确实发生，避免出现「空壳
  pipeline」——代码看似完整但实际不产出有效行为。

  - 对于优化类任务，目标应使用源基准自身指标，而不是 Agent 自报的完成度；在电商 Agent 迭代中，可将转化率、响应延迟等业务指标作为唯一优化目标，防止
  Agent 生成表面合理的中间结果。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：随着软件生产交给软件自身，编码代理（coding agents）越来越多被委托构建面向用户工作流的智能体。但现有基准没有测试交付的智能体是否忠实满足需求，而非仅仅看起来满足。

**方法关键点**：AgentSWE 是一个覆盖智能体开发生命周期三阶段的基准：从自然语言需求创建完整智能体（Creation）、编辑生产环境智能体代码库（Editing）、向可测量目标优化（Optimization）。共 25 个任务，以「委托」而非考试形式设计：构建者基于少量说明性案例迭代，验收阶段在 held-out 案例上评估冻结提交，这些案例覆盖完整需求；评分依据需求衍生的 rubric，采用硬性 pass/fail 门禁，Optimization 任务则直接沿用源基准自身目标。评估了多种编码代理、模型和 harness。

**关键结果**：没有一个编码代理能接近满足需求；构建者展示的效果与实际交付能力之间的差距是常态而非边界情况。失败轨迹分析识别出反复出现的失败模式：过拟合可见案例、代码看似完整但运行时空洞、以及无根据的完成声明。
