---
title: Training LLMs for Multi-Agent Collaboration with Verifiable Information Rewards
title_zh: 用可验证信息奖励训练多智能体协作 LLM
authors:
- Keru Chen
- Sen Lin
- Yingbin Liang
- Nathaniel D. Bastian
- Shaofeng Zou
affiliations:
- Arizona State University
- University of Houston
- The Ohio State University
- Johns Hopkins University
arxiv_id: '2610.17893'
url: https://arxiv.org/abs/2610.17893
pdf_url: https://arxiv.org/pdf/2610.17893
published: '2026-10-13'
collected: '2026-10-15'
category: MultiAgent
direction: 多智能体协作训练 · 可验证信息奖励
tags:
- Multi-agent RL
- Surprisal rewards
- Self-play
- LLM post-training
- Verifiable rewards
- Collaboration
one_liner: 提出 CoSIR，在可验证评分表环境中用团队 surprisal 减少作为信息奖励，训练 LLM 分享/请求/使用信息，迁移到 7 个未见协作任务
practical_value: '- 在多 Agent 搜推系统中，不要只用最终点击/转化奖励整条对话；可在离线、信息完全可知的沙盒中构造“商品属性/用户特征分散在不同
  Agent”的任务，用信息增益（如对正确排序结果的团队后验概率提升）作为消息奖励，训练 Agent 主动分享缺失特征、请求关键信息。

  - 奖励分配要细粒度到 span/属性级：对消息中的实体-属性-值三元组做解析和验证，只有正确且有依据的分享给正奖励，重复、编造给惩罚，避免有效信息和话术得到相同信号。

  - 多智能体协作训练容易损耗通用能力，可加 reference-model KL penalty 和回放通用 prompt 数据；在业务模型上做专项协作微调时尤其重要。

  - 评估 Multi-Agent 系统时，除了最终业务指标，引入 MAST 这样失败分类（忽略队友输入、未澄清、验证缺失），定位瓶颈是信息共享还是信息利用，再进行针对性训练。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：LLM 多智能体系统存在隐藏信息、不澄清、忽略队友输入等协作失败；现有后训练主要奖励最终结果或指令跟随，无法判别单条消息的信息价值。开放任务中信息价值难验证，因此需要可控环境训练可迁移的协作行为。

方法关键点：
- CoSIR 构建评分表环境（4 选项、5 属性，评分 -1/0/+1，选总分最高），每个 agent 只看到部分评分，设置多种信息分布。
- 用 Bayesian evaluator 对每个 agent 的信息记录计算各选项为最佳的后验概率，定义团队 surprisal 为所有 agent 对正确选项的负对数概率之和；消息价值 = 接收后团队 surprisal 的下降（bits）；请求价值 = 假设真实回答带来的潜在下降。
- 奖励分解到 rating statements 和请求 token/span，并要求 statement 必须正确且被 speaker 支持；私有答案奖励评估选项选择概率和计算总分是否正确。
- Self-play 训练 Qwen3-4B/8B 和 Gemma-3-4B-it，使用 PPO 变体，加参考模型惩罚和通用 prompt 数据保留通用能力。

关键结果：在 7 个未见任务上，CoSIR 三模型 SUM 均最高：Qwen3-8B +31.85，Qwen3-4B +24.70，Gemma-3-4B-it +27.92；比 Outcome-RL 分别 +20.72/+22.95/+24.86。行为分析显示 HiddenBench 私有事实披露率上升（Qwen3-8B 68.5%→74.3%），忽略队友输入失败 26.3%→22.8%，未澄清 36.4%→32.0%，不完整验证 51.3%→45.9%；GSM8K/MMLU/IFEval 变化 -0.6~+0.8 个百分点。

最值得记住的一句话：用简单可验证环境中可计算的信息增益作为细粒度奖励，能训练出跨任务迁移的协作行为，且优于只奖励最终结果。
