---
title: 'From Sequence to Structure: Relational Uncertainty Propagation for LLM Agents'
title_zh: 从序列到结构：LLM Agent 的关系型不确定性传播
authors:
- Zhengzhao Ma. Boxi Cao
- Yaojie Lu
- Hongyu Lin
- Xianpei Han
- Le Sun
affiliations:
- Chinese Information Processing Laboratory, Institute of Software, Chinese Academy
  of Sciences
- University of Chinese Academy of Sciences
arxiv_id: '2608.16002'
url: https://arxiv.org/abs/2608.16002
pdf_url: https://arxiv.org/pdf/2608.16002
published: '2026-08-16'
collected: '2026-08-19'
category: Agent
direction: LLM Agent 轨迹级不确定性量化
tags:
- Uncertainty Quantification
- LLM Agents
- Trajectory Graph
- Failure Detection
- Relational Propagation
- Agent Reliability
one_liner: 将 Agent 执行轨迹建模为关系图并传播不确定性，提升长程任务失败检测与提前干预能力
practical_value: '- 在电商导购/客服 Agent 的多步工具调用链中，可把轨迹建成关系图，重点监控 repetition、feedback conflict、goal
  drift 等边类型，形成失败预警信号；这比只看 token entropy 更能提前发现连环错误。

  - 图构建采用轻量规则 + embedding/tool signature 匹配 + lexical cues，不增加大模型调用成本；可在搜索/推荐助手中实时识别
  error、empty observation、重复 action 等，触发降级、重试或人工接管。

  - 不确定性引导采样策略可落地：每步生成多个候选 action/query，选择 RUPA 风险最低者执行，适用于商品搜索、参数补全、推荐解释生成等需要抉择的场景。

  - 论文的 entropy-matched 分析表明，即使单步置信度相近，轨迹结构信息仍有区分度；因此推荐/搜索 Agent 可把轨迹图风险作为排序或策略选择的额外特征，而不是只依赖单步
  model confidence。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
LLM Agent 在长程任务中的失败很少来自单步错误，而是错误沿推理、工具调用、环境反馈之间的依赖关系逐步累积。现有 UQ 方法只从当前 token 概率、预测熵或单步 confidence 估计，或者把轨迹当线性序列聚合，难以捕捉早期步骤引发的后续风险。论文在 τ-2 上发现传统序列概率 AUROC 仅 0.205，接近随机；失败信号分布在整个轨迹中，并频繁伴随重复动作、停滞、反馈冲突等结构特征。因此需要对执行轨迹做关系型建模。

## 方法关键点
- RUPA 把 Agent 执行前缀构造成有向关系图，节点包括用户指令、推理/动作、工具调用、环境观察；边类型覆盖 sequential、latest、repetition、progression、parallel、feedback、goal alignment。
- 每个节点先有局部不确定性 U_t：assistant 节点来自预测熵，环境节点来自失败信号、空工具响应、冲突反馈等。
- 关系边权由 relation reliability、relation strength、temporal decay 共同确定；goal alignment 边用语义相似度估计。对历史邻居节点的不确定性做加权传播，得到当前结构风险 G_t，同时用指数衰减 momentum 保留长期趋势，最后与 U_t 相加得到当前步风险 R_t。
- 图构建使用轻量 deterministic detectors：文本状态化、embedding/token 匹配、tool signature 匹配和 lexical cues；参数在无标签训练轨迹上校准，不依赖未来结果或测试标签。

## 关键实验
- 数据集：τ-2、Terminal-Bench-2、GAIA；模型：Qwen3.5-27B、Qwen3.6-35B、Gemma4-26B/31B、GPT-OSS-120B、MiniMax-M2.7。
- 对比 Entropy、Seq-prob、SAUP、Tracer、UProp。RUPA 在所有模型上取得最高平均 AUROC/AUPRC/F1；例如 MiniMax-M2.7 平均 AUROC 从最强 baseline 的 0.694 提升到 0.718，Gemma4-31B 从 0.842 提升到 0.861。
- 前缀评估显示 RUPA 能在轨迹早期更准确地识别失败；不确定性引导采样下，Terminal-Bench-2 上 Qwen3.5-27B 成功率从 random 的 0.105 提升到 0.213。
- 消融中移除 graph modeling 使 AUROC 从 0.718 降到 0.678，AUPRC 从 0.805 降到 0.642；替换为随机图也显著下降，说明关系结构本身是关键。
- 在 entropy-matched bins 中，RUPA 仍能把相似 token 置信度的成功/失败轨迹区分开，表明结构信号对单步概率有互补价值。

## 最值得记住的一句话
Agent 执行不确定性是轨迹级、关系型属性；显式建模依赖图并传播风险，才能比单步 confidence 更早、更准地抓住失败。
