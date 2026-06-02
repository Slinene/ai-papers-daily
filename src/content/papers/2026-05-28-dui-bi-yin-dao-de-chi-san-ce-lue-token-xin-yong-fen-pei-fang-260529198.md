---
title: Guidance Contrastive Token Credit Assignment for Discrete Policy Optimization
title_zh: 对比引导的离散策略 Token 信用分配方法
authors:
- Shufan Li
- Konstantinos Kallidromitis
- Akash Gokul
- Yuta Kyuragi
- Aditya Grover
affiliations:
- UCLA
- Panasonic AI Research
- NVIDIA
arxiv_id: '2605.29198'
url: https://arxiv.org/abs/2605.29198
pdf_url: https://arxiv.org/pdf/2605.29198
published: '2026-05-28'
collected: '2026-06-02'
category: Multimodal
direction: 离散策略优化 · 对比引导 · Token 信用分配
tags:
- GCPO
- Token Credit Assignment
- Classifier-Free Guidance
- GRPO
- Multimodal RL
one_liner: 通过对比正负提示的 token 预测差异，为 GRPO 分配 token 级优势，提升图像与多模态推理性能。
practical_value: '- 对于使用 LLM 生成推荐理由、对话等序列的 RL 微调，当仅可获得序列级奖励时，可借鉴 GCPO 的对比引导思路：构造正负提示（如“正确回答”
  vs “生成错误回答”），利用 KL 散度定位关键 token，分配差异化优势，提升优化信号的信噪比。

  - 归一化技巧：直方图均衡化（rank-based normalization）能稳定不同序列间的 token 权重分布，避免 softmax/min-max
  对异常值敏感，减少超参数调整，适合工程部署。

  - 在商品广告图生成的 RL 微调中，可直接借用 GCPO，以空文本作为负提示，使模型自动关注与商品描述对齐的图像区域，从而提升生成质量与文本一致性。

  - 方法无需额外价值模型，与 GRPO/DAPO 等流程兼容，可轻量集成进现有 RL 训练管线。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
GRPO 等组优势强化学习方法在数学推理、文本到图像生成等领域表现出色，但它们在将样本级奖励均匀广播到所有 token 时，忽略了 token 之间的重要性差异。例如，推理链中关键计算词与标点符号、图像中与文本提示关联的区域与背景区域贡献明显不同。已有 token 信用分配方法多依赖启发式规则，缺少基于模型内在信号的细粒度分配。本文受分类器自由引导（CFG）启发，提出 GCPO，通过对比正负提示下的 token 预测分布来给出 token 级优势权重，使训练聚焦关键区域。

**方法关键点**  
- 对生成序列的每个 token，计算正提示（如用户指令）和负提示（如空文本或“生成错误答案”）下的模型预测概率之间的 KL 散度，作为该 token 的对比引导强度 η。
- 使用基于排序的直方图均衡化归一化 η，确保不同样本间权重分布一致，避免软性最大、最小最大归一化的 outlier 问题。
- 将归一化权重乘以样本级优势，得到 per-token 优势，代入 GRPO/DAPO 的截断目标进行策略更新。
- 方法自然地扩展至语言生成：通过构造负提示（如追加“请生成错误答案”）揭示模型对 token 正确性的隐式信念，无需在 rollout 时使用 CFG。

**关键实验与结果**  
- 文本到图像：在 Janus-Pro-7B 上用 GenEval 评估，GCPO 获得 0.89 总分，比基线 GRPO（0.85）和 Janus-Pro-R1（0.86）分别提高 +0.04 和 +0.03，尤其在计数（+0.28）和颜色属性（+0.17）上提升显著，并接近大得多模型的表现。
- 多模态推理：在 Qwen2.5-VL-7B 和 Qwen3-VL-8B 上训练，GCPO 在 MathVerse、MathVision、MM12K、LogicVista、MMMU-Pro 上全面超越 GRPO、DAPO、VPPO。例如，Qwen3-VL-8B + GCPO 在 MathVerse 达 84.1，比 DAPO 高 +7.6，比 VPPO 高 +0.3；在 LogicVista 和 MMMU-Pro 等通用推理任务上优势更明显。
- 消融实验验证了 KL 散度优于信息增益/绝对差，直方图均衡化归一化优于 softmax/min-max，以及“生成错误答案”是最佳负提示。
**值得记住的一句话**：GCPO 用 CFG 风格的正负提示对比，自动为序列中语义关键 token 分配高优势权重，让 RL 训练从盲目均匀广播走向聚焦要害。
