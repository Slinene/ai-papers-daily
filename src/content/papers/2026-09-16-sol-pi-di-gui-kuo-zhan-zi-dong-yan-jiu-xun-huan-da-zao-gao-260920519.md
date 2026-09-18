---
title: 'SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness'
title_zh: SoL-Pi：递归扩展自动研究循环，打造高效 Agent Harness
authors:
- Haozhe Liu
- Tian Ye
- Sensen Gao
- Qihang Cao
- Yitong Li
- Mingchen Zhuge
- Duomin Wang
- Ruihua Zhang
- Ping Luo
- Jiawang Bian
affiliations:
- NVIDIA
- NTU
- MIT
arxiv_id: '2609.20519'
url: https://arxiv.org/abs/2609.20519
pdf_url: https://arxiv.org/pdf/2609.20519
published: '2026-09-16'
collected: '2026-09-18'
category: Agent
direction: Agent harness 层 token 效率优化
tags:
- Agent Harness
- Token Efficiency
- Recursive Self-Improvement
- Context Compaction
- Action Fusion
- Coding Agent
one_liner: 在 harness 层递归搜索自动研究循环，保留四种 token 效率机制，性能不变但成本降约三分之一
practical_value: '- **上下文压缩可迁移到多轮推荐 Agent**：Online Context Compact 与 Evidence-Preserving
  Reducer 的思路能直接用于电商对话推荐或搜索 Agent 的长对话历史管理，保留关键商品/用户意图证据，削减冗余交互，降低推理 token 与延迟。

  - **Action Fusion 减少工具调用开销**：在 Agent 需要多次调用商品检索、库存查询、价格比较等 API 时，将多个小操作合并为一次批量执行，可以显著减少重复上下文注入，节省成本；对广告投放
  Agent 的多步出价查询也有参考价值。

  - **ObservationPack 打包观测结果**：让 Agent 一次接收多个工具返回的结构化摘要而非逐条处理，可以提升上下文利用率，适合高吞吐的搜索/推荐实时决策场景。

  - **递归自我改进的 harness 搜索思想**：可以在业务 Agent 流水线上自动探索 token 效率优化配置（如提示压缩、工具调用顺序），用离线环境评估成本与效果，实现自动降本，不必手工调优。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
Coding agent 从监督式代码补全转向无人值守的持续探索，推理、工具调用与反馈的轨迹大幅拉长，token 消耗成为递归自我改进扩展的主要瓶颈。传统方法侧重模型层优化，而 harness 层（执行环境与工具交互）的 token 浪费常被忽略。

**方法关键点**  
受递归自我改进（RSI）启发，在 harness 层自动扩展研究循环：将 agent 置于日益多样的研究环境（不同语言、任务类型）中生成 rollout，通过性能与成本双重筛选保留有效机制。最终四个机制存活，组成 SoL-Pi：  
1. **Action Fusion**：将多个相似 tool call 合并为一次执行，减少上下文往返。  
2. **Online Context Compact**：对历史上下文进行在线压缩，保留关键状态。  
3. **ObservationPack**：聚合多次观测结果为一组摘要，避免碎片化 token。  
4. **Evidence-Preserving Reducer**：在压缩时保留与决策直接相关的证据，防止信息丢失。  

**关键结果**  
在 51 任务 EdgeBench 上，SoL-Pi 性能与 Pi 基准相当（GPT-5.6 Sol 与 Opus 5），但 token 流量降低 44.7–49.0%，API 成本降低约三分之一。相比原生 Codex/Claude Code 每小时节省 $8.75–$13.50，相比 Pi 节省 $4.36–$5.71。
