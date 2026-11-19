---
title: 'Thinking Harder Doesn''t Lead to Better Choices: Reasoning Effort Increases
  the Confidence but Not the Correctness of LLM Shopping Agents'
title_zh: 思考更努力并不会带来更好选择：推理努力提升 LLM 购物智能体的信心而非正确性
authors:
- Adi Krishnamoorthy
- X. Y. Han
affiliations:
- University of Chicago
arxiv_id: '2611.22033'
url: https://arxiv.org/abs/2611.22033
pdf_url: https://arxiv.org/pdf/2611.22033
published: '2026-11-16'
collected: '2026-11-19'
category: Agent
direction: LLM 购物 Agent 评估 · 推理努力与校准
tags:
- LLM agents
- reasoning effort
- calibration
- shared errors
- shopping
- evaluation
one_liner: 在三个购物基准上，提高推理努力仅显著提升 10 款 LLM 的置信度，却不提升决策准确率，且模型错误高度相关
practical_value: '- 在电商导购/Agent 场景中不要盲目加大 reasoning effort：商品属性匹配类任务主要瓶颈是读取和校验 listing
  信息，不是多步推理；新增推理预算更可能抬高 verbalized confidence 而非准确率，应优先做商品结构化信息抽取、约束硬校验和属性对齐。

  - 模型校准应作为选型标准而不是调优目标：Claude 系列在多数据集上 ECE 和过度自信表现稳定且明显优于其他模型，其他模型普遍系统性高估 10-30 个百分点；上线前用
  ECE、可靠性图评估 verbalized confidence，可据此设计拒答或转人工机制。

  - 不要依赖多模型投票或模型间一致性作为防错手段：成对误差相关高达 0.70-0.81，多个模型犯错时 80%+ 集中选择同一个错误商品，说明 frontier
  LLM 共享类似的失败模式；需要引入外部规则、属性硬约束或结构化知识校验，而不是靠“第二意见”。

  - 评估购物 Agent 时固定候选集、分离导航与决策错误，并采用配对检验 + 多重比较校正；同时报告实际 reasoning tokens 而不仅是 effort
  档位，因为不同 provider 对 high effort 的 token 消耗可能差两个数量级。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
LLM 正被部署为自主购物智能体，替消费者处理多模态商品 listing 并做出购买决策。人们自然假设更强的推理能力会带来更高质量的购买决策，但这一假设缺乏实证；同时，过度自信的智能体可能静默购买错误商品，因此需要同时评估决策正确性和置信度校准。

## 方法关键点
- 在 WebShop、Amazon SQID、Wayfair WANDS 三个数据集上构建固定 10 候选 1 正确产品的选择任务，移除搜索/导航环节，使误差完全归因于商品判断；WebShop 和 SQID 含图片与文本，WANDS 仅文本。
- 评测 10 个前沿模型（GPT-6 系列、Claude 系列、Gemini 系列、DeepSeek V4.1 Flash、Qwen 3.8 Max、Kimi K3），通过 OpenRouter API 设置 low/medium/high 三档 reasoning effort。
- 模型需输出 JSON 格式：选择的产品编号、选项值以及 0-10 的置信度；解析成功率 99.92%。
- 指标包括成功率、置信度变化、ECE、Brier score、AUROC，以及共享错误分布：方差比、成对误差相关 ρ、最流行错误产品集中度。

## 关键实验与结果
- 从 low 到 high effort，成功率变化很小：WebShop 上仅 3 个模型显著提升，Holm 校正后只有 Qwen 3.8 Max 存活；SQID 上无模型显著提升；WANDS 上仅 GPT-6 Luna 显著。
- 同一努力变化下，置信度显著上升：WebShop 9/10 模型，SQID 5/10 模型，WANDS 6/10 模型；推理努力买来信心而非正确性。
- 校准是模型自身属性：Claude Fable 5.1 和 Claude Opus 5.5 的 ECE 明显最优（WebShop 3.4/6.7 点 vs 其他 8.9-18.2），其他模型普遍过度自信 7-16 点（WebShop）、27-33 点（SQID）；校准排名跨数据集高度稳定。
- 模型错误高度共享：成对误差相关 0.70-0.81，方差比为 6-8 倍独立基线；当多个模型犯错时，81-87% 的错选集中在同一个错误商品（随机基线仅 32-36%）。

## 最值得记住的一句话
对于商品决策类任务，增加推理努力主要增加置信度而非正确性；选择一个校准好的模型比调高 effort 更重要，模型自信和多模型一致都不是可靠防错信号。
