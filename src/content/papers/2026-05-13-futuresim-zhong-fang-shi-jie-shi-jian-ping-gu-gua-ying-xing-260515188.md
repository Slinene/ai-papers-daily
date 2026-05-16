---
title: 'FutureSim: Replaying World Events to Evaluate Adaptive Agents'
title_zh: FutureSim：重放世界事件评估适应性智能体
authors:
- Shashwat Goel
- Nikhil Chandak
- Arvindh Arun
- Ameya Prabhu
- Steffen Staab
- Moritz Hardt
- Maksym Andriushchenko
- Jonas Geiping
affiliations:
- ELLIS Institute Tübingen
- Max Planck Institute for Intelligent Systems
- University of Stuttgart
- Tübingen AI Center
- University of Southampton
arxiv_id: '2605.15188'
url: https://arxiv.org/abs/2605.15188
pdf_url: https://arxiv.org/pdf/2605.15188
published: '2026-05-13'
collected: '2026-05-16'
category: Agent
tags:
- Agent
- Forecasting
- Benchmark
- Test-time adaptation
- Memory
- Search
one_liner: 通过真实新闻事件按时间顺序重放，评估前沿智能体长期预测与适应的能力
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：AI 智能体在动态开放环境中的长期适应能力评估缺乏真实世界基础。现有游戏或仿真基准的动态通常由人工设计或模型生成，无法反映真实世界的社会演进。FutureSim 提出基于时间戳的真实新闻事件重放，让智能体预测未来事件，以此测度其持续更新信念、适应新信息的能力。

**方法关键点**
- **仿真环境**：按日步进，回放 2026 年 1 月–3 月的新闻语料（Common Crawl News）。智能体每天可搜索当天及过去的文章，提交/更新对 330 个自由形式预测问题的概率分布（最多 5 个候选）。
- **问题生成**：从新闻文章中自动提炼预测问题，过滤掉早于 2026 年的可推断问题，避免信息泄露。环境提供两个动作：`submit_forecast()` 和 `next_day()`，同时沙箱化防未来信息泄露。
- **评价指标**：多类别扩展的 Brier Skill Score（衡量校准与分辨力）和 top-1 准确率。
- **智能体配置**：测试 GPT 5.5、DeepSeek V4 Pro、Opus 4.6、Qwen 3.6 Plus、GLM 5.1 等前沿模型，均在各自推荐的代码 harness 及统一改进 harness 下运行，允许最大推理努力。

**关键结果**
- GPT 5.5 表现最优，最终准确率 25%，Brier skill score 约 0.05，而多数开源模型的 Brier skill score 为负（不如完全不预测）。
- 改进的 harness 显著提升开源模型性能，例如 Qwen 3.6 Plus 的 BSS 从负值升至正值，但校准仍差。
- 测试时适应实验显示，将各模型初始预测固定为最差模型的预测，所有模型均无法通过更新达到不预测的基线（BSS=0），暴露出严重锚定效应。
- 消融实验证实：每日新增文章和智能体搜索对准确率提升至关重要（24.8% → 17.9%）；移除记忆能力后 Brier skill score 普遍下降。
- 多智能体实验中，共享聚合预测导致预测相互收敛，而单智能体运行预测趋于发散。

FutureSim 为研究长期适应、搜索、记忆、推理扩展和多智能体动态等方向提供了可复现的评估平台，并揭示前沿模型在真实世界适应性方面仍有巨大提升空间。
