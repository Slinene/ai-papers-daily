---
title: 'Strategist: Evolving Reasoning with Agents'
title_zh: Strategist：用元智能体进化推理策略并跨任务积累
authors:
- Taiming Lu
- Qi Xu
- Zhigang Hua
- Zhuang Liu
affiliations:
- Princeton University
- Meta
arxiv_id: '2611.03618'
url: https://arxiv.org/abs/2611.03618
pdf_url: https://arxiv.org/pdf/2611.03618
published: '2026-11-02'
collected: '2026-11-03'
category: Agent
direction: Agent 推理策略自动搜索与库积累
tags:
- Meta-Agent
- Inference Strategy
- Blueprint Library
- Multi-tier Routing
- Cross-task Transfer
one_liner: 将推理策略写成可复用蓝图并跨任务搜索积累，在 30 个基准上以 39% 更低成本匹配最强基线
practical_value: '- 电商/推荐 Agent 工作流可把「意图识别→召回→精排→解释/文案」抽象成 Blueprint 库，让 LLM 按小样本和成本约束自动搜索、组合策略，而不是每个场景人工写
  prompt/agent；只换任务化 prompt，结构跨场景复用。

  - 借鉴多层级路由：Amazon-Rec 的发现策略只在「偏好漂移」用户上触发 multi-agent debate，其他用户走 cheap profile/signal
  path。业务上可对高价值或高不确定性 case 单独路由到强模型/复杂流程，避免全局高成本。

  - 评测与上线选择：用 train/validation/hidden/test 四段隔离防止策略搜索过拟合；最终选择规则要求 accuracy 或 cost
  至少一个显著改善且另一个不恶化，否则回退 BL。可作为内部 Agent 策略自动筛选标准。

  - 跨模型迁移：在 Qwen3 上搜索到的策略不改代码迁移到 GPT-5/Gemini 仍有效，说明搜的是任务结构而非后端特性。业务可用廉价模型搜索工作流，再迁移到更强商业模型，降低搜索与试错成本。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
模型只是 AI 系统的一半，决定行为的推理策略（prompt、多步流程、路由、工具调用）仍由人手写且不跨任务积累。已有自动搜索方法要么单任务优化后丢弃，要么只能从固定组件组合，无法发现新结构。Strategist 的目标是把策略设计变成可累积的搜索问题。

**方法关键点**
- Strategy Blueprint：用统一 execute(llm, task) 接口的可执行 Python 代码表示推理流程；基础组件是 chat 和 agent，可互相组合；无环、去重，形成共享库。
- 四阶段循环：Retrieve 用 TF-IDF + embedding 混合检索相关蓝图和跨域灵感；Propose 每轮生成 5 个候选，强制包含 new/composed/reuse 三类；Evaluate 在 train/val/hidden/test 四段隔离下观察轨迹、精度与成本；Accumulate 去掉任务提示词，只把结构、测量卡和经验写回库。
- 多层级模型路由：每个步骤可指定 fast/balanced/complex 三档及 think/nothink 模式，让策略同时优化精度与成本。

**关键实验与结果**
在 30 个主基准、18 个 baseline × 6 种模型配置的矩阵上，Strategist 在 24/30 基准上胜出，平均准确率 74.7% vs 74.0%，加权成本降至 0.61×。10 个留出基准的 one-shot retrieval 达到 81.4% vs 77.8%，成本 0.77×；策略不改代码迁移到 GPT-5 和 Gemini-2.5，成本分别降 35% 和 40%。消融显示完整系统 78.7% vs 无库 65.4% vs 零样本选择 39.4%。

**最值得记住的一句话**
策略设计本身可以像模型权重一样跨任务学习与积累，这是推理系统随使用变强的关键一步。
