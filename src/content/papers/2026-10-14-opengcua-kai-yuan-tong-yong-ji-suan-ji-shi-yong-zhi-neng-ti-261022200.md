---
title: 'OpenGCUA: Toward a Fully Open Stack for Generalist Computer Use'
title_zh: OpenGCUA：开源通用计算机使用智能体全栈系统
authors:
- Hanzhang Zhou
- Long Li
- Quyu Kong
- Lei Wang
- Panrong Tong
- Long Chen
- Tianyu Xia
- Gongjie Zhang
- Xu Zhang
- Chen Liu
affiliations:
- Alibaba Token Hub, Alibaba Group
arxiv_id: '2610.22200'
url: https://arxiv.org/abs/2610.22200
pdf_url: https://arxiv.org/pdf/2610.22200
published: '2026-10-14'
collected: '2026-10-17'
category: Agent
direction: 通用计算机使用智能体 / 代码执行
tags:
- CUA
- code execution
- harness-to-model decision transfer
- OSWorld-v2
- real-device harness
- agent efficiency
one_liner: 开源通用计算机使用智能体栈，用代码执行与决策转移让8个前沿模型在OSWorld-v2平均+19.6分、步数-53%
practical_value: '- 用代码执行替代固定 action list/batch：推荐/营销 Agent 可让模型写短程序（Python/SQL）同时调用内部
  API、读取中间结果、做断言/条件分支，把多轮 model call 压缩成一次，适合批量商品上架、素材改写、数据校验等任务。

  - 按需观测可提高缓存命中：模型不强制每步截图/取数，只在真正需要时请求；论文中 cache hit 提升 10.5/14.4 pp 且不掉点。商品详情页、搜索结果截图、日志等大体积上下文可按需拉取。

  - 任务状态跟踪与意图标注：让模型维护 todo/pending/verified 状态，区分“已改”和“已验证”；面向用户或审核场景输出 <intent> 可解释步骤目的，适合运营
  Agent 和自动化审核流。

  - 资源受限下选模型：不能只看最终 benchmark，要看单位成本/时间内的得分；论文的 cost/score 曲线提示便宜小模型可能更划算，适合做线上 Agent
  模型路由和降级。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
计算机使用正从只有 GUI 交互转向系统级任务完成：模型需要同时通过视觉和程序化接口观察、执行和组织工作。前沿系统如 GPT-6 Astra 的 computer-use 仍闭源，社区难以系统研究设计选择。

**方法关键点**
- 定义 GCUA：每一步模型自行决定 what to observe、how to act、how to organize，覆盖 GUI、Accessibility Tree、CLI、API 四类接口。
- 代码执行：模型写 Python 程序，可在同一 program 中组合 PyAutoGUI、bash()、Playwright 等操作，支持 loops、条件分支、断言；中间结果能决定后续操作，不必反复调用模型。
- harness-to-model decision transfer：将截图请求、任务状态维护、意图说明等原本由框架固定规则控制的决策交给模型；包括 on-demand observation、todo.update、<intent> 标注。
- 上下文策略：rolling screenshot buffer 和 micro-compaction 控制历史上下文长度，并尽量保持 prompt cache 稳定。
- 发布跨设备 SDK 与真实设备 harness，覆盖电脑/浏览器/手机。

**关键实验**
在 OSWorld-v2 离线 82 个任务上评测 8 个前沿模型。OpenGCUA 相对 batch GUI-only baseline，平均 partial score 从 45.3 提到 64.9（+19.6 分），steps/task 平均降 53.0%，所有 8 个模型均提升；GPT-6 Astra 从 67.1 到 75.7，步数从 102.1 降到 33.5。代码执行相比相同 GUI+CLI 访问的 batch 基线，再提高约 6.1 分、步数降 14.8%。on-demand observation 在两个模型上 cache hit 分别提升 10.5 和 14.4 pp 且不掉点。真实 macOS 任务中，Qwen3.8-Max 的 reasoning tokens 是 GPT-6 Astra 的 19.4 倍，显示模型效率差距巨大。

**最值得记住的一句话**
固定 harness 规则向模型转移，代码执行把 GUI/CLI/API 写进同一个程序，让中间结果决定后续操作，是通用 Agent 降步数、提性能的关键。
