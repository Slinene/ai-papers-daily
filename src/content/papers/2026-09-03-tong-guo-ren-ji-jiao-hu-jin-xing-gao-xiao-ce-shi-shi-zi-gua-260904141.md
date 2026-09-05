---
title: Efficient Test-Time Adaptation through Human-AI Interaction
title_zh: 通过人机交互进行高效测试时自适应
authors:
- Zora Zhiruo Wang
- Apurva Gandhi
- Rulin Shao
- Aspen Chen
- Jonas Mueller
- Zhiqi Liang
- Jett Chen
- Michael Ryan
- Qianou Ma
- Luxi He
affiliations:
- Carnegie Mellon University
- University of Washington
- Handshake AI
- Stanford University
- Princeton University
arxiv_id: '2609.04141'
url: https://arxiv.org/abs/2609.04141
pdf_url: https://arxiv.org/pdf/2609.04141
published: '2026-09-03'
collected: '2026-09-05'
category: Agent
direction: Agent 个性化与测试时自适应
tags:
- test-time adaptation
- human-AI interaction
- personalization
- LLM agents
- rubric learning
one_liner: 利用跨会话人机交互信号在测试时适配个体 Agent，写作与视觉创作任务成功率提升 4.5–20.9%，演化 rubric 可多捕获 16–22.3%
  失败
practical_value: '- 用跨会话交互数据做在线个性化：电商对话式导购/客服 Agent 可维护用户历史反馈，在推理时动态注入 context 或更新轻量权重，实现低成本的个性化，尤其适合长尾用户。

  - 演化 rubric 模块可作为偏好对齐工具：将用户对推荐解释、商品描述、广告文案的反复反馈提炼为可进化的评价标准，既可作为奖励/过滤信号，也可用于自动标注失败案例，减少人工评审成本；论文显示比单用
  LM 或人工能多捕获 16-22% 失败。

  - 个性化策略具备跨用户迁移能力：即使目标是个人化，TAHI 训练的个性化策略也能提升其他用户最高 8.8%，提示可构建共享的“个性化底座”，通过少量交互迁移到新用户，缓解冷启动。

  - 在生成式推荐场景，可将用户反复指出的标准显式化为 rubric 并注入 prompt 或评分器，实现可解释的偏好对齐与可控生成。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：通用 LLM Agent 在开放任务上输出趋于平均，难以达到个体专家标准；这些标准往往异构且难以预先完全说明，但在反复人机交互中会不断浮现。跨会话交互数据是缩小与个体专家差距的丰富但未被充分利用的信号。

**方法关键点**：TAHI 在测试时将交互信号融入 Agent 的 context 与 weights，并用一个持续演化的 rubric 模块固化每个用户独特的训练/评估标准。具体包括从用户反馈中提炼规则、更新上下文与轻量参数，使 Agent 在少量任务内快速适配个体偏好。

**关键结果**：在写作与视觉创作两个领域、30 个个体、共 600 个任务上，仅数十个任务后，solo task success 提升 4.5–20.9%；演化 rubric 模块作为可扩展标注工具，构造的评估 rubric 比 LM 或人类单独构造的能多捕获 16.0–22.3% 的失败；个性化 Agent 还能跨用户带来最高 8.8% 的成功率提升。
