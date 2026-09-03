---
title: 'EarlyEval: Cheaper Agent Evaluation via Early Outcome Prediction'
title_zh: EarlyEval：通过早期结果预测降低 Agent 评估成本
authors:
- Yuling Shi
- Zhensu Sun
- Junsen Dong
- Chengcheng Wan
- David Lo
- Xiaodong Gu
affiliations:
- Shanghai Jiao Tong University
- Singapore Management University
- East China Normal University
- Shanghai Innovation Institute
arxiv_id: '2609.02783'
url: https://arxiv.org/abs/2609.02783
pdf_url: https://arxiv.org/pdf/2609.02783
published: '2026-09-01'
collected: '2026-09-03'
category: Eval
direction: Agent 评估成本优化 · 早停预测
tags:
- Agent Evaluation
- Early Stopping
- LightGBM
- Cost Efficiency
- LLM Agents
one_liner: 用 LightGBM 对部分轨迹预测最终成功/失败并提前终止，最高省 44% 输入 token 且几乎不改变排行榜排名
practical_value: '- 对长链路搜索/导购/售后 Agent 的回归评测，可用历史 rollout 日志训练 LightGBM 成功/失败二分类器，在线每步提取行为+文本特征并校准阈值早停；相比
  LLM-as-judge 每步推理，CPU 级推理开销可忽略。

  - 特征设计不必依赖 gold 答案：行为特征（重复操作、错误类型、无编辑持续步数、测试失败趋势）和 TF-IDF+SVD 文本特征已能提供强信号；无参考解时可关闭
  reference 特征，精度损失很小。

  - 双阈值结构与独立 success/failure 分类器比单一联合模型更可控，可按业务需要分别调 precision/coverage，Platt 校准后阈值才可直接比较；建议在评估平台上做留一
  agent/策略配置的验证。

  - 适用于需要反复评测多个 prompt / scaffold / 模型版本迭代的场景：早停不会显著改变相对排名（ρ≥0.959），可作为内部快速反馈，最终对外榜单仍跑全程。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
Agent 基准评估越来越贵：SWE-bench Verified 一次 frontier model 评估要数百美元，多模态或长 rollout 基准可达数千美元；迭代开发中同一基准要反复跑几十次。之前的 benchmark distillation 只减少任务数量，不降低每个任务的执行成本。EarlyEval 走另一条路：如果一个任务的最终成功/失败在轨迹中间就高度可预测，就在足够置信时提前停止，省掉尾部步骤和 token。

**方法关键点**
- 收集目标基准上多个 agent 的完整轨迹（共 21000+ 条），按最终 outcome 标签训练 LightGBM 两个分类器：success predictor 和 failure predictor。
- 每个运行前缀提取三类特征：Behavioral（活动计数、最后一步、事件时机、工作模式、错误与测试状态）；Textual（任务提示、动作历史和反馈的 TF-IDF 后 SVD 压缩）；Reference（gold patch 特征、前缀与 gold 重叠），后者仅在基准发布参考解时使用。
- 部署时每步计算特征；当任意分类器校准概率超过设定阈值即终止，输出预测结果。阈值可调，平衡精度和节省比例。训练中用任务划分避免泄漏，Platt scaling 校准概率。

**关键实验与结果**
在 SWE-bench Verified、TerminalBench、Toolathlon 上做 leave-one-agent-out 评测：
- SWE-bench Verified 阈值 0.95 时节省 26.0% 执行步骤、32.7% 输入 token、28.7% 输出 token，预测准确率 95%，per-agent resolve rate 平均偏差 1.1pp，排行榜 Spearman ρ=0.991。
- TerminalBench 两种防泄漏设置下步骤节省 17.7%–25.4%，排名 ρ≥0.959；Toolathlon 节省 23.0%，ρ=0.994。
- 消融显示 Behavioral 是主要信号，去掉 Reference 只省 24.7%（原 26.0%），所以可扩展到无参考解基准；架构消融中 LightGBM 优于 MLP/逻辑回归，且比 LoRA Qwen judge 更便宜。

**最值得记住的一句话**
Agent 最终结果往往在早期行为中已经可预测；用轻量梯度提升模型每步判断并早停，能在几乎不扭曲 leaderboard 排名的情况下，省掉最贵的尾部步骤。
