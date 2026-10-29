---
title: 'MLE-World: Predicting Machine Learning Experiment Outcomes with a Learned
  World Model'
title_zh: MLE-World：用学习世界模型预测机器学习实验输出
authors:
- Brian Ko
- Han Wang
- Hejia Geng
- Li Erran Li
- Sherry Yang
affiliations:
- University of Washington
- University of Illinois at Urbana-Champaign
- University of Oxford
- Columbia University
- New York University
arxiv_id: '2610.37175'
url: https://arxiv.org/abs/2610.37175
pdf_url: https://arxiv.org/pdf/2610.37175
published: '2026-10-26'
collected: '2026-10-29'
category: Agent
direction: MLE Agent 世界模型与测试时扩展
tags:
- world model
- test-time scaling
- MLE agent
- confidence gating
- execution prediction
- LLM
one_liner: 用 4B 世界模型预测 ML 程序终端输出并以置信度门控执行，使 MLE Agent 在少执行下获得更高分数
practical_value: '- 在昂贵的真实执行/线上实验前，用轻量世界模型（finetuned 小 LLM）预测候选程序、策略或 query 的终端输出（日志/指标/错误类型），一轮推理代替一次完整运行，可把候选筛选成本降
  1-3 个数量级。

  - 置信度门控是核心复用点：按预测结果类型设置不同阈值（成功/失败/超时），只对低置信度候选做真实执行；比随机跳过更省资源，能省 30-40% 执行时间。

  - 结构化输出比单纯预测分数或日志更有效：同时预测 exception class、terminal output、validation metric、submission
  flag，可提升终端输出一致性和指标召回，并支持后续 Debug/Improve。

  - UCB 式 exploration bonus 用模型不确定性（1-pmax）修正贪心 Best-of-N，避免 discard 被低估的候选；可迁移到商品召回/创意筛选等有限验证预算场景。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机

MLE agent 写程序、执行、看终端输出、改程序，但每次执行都要真实训练和评估模型，时间成本极高，限制了 agent 能探索的候选数量。已有工作做剪枝、性能预测或排序，但不提供错误 trace 和训练日志，无法支持后续调试。因此论文提出学习一个执行世界模型，用一次推理预测程序终端输出，替代昂贵的真实执行。

## 方法关键点

- **模型**：finetune Qwen3.5-4B，输入为程序代码、环境包版本、数据概览、时间限制；输出结构化四字段：exception class（82 类单 token）、terminal output、validation metric、submission flag。
- **置信度**：从第一个 token 的异常类别分布得到 pmax、pclean 和 uncertainty score，用于探索和门控。
- **训练数据**：来自 AIDE 在 17 个 MLE-bench Lite 任务上的 497,056 条多模型执行日志，保留大量失败样本。
- **搜索策略**：基于预测输出构建五种 test-time scaling 策略：Best-of-N、Sequential revision、Pairwise judging、Fusion、UCB（加不确定性 bonus）。
- **执行门控**：仅当 pmax 低于阈值时执行真实运行；对成功/失败/超时设置不同阈值，超时永不执行。

## 关键结果

- 在 1,700 条 held-out 程序上，terminal output 匹配率 77.9%，DeepSeek 最强 prompted baseline 为 41.1%，GPU 推理时间低 13–1061 倍。
- 结构化字段消融：增加 exception class 和 metric 使 terminal output 一致性从 59.4% 升至 62.8%，metric recall 从 84.3% 升至 89.5%。
- 搜索性能：UCB 达到 52.1 mean percentile，Base AIDE 为 45.4；所有五种策略均高于 Base。
- 置信度门控减少 30–40% 真实执行时间，性能基本保持或提升。

**最值得记住的一句话**：低成本世界模型 + 置信度门控，让 Agent 用一次推理代替一次训练运行，是 MLE Agent 测试时扩展的关键。
