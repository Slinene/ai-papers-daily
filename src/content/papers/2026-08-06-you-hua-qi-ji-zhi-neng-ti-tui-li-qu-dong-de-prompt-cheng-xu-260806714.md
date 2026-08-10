---
title: 'The Optimizer Is the Agent: Reasoning-Driven Search across Prompts, Programs,
  and ML Workflows'
title_zh: 优化器即智能体：推理驱动的 Prompt、程序与 ML 工作流搜索
authors:
- Junbo Li
- Boyi Liu
- Canwen Xu
- Yite Wang
- Yuxiong He
- Zhangyang Wang
- Qiang Liu
- Zhewei Yao
affiliations:
- The University of Texas at Austin
- Snowflake
arxiv_id: '2608.06714'
url: https://arxiv.org/abs/2608.06714
pdf_url: https://arxiv.org/pdf/2608.06714
published: '2026-08-06'
collected: '2026-08-10'
category: Agent
direction: Agent 驱动的优化搜索
tags:
- agent
- prompt optimization
- program evolution
- ML workflow optimization
- reasoning-driven search
- tool use
one_liner: 用单一工具使用智能体内部化搜索策略，替代外部启发式控制器，在三大领域 14 项任务中达到或超越专用方法。
practical_value: '- **用 Agent 自动优化模型超参与训练流程**：在搜索推荐模型中，可借鉴 ReASearch 的“先诊断再修改”范式，通过
  Python exec 分析训练曲线、定位瓶颈，替代盲目调参。

  - **Prompt 自主进化**：对于生成式推荐或 Query 改写，可让 Agent 自主管理 prompt 候选树、验证增益、回溯失败路径，并通过记忆文件积累领域知识，减少对手工启发式的依赖。

  - **低成本组件易于集成**：Memory 文件（`lessons.md`）记录已尝试的方法、效果与下一步方向，可作为 Agent 的持久经验库，在新任务初始化时复用，类似推荐系统中的历史实验知识复用。

  - **验证粒度控制防过拟合**：仅暴露聚合验证指标（而非逐样本反馈）能有效防止 prompt 优化过拟合，这一 trick 可直接迁移到生成式推荐的 prompt
  调优中。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
现有 LLM 用于优化提示、程序和 ML 工作流时，搜索策略（如进化算法、Bandit、文本梯度）仍由外部控制器硬编码，LLM 仅作为局部文本变体提议器。这限制了对复杂优化空间的探索能力，且不同任务需专门设计控制器。

## 方法关键点
- **统一 Agent 框架 ReASearch**：一个工具使用 Agent 完全掌控优化循环，自主决定何时评估、如何诊断失败、何时验证或重启、如何分配预算，而非依赖固定外部搜索过程。
- **领域工具设计**：
  - **Prompt 优化**：工具包括按批次采样训练数据、调用学生模型、验证候选 prompt（仅返回聚合分数防过拟合），Agent 可通过 Python exec 分析评价轨迹，最终基于全历史推理选择最终 prompt，而非最高验证分。
  - **程序进化**：提供代码编辑子 Agent 保持主上下文清洁，主 Agent 通过 Python 测试中间行为、形成因果假设，并持续积累经验到 `lessons.md`。
  - **ML 工作流优化**：Agent 读取训练代码，运行限时实验，通过 Python 分析训练曲线，调整超参、架构、优化器等，并发现参数间的共依赖改进。
- **记忆与上下文管理**：持久化记忆文件记录成功/失败/下一步尝试，支持环境压缩。

## 关键实验
- **Prompt 优化**：AIME 2025、GSM8K、HotpotQA、Terminal-Bench 2.0，对比 GEPA，ReASearch 在各任务上提升 2%~40%，如 Terminal-Bench 从 35.56 到 53.33 (+50%)。
- **程序进化**：圆包裹、Heilbronn 三角形、事务调度、ARC-AGI-2 等，对比 AdaEvolve 等，多个任务超越已知人类最佳结果，ARC-AGI-2 测试准确率 50% vs 12.5%。
- **ML 工作流优化**：NanoGPT、图像分类、Atari、MuJoCo、加密预测，对比 Claude Code，分类准确率 63.51→83.99，Kaggle 排名 36→6，且 Token 消耗更少。

## 核心发现
复杂的搜索行为（增益验证、失败回溯、复用教训、自适应探索）从 Agent 的推理过程中自然涌现，无需手工控制器，验证了推理本身即可作为开放搜索的强大引擎。
