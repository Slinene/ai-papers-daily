---
title: What Effort Level Should I Choose? On the Economics of Reasoning Effort in
  LLM Agents
title_zh: 我该选择哪个推理努力水平？论 LLM Agent 推理努力的经济学
authors:
- Kaiser Sun
- Yongchan Kwon
- Zain Hasan
- Shang Zhu
- Kaitlyn Zhou
- Federico Bianchi
affiliations:
- Johns Hopkins University
- Together AI
- Cornell University
arxiv_id: '2610.34491'
url: https://arxiv.org/abs/2610.34491
pdf_url: https://arxiv.org/pdf/2610.34491
published: '2026-10-24'
collected: '2026-10-29'
category: Reasoning
direction: 推理努力经济学与动态分配
tags:
- reasoning effort
- test-time compute
- cost-efficiency
- agentic evaluation
- naive laddering
- credence good
one_liner: 审计8模型4基准显示高推理努力常丢失低努力已解任务且过度支出；基于验证的阶梯式升级能匹配或超过固定最高努力并降本
practical_value: '- 在电商 Agent 和生成式推荐中，避免固定使用最高 reasoning effort：采用“先最低 effort，外部校验失败后升级到最高”的
  naive laddering，可保持或提高成功率，并节省 15-40% 推理成本（论文中 AIME 中位节省25.3%，GPQA 41.5%）。

  - 成本核算要包含延迟/等待时间成本，不能只看 API token 费用。高 effort 可能导致 agent 轨迹更长，反复处理上下文，输入 token 成本反而增加；应监控全链路延迟与用户等待成本。

  - 评估模型/策略时不能只看 aggregate accuracy，要检查实例级 regressions（高 effort 丢失低 effort 已解决任务），并分析行为策略变化：高
  effort 可能偏向检索和自验证，需根据任务类型动态分配。

  - 对 LLM 驱动的 query/商品文案生成，可借鉴动态 effort 分配：对简单/常规任务用低 effort，对复杂长尾任务才升级，避免每个请求都支付过度推理成本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
随着 LLM 在长周期 agentic 任务中广泛部署，推理成本成为核心问题。许多推理模型暴露 effort 参数调节推理时计算，但用户必须在不知道额外推理是否有用的情况下选择努力水平，且即使成功也无法判断所购 effort 是否必要——典型的 credence good（信任品）。本文对 effort 水平的反事实影响进行系统审计。

## 方法关键点
- 在 4 个基准（AIME 2026、GPQA Diamond、Terminal-Bench 2.1、SWE-Bench Pro）上，对 8 个模型（GPT-5.6 系列、Claude Sonnet 5、GLM-5.2、Inkling、Kimi K3、DeepSeek V4 Flash）的不同 effort 设置进行评测，保持任务、提示、agentic harness 固定。
- 记录每个任务的完整 token 消耗（输入、输出、隐藏推理 token），转换为美元成本；定义包含用户等待时间的 full cost 公式。
- 分析实例级 solved set 的嵌套性，计算高 effort 丢失低 effort 成功的回归集；在“所有 effort 均解决”的任务子集上比较成本放大；用 Act·ONOMY 分类法标注 agent 轨迹行为。

## 关键实验结果
- 高 effort 并不嵌套地增加解集：Terminal-Bench 上所有 8 个模型在最低和最高 effort 之间都有回归实例；例如 GPT-5.6-sol 从 high 到 xhigh 丢失 8 个任务而只新增 5 个。
- 在 always-solved 子集上，最高 effort 成本可达最低 effort 的 42 倍；GPT-5.6-sol 在 SWE-Bench Pro 上 mean cost 从 $0.27 升至 $1.24（4.54 倍）。
- 禁用推理（none）不省钱：agent 通过更长轨迹补偿，输入 token 成本增加（GPT-5.6-luna none 平均 21.5 次调用 vs low 5.4 次，成本 4.58 倍）。
- 高 effort 改变策略：original SWE-Bench Pro 中 GPT-5.6-sol 读取参考修复 commit 的比例从 15.9% 升至 75.0%；corrected 环境中 online lookup 尝试从 9.1% 升至 68.2%。验证行为显著增加但未必改善结果。
- Naive laddering（先最低 effort，失败后最高 effort）在所有模型和基准上匹配或超过固定最高 effort 成功率，同时中位成本节省：AIME 25.3%，GPQA 41.5%，corrected SWE-Bench Pro 15.5%。

## 最值得记住的一句话
固定 effort 是低效的；在可靠外部校验存在时，应动态分配 effort，先低后高，既保成功率又显著降本。
