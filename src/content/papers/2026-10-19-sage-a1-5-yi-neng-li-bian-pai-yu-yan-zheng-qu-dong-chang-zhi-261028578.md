---
title: 'Sage-A1.5: From Long-Horizon Execution to Scientific Exploration with Capability
  Composition'
title_zh: Sage-A1.5：以能力编排与验证驱动长程执行和科学探索
authors:
- Wenjie Lou
- Tianshuo Peng
- Shiyang Feng
- Shengji Tang
- Runmin Ma
- Ruizhe Chen
- Jinxin Shi
- Haoyang Peng
- Fangchen Yu
- Zhijie Zhong
affiliations:
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2610.28578'
url: https://arxiv.org/abs/2610.28578
pdf_url: https://arxiv.org/pdf/2610.28578
published: '2026-10-19'
collected: '2026-10-21'
category: Agent
direction: Agent 编排与验证优化
tags:
- Agentic Orchestration
- Agentic Verification
- Long-Horizon
- RLHF
- MoE
- Scientific Discovery
one_liner: 35B MoE 智能体模型，通过 Agentic Orchestration 与 Agentic Verification 实现并行子智能体协作与自校正，在多项长程任务上超过更大模型
practical_value: '- 并行子智能体 + 隔离上下文 + 结构化反馈可用于电商导购/搜索 Agent：将复杂 query 拆成候选召回、评价证据、价格趋势、竞品对比等子任务并发执行，每个子
  agent 独立搜索并返回 answer/evidence/unresolved_issues/status，主 agent 再做冲突消解与覆盖检查，避免单线程长上下文噪声累积。

  - 在长程购物参谋或搜索任务中引入内建验证：当连续多轮检索无新增信息或需要形成关键结论时，让模型在推理中显式区分“已证实事实/未验证假设/仍缺失信息”，并据此切换搜索方向；用
  `Verification protocol: enabled` 这类条件提示按需激活，不依赖外部 verifier。

  - 训练框架上，窗口化交互 RL 适配电商 Agent 的延迟转化反馈：把多轮搜索、比较、生成推荐到最终点击/转化的长交互按中间结果切成窗口共享奖励，降低 step-level
  奖励噪声；同时采用 outcome+process mixed supervision，减少对昂贵人工标注的依赖。

  - 合成可验证任务时，将任务构造、审核、评判分离到不同 agent，避免同一个模型出题又评分导致 reward hacking；推荐/搜索 Agent 的任务也可以用
  sandbox + deterministic grader 做自动化质量门禁。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：长程任务中，单个智能体逐步执行容易上下文膨胀、探索低效，错误会沿链累积；仅扩展参数和领域覆盖不够，执行结构本身需要被训练。Sage-A1.5 将能力从“覆盖”推向“组合”，让模型学会分工、并行与自我验证。

方法关键点：
- 35B MoE，基于 Agents-A1 继续训练。
- Agentic Orchestration：主智能体根据任务将工作分解为 Exploratory/Constructive 并行子智能体；子智能体运行在隔离上下文，返回结构化反馈（answer/evidence/unresolved_issues/status），主智能体做证据融合与补缺。
- Agentic Verification：训练数据注入中间反思，模型自行判断进展停滞或关键结论需核验，区分已证实事实与未验证假设并调整后续动作；推理时通过 `Verification protocol: enabled` 按需激活，不需要外部监督器或独立验证工具。
- 统一训练管线：多域 SFT + outcome–process 混合后训练，对 MLE 采用窗口交互 RL，对 SWE/科学/搜索任务做合成、过滤与蒸馏。

关键结果：在 12 个基准上全部超过同尺寸 A1 与 Ornith-1.5；在 FS-Olympiad(81.0)、CMT(80.0)、PinchBench(90.0)、IFBench(81.6) 上超过 Kimi-K3、GLM-5.3、GPT-5.6-sol，SWE-Pro(64.6) 与更大模型持平，BrowseComp(82.8) 具备竞争力。

最值得记住的一句话：执行结构也是可训练能力——学会何时委托、何时核验、何时改道，比单纯扩大领域覆盖更能提升长程智能体上限。
