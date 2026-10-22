---
title: 'Self-Credit: Credit Assignment for Long-Horizon Agentic RL via Intra-group
  Rescaling'
title_zh: Self-Credit：通过组内重标定实现长程智能体 RL 的信用分配
authors:
- Fangcong Yin
- Ming Yin
- Tanvi Bhandarkar
- Aashu Singh
- Eryk Helenowski
- Shlok Kumar Mishra
- Saghar Hosseini
- Karthik Abinav Sankararaman
- Greg Durrett
- Dinkar Juyal
affiliations:
- Meta
- New York University
- Duke University
arxiv_id: '2610.28388'
url: https://arxiv.org/abs/2610.28388
pdf_url: https://arxiv.org/pdf/2610.28388
published: '2026-10-19'
collected: '2026-10-22'
category: Agent
direction: Agentic RL 信用分配与上下文压缩
tags:
- Agentic RL
- Credit Assignment
- Long-Horizon
- Self-Compaction
- GRPO
- RLVR
one_liner: 让策略模型在压缩上下文时引用关键轮次，再用同 prompt 成功/失败样本的组内对比重标定引用权重，将稀疏结果奖励转化为轮次级信用信号
practical_value: '- 在长程 search/导购 agent 训练中，可让模型在上下文压缩时输出带轮次索引的摘要引用（要求 2-5 个 critical
  turns），用这些引用把统一广播的 advantage 改成轮次级加权；只需 prompt 格式约束和格式错误惩罚，不引入额外 reward model 或
  critic。

  - 对同一 query 的 group rollout，可按 action 的检索结果（docid 或商品 ID 集合）做 Jaccard 匹配，统计该 action
  在成功/失败样本中的引用频次：只在成功侧重复出现则提权，只在失败侧重复出现则加重负优势，混合出现则取消提权。这能把“伪相关 action”从正样本中剔除，适合电商多跳搜索、商品对比、策略推荐等长程任务。

  - 对重复失败的惩罚权重做线性退火（如 1.5→1.0），早期强惩罚抑制低效搜索，后期放松以保留探索，可平衡长程 agent 的工具调用效率与深度。

  - 若无 gold action 标注，可用“检索到目标商品/金标文档”作为代理评估引文质量，计算 cited turns 的 F1，快速判断自生成引用是否有用。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM agent 在长程搜索/检索任务中通常用 RLVR 只接收稀疏结果奖励，trajectory 越长，统一广播 advantage 的信用分配问题越严重；外部 judge 或 critic 又需要额外监督且难以应对上下文增长。

**方法关键点**：
- **自压缩与引用**：上下文超过阈值时，策略模型生成带轮次索引的摘要，引用关键轮次作为自生成信用；训练时格式错误整条 rollout reward 置 0。
- **组内重标定**：对 cited turn，在同 prompt 的 group 内按 action 的检索 docid（Jaccard≥0.6）或打开的 page docid 进行匹配；统计成功/失败 rollout 中的引用次数，分三类——repeated success（只被成功侧引用，给 ws=2.5 提权）、mixed outcomes（成功失败都有，取消提权 w=1）、repeated failure（只被失败侧引用，给 wf=1.5 增强负 advantage，并线性退火至 1.0）。其他 cited positive turn 基础权重 β=1.5，uncited turn 权重 1。
- **优势重加权**：token-level advantage = trajectory advantage × turn weight，同一 turn 内所有 token 共享该权重；摘要轮和最终答案轮自动视为 cited，无需显式引用。
- 训练基于 GRPO，异步 rollout，使用 VeRL + Megatron。

**关键实验**：
- BrowseComp-Plus：Qwen3-8B/32B 上 Self-Credit 分别达到 40.6/47.0，相对 zero-shot 提升 37.0/36.2 点，相对最强 baseline ECHO 提升 8.5/5.6 点；训练曲线显示在保持高 reward 的同时避免过度工具调用。
- GAIA 与 xBench-DeepSearch：Gemma4-E4B 上分别达到 39.2 和 16.7，超过最强 baseline 4.9 和 4.7 点。
- 消融：去掉组内重标定、去掉重复失败惩罚、去掉混合结果重标定、去掉自生成引用（改为 all turns 或 random citations）均明显掉点，尤其去掉重复失败惩罚在 32B/8B 分别掉 12.1/14.1 点。
- 引用质量：Self-Credit 的 cited turns 与 gold 检索/打开动作的 F1 显著高于 ECHO 等。

**最值得记住的一句话**：自生成摘要引用 + 组内成功/失败对比重标定，是低成本把稀疏 outcome reward 变成有效轮次级信用信号的关键；其中对失败侧重复动作的惩罚最重要。
