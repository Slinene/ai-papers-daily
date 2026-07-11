---
title: 'When the Judge Changes, So Does the Measurement: Auditing LLM-as-Judge Reliability'
title_zh: 当裁判改变，测量随之改变：审计 LLM 裁判的可靠性
authors:
- Zongyou Yang
- Yinghan Hou
- Xiaokun Yang
affiliations:
- Imperial College London
- Nanchang Institute of Technology
arxiv_id: '2607.08535'
url: https://arxiv.org/abs/2607.08535
pdf_url: https://arxiv.org/pdf/2607.08535
published: '2026-07-09'
collected: '2026-07-11'
category: Eval
direction: LLM-as-Judge 可靠性审计
tags:
- LLM-as-judge
- evaluation reliability
- bias
- model scaling
- jury aggregation
- debate
one_liner: 揭示评估器更换导致的测量歧义，发现模型升级路径不可互换且偏差犹存，强调审计实践
practical_value: '- 若用 LLM 作为推荐解释/对话质量的评判器，更换底层评估模型（如从 GPT-4 切到 GPT-4o）时，分数波动可能源于评估器本身的偏差而非系统真正变好，应配套固定响应集的
  ab 测试来解耦模糊性。

  - 在自动化评测链路中，即使使用更强的 judge，位置偏差和冗长偏差仍存在，建议在 prompt 中显式随机化选项顺序、引入长度惩罚机制。

  - 多 judge 投票（jury）未必提升可靠性：当 judge 间错误相关性高时，重复采样增益有限；可转向异构 judge 组合或只在低相关性场景下加 jury。

  - 若采用结构化辩论（debate）让多 agent 修正判断，务必记录完整的解析器和回退日志，否则决策变化无法归因于 deliberation，审计性差。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：LLM-as-judge 常被用作模型质量的测量工具，但评估器本身就是一个模型。当更换评估模型时，即使候选响应不变，得分也可能改变，这种改变到底来自能力提升还是偏差变化？这构成了“评估器更换歧义”，严重威胁测量有效性，但实践中常被忽略。

方法：作者在四个评判数据集上，模拟两种现实中的升级路径：① 缩放 Qwen3 密集模型（1.7B→4B→8B→14B→32B）；② 迁移 MiniMax 发布的 API 版本（M2→M2.7）。针对相邻版本升级，检测分数水平的稳健增益，同时测量位置偏差和冗长偏差在升级前后的变化。进一步测试了重复采样形成 jury 的效果，以及结构化辩论对最终决策的影响。

关键结果：只有 Qwen3 1.7B→4B 的相邻升级带来可靠的评判增益，MiniMax 相邻发布间分数一致性低、无稳健提升；更强的 judge 能减轻但无法消除位置和冗长偏差；当 judge 犯错相关时，jury 投票增益几乎为零；结构化辩论虽能较大幅度改变决策，但因缺乏解析和回退日志，无法确认变化来自真正的推理。作者据此提出审计清单：数据集切片、偏差探测、错误依赖估计和协议审计追踪。
