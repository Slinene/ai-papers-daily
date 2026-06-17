---
title: 'Prompt-Level Distillation: A Non-Parametric Alternative to Model Fine-Tuning
  for Efficient Reasoning'
title_zh: 提示级蒸馏：非参数替代微调的高效推理方法
authors:
- Sanket Badhe
- Deep Shah
affiliations:
- Google
arxiv_id: '2602.21103'
url: https://arxiv.org/abs/2602.21103
pdf_url: https://arxiv.org/pdf/2602.21103
published: '2026-06-01'
collected: '2026-06-17'
category: Reasoning
direction: 提示蒸馏 · 高效推理
tags:
- Prompt Distillation
- Chain-of-Thought
- System Prompt
- Efficient Reasoning
- Small Models
- Non-Parametric
one_liner: 将教师模型的推理模式蒸馏为结构化的系统提示，让小模型零微调、低延迟达到前沿推理性能
practical_value: '- **实时推理场景降本**：在电商搜索意图理解、推荐理由生成等需要多步推理的任务中，可将大模型的 CoT 推理模板提炼为系统提示注入小模型，延时几乎不增加，推理成本大幅降低。

  - **Agent 决策加速**：在 Multi‑Agent 任务规划中，复杂 CoT 可蒸馏为精简指令，使 Agent 用 4B 模型即可完成原本需要大模型才能做的逻辑推理，适合高并发在线服务。

  - **可解释性与合规**：提炼出的显式推理步骤天然透明，便于风控、内容审核、推荐解释等场景实现人工校验，满足强监管行业需求。

  - **工程快速迭代**：无需微调、不改变模型权重，只需更新系统提示即可迁移推理能力，适合 A/B 测试和快速部署至边缘设备。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：Chain-of-Thought 推理准确但延迟和推理成本过高，微调小模型又带来资源开销和可解释性损失，生产环境急需一种低成本、低延迟、可解释的替代方案。

**方法关键点**：
- 从教师模型（大模型）的 CoT 推理过程中显式提取高频、通用的推理模式。
- 将这些模式组织成结构化的指令列表，直接写入学生模型（小模型）的 System Prompt，形成 Prompt-Level Distillation（PLD）。
- 非参数化：无需反向传播，不修改模型权重，纯粹通过提示工程实现能力迁移。

**关键结果**：
- Gemma-3 4B 上，StereoSet 的 Macro F1 从 57% 提升至 90.0%，Contract-NLI 从 67% 提升至 83%，LogiQA 准确率达到 70%。
- 在 Mistral Small 3.1 上复现同样效果，证明跨架构泛化性。
- 推理延迟几乎无增加，同时决策过程透明，可完全人工核验。
