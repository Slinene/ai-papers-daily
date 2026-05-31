---
title: 'Architecture-Sensitive Supervised Fine-Tuning for Screen-Conditioned Action
  Prediction: A PiSAR Benchmark'
title_zh: 架构敏感监督微调用于屏幕条件动作预测：PiSAR 基准
authors:
- Rahul Bissa
- Abhishek Vyas
- Yash Jain
affiliations:
- AprioriLabs
arxiv_id: '2605.29400'
url: https://arxiv.org/abs/2605.29400
pdf_url: https://arxiv.org/pdf/2605.29400
published: '2026-05-28'
collected: '2026-05-31'
category: Agent
direction: 屏幕条件动作预测 · 架构敏感微调
tags:
- SFT
- LoRA
- Vision-Language
- Action Prediction
- Benchmark
- E-commerce
one_liner: 微调 Qwen3-VL-8B 在屏幕动作预测上语义相似度 0.783，远超零样本前沿模型，并暴露微调效果对模型架构高度敏感。
practical_value: '- **任务特定微调远胜零样本大模型**：在屏幕行为预测这类高度领域特定的任务上，即使前沿视觉语言模型（Claude/GPT）的零样本表现也远不及单一
  LoRA 微调的小模型。对于电商界面优化、Agent 动作规划等场景，必须用自己的领域数据做微调，不能依赖通用大模型的零样本能力。

  - **基座模型选择是关键**：相同数据和微调方法在 Qwen3-VL-8B 上达到 0.783，而在 Gemma-4-26B 上仅 0.441，差距巨大。在落地时，应优先在小规模、非推理调优的视觉模型上尝试微调；推理调优后的大模型抵抗微调信号，可能需要更多数据或更强的微调方法（如更深的参数干预）。

  - **轻量级模型可实现低延迟部署**：8B 微调模型达到亚秒级调用延迟，适合实时动作预测。在需要根据当前屏幕状态快速决策的场景（如智能客服指引、购物车优化）可直接采用。

  - **数据构建方法论可借鉴**：PiSAR 数据集由用户评价、人口统计和购物行为轨迹编织而成，为构建屏幕-行为-意图对齐数据提供了可复用的工程模板。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：前沿视觉语言模型在零样本下预测用户在特定屏幕上下文中的行为（如电商浏览动作）表现不佳，亟需任务特定的微调。  
**方法**：使用 PiSAR 数据集（包含 persona、intent、screen、action、rationale 多元组，共 12,929 条），在 661 行的留出测试集上，通过 LoRA 微调 Qwen3-VL-8B-Instruct 和 Gemma-4-26B-A4B-IT，与 Claude Opus 4.7、GPT-5.5 的零样本输出进行对比，基于语义相似度（sem_sim）评估。  
**关键结果**：微调 Qwen3-VL-8B 的 sem_sim 达 0.783，79% 的预测与参考动作的相似度≥0.7，而最强零样本基线仅 0.482，绝对提升 0.30。同等训练数据和微调方法在 Gemma-4-26B 上仅得 0.441，与零样本相当，揭示微调效果高度依赖模型架构：参数规模更大且经推理调优的模型对 SFT 信号抵抗性强，需更多数据或更强适配手段。
