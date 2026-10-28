---
title: 'AutoRSE: Evaluating LLM Agents as Recommendation Engineers for Self-Evolving
  Recommender Systems'
title_zh: AutoRSE：评估 LLM 推荐工程师 Agent 的自主进化能力
authors:
- Rui Tian
- Yi Fang
- Yejin Hua
- Du Wang
- Yuzhe Wang
- Minxuan Shan
- Zirui Ren
- Xinyu Lin
- Chongming Gao
- Wenjie Wang
affiliations:
- University of Science and Technology of China
- National University of Singapore
arxiv_id: '2610.37228'
url: https://arxiv.org/abs/2610.37228
pdf_url: https://arxiv.org/pdf/2610.37228
published: '2026-10-27'
collected: '2026-10-28'
category: Eval
direction: LLM Agent 自主改进推荐算法评估
tags:
- LLM Agents
- Recommender Systems
- Evaluation
- Trajectory Analysis
- Idea Injection
- Self-Evolving
one_liner: 构建 AutoRSE 框架，量化 LLM RSE-Agent 自主改进推荐算法的能力与瓶颈
practical_value: '- 实际可先用 LLM agent 做**工程级优化**：hyperparameter tuning、模型集成、训练策略调整。在生成式推荐（HSTU/TIGER）等尚未饱和场景，单靠这些就能拿平均
  16.1% 的相对提升；而在 CTR 任务 AUC 接近饱和时，agent 收益有限。

  - 若想让 agent 产出**算法创新**，不要只靠它自我 brainstorm。建立外部 idea library（顶会论文、竞赛方案、专家经验提炼成短条目）注入给
  agent，比 self-generated ideas 平均高 13.35%，novelty 也明显更高。

  - 评估 agent 不能只看最终分数，要做 **trajectory-level 分析**：把实验按策略分类（参数调优/集成/训练策略/特征/架构/损失），能暴露
  agent 真实能力边界；工程优化占比越高，说明创新瓶颈越重。

  - 可复用其 **12 小时单卡预算 + 隐藏测试集 + 强制持续运行协议**，在内部做 agent 优化竞赛或离线评测，避免 agent 提前停下或只做少量修改。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机

LLM agent（如 Claude Code、Codex）在软件工程和 ML 工程上表现强势，催生了 Recommender Systems Engineer Agents（RSE-Agents）——让 agent 自主改进推荐算法。但此前只有零散的工业内部验证，缺乏统一评测框架，也不清楚 agent 的收益到底来自哪里，能力边界在哪里。

## 方法关键点

- 构建 **AutoRSE**：覆盖 6 个工业级推荐任务，包括生成式推荐（HSTU、TIGER、IntSR）和点击率预测（WuKong、RankMixer、OneTrans），指标为 NDCG@10 或 AUC。
- 每个任务给 agent 一个完整 baseline 代码库 + 数据集 + 单张 H200 GPU + **12 小时预算**，隐藏测试标签，禁止联网搜索。要求 agent 自主迭代改进算法。
- 评估 3 个前沿 LLM（Claude Opus 4.8、GPT-5.5、DeepSeek V4 Flash）与 3 个 agent harness（Claude Code、Codex、Terminus-2）共 7 种组合，每个设置跑 3 次。
- 做 **轨迹级分析**：自动分割每个训练/评估实验，用 LLM judge 把修改策略归为 6 类——参数调优、模型集成、训练策略、特征建模、模型架构、目标函数；并对最终代码 diff 用 0–4 分打 novelty。
- 做 **idea-injection 实验**：对比 Standard、Self-generated ideas（每轮生成 8 个想法选 2–3 个）和 Idea-injected（注入来自顶会论文/竞赛方案的外部想法库）。

## 关键结果

- 42 个 settings 中 35 个超过 baseline，5/6 任务提升，平均相对提升 **16.1%**；生成式推荐平均提升 29.2%，CTR 仅 3.1%。
- 轨迹分析显示 **91.7% 的实验是工程优化**：模型集成 59.0%、参数调优 26.2%、训练策略 6.6%；真正算法创新仅 8.3%。
- 最终方案平均 novelty 只有 **2.42/4.0**，且 novelty 与相对提升的 Pearson r = 0.79。
- Idea-injected 比 Standard 平均高 14.23%，比 Self-generated 高 13.35%；Self-generated 相比 Standard 几乎没有增益，在 IntSR 和 RankMixer 上甚至下降。

**最值得记住的一句话**：当前 RSE-Agent 主要是工程优化器而非算法改进者，idea generation 是核心瓶颈；注入高质量外部想法能显著提升，但自主产生真正的算法创新仍远未成熟。
