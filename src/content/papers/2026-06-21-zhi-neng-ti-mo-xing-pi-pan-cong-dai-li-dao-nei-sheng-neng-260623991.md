---
title: Critique of Agent Model
title_zh: 智能体模型批判：从代理到内生能动性
authors:
- Eric Xing
- Mingkai Deng
- Jinyu Hou
affiliations:
- Institute of Foundation Models, Mohamed bin Zayed University of Artificial Intelligence
- School of Computer Science, Carnegie Mellon University
arxiv_id: '2606.23991'
url: https://arxiv.org/abs/2606.23991
pdf_url: https://arxiv.org/pdf/2606.23991
published: '2026-06-21'
collected: '2026-06-26'
category: Agent
direction: Agent 能动性分析与架构设计
tags:
- Agent Architecture
- Agency
- Autonomy
- GIC
- Agentive System
- World Model
one_liner: 区分“代理式”与“内生式”AI系统，提出GIC架构以实现源于系统内部的真正能动性
practical_value: '- **构建自主推荐Agent时区分“流程编排”与“内生能力”**：当前多数推荐LLM Agent（如工具调用搜索）停留在**agentic**阶段，通过外部工作流拼接；真正能适应开放世界的推荐系统应走向**agentive**，让目标分解、用户身份理解、自我纠偏内化至模型，减少硬编码脚本。

  - **在电商Agent中引入身份演化和自我调节**：GIC架构的身份演化机制可用于用户建模，使Agent捕捉长期偏好变化而非仅反应当前会话；自我调节模块可监测推荐是否符合长期客户价值（如避免过度追求短期点击），自动调整策略。

  - **利用分离的世界模型进行仿真推理**：训练一个独立的世界模型（用户行为、市场环境模拟），Agent可在此模拟器中试错（simulative reasoning），安全地学习推荐策略，避免直接在线上探索带来的风险，尤其适用于高价值商品推荐或广告投放。

  - **分级目标分解应对多目标冲突**：电商场景下推荐常面临多目标（点击、转化、GMV、多样性），GIC的分层目标分解提供形式化框架，将抽象公司目标逐层拆解为可执行的子目标，并自主协调冲突。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：当前LLM驱动的“编码Agent”等系统虽冠以Agent之名，实为预设工作流的自动化（agentic），缺乏笛卡尔式独立思考和开放世界自主性。需从哲学和科幻视角厘清“能动性”边界，才能构建真正自主的AI系统并评估其风险。

**方法**：论文从笛卡尔“我思故我在”和科幻中自主生物的描述出发，提出能动性的五个必要维度：目标、身份、决策、自我调节、学习。据此将现有AI系统分为两类：**agentic系统**依赖外部工程编排，能力源于工作流设计；**agentive系统**的能力内化，源于系统自身。作者设计**GIC通用Agent架构**，核心组件包括：
1. **分层目标分解**：将高层目标逐层拆解为子任务，并保持目标一致性；
2. **身份演化**：随时间更新系统对自身及环境的表征，形成稳定身份；
3. **基于世界模型的仿真推理**：用单独训练的预测模型模拟环境后果，指导决策；
4. **学习的自我调节**：内置元认知电路，监控自身行为并修正偏离；
5. **自我导向学习**：从真实和模拟经验中持续更新能力，无需人工干预。

**关键结果**：概念性分析确立了系统从自动化跨越到自主的清晰判据；GIC架构为构建具有内生能动性的Agent提供了可行蓝图。论文同时指出，即使具有高自主性的agentive系统，其可审计性、可控性和安全性仍需置于人类监督之下。
