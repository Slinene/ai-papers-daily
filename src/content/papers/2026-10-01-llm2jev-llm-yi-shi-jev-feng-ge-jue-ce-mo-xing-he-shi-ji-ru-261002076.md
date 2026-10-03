---
title: 'LLM2Jev: LLMs Are Already Jev-Style Decision Models -- When and How to Fine-Tune
  Them'
title_zh: LLM2Jev：LLM 已是 Jev 风格决策模型——何时及如何微调
authors:
- Yinheng Li
- Justin Wagle
affiliations:
- Microsoft
arxiv_id: '2610.02076'
url: https://arxiv.org/abs/2610.02076
pdf_url: https://arxiv.org/pdf/2610.02076
published: '2026-10-01'
collected: '2026-10-03'
category: LLM
direction: LLM 决策建模与结构化输出
tags:
- LLM
- Decision Model
- Structured Output
- Fine-tuning
- KL anchor
- LoRA
one_liner: 提出 LLM2Jev 框架，直接利用括号数字标识符的 next-token 概率提取校准决策，无需训练即可让 4B LLM 匹配专用 Jev
  模型
practical_value: '- 电商/广告中的意图路由、分类、证据校验等决策任务，可直接用 LLM 输出括号数字标识符（如 `[1]`、`[2]`），从 **next-token
  概率** 读取每个选项的概率分布，完全跳过文本生成与解析，降低延迟并消除格式错误风险。

  - 面对任意数量的候选选项（如商品类目、投放策略），无需预先确定选项个数，框架天然支持动态选项集，适合线上 A/B 测试和策略切换。

  - 对于弱基座模型或高难度多选项任务，用 **LoRA + 树因子化 listwise loss + KL 锚定** 微调可稳定提升决策准确率，同时保持对话/文本生成能力不退化；强基座模型则可直接零样本使用，节省训练成本。

  - 多模态决策支持：可直接对图像输入（如商品图）做决策，无需额外适配，适合电商图文混合场景。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：软件系统经常需要在预定义选项上做决策，传统 chat 模型输出文本需解析，带来延迟和格式错误。Jev 风格模型直接返回分类概率分布，但尚不清楚通用 LLM 是否已具备该能力，以及何时需要微调。

**方法关键点**：提出 LLM2Jev 框架，保持原 LLM 架构不变。训练免推理时，从模型对括号数字标识符（如 `[1]`）的 next-token 概率中直接提取各选项的校准概率。微调时，采用树因子化的 listwise loss 优化候选选择，并用 KL 散度惩罚将辅助预测锚定到基模型，避免行为退化。

**关键结果**：在 Qwen3.5-4B 和 Qwen3-0.6B 上，4B 模型零样本即可匹配同基座的社区 Jev 风格模型，优于字母 logit 读出，支持任意选项数量，并原生处理图像多模态决策。微调收益是针对性而非普遍的：弱模型和特定任务（如多选项意图路由）提升显著，强骨干收益递减。KL 锚定有效防止对话文本生成能力下降，LoRA 在强模型上表现最佳。
