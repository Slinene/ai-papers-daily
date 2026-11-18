---
title: Self-Improvement Memory Enables Continual Recursive Self-Improvement
title_zh: 自改进记忆实现持续递归自改进
authors:
- Xin Yu
- Fei Xia
- Jiaqi Pan
- Youbao Tang
- Chengzhi Liu
- Adams Yu
- Sicong Jiang
- Yanfei Chen
- Lingzhou Xue
- Ting Yu
affiliations:
- Google Cloud AI
- Google DeepMind
- Google Cloud AI Research
- The Pennsylvania State University
arxiv_id: '2611.18856'
url: https://arxiv.org/abs/2611.18856
pdf_url: https://arxiv.org/pdf/2611.18856
published: '2026-11-12'
collected: '2026-11-18'
category: Agent
direction: Agent harness 持续自改进与记忆
tags:
- agent harness
- recursive self-improvement
- memory
- continual learning
- LLM agents
- harness transfer
one_liner: 用 SIM 结构化记录 harness 问题、编辑与结果，让 RSI 跨数据/模型持续复用与修订
practical_value: '- 如果业务里用 LLM Agent / prompt + 工具编排做推荐解释、购物助手、query 改写等，建议把每次对 prompt、tool
  schema、控制流的修改按 root-cause 问题分组记录，包含 rationale、predicted/observed outcomes、provenance；模型升级或任务分布变化时，把这些记录原样喂给
  optimizer（proposer + selector），能明显减少重复试错和误改继承机制。

  - 做线上模型迭代时，不要只继承上代 prompt/harness 代码，要同时继承它的改进记忆。论文在 10 组独立 source runs 上做配对比较，带
  SIM 比不带 SIM 平均高 2.36 分（p=0.003），且 9/10 组胜出；工程上可以做一个类似的 paired A/B：同一份继承 harness，只差记忆条件，控制轮次和候选预算。

  - 多模型服务场景（例如同一套 Agent 同时接 Gemini、Claude、Grok）可借鉴其统一合成方案：用多模型反馈 jointly 优化一个共享 harness，文中
  unified synthesis 达到 75.24 held-out，与逐模型单独优化平均 75.20 接近，且高于共享 seed 73.28；避免为每个模型单独维护一套
  prompt/tool 编排。

  - 评估持续改进时，同时看目标端增益和源端保留。论文里 Full SIM 在 TB2.1 上只丢 3/225 个成功 rollout，而 harness-only
  丢 6 个；业务上做模型或数据切换时，应监控旧场景的回归，不能只看新场景提升。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
LLM Agent 同时依赖 policy model 和 harness（上下文、工具、执行流）。递归自改进（RSI）能用执行反馈自动改 harness，但通常固定在单一 benchmark 和模型上。当模型换代或任务分布变化时，只传递 evolved harness 不够：优化器不知道为什么做了某个 edit、预期修什么、实际效果如何，容易重复尝试或误改继承的机制。

## 方法关键点
- 定义 **Continual Recursive Self-Improvement (CRSI)**：在 benchmark 或 policy model 变化后，继续 harness 优化，要求 harness 接口兼容。
- 提出 **Self-Improvement Memory (SIM)**：按 recurring harness problem / root cause 组织 edit 历史。每条 entry 为 `(root cause, [(attempt, rationale, predicted/observed outcomes, provenance)])`，provenance 记 domain、benchmark、policy、round。
- SIM 同时给 proposer 和 selector 读，不做 retrieval 或 truncation；每次 selection 后，即使 edit 失败或回退也追加到对应问题条目，保留早期尝试。
- 比较四条件：Cold Start、Harness Transfer、Problem-Only Memory、Full SIM；后三者共用同一个 source-evolved harness，只用记忆条件区分。
- 所有版本采用相同 target policy、任务、N=10 轮、每轮 k=5 候选，只有 evolve-set 反馈进入优化，held-out 只做评估。

## 关键实验与结果
四个领域：Coding（TB2.1→TB4）、Text classification（3-dataset source→8-dataset target）、Workspace（Harvey LAB→JobBench/GDPval/APEX）、Engineering（EngDesign→Frontier-Eng）。
- **Cross-dataset CRSI**：Full SIM 在全部 6 个 transition 中最终分数最高，比 Harness Transfer 高 2.43–4.35 分，比 Problem-Only 高 0.20–6.06 分。部分来源 harness 起始分低于 seed，但 SIM 能扭转。
- **Cross-model CRSI（Opus 5.5→Gemini 3.8 Flash）**：Full SIM 在 4 个领域全部最高，比 harness-only 高 3.60–11.33 分；workspace 从同样 68.41 起步，Full SIM 到 84.75，harness-only 仅 73.42。
- **10 组独立 source runs 配对检验**：Full SIM 在 9/10 组胜出，平均 +2.36 分，95% CI [1.05, 3.68]，paired t-test p=0.003。
- **Generation chain**：在 Gemini 2.5 Flash / 3.5 Flash / 3.8 Flash / 4 Argon 上，CRSI 在 3.5 Flash 和 3.8 Flash 上比 Fresh RSI 高 3.5 和 1.6 分，但在 4 Argon 上低 0.8 分。
- **Shared harness for multiple models**：统一合成达到 held-out 75.24，接近逐模型单独优化的平均 75.20，高于共享 seed 73.28。

## 最值得记住的一句话
把 harness 编辑按 root-cause 组织并保留 rationale、predicted/observed outcomes 和 provenance，让 optimizer 在模型或数据切换时能复用和修订，而不是只传递一份 harness 代码。
