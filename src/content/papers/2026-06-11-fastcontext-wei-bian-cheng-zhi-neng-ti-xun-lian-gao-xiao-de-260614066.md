---
title: 'FastContext: Training Efficient Repository Explorer for Coding Agents'
title_zh: FastContext：为编程智能体训练高效的仓库探索器
authors:
- Shaoqiu Zhang
- Maoquan Wang
- Yuling Shi
- Yuhang Wang
- Xiaodong Gu
- Yongqiang Yao
- Rao Fu
- Shengyu Fu
affiliations:
- Microsoft
- Shanghai Jiao Tong University
arxiv_id: '2606.14066'
url: https://arxiv.org/abs/2606.14066
pdf_url: https://arxiv.org/pdf/2606.14066
published: '2026-06-11'
collected: '2026-06-16'
category: Agent
direction: Agent子代理专化与token效率优化
tags:
- Subagent
- Token Efficiency
- Repository Exploration
- Coding Agent
- Reinforcement Learning
- Parallel Tool Calls
one_liner: 将仓库探索与任务求解分离，用专用小模型子代理并行搜索，最高提升5.5%解决率并削减60% token消耗
practical_value: '- 在大模型推荐Agent中，可把商品库检索、用户画像查询等上下文探索任务交给专用小模型子代理，通过并行工具调用快速返回相关片段，避免主模型上下文爆炸和token浪费。

  - 采用“强模型轨迹引导 + 任务奖励微调”两阶段训练法，利用大模型生成高质量探索路径，再在业务数据上微调小模型，低成本定制垂直领域（如电商搜索、广告定向）的探索器。

  - 分离探索与推理的架构思想可直接迁移：设计“探索员-求解员”模式，探索员专注信息收集并返回带精确引用的证据，求解员仅做决策，可提升系统响应速度和决策准确性。

  - token消耗降低60%的结论提示，在线上高并发推荐或对话场景中，通过精简上下文输入可大幅降低推理成本，且小模型额外开销极小，适合成本敏感业务。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机：** LLM 编程智能体在解决仓库级任务时，探索代码仓库会消耗大量 token，并让无关片段污染上下文。现有方案常由同一模型负责探索和求解，效率低下。

**方法关键点：**
- **架构分离：** 将仓库探索抽象为专用子代理 FastContext，按需调用，与求解模型解耦。
- **并行高效：** FastContext 并行发出工具调用，返回精确的文件路径和行范围作为聚焦上下文，而非冗长代码块。
- **训练策略：** 使用 4B–30B 参数小模型，先用强参考模型（如大模型）的探索轨迹进行引导训练，再基于任务奖惩信号微调，涵盖首轮广搜、多轮证据收集和精准引用生成三种能力。
- **即插即用：** 可直接接入现有智能体（如 Mini-SWE-Agent），无架构侵入。

**关键结果：** 在 SWE-bench Multilingual、SWE-bench Pro 和 SWE-QA 三个基准上，集成 FastContext 后，端到端任务解决率最高提升 5.5%，编码智能体的 token 消耗减少高达 60%，且额外计算开销极小。
