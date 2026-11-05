---
title: 'CompressionBench: How can your coding agents compress LLMs?'
title_zh: CompressionBench：编码智能体如何自主压缩大语言模型
authors:
- Xinrui Zhong
- Zhifeng Li
- Zhiming Wang
- Yongqi Liu
- Shanglin Yang
- Yang Zhou
- Zikun Li
- Zhuoming Chen
- Beidi Chen
affiliations:
- Carnegie Mellon University
arxiv_id: '2611.06858'
url: https://arxiv.org/abs/2611.06858
pdf_url: https://arxiv.org/pdf/2611.06858
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: Agent 自主模型压缩与效率优化
tags:
- LLM compression
- coding agents
- self-improvement
- perplexity
- model efficiency
- autonomous agents
one_liner: 提出 CompressionBench 基准，评估编码智能体在存储限制下自主压缩 LLM 的能力与局限
practical_value: '- 将效率优化任务定义为 agent 可自主探索的 terminal task（明确存储预算、推理环境、验证协议），可借鉴用于业务中
  LLM serving 成本优化，例如让 coding agent 自动搜索 KV cache 量化或蒸馏方案。

  - 使用 perplexity 作为快速反馈信号，但必须配合完整模型评估与生成/推理测试来避免局部最优，业务中不能只看 log-likelihood 或离线指标，需验证线上效果。

  - 关注 representation design（权重表示）与实验判断：agent 会自动尝试不同量化/剪枝方案并记录实验过程，可将其作为自动模型压缩的起点，减少人工调参成本。

  - 工程上将 agent 生成的压缩权重与可执行推理代码分离验证，保证可复现性，类似业务模型上线前需要独立的模型评估套件。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：递归自我提升要求 AI 系统改进后续系统使用的模型与基础设施，LLM 压缩提供了具体的效率目标——在更小的存储预算内保留预训练模型行为。

**方法关键点**：将压缩形式化为 terminal task，agent 接收源 checkpoint、存储限制、推理环境与时间预算，自主构建压缩权重和可执行推理代码；perplexity 反馈引导搜索，独立验证检查最终模型。

**关键结果**：在 6 个 agent 和 6 种模型规模设置下，36 个提交中 29 个通过验证；选择每个任务最低 perplexity 的 agent 设计，平均 PPL 相比 BF16 仅增加 3.4%，下游准确率 77.33%（BF16 为 79.56%）；agent 在 24 次修订中 21 次降低 PPL，complete-model feedback 反转了 79 个局部排序中的 17 个；生成与推理测试暴露了仅靠 likelihood 无法发现的失败。结论：表示设计、实验判断与能力验证是 agent 驱动模型压缩的核心。
