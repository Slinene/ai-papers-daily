---
title: 'KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Evolving
  Memory and Skill'
title_zh: KnowAct-GUIClaw：知识驱动、完美执行的个人 GUI 助理，具备自演化记忆与技能
authors:
- Yunxin Li
- Jinchao Li
- Shibo Su
- Zhenran Xu
- Chenrui Zhao
- Tongshu Bian
- Xiaoman Liang
- Meishan Zhang
- Baotian Hu
- Min Zhang
affiliations:
- Harbin Institute of Technology, Shenzhen
- Shenzhen Loop Area Institute
arxiv_id: '2607.12625'
url: https://arxiv.org/abs/2607.12625
pdf_url: https://arxiv.org/pdf/2607.12625
published: '2026-07-14'
collected: '2026-07-17'
category: Agent
direction: Agent 框架 · 自我演化 · GUI 交互
tags:
- GUI Agent
- Self-Evolving Memory
- Cross-Platform
- Skill Library
- OpenClaw
one_liner: 提出 KnowAct-GUIClaw 框架，通过可插拔的 GUI 子智能体与经验归因记忆、自演化技能库，实现跨平台长程任务自动化，性能超越闭源模型
practical_value: '- **经验归因记忆与技能库的架构可迁移至对话或推荐 Agent**：将用户交互历史与反馈持续存入记忆，用于动态更新用户画像和决策策略，提升长会话中的准确性。

  - **可插拔子智能体设计适用于多端部署**：在电商/广告场景中，可为不同平台（App、小程序、网页）开发专用 GUI 子智能体，共享同一记忆与技能库，降低跨平台迁移成本。

  - **技能自演化机制可用于工具调用优化**：借鉴其从执行经验中自动提取并泛化“技能”的思路，可让推荐系统或广告投放 Agent 根据历史效果数据自动发现高频操作模式，形成可复用的执行捷径。

  - **基于开源的 Agent 框架改造**：在 OpenClaw 等现有框架上引入 Know-Route-Act-Reflect 管线，无需从零开发，即可尝试为用户助理类产品增加自我改进能力。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：OpenClaw 等现有 GUI Agent 框架跨平台支持不足，且缺乏从执行经验中持续学习的自演化机制，难以适应多设备生态和性能增长的闭环优化。

**方法**：提出 “Know Deeply, Act Perfectly” 范式，认为积累的人机交互与任务执行经验能直接提升准确率与效率。设计 KnowAct-GUIClaw 框架，分为四阶段：
- **Know**：主智能体利用积累的交互经验与领域知识进行长程任务分解和子任务分配；
- **Route**：将子任务路由至合适的可插拔 GUI 子智能体；
- **Act**：GUI 子智能体配备经验归因记忆系统（Know）与自演化技能库（Act），能识别过往相似情境并复用成功操作序列，同时根据新反馈更新技能；
- **Reflect**：持续存储用户画像与执行反馈，优化任务分解与工具调用。

**结果**：在 Android、iOS、HarmonyOS、Windows 跨平台测试中，GUIClaw 基于开源 Kimi-2.6 模型在长程 MobileWorld 基准上取得 64.1% 成功率，超过 Seed-2.0-Pro、GPT-5.5 等闭源智能体模型。记忆与技能可跨基础模型迁移，为 Kimi-2.6 和 Qwen3.5-35B 分别带来 8.5% 和 16.2% 的额外提升。
