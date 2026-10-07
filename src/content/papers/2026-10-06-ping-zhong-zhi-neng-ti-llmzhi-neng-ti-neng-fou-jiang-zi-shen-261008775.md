---
title: 'Agent in a Bottle: Can LLM Agents Turn Their Capabilities Into Cheap, Scalable
  Artifacts?'
title_zh: 瓶中智能体：LLM智能体能否将自身能力转为廉价可扩展制品
authors:
- Ankit Sonthalia
- Haritz Puerto
- Alexander Rubinstein
- Martin Gubri
- Seong Joon Oh
affiliations:
- University of Tübingen
- ELLIS Institute Tübingen, Max Planck Institute for Intelligent Systems, Tübingen
  AI Center
- École Polytechnique, Institut Polytechnique de Paris, CNRS
- KAIST AI
arxiv_id: '2610.08775'
url: https://arxiv.org/abs/2610.08775
pdf_url: https://arxiv.org/pdf/2610.08775
published: '2026-10-06'
collected: '2026-10-07'
category: Agent
direction: Agent 自动化低成本制品生成与评估
tags:
- LLM Agents
- Benchmark
- Distillation
- Cost Amortization
- E-commerce
- Automation
one_liner: 用BOTTLED基准评估LLM智能体在固定预算下把通用能力封装为任务专用廉价制品的能力，发现零样本强不必然装瓶强
practical_value: '- 大规模重复性电商文本任务（商品属性抽取 MAVE、query-product 相关性 ESCI、内容审核）不要逐条调用大模型：先用固定蒸馏脚本做基线——用便宜模型标注到预算耗尽，再训练
  Qwen3-0.6B / SmolLM2-360M。论文里这个 naive 基线击败了 31/60 个 agent 装瓶 run，落地时应当优先验证。

  - 选型别只看零样本指标：GPT 5.6 Terra 与 Sonnet 5 在 MAVE 零样本 F1 都约 0.44，但装瓶后 F1 分别为 0.405 和
  0.154。实际业务中若要让 LLM agent 自己生成廉价制品，必须在同等 token/时间预算下重新评估模型，而不是沿用零样本/少样本 leaderboard。

  - 工程上必须设置硬性预算、强制交付 out.txt 并监控预算：21/60 run 耗尽 token，8 个没有任何输出；Gemini Flash-Lite
  甚至把数百万条输入误判为 49 条。生产系统需要 fallback、预算跟踪工具和超时熔断，否则 agent 会浪费资源无产出。

  - 对于超大规模重复推理，自蒸馏小模型/规则程序可以接近专用廉价模型 Jev：Opus 5 在 ESCI 上恢复 Jev 94% 的 macro-F1，成本约
  1/4；在 RAID 上 Gemini 3.1 Pro 达到 Jev 97% AUROC，成本约 2%。可优先尝试 bottling 而不是引入另一套专用推理模型。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
LLM 能解决许多窄任务，但对数百万相关实例逐条查询成本过高。能否让 LLM agent 自主把通用能力“装瓶”成任务专用低价制品，在固定预算内平衡质量与摊销成本？为此工作引入 BOTTLED，评估 agent 是否能把有限资源投资到可复用解决方案上，而不是简单逐条调用大模型。

## 方法关键点
- **问题定义**：agent 一次性接收完整无标签工作负载，在固定时间（10 小时）、token（5M）和硬件（单张 A100 40GB）预算内，必须返回所有预测到 out.txt。制品形式不限：可训练小模型、写规则程序、检索索引或混合路由；仅评估最终预测质量与成本。
- **任务**：MAVE 商品属性抽取（477 万对）、ESCI 搜索 query-product 相关性分类（262 万对）、RAID AI 检测（562 万篇），覆盖电商与内容审核场景。
- **成本模型**：token 按输入/缓存/输出加权，输出 2 倍、缓存输入 1/10，与真实 API 计费近似。
- **固定蒸馏基线**：用 GLM 5.3 Flash 采样标注直到 5M token 耗尽，再训练 Qwen3-0.6B 和 SmolLM2-360M-Instruct，完全不做 agent 自主决策，用于检验 agent 增益是否有价值。

## 关键结果
- 10 模型 × 3 任务 × 2 run：48/60 个装瓶 run 低于自身零样本 95% CI；31/60 低于较强小模型蒸馏基线。
- 零样本相近的模型装瓶后差异极大：MAVE 上 GPT 5.6 Terra 与 Sonnet 5 零样本 F1 均约 0.44，装瓶后分别为 0.405 与 0.154。
- 最强案例：Opus 5 在 ESCI 保留零样本 82% macro-F1（0.499 vs 0.609），成本约 1/657；与专用廉价模型 Jev 对比，恢复 Jev 94% 性能，成本约 1/4。
- GLM 5.3 Flash 的 aggregate 相对增益约 39%，成本不到 $1；GPT 5.6 Sol 仅约 6% 却花 $12。
- 21/60 run 耗尽预算，其中 8 个未交付 out.txt；允许超预算后 47/60 仍低于零样本 CI，说明失败不全是预算问题。

## 最值得记住的一句话
零样本任务能力强不保证“装瓶”能力强；固定 token 预算下，简单蒸馏基线经常击败 LLM agent，实际业务应先跑这个基线。
