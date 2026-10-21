---
title: 'HERA: Harness-Environment Co-Evolution for Reliable Agentic Abstention'
title_zh: HERA：可靠 Agent 弃权的 Harness-环境协同进化框架
authors:
- Han Luo
- Bingbing Wen
- Guang Yang
- Zora Zhiruo Wang
- Pan Lu
- Lucy Lu Wang
affiliations:
- University of Washington
- University of Leeds
- Carnegie Mellon University
- Stanford University
- Allen Institute for AI
arxiv_id: '2610.06563'
url: https://arxiv.org/abs/2610.06563
pdf_url: https://arxiv.org/pdf/2610.06563
published: '2026-10-04'
collected: '2026-10-21'
category: Agent
direction: Agentic Abstention · 环境协同进化
tags:
- Agentic Abstention
- LLM Agents
- Harness Co-Evolution
- Tool Use
- Reliability
- Task Generation
one_liner: 提出 harness 与环境协同进化框架，自动构造可行/不可行任务对，弃权准确率提升至83.3%，跨19个LLM平均提升15.3个百分点
practical_value: '- 构建 Agent 拒答能力：借鉴 HERA 的受控环境变异，对正常可完成商品查询/推荐任务注入库存为零、优惠冲突、参数不合法等扰动，自动批量生成不可行任务对，用于训练或评测
  Agent 在缺货、超范围请求时主动弃权/澄清，而不是硬给一个错误推荐。

  - 分离 harness 与模型：优化与底层 LLM 解耦的 Agent 控制层（系统提示、工具 schema、终止条件、校验规则），可跨模型复用。HERA 显示优化后的
  harness 在 19 个模型上平均提升弃权准确率 15.3%，且小模型搭配优化 harness 可达到大模型效果、成本降 85%，适合电商低成本多模型部署。

  - 协同进化环境生成：将线上 badcase 反馈到环境变异器，定向生成针对薄弱点的困难场景（如长尾商品属性缺失、组合优惠冲突），用于持续微调 Agent 行为或补充回归测试集，比固定测试集更能发现边界失效。

  - 双指标监控：将可行任务完成率和不可行任务弃权准确率分开评估，避免只优化完成率导致 Agent 在不可行任务上强行输出。在电商推荐 Agent 中，应同时监控“该推荐时推荐”和“该拒绝时拒绝”两个指标。'
score: 7
source: huggingface-daily
depth: abstract
---

LLM Agent 在复杂工具环境中常无法识别不可行任务，该可靠性问题被形式化为 agentic abstention。现有方法在固定任务集上优化，泛化差。HERA 通过 harness 与环境协同进化解决。首先自动构造可验证的可行/不可行任务对：对可解任务施加受控环境变异（如移除必要工具、引入冲突条件），生成需要弃权的不可行任务。然后利用历史失败驱动 harness 迭代调整，并针对弱点生成新环境和新任务。

在 held-out 评估中，最佳 harness 将弃权准确率从 61.7% 提升至 83.3%，可行任务完成率从 68.3% 提升至 76.7%，均优于对比方法。该 harness 迁移到 19 个其他 LLM，平均提升弃权准确率 15.3 个百分点，无需模型特定优化，并让小模型以约 85% 更低成本达到更强模型的性能。
