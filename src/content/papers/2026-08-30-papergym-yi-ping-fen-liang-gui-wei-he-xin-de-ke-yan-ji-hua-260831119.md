---
title: 'PaperGym: Rubric-Centered Evolution for Research-Plan Generation'
title_zh: PaperGym：以评分量规为核心的科研计划生成进化训练框架
authors:
- Yuhan Wang
- Zhengxi Lu
- Yuchen Yan
- Kaitao Song
- Wenqi Zhang
- Weiming Lu
- Jun Xiao
- Yueting Zhuang
- Yongliang Shen
affiliations:
- Zhejiang University
- Apple
arxiv_id: '2608.31119'
url: https://arxiv.org/abs/2608.31119
pdf_url: https://arxiv.org/pdf/2608.31119
published: '2026-08-30'
collected: '2026-09-01'
category: Training
direction: LLM 研究计划生成 · rubric 驱动 RL
tags:
- Research Planning
- Rubric
- GRPO
- RL
- Reward Hacking
- PaperGym
one_liner: 把每篇论文拆成训练环境：问题来自目标/背景、标准来自方法/实验，用 rubric 做自蒸馏与 GRPO 奖励，显著降低泄漏并提升计划质量
practical_value: '- 做 LLM 文案/query/商品标题生成的 reward model 时，别让 reward criteria 与训练样本来自同一段内容：把任务输入从目标/背景合成，评估标准从方法、实验结果或业务指标独立抽取，可明显降低
  paraphrase leakage（PaperGym 降到 3.7%）。

  - 奖励 rubric 不要拍平成一个标量：按方法创新、实验设计/业务效果、可执行性等维度分别计分，能抑制 reward hacking，并给 GRPO 更细的奖励信号。

  - 两阶段复用 rubric 的训练顺序值得搬：先让 self-teacher 用 privileged rubric 做蒸馏（OPSD），再把它当 GRPO
  奖励；类似电商文案训练可先提供高维商品属性/卖点做 SFT，再用多维评分做 RL。

  - 把历史 campaign/实验报告变成 RL 环境：用 campaign goal/background 作为问题，用实际方法论与效果指标构造 rubric，可形成低泄漏的训练数据飞轮。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：科研计划没有可验证答案，RL 缺少 critic；从论文提取 rubric 可充当 critic，但现有 pipeline 的 question 与 criteria 同源，模型靠复述即可拿分，rubric 还被压缩成单标量，奖励信号粗糙。

**方法**：PaperGym 把每篇论文构造成完整训练环境——question 由 research goal/background 合成，criteria 从 method/experiments 独立提取，覆盖方法创新与实验设计。训练中 rubric 复用两次：先作为 privileged context 给 OPSD self-teacher 做监督/蒸馏，再作为 GRPO 奖励做强化；与 SFT、单阶段、逆序都做了对比。

**关键结果**：criterion leakage 降至 3.7%，现有数据集为 11.90%–34.10%；Qwen3-1.7B/4B/8B 五基准平均提升 +5.6/+5.0/+4.8；PaperGym-20k 三选一胜率 58.1% vs RubricHub Science 28.2%；Qwen3-8B 在 ResearchQA 达 73.48，超过更大模型 Kimi K2.6。
