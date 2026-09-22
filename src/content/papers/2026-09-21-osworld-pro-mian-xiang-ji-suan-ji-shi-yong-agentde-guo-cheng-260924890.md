---
title: 'OSWorld-Pro: Process-based Evaluation for Computer Use Agents'
title_zh: OSWorld-Pro：面向计算机使用Agent的过程性评估基准
authors:
- Zhilin Wang
- Shaokun Zhang
- Yifan Zhang
- Hao Zhang
- Jin Xu
- Binfeng Xu
- Jian Hu
- Yunheng Zou
- Karan Sapra
- Andrew Tao
affiliations:
- NVIDIA
arxiv_id: '2609.24890'
url: https://arxiv.org/abs/2609.24890
pdf_url: https://arxiv.org/pdf/2609.24890
published: '2026-09-21'
collected: '2026-09-22'
category: Eval
direction: Agent 过程性评估基准
tags:
- Computer Use Agents
- Benchmark
- Process Evaluation
- LLM Judge
- Subgoal
- Failure Analysis
one_liner: 用 2800+ 子目标与 LLM-Judge 评估 CUA 过程性失败，揭示 Claude Opus 5 仅 75.7%
practical_value: '- 对推荐/电商 Agent 的长链路任务（如“找到商品并下单”）不要只看最终成交，可拆成 query 理解、筛选、加购等顺序子目标，用
  LLM-Judge 对每个子目标达成做过程性奖励，定位失败环节。

  - 可以借鉴其 subgoal 标注方法：由人工标注关键中间态，构建带部分奖励的数据集，用于强化学习或 SFT，让模型学会逐步推进而不是跳步。

  - 关注失败模式分类（如点击错误 vs 键盘输入错误、子目标无关动作），在 GUI Agent 中可对应到 UI 操作与 API 调用，针对高频错误做 action
  space 剪枝或提示优化。

  - 用 LLM-Judge 代替人工做过程性校验时，需要与人工标注做对齐验证，确保 judge 可靠后再上线到自动化评估流水线。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

## 动机
现有 Computer-Use Agents (CUAs) 评估只看最终交付物（例如 OSWorld 的几百步后结果），无法解释失败发生在哪个环节。比如键盘输入错误和 GUI 点击不准确需要完全不同的修复策略，但终态评估掩盖了这些差异。

## 方法关键点
OSWorld-Pro 包含超过 300 个任务、2800 多个子目标，覆盖 67,000 多条人工标注。它将长序列任务拆成顺序依赖的子目标，用与人类对齐的 LLM-Judge 判断每个子目标是否达成，从而提供过程性 partial reward 与进展曲线，而不依赖最终交付物。

## 关键结果数字
OSWorld-Pro 对 SOTA LLM 依然有挑战：Claude Opus 5 在 OSWorld-Pro 上仅 75.7%，而在原 OSWorld 终态评估上为 83.4%，说明过程性评估能暴露更多失败。进一步识别出子目标无关动作、点击错误等关键过程失败模式，为 CUA 改进提供依据。
