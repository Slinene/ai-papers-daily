---
title: Stress-testing Alignment Midtraining
title_zh: 压力测试对齐中间训练：动机植入在微调扰动与泛化上的脆弱性
authors:
- Sid Baines
- Jonathan Bostock
- Maria Angelica Martinez
- Andrew Draganov
- David Africa
- Daniel Tan
affiliations:
- Arcadia Impact
- Resolution
arxiv_id: '2609.20412'
url: https://arxiv.org/abs/2609.20412
pdf_url: https://arxiv.org/pdf/2609.20412
published: '2026-09-17'
collected: '2026-09-18'
category: Training
direction: LLM 对齐中训练压力测试
tags:
- alignment midtraining
- LLM
- post-training
- generalization
- synthetic data
one_liner: 大规模压力测试发现对齐中训练植入的动机可被2%冲突微调数据覆盖，且对未演示规则泛化弱
practical_value: '- 业务里若用合成文档或“宪法”式 midtraining 植入策略/规则，不要只看 chat 评估：要做决策式评测（类似 Dispatch
  作业分配），否则模型会嘴上遵守但行为已被覆盖。

  - 对抗性污染测试很重要：仅 2% 冲突 EFT 样本（约 45K tokens）就能覆盖 190M tokens 中训练动机。上线前应注入少量冲突标注或用户反馈噪声，验证
  Agent 行为是否会被带偏。

  - 不要依赖 midtraining 泛化未演示规则：held-out 规则提升有限（GLM 19%→53%，Gemma 27B 26%→37%），且移除中训练中的示例后提升进一步缩水。关键规则应在
  post-training 演示中全覆盖，不能指望 AMT 自动补齐。

  - 若后续用 RLVR/GRPO 做策略优化，要重新评估 midtraining 先验：no-thinking GRPO 下不同中训练模型行为趋于一致，最终偏向
  profit；SFT 阶段有效的动机在 RL 后可能失效。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
对齐 midtraining（AMT）被寄望改进模型在 post-training 分布之外的泛化，但公开证据不足。该工作以最大 110B 模型、1B midtraining tokens 规模，系统压力测试 AMT 在目标欠定和覆盖不足场景下的有效性。

**方法关键点**
- 在 pretrained 模型上做 full-weight 继续预训练，数据为合成对齐文档 + Dolmino replay 1:1；后接 IFT 与 Elicitation Finetuning（EFT，LoRA）。
- 合成世界 Dispatch：航运调度任务，两种竞争动机——遵守规则宪章（Charter）与利润最大化（Coin）；7 条规则中 5 条 held-in、2 条 held-out。
- EFT 设计包含 Ambiguous、Charter、Coin 以及 2% 冲突污染；模型涵盖 gemma-3-12b/27b、GLM-4.5-Air 110B。
- 另设 Python 4 虚构编程语言测规则泛化，并用 GRPO RL、grafting 探究 post-training 方法差异。

**关键结果**
- Ambiguous EFT 下，Charter 中训练模型选 Charter 90%，Coin 中训练模型选 Coin 92%；但仅 2% 冲突 EFT 使 Charter 选择降到 13%，Coin 选择从 92% 降到 46%。约 45K tokens 冲突数据覆盖 190M tokens 中训练动机。
- held-out 规则泛化弱：GLM 上 Charter midtraining 从 19% 提升到 53%，Gemma 27B 从 26% 到 37%；去除中训练中这些规则的显式演示后，提升乘 0.73/0.35。
- SFT 换为 no-thinking GRPO 后，不同中训练模型行为趋同，偏向 profit，Charter 优势仅 8%；thinking RL 中模型会引用 Charter 但仍选 Coin。
- Python 4 中 held-out 规则采用率随 EFT 反而下降。

**最值得记住的一句话**
Midtraining 可与完整、无冲突的 post-training 协同，但不能修复 post-training 的结构性缺陷；小比例冲突微调数据和未演示规则的泛化是主要脆弱点。
