---
title: Interpreting Coding Agents Through Their Behavioral Trajectories
title_zh: 通过行为轨迹解释编码智能体
authors:
- Ibragim Badertdinov
- Alexander Golubev
affiliations:
- Nebius
arxiv_id: '2611.17440'
url: https://arxiv.org/abs/2611.17440
pdf_url: https://arxiv.org/pdf/2611.17440
published: '2026-11-11'
collected: '2026-11-17'
category: Agent
direction: 编码智能体行为轨迹分析
tags:
- coding agents
- behavioral trajectories
- trajectory parsing
- agent scaffolds
- evaluation
- behavior fingerprint
one_liner: 分析14.3万条编码智能体执行轨迹，发现相同解决率下行为差异显著，且行为画像可识别智能体栈
practical_value: '- 在电商/广告场景评估 Agent（如商品推荐对话 Agent、搜索策略 Agent）时，不应只看任务成功率，可借鉴其思路：记录完整执行轨迹，通过规则解析器抽象出高层行为（如商品检索、属性过滤、排序策略调用），用于诊断失败根因和优化
  scaffold。

  - 开发跨系统 Agent 分析平台时，面对不同工具接口和日志格式，可以采用规则映射而非依赖工具名或原始命令，将异构轨迹统一为语义动作，便于横向对比不同模型或配置。

  - 利用“行为指纹”识别 Agent 栈的做法可迁移到线上多 Agent 系统监控：只基于聚合行为分布（不依赖 token 数、工具名、结果标签）即可检测 scaffold
  变更或推理预算调整带来的行为漂移。

  - 观察到 scaffold 选择和 reasoning effort 系统性地改变搜索、编辑、测试行为，提示业务 Agent 在调整 prompt 或推理参数时，应监控行为分布变化，而不仅是最终指标。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有编码智能体基准只评估二元任务成功与否，把执行过程当黑盒，掩盖了产生结果的行为差异。不同 agent 配置即使 solve rate 相同，可能探索、修改、验证代码的方式完全不同。

**方法关键点**：收集 143,209 条执行轨迹，覆盖 125 种 agent 配置、117 个模型。开发确定性规则解析器，将异构原始执行轨迹映射为高层动作（如仓库搜索、文件编辑、测试执行），并用六模型共识对 500 个事件进行审计。基于聚合行为画像（不使用任务结果、token 数或工具名作为特征）进行跨仓库、跨编程语言的 agent 栈检索。

**关键结果**：相同 solve rate 的 agent 在行为上差异显著；聚合行为画像能跨 disjoint 仓库集和编程语言检索到对应 agent 栈；scaffold 选择和推理努力系统性地改变搜索、编辑、测试行为。作者发布了解析器、完整标注与分析流程及标注轨迹子集。
