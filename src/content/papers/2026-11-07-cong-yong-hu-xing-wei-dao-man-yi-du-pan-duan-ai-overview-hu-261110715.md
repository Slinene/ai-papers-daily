---
title: 'From User Behaviors to Satisfaction Judgments: Reasoning about User Satisfaction
  with AI Overviews'
title_zh: 从用户行为到满意度判断：AI Overview 用户满意度推理预测
authors:
- Xingzhu Wang
- Yitong Xu
- Yue Li
- Daiting Shi
- Jingzhou He
- Jiaxin Mao
affiliations:
- Renmin University of China
- Baidu Inc.
arxiv_id: '2611.10715'
url: https://arxiv.org/abs/2611.10715
pdf_url: https://arxiv.org/pdf/2611.10715
published: '2026-11-07'
collected: '2026-11-10'
category: Eval
direction: 搜索评估 · 用户行为信号 · LLM 推理
tags:
- User Satisfaction Prediction
- AI Overview
- LLM Reasoning
- Reward Shaping
- GRPO
- Behavioral Signals
one_liner: 提出 STaRS，用 LLM 结构化逐行为推理与 reward shaping RL，将行为信号引入 AI overview 满意度预测，显著优于内容评估和传统行为模型
practical_value: '- 在搜索/电商的 AI 摘要、推荐理由等混合页面，不要用固定 dwell/click heuristic 判断满意；把曝光时长、点击、query
  改写等行为与对应内容上下文一起交给 LLM 逐信号推理，能避免传统行为极性反转。

  - 少量显式反馈时，可以直接用结构化 prompt 零样本上线；有数据后再用 GRPO + 中间信号 reward shaping 微调小模型，参考监督可通过大模型采样投票
  + counterfactual removal 筛选关键行为信号。

  - Reward 设计上，除了最终打分，增加行为信号极性匹配奖励能显著增强可解释中间推理质量，适合广告归因、推荐理由生成等需要过程监督的任务。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：AI overview 已成为搜索 SERP 的常见组成部分，但现有评估主要是系统中心、只看 query 和 answer 内容，缺少用户满意度预测；传统 IR 中 click/dwell/query reformulation 等行为信号的满意度含义在 AI overview 混合页面会反转（如长 dwell 可能表示 AI overview 未满足需求），固定 heuristic 和数值特征难以迁移。

**方法关键点**：
- 构建两个数据集：实验室 UserStudy 554 条 query record、工业 SearchLog26 6,589 条日志，均含 query、AI overview、行为信号和显式满意度评分。
- STaRS 采用 LLM 结构化推理：先对每个行为信号输出解释 e_i 和满意度极性 p_i（+/-, 0），再综合 reason 与整体 satisfaction score。
- 用 GRPO 做 RL 优化；reward 由 format、outcome（归一化 MAE）和 behavior-signal-level reward 组成。
- 行为信号级监督生成：高能力 LLM 采样 K 条 traces，拒绝采样保留预测正确样本，多数投票得到参考极性，再通过 counterfactual removal 筛选对最终分数影响 |Δ|≥1 的关键非中性信号，只在关键信号上计算匹配比例。

**关键结果**：UserStudy 上 zero-shot STaRS 获得 Pearson 0.4051 / Spearman 0.4157 / MAE 0.8646；SearchLog26 上 full STaRS（Qwen3-8B + RL）获得 Pearson 0.4638 / Spearman 0.4652 / MAE 1.0844，均显著优于 GBDT、G-CoS 等行为模型和各类内容评估 baseline；消融显示行为信号、上下文、结构化推理和 reward shaping 都有效。

**最值得记住的一句话**：用户行为信号的价值在 AI 生成结果与传统结果混合的页面中不能被旧规则直接继承，必须结合内容上下文让 LLM 重新解释每个行为，再做整体满意度判断。
