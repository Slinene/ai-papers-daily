---
title: Improving Multi-turn Dialogue Consistency with Self-Recall Thinking
title_zh: 通过自我回忆思维提升多轮对话一致性
authors:
- Renning Pang
- Tian Lan
- Leyuan Liu
- Xiaoming Huang
- Piao Tong
- Xiaosong Zhang
affiliations:
- University of Electronic Science and Technology of China
arxiv_id: '2605.15102'
url: https://arxiv.org/abs/2605.15102
pdf_url: https://arxiv.org/pdf/2605.15102
published: '2026-05-14'
collected: '2026-05-16'
category: Reasoning
tags:
- Multi-turn Dialogue
- Self-Recall
- Chain-of-Thought
- GRPO
- Verifiable Reward
- LLM
one_liner: 提出 Self-Recall Thinking 框架，让 LLM 在推理中内生回忆并引用关键历史轮次，兼顾多轮对话准确率与效率。
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
多轮对话中，关键信息散布在遥远的历史轮次，直接处理完整历史导致注意力稀释和推理量激增。现有方法要么依赖外部记忆引入高延迟，要么通过压缩记忆丢失细节，亟需一种精确且高效利用长程历史信息的机制。

**方法核心**
SRT 赋予模型自我回忆能力，在推理时按“分析→回忆→引用→推理→回答”循环自主识别并拉取关键历史语句。其实现分为三个阶段：
- **依赖构建**：使用 Claude 3.7 Sonnet 为每个轮次标注最小回忆集，生成带 `<HIS>` 标签的推理链，确保答案严格基于回忆内容。
- **能力初始化**：先利用依赖剪枝的简化历史进行监督微调，再迁移至完整对话，教会模型何时并如何引用历史。
- **推理优化**：采用 GRPO 强化学习，设计可验证的组合奖励——格式检查、回忆 Jaccard 精度（奖励 IoU 最大化）以及答案语义相似度，联合优化回忆与推理行为，避免外部判别器偏差。

**关键结果**
- 在 SRQA、CoQA、SimpleQA 三个基准上，SRT 平均 F1 提升 3.4%，端到端延迟降低 13.1%。尤其在长对话 SRQA 上，F1 达 78.4，优于 Coconut（75.0）且延迟低 1.4 秒。
- 消融实验表明，去除 RL 阶段导致回忆准确率下降 7.2%，去除 CoT 模块则答案质量损失 4.8%。
- 可插拔策略 SRT‑P 应用于闭源模型（DeepSeek‑V3、Qwen‑Max、Claude 3.5 Sonnet），在 24 轮以上对话中最高提升 2.7% 准确率，验证了方法的通用性。
