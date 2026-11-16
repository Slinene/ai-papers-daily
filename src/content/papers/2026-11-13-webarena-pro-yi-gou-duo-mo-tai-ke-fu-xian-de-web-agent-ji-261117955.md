---
title: 'WebArena-Pro: A Heterogeneous, Multimodal, Reproducible Benchmark for Web
  Agents'
title_zh: WebArena-Pro：异构多模态可复现的 Web Agent 基准
authors:
- Imene Kerboua
- Fatemeh Pesaran Zadeh
- Xing Han Lù
- Weijian Qi
- Alexander Miller
- Junyi Song
- Yunjia Tian
- Dongjin Kang
- Seyeon Choi
- Marzia Nouri
affiliations:
- INSA Lyon, LIRIS
- Seoul National University
- McGill University
- Mila – Quebec AI Institute
- ServiceNow AI Research
arxiv_id: '2611.17955'
url: https://arxiv.org/abs/2611.17955
pdf_url: https://arxiv.org/pdf/2611.17955
published: '2026-11-13'
collected: '2026-11-16'
category: Eval
direction: Web Agent 多模态基准评测
tags:
- Web Agent
- Benchmark
- Multimodal
- Reproducible
- Audio-Video
- LLM Agent
one_liner: 提出包含 300 任务、20 个自托管应用、支持音频视频模态的可复现 Web Agent 基准，最佳 agent 得分 62.3%
practical_value: '- 可复现的自托管浏览器环境：在电商场景中做网页操作 Agent 评测时，可搭建自托管应用（如商品后台、订单系统），保证数据与页面稳定，避免线上页面漂移。

  - 将音频/视频作为一等公民：对于直播带货、商品视频等场景，可设计专门 action 提取音频/视频信息，评估 Agent 对这些模态的理解，而不仅仅依赖文本和截图。

  - 任务构建 pipeline：使用标注界面 + LLM 辅助筛选 + 人工验证，可降低构建高质量评测集成本，适合搭建内部 agent 回归测试集。

  - 异构应用覆盖：评测应覆盖不同 UI 范式和数据模型的应用，而不是单一电商站点，以评估泛化能力。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：现有可复现 web-agent benchmark 覆盖应用数量少、软件类别单一，模态仅限文本和视觉；live benchmark 覆盖广但页面和数据会漂移，牺牲可复现性；且缺乏对音频、视频内容理解的评估。

方法关键点：
- 构建 WebArena-Pro，包含 300 个任务，横跨 20 个自托管 web 应用、六个领域类别，覆盖不同 UI 约定、工作流和数据模型。
- 将音频和视频作为核心观察，设计专门 action 从音视频中提取信息，打破仅文本+视觉的局限。
- 每个任务隔离运行，支持可复现、并行评估。
- 任务通过专用标注界面创作，经 LLM 辅助筛选，最后人工验证后发布。

关键结果数字：
- 最佳 agent：Codex with GPT 6.1 Sol 和 Claude Code with Claude Opus 5.5，均取得 62.3%；
- OpenCode with Kimi 3.1 Pro 为 60.7%；
- 最强 GenericAgent（Gemini 3.1 Pro omni 和 Gemma4 31B）均为 30.3%；
- 在可复现、人工 curator 的 web agent benchmark 中，WebArena-Pro 提供最广应用覆盖和最全面的多模态支持。
