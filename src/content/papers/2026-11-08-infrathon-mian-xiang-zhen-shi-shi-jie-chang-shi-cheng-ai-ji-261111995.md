---
title: 'Infrathon: Benchmarking Language Agents for Real-World, Long-Horizon AI Infra
  Optimization'
title_zh: Infrathon：面向真实世界长时程 AI 基础设施优化的语言智能体基准
authors:
- Zhengyu Hu
- Zheyuan Xiao
- Yike Wang
- Hamish Ivison
- Haoyu Wang
- Yige Yuan
- Rulin Shao
- Yuetai Li
- Niqi Lyu
- Yicheng Ding
affiliations:
- University of Washington
- Allen Institute for AI
- University of Pennsylvania
- Pyromind Dynamics
- Stanford University
arxiv_id: '2611.11995'
url: https://arxiv.org/abs/2611.11995
pdf_url: https://arxiv.org/pdf/2611.11995
published: '2026-11-08'
collected: '2026-11-11'
category: Eval
direction: 语言智能体长时程优化评估
tags:
- Language Agents
- Benchmark
- Infrastructure Optimization
- Long-Horizon
- KV Cache
one_liner: 提出 Infrathon 长时程 AI 基础设施优化基准，评估 6 个模型 150 次运行，发现短评估掩盖优化收益且智能体可超越人工基线
practical_value: '- 评估推荐/搜索 Agent 时应设置长时程预算（如数小时到一天）而非仅短窗口，否则会漏掉后期探索带来的提升，且模型相对排名可能随评估时长改变；可借鉴
  Infrathon 的 24 小时、150 次运行统计设计自动化长时程评估 pipeline。

  - 引入人类专家基线作下限，检验 LLM Agent 能否发现超越人工配置的方案；例如在电商推荐中让 Agent 优化召回/排序参数、KV cache 或推理性能，与人工调优对比，可挖掘被忽略的收益。

  - 监控 Agent 轨迹中的任务违规、不可靠测试、过早完成三类失败模式；对应到推荐/广告 Agent 可设置业务规则护栏、可靠性检查和终止条件，防止过早停止调参或错误评估。

  - 该基准提供可复现的 Docker/代码环境，可用于构建内部长时程 Agent 评估平台，验证 LLM 在基础设施优化上的能力，为后端降本增效提供参考。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**  
现有语言智能体评估多集中在短程、简单任务，无法反映真实 AI 基础设施优化中持续改进的能力。长时程优化需要反复实现、profiling、验证，且要保持数值与硬件约束下的正确性。

**方法关键点**  
- 构建 Infrathon 基准，包含跨层次、多样化的长时程 AI 基础设施优化任务。  
- 评估 6 个前沿模型，共 150 次运行，每次预算 24 小时，总计算超过 10,000 GPU-hours。  
- 提供 Docker 环境、代码、数据集，保证可复现性。  
- 追踪 Agent 轨迹，分析任务违规、不可靠测试、过早完成等失败模式。

**关键结果**  
- 135/150 次运行在后半预算仍获得进一步改进；短评估会同时掩盖优化收益和模型相对排名变化。  
- Claude Opus 5.5 在 KV-cache 压缩任务上，将平均压缩比从人工设计 Quant-VideoGen codec 的 6.82× 提升到 19.86×，证明 Agent 可超越人类基线。  
- 轨迹分析显示任务违规、不可靠测试、过早完成是持续改进的主要障碍。
