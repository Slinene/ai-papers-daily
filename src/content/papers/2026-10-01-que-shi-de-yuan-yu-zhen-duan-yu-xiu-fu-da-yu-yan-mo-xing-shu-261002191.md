---
title: 'The Missing Primitive: Diagnosing and Repairing Mathematical Reasoning in
  Large Language Models'
title_zh: 缺失的原语：诊断与修复大语言模型数学推理
authors:
- Shuo Xing
- Zilin Dai
- Chengyuan Qian
- Fangzhou Lin
- Wenjing Chen
- Ping He
- Pan Lu
- Alvaro Velasquez
- Mohit Bansal
- Zhengzhong Tu
affiliations:
- Texas A&M University
- Harvard University
- Vanderbilt University
- Stanford University
- DARPA
arxiv_id: '2610.02191'
url: https://arxiv.org/abs/2610.02191
pdf_url: https://arxiv.org/pdf/2610.02191
published: '2026-10-01'
collected: '2026-10-02'
category: Reasoning
direction: 数学推理诊断与后训练蒸馏
tags:
- Mathematical Reasoning
- Self-Distillation
- Privileged Information
- Benchmark
- Structural Understanding
- LLM
one_liner: 提出 Mathematical Primitive 与 PRIM benchmark 诊断结构性理解，并用 ABSORB 蒸馏框架提升推理
practical_value: '- 在推荐/Agent 场景中，把复杂推理拆成「意图/结构发现」与「执行/生成」，用诊断 benchmark 定位瓶颈是 discovery
  还是 execution。例如 query 推荐中区分「用户意图识别」与「候选生成/排序」，不要只看最终指标掩盖能力差异。

  - 做 privileged information 蒸馏时，教师侧不要给完整 solution，而是给 concise structural hint（如 query
  的语义类目、用户意图标签、商品属性约束），并采用 bounded override / one-sided clamp 限制教师过度覆盖学生自身策略，减少已解决
  case 的回退。

  - 后训练样本优先选择 discovery-limited failures：模型拿到正确 hint 就能解的问题，修复收益约为联合失败 case 的 3 倍。对应推荐系统中可优先构造「给了正确类目/意图就能推对」的
  hard case 用于 SFT 或蒸馏。

  - 评估体系增加结构性理解维度（如能否从完整 session 中识别核心购买动机），避免单纯 final answer accuracy 掩盖模型能力画像差异，尤其在迭代模型版本时用于回归监控。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
LLM 在数学问题上表现越来越强，但正确最终答案可能来自投机推理，也可能识别了正确结构却执行失败。现有评估只看 final answer accuracy，无法区分「发现解题结构」和「执行推导」两种能力。论文希望系统诊断 LLM 的结构性数学理解，并利用诊断结论改进后训练。

## 方法关键点
- 提出 **Mathematical Primitive**：一个简洁、问题特定、解释性的核心概念，说明问题为何可解，区别于通用策略或完整证明。
- 构建 **PRIM benchmark**：从 HLE-Verified 抽取 182 道数学题，人工标注 primitive；四个维度：**Discovery**（从问题直接发现 primitive）、**Generation**（直接解题）、**Digestion**（从完整解中提取 primitive）、**Execution**（给定 primitive 后解题）。评分采用 V·σgate·(0.6+0.4σmech)，阈值 0.8。
- 诊断 12 个模型：GPT-5.4 系列、Qwen3.5/3.6、DeepSeek-R1 Distill。
- 提出 **ABSORB**：primitive-privileged self-distillation。教师以 primitive 为特权信息，学生 on-policy 生成；使用 reverse KL with one-sided clamp 保留教师正引导，同时限制对学生已有偏好的过度压制。训练数据为 709 道数学博士资格考试题。

## 关键实验结果
- 提供正确 primitive 后，12 个模型 Execution 相比 Generation 提升 **17.58–29.67 个百分点**，说明存在大量被 discovery 瓶颈掩盖的执行能力。
- 模型 Digestion 远高于 Discovery，例如 Qwen3.6-27B 从 24.73% 升至 92.31%，表明「事后识别」远强于「事前发现」；83.6% 的 Generation 失败落在 D− regime。
- 后训练修复率：D−E+ 约 20.4%–21.1%，是 D−E− 的约 3 倍。
- 在 Qwen3.5-4B/9B/27B 上，ABSORB 平均提升 **2.42–4.48 点**，优于 SFT 和 OPSD；9B 上 Generation 提升 5.49 点，27B 上 HMMT25 达到 100%。

## 最值得记住的一句话
正确 primitive 能解锁大量潜在执行能力，独立发现结构是主要瓶颈；后训练中传递「结构提示」而非完整解，并用 bounded override 防止已解决 case 回退。
