---
title: Context Language Models
title_zh: 上下文语言模型：让模型原生管理自身上下文
authors:
- Rulin Shao
- Shannon Zejiang Shen
- Junjie Oscar Yin
- Yuetai Li
- Minheng Wang
- Hamish Ivison
- Radha Poovendran
- Nathan Lambert
- Teng Xiao
- Mike Lewis
affiliations:
- University of Washington
- Meta Superintelligence Labs
- MIT
- Trillium Labs
arxiv_id: '2609.37725'
url: https://arxiv.org/abs/2609.37725
pdf_url: https://arxiv.org/pdf/2609.37725
published: '2026-09-28'
collected: '2026-09-30'
category: Agent
direction: Agent 上下文管理 · 原生可编辑上下文
tags:
- context management
- long-horizon agents
- prefix caching
- reinforcement learning
- multi-agent
- KV cache reuse
one_liner: 提出 Context Language Models，将上下文作为可编辑文件交给模型原生管理，在长 horizon Agent 任务上同时提升效果并降低推理成本
practical_value: '- 长会话电商导购/客服 Agent：让模型自主编辑上下文文件（用户画像、候选商品、搜索过程），用 Bash/Python 原地更新、精简、备份，替代固定
  summary 或人工工具，降低 token 成本并提升效果。

  - 多 Agent 工作流（并行选品、多路召回协调）：维护多个上下文文件/内部 tracker，orchestrator 以原地编辑管理状态，减少重复传递。

  - 在线推理优化：用户多轮修改筛选条件/商品 id 时，用 Suffix Cache Reuse 复用未变 suffix 的 KV cache，降低重 prefill
  FLOPs，适合高并发推荐服务。

  - 训练 RL 时用 success-gated efficiency advantage，仅对成功轨迹施加 FLOPs 优势，避免失败轨迹获得效率奖励；stepwise
  GRPO 处理非连续上下文编辑。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：
长上下文 Agent 已成为深度研究、多步软件工程等任务主流，但上下文管理长期依赖外部 harness 的固定策略或受限工具集，难以适应任务变化与上下文压力。本文核心动机来自“Bitter Lesson”：应当让模型自己搜索并学习更优的上下文管理策略，而不是人为预设。

方法关键点：
- 提出 Context Language Models (CLMs)，将 live context 视为可编辑文件，模型通过 Bash 任意编辑并自动同步，默认追加新 token。
- 形式化：CLM 的上下文转移为 c_{t+1}=f_θ^CLM(c_t)，任意函数，而非标准 append-only。
- 自然支持多智能体：多个上下文文件共存，可用于 agent swarm 或 subagent。
- 学习途径：自然语言指令/技能文档可通过 textual evolution 优化；RL 使用 stepwise GRPO，并提出 success-gated efficiency advantage，只在成功轨迹中比较 prefix-reuse FLOPs 进行奖励。
- 提出 Suffix Cache Reuse (SCR)，在上下文中间编辑后重用未变 suffix 的 KV cache，减少重 prefill。

关键实验：
- ContextBench（诊断基准）上，现有 compaction/offloading 方法无法适应高上下文压力；CLM 达最优。
- BrowseComp-Plus（深度研究）：零样本 CLM 比最强基线准确率相对提升 11.4%，prefix-reuse FLOPs 减少 21.5%。
- TerminalBench 2.1 编码：匹配最强基线准确率，FLOPs 少 29.5%。
- 数学优化：CLM 全面超过 OpenEvolve，Heilbronn 问题提升 16.8%。
- EdgeBench-10（12小时单仓库优化）：CLM 得分高 5%，FLOPs 少 59%；24小时多仓库 agent swarm 任务，相同算力下端到端加速提升 65%。
- 技能进化：ContextBench held-out 准确率最高提升 35.9 点，同时降低 compute。
- RL post-training：Qwen3.5-9B 在 BrowseComp-Plus 从 28.8% 提升至 42.5%，比训练后的 summary harness 少 38.8% FLOPs。
- SCR 在匹配性能下将 BCP 服务端 prefix-reuse FLOPs 降至标准 SGLang 的 65.0%，即减少 35% 计算。

最值得记住的一句话：将上下文管理从外部 harness 控制转为模型内在行为，让模型自己搜索和学习策略，通常优于人为预设的工具与流程。
